import pandas as pd
import logging
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore

logger = logging.getLogger(__name__)


class EventLoader:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake
        self.feature_store = FeatureStore(data_lake)

        self.event_group_mapping = {
            "momentum": "momentum_events",
            "trend": "trend_events",
            "volatility": "volatility_events",
            "volume": "volume_events",
            "mean_reversion": "mean_reversion_events",
            "price_action": "price_action_events",
            "divergence": "divergence_events",
            "mtf": "mtf_events",
            "regime": "regime_events",
            "macro": "macro_events",
            "asset_profile": "asset_profile_events",
        }

    def load_event_frames(
        self,
        spec: SymbolSpec,
        timeframe: str,
        event_groups: tuple[str, ...],
    ) -> tuple[dict[str, pd.DataFrame], dict]:

        event_frames = {}
        missing_event_groups = []

        for group in event_groups:
            if group not in self.event_group_mapping:
                logger.warning(f"Unknown event group requested: {group}")
                missing_event_groups.append(group)
                continue

            feature_set_name = self.event_group_mapping[group]

            try:
                # Handle macro specially as it doesn't take spec and timeframe normally
                if group == "macro":
                    df = self.feature_store.load_macro_events()
                # Handle asset profile specially
                elif group == "asset_profile":
                    df = self.feature_store.load_asset_profile_events(spec, timeframe)
                # Handle standard technical events
                else:
                    if self.data_lake.has_features(spec, timeframe, feature_set_name):
                        df = self.data_lake.load_features(
                            spec, timeframe, feature_set_name
                        )
                    else:
                        df = pd.DataFrame()

                if df is not None and not df.empty:
                    # ensure datetime index
                    if not isinstance(df.index, pd.DatetimeIndex):
                        if "date" in df.columns:
                            df = df.set_index("date")
                            df.index = pd.to_datetime(df.index)
                        elif "time" in df.columns:
                            df = df.set_index("time")
                            df.index = pd.to_datetime(df.index)
                        elif "timestamp" in df.columns:
                            df = df.set_index("timestamp")
                            df.index = pd.to_datetime(df.index)
                        else:
                            df.index = pd.to_datetime(df.index)

                    if df.index.duplicated().any():
                        logger.warning(
                            f"Duplicate index found in event group {group} for {spec.symbol}"
                        )
                        df = df[~df.index.duplicated(keep="last")]

                    event_frames[group] = df
                else:
                    missing_event_groups.append(group)
            except Exception as e:
                logger.warning(
                    f"Failed to load event group {group} for {spec.symbol}: {e}"
                )
                missing_event_groups.append(group)

        summary = {
            "loaded_groups": list(event_frames.keys()),
            "missing_event_groups": missing_event_groups,
        }

        return event_frames, summary

    def load_context_frames(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> tuple[dict[str, pd.DataFrame], dict]:

        context_frames = {}
        missing_contexts = []

        # Load trend context
        try:
            if self.data_lake.has_features(spec, timeframe, "trend"):
                df = self.data_lake.load_features(spec, timeframe, "trend")
                if df is not None and not df.empty:
                    context_frames["trend"] = df
            else:
                missing_contexts.append("trend")
        except Exception:
            missing_contexts.append("trend")

        # Load mtf context
        try:
            df = self.feature_store.load_mtf_features(spec, timeframe)
            if df is not None and not df.empty:
                context_frames["mtf"] = df
            else:
                missing_contexts.append("mtf")
        except Exception:
            missing_contexts.append("mtf")

        # Load regime context
        try:
            df = self.feature_store.load_regime_features(spec, timeframe)
            if df is not None and not df.empty:
                context_frames["regime"] = df
            else:
                missing_contexts.append("regime")
        except Exception:
            missing_contexts.append("regime")

        # Load macro context
        try:
            df = self.feature_store.load_macro_features()
            if df is not None and not df.empty:
                context_frames["macro"] = df
            else:
                missing_contexts.append("macro")
        except Exception:
            missing_contexts.append("macro")

        # Load asset profile context
        try:
            df = self.feature_store.load_asset_profile_features(spec, timeframe)
            if df is not None and not df.empty:
                context_frames["asset_profile"] = df
            else:
                missing_contexts.append("asset_profile")
        except Exception:
            missing_contexts.append("asset_profile")

        # Load technical basic context (for volatility, momentum etc)
        try:
            if self.data_lake.has_features(spec, timeframe, "technical"):
                df = self.data_lake.load_features(spec, timeframe, "technical")
                if df is not None and not df.empty:
                    context_frames["technical"] = df
            else:
                missing_contexts.append("technical")
        except Exception:
            missing_contexts.append("technical")

        summary = {
            "loaded_contexts": list(context_frames.keys()),
            "missing_contexts": missing_contexts,
        }

        return context_frames, summary
