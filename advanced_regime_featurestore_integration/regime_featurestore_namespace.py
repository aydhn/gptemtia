"""Phase 134: Regime FeatureStore Namespace Management.

Enforces standardized, lowercase snake_case naming policies with regime_store_ prefix
and rejects any keys containing trade signal or target/prediction terminology.
"""

from typing import Any, Dict, List, Optional, Tuple
import re
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_FEATURESTORE_NAMESPACE_DOMAIN,
    REGIME_STORE_READY,
)

FORBIDDEN_NAMESPACE_WORDS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
]

CANONICAL_NAMESPACES: List[Dict[str, Any]] = [
    {
        "namespace_name": "regime_store_taxonomy_namespace",
        "entity_type": "store_entity_regime_taxonomy",
        "prefix": "regime_store_taxonomy",
        "pattern": r"^regime_store_taxonomy_[a-z0-9_]+$",
        "non_signal": True,
    },
    {
        "namespace_name": "regime_store_matrix_namespace",
        "entity_type": "store_entity_regime_matrix",
        "prefix": "regime_store_matrix",
        "pattern": r"^regime_store_matrix_[a-z0-9_]+$",
        "non_signal": True,
    },
    {
        "namespace_name": "regime_store_candidate_state_namespace",
        "entity_type": "store_entity_candidate_state",
        "prefix": "regime_store_candidate_state",
        "pattern": r"^regime_store_candidate_state_[a-z0-9_]+$",
        "non_signal": True,
    },
    {
        "namespace_name": "regime_store_pseudo_state_namespace",
        "entity_type": "store_entity_pseudo_state",
        "prefix": "regime_store_pseudo_state",
        "pattern": r"^regime_store_pseudo_state_[a-z0-9_]+$",
        "non_signal": True,
    },
    {
        "namespace_name": "regime_store_transition_namespace",
        "entity_type": "store_entity_transition",
        "prefix": "regime_store_transition",
        "pattern": r"^regime_store_transition_[a-z0-9_]+$",
        "non_signal": True,
    },
    {
        "namespace_name": "regime_store_cross_asset_namespace",
        "entity_type": "store_entity_cross_asset_context",
        "prefix": "regime_store_cross_asset",
        "pattern": r"^regime_store_cross_asset_[a-z0-9_]+$",
        "non_signal": True,
    },
    {
        "namespace_name": "regime_store_macro_news_namespace",
        "entity_type": "store_entity_macro_event_news_context",
        "prefix": "regime_store_macro_news",
        "pattern": r"^regime_store_macro_news_[a-z0-9_]+$",
        "non_signal": True,
    },
    {
        "namespace_name": "regime_store_validation_namespace",
        "entity_type": "store_entity_validation_acceptance",
        "prefix": "regime_store_validation",
        "pattern": r"^regime_store_validation_[a-z0-9_]+$",
        "non_signal": True,
    },
]


def build_regime_store_key(entity_type: str, entity_id: str, component_name: str) -> str:
    """Generate canonical snake_case store key with mandatory regime_store_ prefix."""
    clean_type = re.sub(r"[^a-z0-9_]", "_", entity_type.lower().replace("store_entity_", ""))
    clean_id = re.sub(r"[^a-z0-9_]", "_", entity_id.lower())
    clean_comp = re.sub(r"[^a-z0-9_]", "_", component_name.lower())
    return f"regime_store_{clean_type}_{clean_comp}_{clean_id}"


def validate_regime_store_key(key: str) -> Dict[str, Any]:
    """Validate that a store key starts with regime_store_, uses snake_case, and has no forbidden words."""
    errors = []
    if not key.startswith("regime_store_"):
        errors.append("Store key must start with 'regime_store_' prefix")
    if not re.match(r"^[a-z0-9_]+$", key):
        errors.append("Store key must contain only lowercase alphanumeric characters and underscores")

    lower_key = key.lower()
    found_forbidden = [w for w in FORBIDDEN_NAMESPACE_WORDS if w in lower_key]
    if found_forbidden:
        errors.append(f"Store key contains forbidden signal/prediction terms: {found_forbidden}")

    return {
        "store_key": key,
        "is_valid": len(errors) == 0,
        "errors": errors,
        "non_signal": len(found_forbidden) == 0,
    }


def build_regime_featurestore_namespace_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct tabular namespace registry."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_NAMESPACES)
    summary = {
        "domain": REGIME_FEATURESTORE_NAMESPACE_DOMAIN,
        "total_namespaces": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "forbidden_words_count": len(FORBIDDEN_NAMESPACE_WORDS),
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def summarize_regime_featurestore_namespace(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize namespace registry DataFrame."""
    return {
        "total_namespaces": len(df),
        "namespace_names": df["namespace_name"].tolist() if not df.empty else [],
        "prefixes": df["prefix"].tolist() if not df.empty else [],
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
