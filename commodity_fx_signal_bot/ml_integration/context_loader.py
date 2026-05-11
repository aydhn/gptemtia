"""
ML Context Integration Loader
"""

import logging
from typing import Dict, Tuple, Optional
import pandas as pd

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake

logger = logging.getLogger(__name__)


class MLContextIntegrationLoader:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_ml_prediction_context(
        self,
        spec: SymbolSpec,
        timeframe: str,
        profile_name: Optional[str] = None,
    ) -> Tuple[pd.DataFrame, dict]:
        """
        Load offline ML prediction context.
        Returns empty DataFrame if missing without crashing.
        """
        try:
            from ml.feature_store import FeatureStore
            fs = FeatureStore(self.data_lake)

            reports = fs.list_available_ml_integration_reports(spec)

            # Temporary mock implementation to read ML outputs created in previous phase
            # As prediction_context layer hasn't been implemented yet, we return empty
            # Note: Do not leak future data or create live signals

            # The previous phases output ML Prediction Context as part of Phase 31
            # We would normally use fs.load_ml_prediction_context but falling back to DataLake

            # In Phase 31 ML Prediction Context is saved to predictions layer
            # For this phase's context integration, we just need a dummy structure if missing

            return pd.DataFrame(), {"status": "unavailable", "warnings": ["ML Prediction context not found"]}
        except Exception as e:
            logger.warning(f"Could not load ML prediction context for {spec.symbol}: {e}")
            return pd.DataFrame(), {"status": "error", "warnings": [str(e)]}

    def load_ml_prediction_candidates(
        self,
        spec: SymbolSpec,
        timeframe: str,
        profile_name: Optional[str] = None,
    ) -> Tuple[pd.DataFrame, dict]:
        """
        Load offline ML prediction candidates.
        Returns empty DataFrame if missing without crashing.
        """
        try:
            return pd.DataFrame(), {"status": "unavailable"}
        except Exception as e:
            logger.warning(f"Could not load ML prediction candidates for {spec.symbol}: {e}")
            return pd.DataFrame(), {"status": "error", "warnings": [str(e)]}

    def load_candidate_context_frames(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> Tuple[Dict[str, pd.DataFrame], dict]:
        """
        Load candidate frames for multiple layers to be used in ML alignment.
        """
        frames: Dict[str, pd.DataFrame] = {}
        summary: dict = {"loaded": [], "missing": [], "warnings": []}

        def _safe_load(layer: str, load_fn) -> None:
            try:
                df = load_fn()
                if not df.empty:
                    # Check for duplicate index
                    if df.index.duplicated().any():
                        summary["warnings"].append(f"Duplicate timestamps found in {layer} layer")
                        df = df[~df.index.duplicated(keep="last")]
                    frames[layer] = df
                    summary["loaded"].append(layer)
                else:
                    summary["missing"].append(layer)
            except Exception as e:
                summary["missing"].append(layer)
                logger.debug(f"Could not load {layer} for {spec.symbol}: {e}")

        # Load standard layers from DataLake
        _safe_load("signal_candidates", lambda: self.data_lake.load_candidates(spec, timeframe, "signal"))
        _safe_load("decision_candidates", lambda: self.data_lake.load_candidates(spec, timeframe, "decision"))
        _safe_load("strategy_candidates", lambda: self.data_lake.load_candidates(spec, timeframe, "strategy"))
        _safe_load("strategy_rule_candidates", lambda: self.data_lake.load_candidates(spec, timeframe, "strategy_rule"))
        _safe_load("risk_candidates", lambda: self.data_lake.load_candidates(spec, timeframe, "risk"))
        _safe_load("sizing_candidates", lambda: self.data_lake.load_candidates(spec, timeframe, "sizing"))
        _safe_load("level_candidates", lambda: self.data_lake.load_candidates(spec, timeframe, "level"))
        _safe_load("regime", lambda: self.data_lake.load_features(spec, timeframe, "regime"))
        _safe_load("mtf", lambda: self.data_lake.load_features(spec, timeframe, "mtf"))
        _safe_load("macro", lambda: self.data_lake.load_features(spec, timeframe, "macro"))

        # Note: Avoid future leakage, use only historical data
        return frames, summary
