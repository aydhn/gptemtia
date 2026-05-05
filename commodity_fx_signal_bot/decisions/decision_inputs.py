import pandas as pd
from typing import Dict, Tuple, Optional
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
import logging

logger = logging.getLogger(__name__)


class DecisionInputLoader:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_signal_candidates(
        self,
        spec: SymbolSpec,
        timeframe: str,
        profile_name: Optional[str] = None,
    ) -> Tuple[pd.DataFrame, Dict]:
        try:
            if self.data_lake.has_features(spec, timeframe, "signal_candidates"):
                df = self.data_lake.load_features(spec, timeframe, "signal_candidates")
                return df, {"loaded": True, "count": len(df)}
        except Exception as e:
            logger.error(f"Error loading signal candidates for {spec.symbol}: {e}")
        return pd.DataFrame(), {"loaded": False, "count": 0}

    def load_decision_context(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        context_frames = {}
        missing_frames = []

        frames_to_load = [
            "regime",
            "regime_events",
            "mtf",
            "mtf_events",
            "asset_profiles",
            "asset_profile_events",
            "trend",
            "momentum",
            "volatility",
            "mean_reversion",
            "price_action",
            "divergence",
        ]

        for frame in frames_to_load:
            try:
                if self.data_lake.has_features(spec, timeframe, frame):
                    context_frames[frame] = self.data_lake.load_features(
                        spec, timeframe, frame
                    )
                else:
                    missing_frames.append(frame)
            except Exception:
                missing_frames.append(frame)

        # Macro is symbol-independent, load separately
        try:
            macro_df = self.data_lake.load_feature_set("macro", "macro_features")
            context_frames["macro"] = macro_df
        except Exception:
            missing_frames.append("macro")

        try:
            macro_events_df = self.data_lake.load_feature_set(
                "macro_events", "macro_events"
            )
            context_frames["macro_events"] = macro_events_df
        except Exception:
            missing_frames.append("macro_events")

        summary = {
            "loaded_frames": list(context_frames.keys()),
            "missing_frames": missing_frames,
        }

        return context_frames, summary

    def load_latest_context_row(
        self,
        context_frames: Dict[str, pd.DataFrame],
        timestamp: pd.Timestamp,
    ) -> Dict:
        latest_context = {}

        for frame_name, df in context_frames.items():
            if df.empty:
                latest_context[frame_name] = pd.Series(dtype=object)
                continue

            try:
                # Ensure index is datetime for asof
                if not isinstance(df.index, pd.DatetimeIndex):
                    df = df.copy()
                    df.index = pd.to_datetime(df.index)

                # Use asof to get latest data point without lookahead
                idx = df.index.asof(timestamp)
                if pd.isna(idx):
                    latest_context[frame_name] = pd.Series(dtype=object)
                else:
                    latest_context[frame_name] = df.loc[idx]
            except Exception as e:
                logger.warning(f"Error extracting latest context for {frame_name}: {e}")
                latest_context[frame_name] = pd.Series(dtype=object)

        return latest_context
