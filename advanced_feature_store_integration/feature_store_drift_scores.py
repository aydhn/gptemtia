"""Phase 124 Feature Store Drift Scores."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

STORE_DRIFT_SCORES = [
    {
        "score_id": "DSC_001",
        "feature_name": "sma_20",
        "entity_id": "eurusd",
        "drift_score": 0.05,
        "ks_statistic": 0.04,
        "psi_score": 0.03,
        "drift_detected": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "score_id": "DSC_002",
        "feature_name": "ema_50",
        "entity_id": "eurusd",
        "drift_score": 0.04,
        "ks_statistic": 0.03,
        "psi_score": 0.02,
        "drift_detected": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "score_id": "DSC_003",
        "feature_name": "rsi_14",
        "entity_id": "eurusd",
        "drift_score": 0.08,
        "ks_statistic": 0.07,
        "psi_score": 0.05,
        "drift_detected": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "score_id": "DSC_004",
        "feature_name": "atr_14",
        "entity_id": "brent",
        "drift_score": 0.07,
        "ks_statistic": 0.06,
        "psi_score": 0.04,
        "drift_detected": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "score_id": "DSC_005",
        "feature_name": "rolling_mean_20",
        "entity_id": "brent",
        "drift_score": 0.03,
        "ks_statistic": 0.02,
        "psi_score": 0.01,
        "drift_detected": False,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "score_id": "DSC_006",
        "feature_name": "brent_eurusd_corr_30",
        "entity_id": "cross_asset",
        "drift_score": 0.12,
        "ks_statistic": 0.11,
        "psi_score": 0.08,
        "drift_detected": False,
        "non_signal": True,
        "source_preserved": True,
    },
]


def build_feature_store_drift_score_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of feature drift scores."""
    records = list(STORE_DRIFT_SCORES)
    df = pd.DataFrame(records)
    mean_drift = float(df["drift_score"].mean()) if not df.empty else 0.0
    summary = {
        "total_drift_scores": len(records),
        "mean_drift_score": round(mean_drift, 4),
        "any_drift_detected": any(r["drift_detected"] for r in records),
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_drift_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize drift scores."""
    if df.empty:
        return {"total_scores": 0, "mean_drift_score": 0.0, "non_signal": True}
    return {
        "total_scores": len(df),
        "mean_drift_score": round(float(df["drift_score"].mean()), 4) if "drift_score" in df.columns else 0.0,
        "max_drift_score": round(float(df["drift_score"].max()), 4) if "drift_score" in df.columns else 0.0,
        "all_non_signal": bool(all(df.get("non_signal", [True]))),
    }
