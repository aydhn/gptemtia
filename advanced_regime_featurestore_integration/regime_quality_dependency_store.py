"""Phase 134: Regime Quality Dependency Store.

Maintains dependencies on upstream feature quality and drift monitoring layers
(Phase 123, Phase 124, Phase 129, Phase 133).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    QUALITY_DEPENDENCY_STORE_DOMAIN,
    REGIME_STORE_READY,
)

CANONICAL_QUALITY_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "qual_dep_phase_123_feature_quality",
        "source_phase": 123,
        "source_component": "advanced_feature_quality_drift",
        "metric_ref": "feature_quality_score",
        "min_required_score": 0.45,
        "dependency_status": "SATISFIED",
        "non_signal": True,
    },
    {
        "dependency_id": "qual_dep_phase_124_featurestore_contracts",
        "source_phase": 124,
        "source_component": "advanced_feature_store_integration",
        "metric_ref": "featurestore_readiness_score",
        "min_required_score": 0.45,
        "dependency_status": "SATISFIED",
        "non_signal": True,
    },
    {
        "dependency_id": "qual_dep_phase_129_market_behavior_diagnostics",
        "source_phase": 129,
        "source_component": "advanced_market_behavior_diagnostics",
        "metric_ref": "behavior_diagnostics_quality_score",
        "min_required_score": 0.45,
        "dependency_status": "SATISFIED",
        "non_signal": True,
    },
    {
        "dependency_id": "qual_dep_phase_133_regime_validation_acceptance",
        "source_phase": 133,
        "source_component": "advanced_regime_validation_acceptance",
        "metric_ref": "regime_acceptance_score",
        "min_required_score": 0.45,
        "dependency_status": "SATISFIED",
        "non_signal": True,
    },
]


def build_regime_quality_dependency_store_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for quality dependency store."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_QUALITY_DEPENDENCIES)
    summary = {
        "domain": QUALITY_DEPENDENCY_STORE_DOMAIN,
        "total_dependencies": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_satisfied": bool((df["dependency_status"] == "SATISFIED").all()),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "status": REGIME_STORE_READY,
    }
    return df, summary


def summarize_regime_quality_dependency_store(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize quality dependency store DataFrame."""
    return {
        "total_dependencies": len(df),
        "dependency_ids": df["dependency_id"].tolist() if not df.empty else [],
        "all_satisfied": bool((df["dependency_status"] == "SATISFIED").all()) if not df.empty else True,
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
