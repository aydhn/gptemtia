import os

os.makedirs('commodity_fx_signal_bot/indicators', exist_ok=True)
os.makedirs('commodity_fx_signal_bot/scripts', exist_ok=True)
os.makedirs('commodity_fx_signal_bot/tests', exist_ok=True)

with open('commodity_fx_signal_bot/indicators/momentum_advanced.py', 'w') as f:
    f.write("""import numpy as np
import pandas as pd

from indicators.momentum import (
    calculate_rsi,
    calculate_roc,
    calculate_momentum,
    calculate_stochastic,
    calculate_williams_r,
)


def calculate_multi_rsi(
    df: pd.DataFrame, windows: tuple[int, ...] = (7, 14, 21, 28)
) -> pd.DataFrame:
    results = []
    for window in windows:
        rsi_df = calculate_rsi(df, window=window)
        results.append(rsi_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_multi_roc(
    df: pd.DataFrame, windows: tuple[int, ...] = (5, 10, 20)
) -> pd.DataFrame:
    results = []
    for window in windows:
        roc_df = calculate_roc(df, window=window)
        results.append(roc_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_multi_momentum(
    df: pd.DataFrame, windows: tuple[int, ...] = (5, 10, 20)
) -> pd.DataFrame:
    results = []
    for window in windows:
        mom_df = calculate_momentum(df, window=window)
        results.append(mom_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_multi_stochastic(
    df: pd.DataFrame, windows: tuple[int, ...] = (14, 21), smooth_window: int = 3
) -> pd.DataFrame:
    results = []
    for window in windows:
        stoch_df = calculate_stochastic(df, window=window, smooth_window=smooth_window)
        results.append(stoch_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_multi_williams_r(
    df: pd.DataFrame, windows: tuple[int, ...] = (14, 21)
) -> pd.DataFrame:
    results = []
    for window in windows:
        will_df = calculate_williams_r(df, window=window)
        results.append(will_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_cci(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    if not all(col in df.columns for col in ["high", "low", "close"]):
        raise ValueError("Missing required columns: high, low, close")

    typical_price = (df["high"] + df["low"] + df["close"]) / 3
    sma_tp = typical_price.rolling(window=window, min_periods=window).mean()

    mean_deviation = typical_price.rolling(window=window, min_periods=window).apply(
        lambda x: np.mean(np.abs(x - np.mean(x))), raw=True
    )

    cci = (typical_price - sma_tp) / (0.015 * mean_deviation)
    cci = cci.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"cci_{window}": cci}, index=df.index)


def calculate_multi_cci(
    df: pd.DataFrame, windows: tuple[int, ...] = (14, 20, 30)
) -> pd.DataFrame:
    results = []
    for window in windows:
        cci_df = calculate_cci(df, window=window)
        results.append(cci_df)
    if results:
        res_df = pd.concat(results, axis=1)
        res_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return res_df
    return pd.DataFrame(index=df.index)


def calculate_momentum_slope(
    df: pd.DataFrame, source_col: str, window: int = 5
) -> pd.DataFrame:
    if source_col not in df.columns:
        raise ValueError(f"Source column {source_col} not found in dataframe.")

    slope = (df[source_col] - df[source_col].shift(window)) / window
    slope = slope.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"slope_{source_col}_{window}": slope}, index=df.index)


def calculate_momentum_acceleration(
    df: pd.DataFrame, source_col: str, window: int = 5
) -> pd.DataFrame:
    if source_col not in df.columns:
        raise ValueError(f"Source column {source_col} not found in dataframe.")

    slope_df = calculate_momentum_slope(df, source_col=source_col, window=window)
    slope_col = f"slope_{source_col}_{window}"

    accel = (slope_df[slope_col] - slope_df[slope_col].shift(window)) / window
    accel = accel.replace([np.inf, -np.inf], np.nan)

    return pd.DataFrame({f"accel_{source_col}_{window}": accel}, index=df.index)


def calculate_relative_momentum_rank(
    feature_df: pd.DataFrame, columns: list[str]
) -> pd.DataFrame:
    missing = [c for c in columns if c not in feature_df.columns]
    if missing:
        raise ValueError(f"Missing columns for relative rank: {missing}")

    subset = feature_df[columns]
    rank_df = subset.rank(axis=1, pct=True)

    rank_df.columns = [f"rel_rank_{c}" for c in columns]
    return rank_df
""")


with open('commodity_fx_signal_bot/indicators/momentum_events.py', 'w') as f:
    f.write("""import re
from dataclasses import dataclass
from typing import Optional, Tuple

import pandas as pd


@dataclass
class MomentumEventConfig:
    rsi_overbought: float = 70.0
    rsi_oversold: float = 30.0
    stochastic_overbought: float = 80.0
    stochastic_oversold: float = 20.0
    cci_upper: float = 100.0
    cci_lower: float = -100.0
    roc_neutral: float = 0.0
    min_event_strength: float = 0.0


def _get_columns_by_prefix(df: pd.DataFrame, prefix: str) -> list[str]:
    return [c for c in df.columns if c.startswith(prefix)]


def detect_rsi_zone_events(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> pd.DataFrame:
    config = config or MomentumEventConfig()
    events = pd.DataFrame(index=features.index)
    rsi_cols = _get_columns_by_prefix(features, "rsi_")
    for col in rsi_cols:
        window_match = re.search(r"rsi_(\d+)", col)
        if not window_match:
            continue
        window = window_match.group(1)
        events[f"event_rsi_{window}_oversold"] = (features[col] < config.rsi_oversold).astype(int)
        events[f"event_rsi_{window}_overbought"] = (features[col] > config.rsi_overbought).astype(int)
    return events


def detect_rsi_crossback_events(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> pd.DataFrame:
    config = config or MomentumEventConfig()
    events = pd.DataFrame(index=features.index)
    rsi_cols = _get_columns_by_prefix(features, "rsi_")
    for col in rsi_cols:
        window_match = re.search(r"rsi_(\d+)", col)
        if not window_match:
            continue
        window = window_match.group(1)
        rsi_series = features[col]
        prev_rsi = rsi_series.shift(1)
        events[f"event_rsi_{window}_recovery_cross"] = ((prev_rsi <= config.rsi_oversold) & (rsi_series > config.rsi_oversold)).astype(int)
        events[f"event_rsi_{window}_bearish_crossback"] = ((prev_rsi >= config.rsi_overbought) & (rsi_series < config.rsi_overbought)).astype(int)
    return events


def detect_stochastic_cross_events(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> pd.DataFrame:
    config = config or MomentumEventConfig()
    events = pd.DataFrame(index=features.index)
    k_cols = _get_columns_by_prefix(features, "stoch_k_")
    for k_col in k_cols:
        parts = k_col.split("_")
        if len(parts) >= 4:
            window = parts[2]
            d_col = k_col.replace("stoch_k_", "stoch_d_")
            if d_col in features.columns:
                k_series = features[k_col]
                d_series = features[d_col]
                prev_k = k_series.shift(1)
                prev_d = d_series.shift(1)
                events[f"event_stoch_{window}_bullish_cross"] = ((prev_k <= prev_d) & (k_series > d_series)).astype(int)
                events[f"event_stoch_{window}_bearish_cross"] = ((prev_k >= prev_d) & (k_series < d_series)).astype(int)
    return events


def detect_roc_shift_events(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> pd.DataFrame:
    config = config or MomentumEventConfig()
    events = pd.DataFrame(index=features.index)
    roc_cols = _get_columns_by_prefix(features, "roc_")
    for col in roc_cols:
        window_match = re.search(r"roc_(\d+)", col)
        if not window_match:
            continue
        window = window_match.group(1)
        roc_series = features[col]
        prev_roc = roc_series.shift(1)
        events[f"event_roc_{window}_positive_shift"] = ((prev_roc <= config.roc_neutral) & (roc_series > config.roc_neutral)).astype(int)
        events[f"event_roc_{window}_negative_shift"] = ((prev_roc >= config.roc_neutral) & (roc_series < config.roc_neutral)).astype(int)
    return events


def detect_cci_zone_events(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> pd.DataFrame:
    config = config or MomentumEventConfig()
    events = pd.DataFrame(index=features.index)
    cci_cols = _get_columns_by_prefix(features, "cci_")
    for col in cci_cols:
        window_match = re.search(r"cci_(\d+)", col)
        if not window_match:
            continue
        window = window_match.group(1)
        events[f"event_cci_{window}_oversold"] = (features[col] < config.cci_lower).astype(int)
        events[f"event_cci_{window}_overbought"] = (features[col] > config.cci_upper).astype(int)
    return events


def detect_momentum_slope_events(features: pd.DataFrame) -> pd.DataFrame:
    events = pd.DataFrame(index=features.index)
    slope_cols = _get_columns_by_prefix(features, "slope_")
    for col in slope_cols:
        events[col.replace("slope_", "event_momentum_slope_positive_")] = (features[col] > 0).astype(int)
        events[col.replace("slope_", "event_momentum_slope_negative_")] = (features[col] < 0).astype(int)
    return events


def build_momentum_event_frame(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> Tuple[pd.DataFrame, dict]:
    config = config or MomentumEventConfig()
    event_dfs = [
        detect_rsi_zone_events(features, config),
        detect_rsi_crossback_events(features, config),
        detect_stochastic_cross_events(features, config),
        detect_roc_shift_events(features, config),
        detect_cci_zone_events(features, config),
        detect_momentum_slope_events(features),
    ]
    event_df = pd.concat(event_dfs, axis=1)
    event_df.fillna(0, inplace=True)
    event_df = event_df.astype(int)
    event_columns = event_df.columns.tolist()
    active_last_row = []
    if not event_df.empty:
        last_row = event_df.iloc[-1]
        active_last_row = last_row[last_row == 1].index.tolist()
    event_count_by_column = event_df.sum().to_dict()
    summary = {
        "input_rows": len(features),
        "event_columns": event_columns,
        "total_event_count": int(event_df.sum().sum()),
        "event_count_by_column": event_count_by_column,
        "active_last_row_events": active_last_row,
        "warnings": [],
        "notes": "Generated candidate events based on momentum indicators. These are not trade signals.",
    }
    return event_df, summary
""")

with open('commodity_fx_signal_bot/indicators/momentum_feature_set.py', 'w') as f:
    f.write("""import logging
from typing import Tuple, Optional

import numpy as np
import pandas as pd

from config.settings import settings
from indicators.momentum_advanced import (
    calculate_multi_rsi,
    calculate_multi_roc,
    calculate_multi_momentum,
    calculate_multi_stochastic,
    calculate_multi_williams_r,
    calculate_cci,
    calculate_momentum_slope,
    calculate_momentum_acceleration,
)
from indicators.momentum_events import build_momentum_event_frame, MomentumEventConfig

logger = logging.getLogger(__name__)


class MomentumFeatureSetBuilder:
    def __init__(self):
        self.config = MomentumEventConfig(
            rsi_overbought=settings.default_momentum_overbought_rsi,
            rsi_oversold=settings.default_momentum_oversold_rsi,
            stochastic_overbought=settings.default_stochastic_overbought,
            stochastic_oversold=settings.default_stochastic_oversold,
        )

    def _clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df = df.loc[:, ~df.columns.duplicated()]
        return df

    def build_momentum_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        if df.empty:
            return df, {"error": "Empty dataframe"}
        features_list = [df]
        try:
            features_list.append(calculate_multi_rsi(df, windows=settings.default_momentum_windows))
        except Exception as e:
            logger.warning(f"Failed to calculate multi RSI: {e}")
        try:
            features_list.append(calculate_multi_roc(df, windows=settings.default_roc_windows))
        except Exception as e:
            logger.warning(f"Failed to calculate multi ROC: {e}")
        try:
            features_list.append(calculate_multi_momentum(df, windows=settings.default_roc_windows))
        except Exception as e:
            logger.warning(f"Failed to calculate multi Momentum: {e}")
        try:
            features_list.append(calculate_multi_stochastic(df, windows=(14, 21)))
        except Exception as e:
            logger.warning(f"Failed to calculate multi Stochastic: {e}")
        try:
            features_list.append(calculate_multi_williams_r(df, windows=(14, 21)))
        except Exception as e:
            logger.warning(f"Failed to calculate multi Williams %R: {e}")
        try:
            features_list.append(calculate_cci(df, window=20))
        except Exception as e:
            logger.warning(f"Failed to calculate CCI: {e}")

        feature_df = pd.concat(features_list, axis=1)
        feature_df = self._clean_dataframe(feature_df)

        deriv_features = []
        if "rsi_14" in feature_df.columns:
            deriv_features.append(calculate_momentum_slope(feature_df, "rsi_14", window=5))
            deriv_features.append(calculate_momentum_acceleration(feature_df, "rsi_14", window=5))
        if "roc_10" in feature_df.columns:
            deriv_features.append(calculate_momentum_slope(feature_df, "roc_10", window=5))

        if deriv_features:
            feature_df = pd.concat([feature_df] + deriv_features, axis=1)
            feature_df = self._clean_dataframe(feature_df)

        event_cols = []
        event_summary = {}

        if include_events and getattr(settings, "momentum_events_enabled", True):
            try:
                event_df, event_summary = build_momentum_event_frame(feature_df, self.config)
                if not event_df.empty:
                    feature_df = pd.concat([feature_df, event_df], axis=1)
                    feature_df = self._clean_dataframe(feature_df)
                    event_cols = event_summary.get("event_columns", [])
            except Exception as e:
                logger.error(f"Failed to build momentum events: {e}")

        all_cols = feature_df.columns.tolist()
        input_cols = df.columns.tolist()
        feat_cols = [c for c in all_cols if c not in input_cols and c not in event_cols]

        total_nans = feature_df.isna().sum().sum()
        total_cells = feature_df.size
        nan_ratio = float(total_nans / total_cells) if total_cells > 0 else 0.0

        summary = {
            "input_rows": len(df),
            "output_rows": len(feature_df),
            "feature_columns": feat_cols,
            "event_columns": event_cols,
            "feature_count": len(feat_cols),
            "event_count": len(event_cols),
            "total_nan_ratio": nan_ratio,
            "failed_components": [],
            "warnings": [],
            "event_summary": event_summary,
        }
        return feature_df, summary

    def build_compact_momentum_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        if df.empty:
            return df, {"error": "Empty dataframe"}
        features_list = [df]
        try:
            features_list.append(calculate_multi_rsi(df, windows=(14, 21)))
            features_list.append(calculate_multi_roc(df, windows=(10, 20)))
            features_list.append(calculate_multi_momentum(df, windows=(10,)))
            features_list.append(calculate_multi_stochastic(df, windows=(14,)))
            features_list.append(calculate_multi_williams_r(df, windows=(14,)))
            features_list.append(calculate_cci(df, window=20))
        except Exception as e:
            logger.warning(f"Error building compact momentum base features: {e}")

        feature_df = pd.concat(features_list, axis=1)
        feature_df = self._clean_dataframe(feature_df)

        if "rsi_14" in feature_df.columns:
            slope_df = calculate_momentum_slope(feature_df, "rsi_14", window=5)
            feature_df = pd.concat([feature_df, slope_df], axis=1)
            feature_df = self._clean_dataframe(feature_df)

        event_cols = []
        event_summary = {}

        if include_events and getattr(settings, "momentum_events_enabled", True):
            try:
                event_df, event_summary = build_momentum_event_frame(feature_df, self.config)
                if not event_df.empty:
                    feature_df = pd.concat([feature_df, event_df], axis=1)
                    feature_df = self._clean_dataframe(feature_df)
                    event_cols = event_summary.get("event_columns", [])
            except Exception as e:
                logger.error(f"Failed to build compact momentum events: {e}")

        all_cols = feature_df.columns.tolist()
        input_cols = df.columns.tolist()
        feat_cols = [c for c in all_cols if c not in input_cols and c not in event_cols]

        total_nans = feature_df.isna().sum().sum()
        total_cells = feature_df.size
        nan_ratio = float(total_nans / total_cells) if total_cells > 0 else 0.0

        summary = {
            "input_rows": len(df),
            "output_rows": len(feature_df),
            "feature_columns": feat_cols,
            "event_columns": event_cols,
            "feature_count": len(feat_cols),
            "event_count": len(event_cols),
            "total_nan_ratio": nan_ratio,
            "failed_components": [],
            "warnings": [],
            "event_summary": event_summary,
        }
        return feature_df, summary

    def validate_momentum_features(self, df: pd.DataFrame) -> dict:
        if df.empty:
            return {"valid": False, "reason": "Empty DataFrame"}
        has_inf = np.isinf(df.select_dtypes(include=[np.number])).values.any()
        nan_ratio = float(df.isna().sum().sum() / df.size) if df.size > 0 else 1.0
        return {
            "valid": not has_inf and nan_ratio < 0.99,
            "has_inf": bool(has_inf),
            "nan_ratio": nan_ratio,
            "rows": len(df),
            "columns": len(df.columns),
        }
""")

with open('commodity_fx_signal_bot/scripts/run_momentum_feature_preview.py', 'w') as f:
    f.write("""import argparse
import logging

from config.settings import settings
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.momentum_feature_set import MomentumFeatureSetBuilder
from reports.report_builder import build_momentum_feature_preview_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Preview Momentum Features")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 4h)")
    parser.add_argument("--last", type=int, default=10, help="Number of recent rows to show")
    parser.add_argument("--full", action="store_true", help="Build full feature set instead of compact")
    parser.add_argument("--no-events", action="store_true", help="Skip event columns")
    parser.add_argument("--use-processed", action="store_true", default=True, help="Use processed data if available")
    return parser.parse_args()

def main():
    args = parse_args()
    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in config.")
        return
    lake = DataLake()
    df = None
    if args.use_processed and lake.has_processed_ohlcv(spec, args.timeframe):
        df = lake.load_processed_ohlcv(spec, args.timeframe)
        logger.info(f"Loaded PROCESSED data for {args.symbol} {args.timeframe}")
    elif lake.has_ohlcv(spec, args.timeframe):
        df = lake.load_ohlcv(spec, args.timeframe)
        logger.info(f"Loaded RAW data for {args.symbol} {args.timeframe}")
    else:
        logger.error(f"No OHLCV data found for {args.symbol} {args.timeframe}")
        return
    if df is None or df.empty:
        logger.error("Dataframe is empty.")
        return
    builder = MomentumFeatureSetBuilder()
    include_events = not args.no_events
    if args.full:
        logger.info("Building full momentum feature set...")
        features, summary = builder.build_momentum_features(df, include_events=include_events)
    else:
        logger.info("Building compact momentum feature set...")
        features, summary = builder.build_compact_momentum_features(df, include_events=include_events)
    tail_df = features.tail(args.last)
    report_str = build_momentum_feature_preview_report(args.symbol, args.timeframe, summary, tail_df)

    from config.paths import MOMENTUM_REPORTS_DIR
    out_file = MOMENTUM_REPORTS_DIR / f"momentum_feature_preview_{args.symbol}_{args.timeframe}.txt"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w") as f:
        f.write(report_str)
    print(report_str)
    logger.info(f"Report saved to {out_file}")

if __name__ == "__main__":
    main()
""")

with open('commodity_fx_signal_bot/scripts/run_momentum_batch_build.py', 'w') as f:
    f.write("""import argparse
import logging

from config.settings import settings
from config.symbols import get_symbol_spec, get_enabled_symbols, get_symbols_by_asset_class
from config.symbols import get_allowed_timeframes_for_symbol
from data.storage.data_lake import DataLake
from indicators.feature_builder import FeatureBuilder
from indicators.indicator_pipeline import IndicatorPipeline
from reports.report_builder import build_momentum_batch_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Batch build Momentum features")
    parser.add_argument("--limit", type=int, help="Limit number of symbol/timeframe combos")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Specific symbol to build")
    parser.add_argument("--timeframe", type=str, help="Specific timeframe to build")
    parser.add_argument("--profile", type=str, default=settings.default_scan_profile, help="Scan profile name")
    parser.add_argument("--full", action="store_true", help="Build full feature set")
    parser.add_argument("--no-events", action="store_true", help="Skip events")
    parser.add_argument("--save", action="store_true", default=True, help="Save to data lake")
    parser.add_argument("--use-processed", action="store_true", default=True, help="Use processed data")
    return parser.parse_args()

def main():
    args = parse_args()
    lake = DataLake()
    fb = FeatureBuilder()
    pipeline = IndicatorPipeline(lake, fb, settings)
    specs = []
    if args.symbol:
        spec = get_symbol_spec(args.symbol)
        if spec:
            specs.append(spec)
    else:
        specs = get_symbols_by_asset_class(args.asset_class) if args.asset_class else get_enabled_symbols()
    timeframes_by_symbol = {}
    for s in specs:
        if args.timeframe:
            timeframes_by_symbol[s.symbol] = (args.timeframe,)
        else:
            timeframes_by_symbol[s.symbol] = get_allowed_timeframes_for_symbol(s)
    compact = not args.full
    include_events = not args.no_events
    logger.info(f"Starting batch momentum build. Target: {len(specs)} symbols.")
    results = pipeline.build_momentum_for_universe(
        specs=specs,
        timeframes_by_symbol=timeframes_by_symbol,
        limit=args.limit,
        use_processed=args.use_processed,
        save=args.save,
        compact=compact,
        include_events=include_events,
    )
    report_str = build_momentum_batch_report(results)

    from config.paths import MOMENTUM_REPORTS_DIR
    out_txt = MOMENTUM_REPORTS_DIR / "momentum_batch_summary.txt"
    out_txt.parent.mkdir(parents=True, exist_ok=True)
    with open(out_txt, "w") as f:
        f.write(report_str)
    logger.info(f"Batch completed. Saved text report to {out_txt}")
    import pandas as pd
    df_res = pd.DataFrame(results.get("details", []))
    if not df_res.empty:
        out_csv = MOMENTUM_REPORTS_DIR / "momentum_batch_summary.csv"
        df_res.to_csv(out_csv, index=False)
        logger.info(f"Saved CSV report to {out_csv}")

if __name__ == "__main__":
    main()
""")

with open('commodity_fx_signal_bot/scripts/run_momentum_event_preview.py', 'w') as f:
    f.write("""import argparse
import logging

from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from indicators.momentum_feature_set import MomentumFeatureSetBuilder
from reports.report_builder import build_momentum_event_preview_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Preview Momentum Events")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe")
    parser.add_argument("--last", type=int, default=20, help="Number of recent rows to show")
    parser.add_argument("--use-saved-features", action="store_true", default=False, help="Use already saved momentum features")
    return parser.parse_args()

def main():
    args = parse_args()
    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found.")
        return
    lake = DataLake()
    features = None
    summary = {}
    if args.use_saved_features and lake.has_features(spec, args.timeframe, "momentum"):
        features = lake.load_features(spec, args.timeframe, "momentum")
        logger.info("Loaded pre-calculated momentum features.")
        from indicators.momentum_events import build_momentum_event_frame
        event_df, ev_summary = build_momentum_event_frame(features)
        summary = ev_summary
        summary["input_rows"] = len(features)
        event_tail = event_df.tail(args.last)
    else:
        if lake.has_processed_ohlcv(spec, args.timeframe):
            df = lake.load_processed_ohlcv(spec, args.timeframe)
        elif lake.has_ohlcv(spec, args.timeframe):
            df = lake.load_ohlcv(spec, args.timeframe)
        else:
            logger.error("No OHLCV data found.")
            return
        builder = MomentumFeatureSetBuilder()
        _, fs_summary = builder.build_compact_momentum_features(df, include_events=True)
        summary = fs_summary.get("event_summary", {})
        features_only, _ = builder.build_compact_momentum_features(df, include_events=False)
        from indicators.momentum_events import build_momentum_event_frame
        event_df, _ = build_momentum_event_frame(features_only)
        event_tail = event_df.tail(args.last)
    report_str = build_momentum_event_preview_report(args.symbol, args.timeframe, summary, event_tail)

    from config.paths import MOMENTUM_REPORTS_DIR
    out_file = MOMENTUM_REPORTS_DIR / f"momentum_event_preview_{args.symbol}_{args.timeframe}.txt"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w") as f:
        f.write(report_str)
    print(report_str)
    logger.info(f"Report saved to {out_file}")

if __name__ == "__main__":
    main()
""")

with open('commodity_fx_signal_bot/scripts/run_momentum_status.py', 'w') as f:
    f.write("""import logging

import pandas as pd

from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from config.symbols import get_allowed_timeframes_for_symbol
from reports.report_builder import build_momentum_status_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    lake = DataLake()
    specs = get_enabled_symbols()
    rows = []
    for spec in specs:
        timeframes = get_allowed_timeframes_for_symbol(spec)
        for tf in timeframes:
            has_raw = lake.has_ohlcv(spec, tf)
            has_processed = lake.has_processed_ohlcv(spec, tf)
            has_tech = lake.has_features(spec, tf, "technical")
            has_mom = lake.has_features(spec, tf, "momentum")
            rows.append({
                "Symbol": spec.symbol,
                "Timeframe": tf,
                "Has Raw": has_raw,
                "Has Processed": has_processed,
                "Has Technical": has_tech,
                "Has Momentum": has_mom,
            })
    df = pd.DataFrame(rows)
    summary = {
        "total_combinations": len(df),
        "missing_momentum": len(df[(df["Has Technical"] is True) & (df["Has Momentum"] is False)]),
        "processed_without_momentum": len(df[(df["Has Processed"] is True) & (df["Has Momentum"] is False)]),
    }
    report_str = build_momentum_status_report(df, summary)

    from config.paths import MOMENTUM_REPORTS_DIR
    MOMENTUM_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    txt_path = MOMENTUM_REPORTS_DIR / "momentum_status_report.txt"
    with open(txt_path, "w") as f:
        f.write(report_str)
    csv_path = MOMENTUM_REPORTS_DIR / "momentum_status.csv"
    df.to_csv(csv_path, index=False)
    print(report_str)
    logger.info(f"Saved text report to {txt_path} and CSV to {csv_path}")

if __name__ == "__main__":
    main()
""")

with open('commodity_fx_signal_bot/tests/test_momentum_advanced.py', 'w') as f:
    f.write("""import pytest
import numpy as np
import pandas as pd

from indicators.momentum_advanced import (
    calculate_multi_rsi,
    calculate_multi_roc,
    calculate_multi_momentum,
    calculate_multi_stochastic,
    calculate_multi_williams_r,
    calculate_multi_cci,
    calculate_momentum_slope,
    calculate_momentum_acceleration,
    calculate_relative_momentum_rank,
)


@pytest.fixture
def sample_ohlcv():
    dates = pd.date_range("2023-01-01", periods=100, freq="D")
    df = pd.DataFrame(
        {
            "open": np.random.uniform(100, 200, 100),
            "high": np.random.uniform(150, 250, 100),
            "low": np.random.uniform(50, 150, 100),
            "close": np.random.uniform(100, 200, 100),
            "volume": np.random.uniform(1000, 5000, 100),
        },
        index=dates,
    )
    df["high"] = df[["open", "close", "high"]].max(axis=1)
    df["low"] = df[["open", "close", "low"]].min(axis=1)
    return df


def test_calculate_multi_rsi(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_rsi(df, windows=(7, 14))
    assert "rsi_7" in res.columns
    assert "rsi_14" in res.columns
    assert len(res) == len(df)
    assert df.equals(sample_ohlcv)


def test_calculate_multi_roc(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_roc(df, windows=(5, 10))
    assert "roc_5" in res.columns
    assert "roc_10" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_momentum(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_momentum(df, windows=(5, 10))
    assert "momentum_5" in res.columns
    assert "momentum_10" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_stochastic(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_stochastic(df, windows=(14,), smooth_window=3)
    assert "stoch_k_14_3" in res.columns
    assert "stoch_d_14_3" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_williams_r(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_williams_r(df, windows=(14, 21))
    assert "williams_r_14" in res.columns
    assert "williams_r_21" in res.columns
    assert len(res) == len(df)


def test_calculate_multi_cci(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_multi_cci(df, windows=(14, 20))
    assert "cci_14" in res.columns
    assert "cci_20" in res.columns
    assert len(res) == len(df)


def test_calculate_momentum_slope(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_momentum_slope(df, source_col="close", window=5)
    assert "slope_close_5" in res.columns
    assert len(res) == len(df)


def test_calculate_momentum_acceleration(sample_ohlcv):
    df = sample_ohlcv.copy()
    res = calculate_momentum_acceleration(df, source_col="close", window=5)
    assert "accel_close_5" in res.columns
    assert len(res) == len(df)


def test_calculate_relative_momentum_rank(sample_ohlcv):
    df = sample_ohlcv.copy()
    features = calculate_multi_rsi(df, windows=(7, 14, 21))
    res = calculate_relative_momentum_rank(features, columns=["rsi_7", "rsi_14", "rsi_21"])
    assert "rel_rank_rsi_7" in res.columns
    assert "rel_rank_rsi_21" in res.columns
    assert len(res) == len(df)
""")


with open('commodity_fx_signal_bot/tests/test_momentum_events.py', 'w') as f:
    f.write("""import pytest
import numpy as np
import pandas as pd

from indicators.momentum_events import (
    detect_rsi_zone_events,
    detect_rsi_crossback_events,
    detect_stochastic_cross_events,
    detect_roc_shift_events,
    detect_cci_zone_events,
    detect_momentum_slope_events,
    build_momentum_event_frame,
)


@pytest.fixture
def sample_features():
    dates = pd.date_range("2023-01-01", periods=10)
    df = pd.DataFrame(
        {
            "rsi_14": [50, 40, 25, 35, 60, 75, 65, 50, 20, 40],
            "stoch_k_14_3": [50, 40, 30, 20, 40, 60, 80, 90, 80, 60],
            "stoch_d_14_3": [50, 45, 40, 30, 25, 40, 60, 70, 85, 75],
            "roc_10": [0, -2, -5, 1, 3, 5, 2, -1, -3, 1],
            "cci_20": [0, -50, -150, -50, 0, 150, 50, 0, -120, -80],
            "slope_rsi_14_5": [0, -1, -2, 1, 2, 3, -1, -2, -3, 1],
        },
        index=dates,
    )
    return df


def test_detect_rsi_zone_events(sample_features):
    events = detect_rsi_zone_events(sample_features)
    assert "event_rsi_14_oversold" in events.columns
    assert "event_rsi_14_overbought" in events.columns
    assert events["event_rsi_14_oversold"].iloc[2] == 1
    assert events["event_rsi_14_oversold"].iloc[8] == 1
    assert events["event_rsi_14_overbought"].iloc[5] == 1


def test_detect_rsi_crossback_events(sample_features):
    events = detect_rsi_crossback_events(sample_features)
    assert "event_rsi_14_recovery_cross" in events.columns
    assert "event_rsi_14_bearish_crossback" in events.columns
    assert events["event_rsi_14_recovery_cross"].iloc[3] == 1
    assert events["event_rsi_14_bearish_crossback"].iloc[6] == 1


def test_detect_stochastic_cross_events(sample_features):
    events = detect_stochastic_cross_events(sample_features)
    assert "event_stoch_14_bullish_cross" in events.columns
    assert "event_stoch_14_bearish_cross" in events.columns
    assert events["event_stoch_14_bullish_cross"].iloc[4] == 1
    assert events["event_stoch_14_bearish_cross"].iloc[8] == 1


def test_detect_roc_shift_events(sample_features):
    events = detect_roc_shift_events(sample_features)
    assert "event_roc_10_positive_shift" in events.columns
    assert "event_roc_10_negative_shift" in events.columns
    assert events["event_roc_10_positive_shift"].iloc[3] == 1
    assert events["event_roc_10_negative_shift"].iloc[7] == 1


def test_detect_cci_zone_events(sample_features):
    events = detect_cci_zone_events(sample_features)
    assert "event_cci_20_oversold" in events.columns
    assert "event_cci_20_overbought" in events.columns
    assert events["event_cci_20_oversold"].iloc[2] == 1
    assert events["event_cci_20_overbought"].iloc[5] == 1


def test_detect_momentum_slope_events(sample_features):
    events = detect_momentum_slope_events(sample_features)
    assert "event_momentum_slope_positive_rsi_14_5" in events.columns
    assert "event_momentum_slope_negative_rsi_14_5" in events.columns
    assert events["event_momentum_slope_positive_rsi_14_5"].iloc[3] == 1
    assert events["event_momentum_slope_negative_rsi_14_5"].iloc[1] == 1


def test_build_momentum_event_frame(sample_features):
    event_df, summary = build_momentum_event_frame(sample_features)
    assert len(event_df) == len(sample_features)
    assert "input_rows" in summary
    assert "event_columns" in summary
    assert "total_event_count" in summary
    assert event_df.dtypes.iloc[0] in [np.int64, np.int32, int]
    for col in event_df.columns:
        assert "buy" not in col.lower()
        assert "sell" not in col.lower()
""")


with open('commodity_fx_signal_bot/tests/test_momentum_feature_set.py', 'w') as f:
    f.write("""import pytest
import numpy as np
import pandas as pd

from indicators.momentum_feature_set import MomentumFeatureSetBuilder


@pytest.fixture
def sample_ohlcv():
    dates = pd.date_range("2023-01-01", periods=100)
    df = pd.DataFrame(
        {
            "open": np.random.uniform(100, 200, 100),
            "high": np.random.uniform(150, 250, 100),
            "low": np.random.uniform(50, 150, 100),
            "close": np.random.uniform(100, 200, 100),
            "volume": np.random.uniform(1000, 5000, 100),
        },
        index=dates,
    )
    df["high"] = df[["open", "close", "high"]].max(axis=1)
    df["low"] = df[["open", "close", "low"]].min(axis=1)
    return df


def test_build_compact_momentum_features(sample_ohlcv):
    builder = MomentumFeatureSetBuilder()
    df, summary = builder.build_compact_momentum_features(sample_ohlcv, include_events=True)
    assert not df.empty
    assert len(df) == len(sample_ohlcv)
    assert "rsi_14" in df.columns
    assert "roc_10" in df.columns
    assert "slope_rsi_14_5" in df.columns
    assert "event_rsi_14_oversold" in df.columns
    assert summary["feature_count"] > 0
    assert summary["event_count"] > 0
    assert not df.columns.duplicated().any()


def test_build_full_momentum_features(sample_ohlcv):
    builder = MomentumFeatureSetBuilder()
    df, summary = builder.build_momentum_features(sample_ohlcv, include_events=True)
    assert not df.empty
    assert len(df) == len(sample_ohlcv)
    assert "rsi_28" in df.columns
    assert "accel_rsi_14_5" in df.columns
    assert summary["feature_count"] > 0
    assert summary["event_count"] > 0
    assert not df.columns.duplicated().any()


def test_include_events_flag(sample_ohlcv):
    builder = MomentumFeatureSetBuilder()
    df, summary = builder.build_compact_momentum_features(sample_ohlcv, include_events=False)
    assert summary["event_count"] == 0
    event_cols = [c for c in df.columns if c.startswith("event_")]
    assert len(event_cols) == 0


def test_validate_momentum_features(sample_ohlcv):
    builder = MomentumFeatureSetBuilder()
    df, summary = builder.build_compact_momentum_features(sample_ohlcv)
    val_res = builder.validate_momentum_features(df)
    assert val_res["valid"] is True
    assert val_res["has_inf"] is False
""")

with open('commodity_fx_signal_bot/tests/test_momentum_scripts_contract.py', 'w') as f:
    f.write("""import pytest
import importlib

def test_run_momentum_feature_preview_contract():
    mod = importlib.import_module("scripts.run_momentum_feature_preview")
    assert hasattr(mod, "main")
    assert hasattr(mod, "parse_args")


def test_run_momentum_batch_build_contract():
    mod = importlib.import_module("scripts.run_momentum_batch_build")
    assert hasattr(mod, "main")
    assert hasattr(mod, "parse_args")


def test_run_momentum_event_preview_contract():
    mod = importlib.import_module("scripts.run_momentum_event_preview")
    assert hasattr(mod, "main")
    assert hasattr(mod, "parse_args")


def test_run_momentum_status_contract():
    mod = importlib.import_module("scripts.run_momentum_status")
    assert hasattr(mod, "main")
""")
