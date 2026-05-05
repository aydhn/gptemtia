import logging
import pandas as pd
from typing import Optional

from config.symbols import SymbolSpec
from config.settings import Settings
from data.storage.data_lake import DataLake
from asset_profiles.asset_profile_config import get_asset_profile, AssetProfile
from asset_profiles.asset_class_registry import (
    group_symbols_by_asset_class,
    get_group_members,
    filter_symbols_for_group_analysis,
)
from asset_profiles.asset_behavior_features import build_asset_behavior_features
from asset_profiles.group_features import build_group_feature_frame
from asset_profiles.relative_strength import build_relative_strength_features
from asset_profiles.correlation_features import (
    calculate_symbol_group_correlation,
    calculate_macro_correlation_features,
)
from asset_profiles.dispersion_features import build_dispersion_feature_frame
from asset_profiles.asset_class_regime import (
    classify_asset_behavior_regime,
    classify_group_regime,
    classify_relative_strength_regime,
    classify_correlation_regime,
)
from asset_profiles.asset_class_events import build_asset_class_event_frame
from asset_profiles.asset_profile_quality import build_asset_profile_quality_report

logger = logging.getLogger(__name__)


class AssetProfilePipeline:
    """Orchestrates the creation of asset profiles, group features, and events."""

    def __init__(self, data_lake: DataLake, settings: Settings, timeframe: str = "1d"):
        self.data_lake = data_lake
        self.settings = settings
        self.timeframe = timeframe
        self.group_cache = {}

    def build_symbol_input_frame(
        self, spec: SymbolSpec, timeframe: str
    ) -> tuple[pd.DataFrame, dict]:
        """Load all available feature sets for a symbol."""
        summary = {"missing_feature_sets": [], "warnings": []}

        feature_sets = [
            "technical",
            "trend",
            "momentum",
            "volatility",
            "volume",
            "mean_reversion",
            "price_action",
            "divergence",
            "mtf",
            "regime",
        ]

        frames = []
        for fset in feature_sets:
            try:
                if self.data_lake.has_features(spec, timeframe, fset):
                    df = self.data_lake.load_features(spec, timeframe, fset)
                    # Deduplicate columns before concat to avoid "regime_primary_label" collision
                    df = df.loc[:, ~df.columns.duplicated()]
                    frames.append(df)
                else:
                    summary["missing_feature_sets"].append(fset)
            except Exception as e:
                summary["warnings"].append(f"Error loading {fset}: {e}")

        if not frames:
            return pd.DataFrame(), summary

        combined = pd.concat(frames, axis=1)
        # Drop fully duplicate columns
        combined = combined.loc[:, ~combined.columns.duplicated()]

        return combined, summary

    def build_group_inputs(
        self, specs: list[SymbolSpec], asset_class: str, timeframe: str
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        """Build input frames for all members of a group."""
        summary = {"warnings": []}
        data_by_symbol = {}

        members = get_group_members(specs, asset_class)
        for spec in members:
            df, _ = self.build_symbol_input_frame(spec, timeframe)
            if not df.empty:
                data_by_symbol[spec.symbol] = df

        return data_by_symbol, summary

    def _get_group_features(
        self,
        asset_class: str,
        data_by_symbol: dict[str, pd.DataFrame],
        save: bool = True,
    ):
        """Build and cache group features."""
        cache_key = f"{asset_class}_{self.timeframe}"
        if cache_key in self.group_cache:
            return self.group_cache[cache_key]

        group_features, group_summary = build_group_feature_frame(
            asset_class, data_by_symbol
        )

        # Dispersion
        if data_by_symbol:
            from asset_profiles.group_features import (
                build_group_return_matrix,
                build_group_price_matrix,
            )

            price_matrix = build_group_price_matrix(data_by_symbol)
            return_matrix = build_group_return_matrix(price_matrix)
            disp_features, _ = build_dispersion_feature_frame(
                asset_class, return_matrix
            )
            group_features = pd.concat([group_features, disp_features], axis=1)

        if save and not group_features.empty:
            self.data_lake.save_group_features(
                asset_class, self.timeframe, group_features
            )

        self.group_cache[cache_key] = (group_features, group_summary, data_by_symbol)
        return self.group_cache[cache_key]

    def build_for_symbol(
        self,
        spec: SymbolSpec,
        all_symbols: list[SymbolSpec],
        timeframe: str = "1d",
        save: bool = True,
        include_events: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        """Build full asset profile for a single symbol."""
        summary = {
            "symbol": spec.symbol,
            "asset_class": spec.asset_class,
            "timeframe": timeframe,
            "warnings": [],
            "missing_feature_sets": [],
        }

        if spec.asset_class in ("macro", "synthetic", "benchmark"):
            summary["warnings"].append(
                "Skipped: Not a tradeable asset class for behavior profile."
            )
            return pd.DataFrame(), summary

        try:
            asset_profile = get_asset_profile(spec.asset_class)
            summary["asset_profile"] = asset_profile.name
        except Exception as e:
            summary["warnings"].append(str(e))
            return pd.DataFrame(), summary

        # Load inputs
        df, input_summary = self.build_symbol_input_frame(spec, timeframe)
        summary["missing_feature_sets"] = input_summary.get("missing_feature_sets", [])
        if df.empty:
            summary["warnings"].append("Empty input dataframe.")
            return pd.DataFrame(), summary

        # Build group inputs
        data_by_symbol, _ = self.build_group_inputs(
            all_symbols, spec.asset_class, timeframe
        )
        summary["group_member_count"] = len(
            get_group_members(all_symbols, spec.asset_class)
        )
        summary["available_group_members"] = len(data_by_symbol)

        # Build symbol behavior features
        features, _ = build_asset_behavior_features(
            df, asset_profile, spec.symbol, timeframe
        )

        # Group contextual features
        group_features, _, _ = self._get_group_features(
            spec.asset_class, data_by_symbol, save=save
        )

        # Join relevant group features
        if not group_features.empty:
            features = pd.concat([features, group_features], axis=1)

            # Relative Strength
            group_idx_col = f"group_{spec.asset_class}_index"
            group_idx = (
                group_features[group_idx_col]
                if group_idx_col in group_features.columns
                else None
            )

            from asset_profiles.group_features import (
                build_group_return_matrix,
                build_group_price_matrix,
            )

            price_matrix = build_group_price_matrix(data_by_symbol)
            return_matrix = build_group_return_matrix(price_matrix)

            rs_features, _ = build_relative_strength_features(
                spec.symbol, df, group_idx, return_matrix
            )
            features = pd.concat([features, rs_features], axis=1)

            # Correlation
            if group_idx is not None and "close" in df.columns:
                sym_ret = df["close"].pct_change()
                grp_ret = group_idx.pct_change()
                corr_features = calculate_symbol_group_correlation(sym_ret, grp_ret)
                features = pd.concat([features, corr_features], axis=1)

        # Regimes
        beh_regime, _ = classify_asset_behavior_regime(features, asset_profile)
        grp_regime, _ = classify_group_regime(features, spec.asset_class)
        rs_regime, _ = classify_relative_strength_regime(features)
        corr_regime, _ = classify_correlation_regime(features)

        features = pd.concat(
            [features, beh_regime, grp_regime, rs_regime, corr_regime], axis=1
        )

        # Summary metrics
        if "asset_behavior_regime_label" in features.columns:
            summary["latest_asset_regime"] = features[
                "asset_behavior_regime_label"
            ].iloc[-1]
        if "asset_group_regime_label" in features.columns:
            summary["latest_group_regime"] = features["asset_group_regime_label"].iloc[
                -1
            ]
        if "asset_relative_strength_regime_label" in features.columns:
            summary["latest_relative_strength_label"] = features[
                "asset_relative_strength_regime_label"
            ].iloc[-1]

        summary["rows"] = len(features)
        summary["columns"] = list(features.columns)

        # Quality
        quality = build_asset_profile_quality_report(features, summary)
        summary["quality_report"] = quality

        # Save Features
        if save:
            self.data_lake.save_features(
                spec, timeframe, features, feature_set_name="asset_profiles"
            )

        # Events
        if include_events:
            events, event_summary = build_asset_class_event_frame(features)
            summary["event_summary"] = event_summary
            if save:
                self.data_lake.save_features(
                    spec, timeframe, events, feature_set_name="asset_profile_events"
                )

        return features, summary

    def build_for_asset_class(
        self,
        asset_class: str,
        symbols: list[SymbolSpec],
        timeframe: str = "1d",
        save: bool = True,
        include_events: bool = True,
    ) -> dict:
        """Build asset profiles for all members of an asset class."""
        summary = {"asset_class": asset_class, "symbols": {}, "warnings": []}
        members = get_group_members(symbols, asset_class)

        for spec in members:
            try:
                _, sym_summary = self.build_for_symbol(
                    spec, symbols, timeframe, save, include_events
                )
                summary["symbols"][spec.symbol] = sym_summary
            except Exception as e:
                logger.error(f"Error building asset profile for {spec.symbol}: {e}")
                summary["warnings"].append(f"{spec.symbol}: {e}")

        return summary

    def build_for_universe(
        self,
        symbols: list[SymbolSpec],
        timeframe: str = "1d",
        limit: int | None = None,
        save: bool = True,
        include_events: bool = True,
    ) -> dict:
        """Build asset profiles for the entire universe."""
        summary = {"processed": 0, "errors": 0, "asset_classes": {}}

        tradeable_groups = filter_symbols_for_group_analysis(symbols)

        processed_count = 0
        for ac, members in tradeable_groups.items():
            if limit and processed_count >= limit:
                break

            # To limit strictly, we slice the members
            if limit:
                members = members[: limit - processed_count]

            ac_summary = self.build_for_asset_class(
                ac, symbols, timeframe, save, include_events
            )
            summary["asset_classes"][ac] = ac_summary

            success_count = sum(
                1
                for sym_sum in ac_summary["symbols"].values()
                if not sym_sum.get("warnings")
            )
            summary["processed"] += success_count
            summary["errors"] += len(members) - success_count
            processed_count += len(members)

        return summary
