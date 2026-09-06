"""Phase 134: Transition Store Catalog.

Connects Phase 130 regime transition and stability outputs to the FeatureStore catalog.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_STORE_READY,
    STORE_ENTITY_TRANSITION,
    TRANSITION_STORE_CATALOG_DOMAIN,
)

CANONICAL_TRANSITION_ITEMS: List[Dict[str, Any]] = [
    {
        "store_catalog_name": "regime_transition_frequency_matrix",
        "store_entity_type": STORE_ENTITY_TRANSITION,
        "source_phase": 130,
        "source_component": "advanced_regime_transition",
        "source_report_ref": "reports/output/advanced_regime_transition/report_balanced_local_regime_transition.json",
        "validation_acceptance_ref": "phase_133_gate_transition_acceptance_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "regime_stability_persistence_scores",
        "store_entity_type": STORE_ENTITY_TRANSITION,
        "source_phase": 130,
        "source_component": "advanced_regime_transition",
        "source_report_ref": "reports/output/advanced_regime_transition/report_balanced_local_regime_transition.json",
        "validation_acceptance_ref": "phase_133_gate_transition_acceptance_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "regime_transition_ambiguity_diagnostics",
        "store_entity_type": STORE_ENTITY_TRANSITION,
        "source_phase": 130,
        "source_component": "advanced_regime_transition",
        "source_report_ref": "reports/output/advanced_regime_transition/report_balanced_local_regime_transition.json",
        "validation_acceptance_ref": "phase_133_gate_transition_acceptance_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
]


def build_transition_store_catalog(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for transition store catalog."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_TRANSITION_ITEMS)
    summary = {
        "domain": TRANSITION_STORE_CATALOG_DOMAIN,
        "total_items": len(df),
        "active_profile": active_profile.profile_name,
        "source_phase": 130,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "all_source_preserved": bool((df["source_preserved"] == True).all()),
        "production_ready": False,
        "broker_ready": False,
        "status": REGIME_STORE_READY,
    }
    return df, summary


def summarize_transition_store_catalog(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize transition catalog DataFrame."""
    return {
        "total_items": len(df),
        "catalog_names": df["store_catalog_name"].tolist() if not df.empty else [],
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
