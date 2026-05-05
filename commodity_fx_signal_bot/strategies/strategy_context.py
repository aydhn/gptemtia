import logging

import pandas as pd

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake

logger = logging.getLogger(__name__)


class StrategyContextLoader:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_decision_candidates(
        self,
        spec: SymbolSpec,
        timeframe: str,
        profile_name: str | None = None,
    ) -> tuple[pd.DataFrame, dict]:
        summary = {"missing_decision_candidates": False, "loaded_rows": 0}

        if not self.data_lake.has_features(spec, timeframe, "decision_candidates"):
            summary["missing_decision_candidates"] = True
            return pd.DataFrame(), summary

        try:
            df = self.data_lake.load_features(spec, timeframe, "decision_candidates")
            summary["loaded_rows"] = len(df)
            return df, summary
        except Exception as e:
            logger.error(f"Error loading decision candidates for {spec.symbol}: {e}")
            summary["missing_decision_candidates"] = True
            return pd.DataFrame(), summary

    def load_strategy_context_frames(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        frames = {}
        missing_frames = []

        feature_sets = [
            "regime",
            "regime_events",
            "mtf",
            "mtf_events",
            "macro_events",
            "asset_profiles",
            "asset_profile_events",
            "signal_candidates",
            "trend",
            "momentum",
            "volatility",
            "price_action",
            "divergence",
        ]

        for fset in feature_sets:
            try:
                if self.data_lake.has_features(spec, timeframe, fset):
                    df = self.data_lake.load_features(spec, timeframe, fset)
                    if not df.empty:
                        frames[fset] = df
                    else:
                        missing_frames.append(fset)
                else:
                    missing_frames.append(fset)
            except Exception:
                missing_frames.append(fset)

        summary = {
            "missing_context_frames": missing_frames,
            "loaded_frames": list(frames.keys()),
        }
        return frames, summary

    def get_context_snapshot(
        self,
        context_frames: dict[str, pd.DataFrame],
        timestamp: pd.Timestamp,
    ) -> dict:
        snapshot = {}

        for name, df in context_frames.items():
            if df.empty:
                continue
            try:
                idx = df.index.get_indexer([timestamp], method="ffill")[0]
                if idx != -1:
                    row = df.iloc[idx].to_dict()
                    snapshot[name] = row
            except Exception:
                pass

        return snapshot
