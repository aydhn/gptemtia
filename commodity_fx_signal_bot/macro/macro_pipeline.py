import logging
from typing import Dict, Optional, Tuple

import pandas as pd

from config.settings import Settings
from data.storage.data_lake import DataLake
from macro.benchmark_builder import build_benchmark_frame
from macro.fx_macro_features import build_fx_macro_feature_frame
from macro.inflation_features import build_inflation_feature_frame
from macro.macro_config import MacroProfile, get_default_macro_profile
from macro.macro_events import build_macro_event_frame
from macro.macro_provider import MacroProvider
from macro.macro_quality import build_macro_quality_report
from macro.macro_regime import classify_macro_regime
from macro.macro_series import get_macro_series_spec

logger = logging.getLogger(__name__)


class MacroPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: Optional[MacroProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_macro_profile()
        self.provider = MacroProvider(settings=settings)

    def update_macro_data(
        self,
        profile: Optional[MacroProfile] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        save: bool = True,
    ) -> Tuple[Dict[str, pd.DataFrame], dict]:
        p = profile or self.profile

        summary = {"fetched_series": [], "failed_series": []}
        results = {}

        specs = [get_macro_series_spec(code) for code in p.macro_series]

        raw_data = self.provider.fetch_many(
            specs, start_date=start_date, end_date=end_date
        )

        for code, df in raw_data.items():
            if not df.empty:
                results[code] = df
                summary["fetched_series"].append(code)
                if save:
                    self.data_lake.save_macro_series(code, df, processed=False)
            else:
                summary["failed_series"].append(code)

        return results, summary

    def build_macro_features(
        self,
        profile: Optional[MacroProfile] = None,
        save: bool = True,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        p = profile or self.profile
        summary = {"processed": []}

        # Load raw
        raw_data = {}
        for code in p.macro_series:
            df = self.data_lake.load_macro_series(code, processed=False)
            if not df.empty:
                raw_data[code] = df

        if not raw_data:
            return pd.DataFrame(), {"error": "No raw macro data available"}

        # Combine all to a single dataframe and forward fill if requested
        all_dates = set()
        for df in raw_data.values():
            all_dates.update(df.index)

        date_idx = pd.DatetimeIndex(sorted(list(all_dates)))
        if p.forward_fill_to_daily:
            date_idx = pd.date_range(start=date_idx.min(), end=date_idx.max(), freq="D")

        combined_df = pd.DataFrame(index=date_idx)

        for code, df in raw_data.items():
            aligned = df.reindex(date_idx)
            if p.forward_fill_to_daily:
                aligned = aligned.ffill()
            combined_df[code] = aligned["value"]

        feature_frames = []

        # Build features for each relevant series
        if "TR_CPI" in combined_df.columns:
            inf_df = pd.DataFrame({"value": combined_df["TR_CPI"]})
            tr_cpi_f, _ = build_inflation_feature_frame(inf_df, "TR_CPI")
            feature_frames.append(tr_cpi_f)

        if "US_CPI" in combined_df.columns:
            inf_df = pd.DataFrame({"value": combined_df["US_CPI"]})
            us_cpi_f, _ = build_inflation_feature_frame(inf_df, "US_CPI")
            feature_frames.append(us_cpi_f)

        if "USDTRY" in combined_df.columns:
            fx_df = pd.DataFrame({"value": combined_df["USDTRY"]})
            usdtry_f, _ = build_fx_macro_feature_frame(fx_df, "usdtry")
            feature_frames.append(usdtry_f)

        # Compile features
        macro_features = pd.DataFrame(index=date_idx)
        for f in feature_frames:
            if not f.empty:
                macro_features = pd.concat([macro_features, f], axis=1)

        # Regime features
        regime_df, _ = classify_macro_regime(macro_features)
        if not regime_df.empty:
            macro_features = pd.concat([macro_features, regime_df], axis=1)

        # Save features
        if save and self.settings.save_macro_features:
            self.data_lake.save_feature_set("macro", "macro_features", macro_features)
            summary["processed"].append("macro_features_saved")

        # Events
        if include_events:
            events_df, _ = build_macro_event_frame(macro_features)
            if save and self.settings.save_macro_events and not events_df.empty:
                self.data_lake.save_feature_set(
                    "macro_events", "macro_events", events_df
                )
                summary["processed"].append("macro_events_saved")

        # Quality report
        quality_summary = build_macro_quality_report(macro_features, summary)

        return macro_features, quality_summary

    def build_benchmarks(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        p = self.profile

        inputs = {}
        for code in ["USDTRY", "GOLD_USD", "OIL_WTI", "TR_CPI", "US_CPI"]:
            df = self.data_lake.load_macro_series(code, processed=False)
            if not df.empty:
                inputs[code] = df["value"]

        bench_df, summary = build_benchmark_frame(inputs)

        if save and self.settings.save_benchmark_features and not bench_df.empty:
            self.data_lake.save_feature_set(
                "benchmarks", "benchmark_features", bench_df
            )
            summary["saved"] = True

        return bench_df, summary
