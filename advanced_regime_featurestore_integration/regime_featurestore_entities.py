"""Phase 134: Regime FeatureStore Entities.

Registers canonical entity definitions across all regime components.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_FEATURESTORE_ENTITY_DOMAIN,
    REGIME_STORE_READY,
    STORE_ENTITY_CANDIDATE_STATE,
    STORE_ENTITY_CROSS_ASSET_CONTEXT,
    STORE_ENTITY_MACRO_EVENT_NEWS_CONTEXT,
    STORE_ENTITY_PSEUDO_STATE,
    STORE_ENTITY_REGIME_MATRIX,
    STORE_ENTITY_REGIME_TAXONOMY,
    STORE_ENTITY_TRANSITION,
    STORE_ENTITY_VALIDATION_ACCEPTANCE,
)

CANONICAL_ENTITIES: List[Dict[str, Any]] = [
    {
        "entity_name": "regime_taxonomy_entity",
        "store_entity_type": STORE_ENTITY_REGIME_TAXONOMY,
        "primary_key": "taxonomy_id",
        "description": "Canonical 4-family macro/behavioral regime taxonomy specifications.",
        "source_phase": 126,
        "source_component": "advanced_regime_foundation",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "entity_name": "regime_matrix_entity",
        "store_entity_type": STORE_ENTITY_REGIME_MATRIX,
        "primary_key": "matrix_id",
        "description": "Standardized multi-timeframe feature matrix and state dataset contracts.",
        "source_phase": 127,
        "source_component": "advanced_regime_matrix",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "entity_name": "candidate_state_entity",
        "store_entity_type": STORE_ENTITY_CANDIDATE_STATE,
        "primary_key": "candidate_state_id",
        "description": "Rule-free unsupervised candidate feature sets and state preparation metadata.",
        "source_phase": 128,
        "source_component": "advanced_regime_rule_free",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "entity_name": "pseudo_state_entity",
        "store_entity_type": STORE_ENTITY_PSEUDO_STATE,
        "primary_key": "pseudo_state_id",
        "description": "Non-directional pseudo-state heuristic labeling contracts.",
        "source_phase": 128,
        "source_component": "advanced_regime_rule_free",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "entity_name": "transition_context_entity",
        "store_entity_type": STORE_ENTITY_TRANSITION,
        "primary_key": "transition_id",
        "description": "Regime sequence transitions, persistence diagnostics, and stability metrics.",
        "source_phase": 130,
        "source_component": "advanced_regime_transition",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "entity_name": "cross_asset_regime_context_entity",
        "store_entity_type": STORE_ENTITY_CROSS_ASSET_CONTEXT,
        "primary_key": "cross_asset_id",
        "description": "Cross-asset multi-market regime alignment and divergence context.",
        "source_phase": 131,
        "source_component": "advanced_cross_asset_regime_context",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "entity_name": "macro_event_news_context_entity",
        "store_entity_type": STORE_ENTITY_MACRO_EVENT_NEWS_CONTEXT,
        "primary_key": "macro_context_id",
        "description": "Macro indicator releases, economic calendar events, and news metadata context.",
        "source_phase": 132,
        "source_component": "advanced_macro_event_news_regime",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "entity_name": "validation_acceptance_entity",
        "store_entity_type": STORE_ENTITY_VALIDATION_ACCEPTANCE,
        "primary_key": "acceptance_id",
        "description": "Verification gates, no-lookahead proofs, and acceptance findings metadata.",
        "source_phase": 133,
        "source_component": "advanced_regime_validation_acceptance",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "entity_name": "acceptance_manifest_entity",
        "store_entity_type": "acceptance_manifest_entity",
        "primary_key": "manifest_id",
        "description": "Master audit manifest verifying acceptance gate proofs.",
        "source_phase": 133,
        "source_component": "advanced_regime_validation_acceptance",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "entity_name": "manual_review_blocker_entity",
        "store_entity_type": "manual_review_blocker_entity",
        "primary_key": "blocker_id",
        "description": "Safety blockers and manual review requirement items in the FeatureStore.",
        "source_phase": 134,
        "source_component": "advanced_regime_featurestore_integration",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    },
]


def build_regime_featurestore_entity_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct tabular entity registry."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_ENTITIES)
    summary = {
        "domain": REGIME_FEATURESTORE_ENTITY_DOMAIN,
        "total_entities": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "all_production_false": bool((df["production_ready"] == False).all()),
        "status": REGIME_STORE_READY,
    }
    return df, summary


def summarize_regime_featurestore_entities(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize entity registry DataFrame."""
    return {
        "total_entities": len(df),
        "entity_names": df["entity_name"].tolist() if not df.empty else [],
        "primary_keys": df["primary_key"].tolist() if not df.empty else [],
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
