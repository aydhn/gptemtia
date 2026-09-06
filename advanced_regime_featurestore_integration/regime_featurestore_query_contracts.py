"""Phase 134: Regime FeatureStore Query Contracts.

Defines permitted query parameters (entity type, source phase, validation status, etc.)
and rejects any query attempting to filter or extract trade signals or predictions.
"""
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    QUERY_CONTRACT_DOMAIN,
    REGIME_STORE_READY,
)

CANONICAL_QUERY_FILTERS: List[Dict[str, Any]] = [
    {"filter_name": "store_entity_type", "permitted": True, "description": "Filter by canonical entity type"},
    {"filter_name": "source_phase", "permitted": True, "description": "Filter by originating phase index"},
    {"filter_name": "component_name", "permitted": True, "description": "Filter by subsystem name"},
    {"filter_name": "validation_acceptance_status", "permitted": True, "description": "Filter by acceptance verification status"},
    {"filter_name": "no_lookahead_status", "permitted": True, "description": "Filter by no-lookahead status"},
    {"filter_name": "metadata_only_news_status", "permitted": True, "description": "Filter by metadata-only news status"},
    {"filter_name": "manual_review_required", "permitted": True, "description": "Filter by manual review flag"},
    {"filter_name": "non_signal", "permitted": True, "description": "Filter verifying non_signal=True"},
]

FORBIDDEN_QUERY_TERMS: List[str] = [
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
    "live_readiness",
    "production_approval",
]


def build_regime_featurestore_query_contract_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for query contracts."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_QUERY_FILTERS)
    summary = {
        "domain": QUERY_CONTRACT_DOMAIN,
        "total_query_filters": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "forbidden_query_terms_count": len(FORBIDDEN_QUERY_TERMS),
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def validate_regime_featurestore_query_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that a query request uses only permitted metadata filters and zero signal terms."""
    errors = []
    query_keys = [str(k).lower() for k in request.keys()]
    query_values = [str(v).lower() for v in request.values()]

    for term in FORBIDDEN_QUERY_TERMS:
        if any(term in k for k in query_keys) or any(term in v for v in query_values):
            errors.append(f"Query contains prohibited trading/prediction term: '{term}'")

    return {
        "query_id": request.get("query_id", "query_default"),
        "is_valid": len(errors) == 0,
        "errors": errors,
        "non_signal": len(errors) == 0,
    }


def summarize_regime_featurestore_query_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize query contract registry DataFrame."""
    return {
        "total_permitted_filters": len(df),
        "filter_names": df["filter_name"].tolist() if not df.empty else [],
        "all_permitted": bool((df["permitted"] == True).all()) if not df.empty else True,
    }
