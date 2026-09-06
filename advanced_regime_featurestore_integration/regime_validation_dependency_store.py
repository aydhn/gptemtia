"""Phase 134: Regime Validation Dependency Store.

Maintains dependencies on formal validation and acceptance layers
from Phase 125, Phase 133, and related subsystems.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_STORE_READY,
    VALIDATION_DEPENDENCY_STORE_DOMAIN,
)

CANONICAL_VALIDATION_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "val_dep_phase_125_feature_factor_acceptance",
        "source_phase": 125,
        "source_component": "advanced_feature_factor_acceptance",
        "validation_ref": "feature_factor_acceptance_manifest",
        "validation_status": "SATISFIED",
        "non_signal": True,
    },
    {
        "dependency_id": "val_dep_phase_126_regime_foundation_validation",
        "source_phase": 126,
        "source_component": "advanced_regime_foundation",
        "validation_ref": "regime_foundation_validation_report",
        "validation_status": "SATISFIED",
        "non_signal": True,
    },
    {
        "dependency_id": "val_dep_phase_127_regime_matrix_validation",
        "source_phase": 127,
        "source_component": "advanced_regime_matrix",
        "validation_ref": "regime_matrix_validation_report",
        "validation_status": "SATISFIED",
        "non_signal": True,
    },
    {
        "dependency_id": "val_dep_phase_128_rule_free_validation",
        "source_phase": 128,
        "source_component": "advanced_regime_rule_free",
        "validation_ref": "regime_rule_free_validation_report",
        "validation_status": "SATISFIED",
        "non_signal": True,
    },
    {
        "dependency_id": "val_dep_phase_130_transition_validation",
        "source_phase": 130,
        "source_component": "advanced_regime_transition",
        "validation_ref": "regime_transition_validation_report",
        "validation_status": "SATISFIED",
        "non_signal": True,
    },
    {
        "dependency_id": "val_dep_phase_131_cross_asset_validation",
        "source_phase": 131,
        "source_component": "advanced_cross_asset_regime_context",
        "validation_ref": "cross_asset_regime_validation_report",
        "validation_status": "SATISFIED",
        "non_signal": True,
    },
    {
        "dependency_id": "val_dep_phase_132_macro_news_validation",
        "source_phase": 132,
        "source_component": "advanced_macro_event_news_regime",
        "validation_ref": "macro_event_news_regime_validation_report",
        "validation_status": "SATISFIED",
        "non_signal": True,
    },
    {
        "dependency_id": "val_dep_phase_133_regime_validation_acceptance",
        "source_phase": 133,
        "source_component": "advanced_regime_validation_acceptance",
        "validation_ref": "regime_validation_acceptance_manifest",
        "validation_status": "SATISFIED",
        "non_signal": True,
    },
]


def build_regime_validation_dependency_store_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for validation dependency store."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_VALIDATION_DEPENDENCIES)
    summary = {
        "domain": VALIDATION_DEPENDENCY_STORE_DOMAIN,
        "total_dependencies": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_satisfied": bool((df["validation_status"] == "SATISFIED").all()),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "status": REGIME_STORE_READY,
    }
    return df, summary


def summarize_regime_validation_dependency_store(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize validation dependency store DataFrame."""
    return {
        "total_dependencies": len(df),
        "dependency_ids": df["dependency_id"].tolist() if not df.empty else [],
        "all_satisfied": bool((df["validation_status"] == "SATISFIED").all()) if not df.empty else True,
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
