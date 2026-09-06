"""Phase 134: Regime Lineage References.

Tracks end-to-end data and contract provenance across the entire regime block
from Phase 126 through Phase 134.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    LINEAGE_REFERENCE_DOMAIN,
    REGIME_STORE_READY,
)

CANONICAL_LINEAGE_STEPS: List[Dict[str, Any]] = [
    {
        "lineage_id": "lineage_p126_foundation",
        "source_phase": 126,
        "source_component": "advanced_regime_foundation",
        "target_component": "advanced_regime_matrix",
        "dependency_chain": "phase_126_taxonomy -> phase_127_matrix",
        "traceability_status": "VERIFIED",
        "non_signal": True,
    },
    {
        "lineage_id": "lineage_p127_matrix",
        "source_phase": 127,
        "source_component": "advanced_regime_matrix",
        "target_component": "advanced_regime_rule_free",
        "dependency_chain": "phase_127_matrix -> phase_128_candidate_states",
        "traceability_status": "VERIFIED",
        "non_signal": True,
    },
    {
        "lineage_id": "lineage_p128_rule_free",
        "source_phase": 128,
        "source_component": "advanced_regime_rule_free",
        "target_component": "advanced_market_behavior_diagnostics",
        "dependency_chain": "phase_128_states -> phase_129_diagnostics",
        "traceability_status": "VERIFIED",
        "non_signal": True,
    },
    {
        "lineage_id": "lineage_p129_diagnostics",
        "source_phase": 129,
        "source_component": "advanced_market_behavior_diagnostics",
        "target_component": "advanced_regime_transition",
        "dependency_chain": "phase_129_diagnostics -> phase_130_transition",
        "traceability_status": "VERIFIED",
        "non_signal": True,
    },
    {
        "lineage_id": "lineage_p130_transition",
        "source_phase": 130,
        "source_component": "advanced_regime_transition",
        "target_component": "advanced_cross_asset_regime_context",
        "dependency_chain": "phase_130_transition -> phase_131_cross_asset",
        "traceability_status": "VERIFIED",
        "non_signal": True,
    },
    {
        "lineage_id": "lineage_p131_cross_asset",
        "source_phase": 131,
        "source_component": "advanced_cross_asset_regime_context",
        "target_component": "advanced_macro_event_news_regime",
        "dependency_chain": "phase_131_cross_asset -> phase_132_macro_news",
        "traceability_status": "VERIFIED",
        "non_signal": True,
    },
    {
        "lineage_id": "lineage_p132_macro_news",
        "source_phase": 132,
        "source_component": "advanced_macro_event_news_regime",
        "target_component": "advanced_regime_validation_acceptance",
        "dependency_chain": "phase_132_macro_news -> phase_133_validation_acceptance",
        "traceability_status": "VERIFIED",
        "non_signal": True,
    },
    {
        "lineage_id": "lineage_p133_validation_acceptance",
        "source_phase": 133,
        "source_component": "advanced_regime_validation_acceptance",
        "target_component": "advanced_regime_featurestore_integration",
        "dependency_chain": "phase_133_validation_acceptance -> phase_134_featurestore",
        "traceability_status": "VERIFIED",
        "non_signal": True,
    },
    {
        "lineage_id": "lineage_p134_featurestore_integration",
        "source_phase": 134,
        "source_component": "advanced_regime_featurestore_integration",
        "target_component": "phase_135_regime_classification_acceptance_report",
        "dependency_chain": "phase_134_featurestore -> phase_135_acceptance_report",
        "traceability_status": "VERIFIED",
        "non_signal": True,
    },
]


def build_regime_lineage_reference_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for regime lineage references."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_LINEAGE_STEPS)
    summary = {
        "domain": LINEAGE_REFERENCE_DOMAIN,
        "total_lineage_steps": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_verified": bool((df["traceability_status"] == "VERIFIED").all()),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "status": REGIME_STORE_READY,
    }
    return df, summary


def summarize_regime_lineage_references(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize lineage reference DataFrame."""
    return {
        "total_lineage_steps": len(df),
        "lineage_ids": df["lineage_id"].tolist() if not df.empty else [],
        "all_verified": bool((df["traceability_status"] == "VERIFIED").all()) if not df.empty else True,
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
