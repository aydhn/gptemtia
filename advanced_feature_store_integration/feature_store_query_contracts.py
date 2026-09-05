"""Phase 124 Feature Store Query Contracts."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

QUERY_CONTRACTS = [
    {
        "contract_id": "QCON_001",
        "contract_name": "metadata_catalog_query_contract",
        "allowed_filters": "entity_type,feature_family,source_phase,validation_status,manual_review_required,non_signal",
        "prohibited_filters": "signal,target,label,prediction,recommendation,entry_exit",
        "non_signal_guaranteed": True,
        "source_preserved": True,
    },
    {
        "contract_id": "QCON_002",
        "contract_name": "time_series_feature_query_contract",
        "allowed_filters": "symbol,timestamp_range,feature_names,entity_id",
        "prohibited_filters": "future_return,forward_return,predicted_price",
        "non_signal_guaranteed": True,
        "source_preserved": True,
    },
]


def validate_feature_store_query_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Validate query parameters against non-signal query contracts."""
    filters = request.get("filters", {})
    issues = []

    prohibited_keys = ["signal", "target", "label", "prediction", "recommendation", "future_return", "forward_return"]
    for k in filters.keys():
        if k.lower() in prohibited_keys:
            issues.append(f"Query filter '{k}' is prohibited by non-signal policy.")

    return {
        "is_allowed": len(issues) == 0,
        "issues": issues,
        "non_signal": len(issues) == 0,
    }


def build_feature_store_query_contract_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of query contracts."""
    records = list(QUERY_CONTRACTS)
    df = pd.DataFrame(records)
    summary = {
        "total_query_contracts": len(records),
        "non_signal_guaranteed": True,
        "target_prediction_query_forbidden": True,
    }
    return df, summary


def summarize_feature_store_query_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize query contracts."""
    return {
        "total_contracts": len(df) if not df.empty else 0,
        "non_signal": True,
    }
