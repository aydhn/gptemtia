"""Phase 124 Feature Store Read Contracts."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

READ_CONTRACTS = [
    {
        "contract_id": "RCON_001",
        "contract_name": "local_offline_read_contract",
        "allowed_sources": ["local_disk", "data_lake", "feature_store_parquet_csv"],
        "prohibited_actions": ["network_call", "provider_api_call", "scraping", "broker_call"],
        "non_signal_enforced": True,
        "status": "enforced",
    },
    {
        "contract_id": "RCON_002",
        "contract_name": "no_prediction_query_contract",
        "allowed_sources": ["feature_registry", "factor_registry", "catalog_reports"],
        "prohibited_actions": ["target_query", "label_query", "prediction_query", "signal_query"],
        "non_signal_enforced": True,
        "status": "enforced",
    },
]


def validate_feature_store_read_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a read request against non-signal and local-only read contracts."""
    query = request.get("query_text", "").lower()
    source = request.get("source", "local_disk").lower()
    issues = []

    if source not in ["local_disk", "data_lake", "feature_store", "local_cache"]:
        issues.append(f"Remote/network source '{source}' is strictly prohibited.")

    prohibited_terms = ["signal", "buy", "sell", "target", "label", "prediction", "forecast", "execution"]
    for term in prohibited_terms:
        if term in query:
            issues.append(f"Query contains prohibited term: '{term}'")

    return {
        "is_allowed": len(issues) == 0,
        "issues": issues,
        "non_signal": len([i for i in issues if "prohibited term" in i]) == 0,
    }


def build_feature_store_read_contract_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of read contracts."""
    records = []
    for c in READ_CONTRACTS:
        item = dict(c)
        item["allowed_sources_str"] = ",".join(item["allowed_sources"])
        item["prohibited_actions_str"] = ",".join(item["prohibited_actions"])
        records.append(item)

    df = pd.DataFrame(records)
    summary = {
        "total_read_contracts": len(records),
        "local_only_enforced": True,
        "non_signal_enforced": True,
    }
    return df, summary


def summarize_feature_store_read_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize read contracts."""
    return {
        "total_contracts": len(df) if not df.empty else 0,
        "local_only_enforced": True,
        "non_signal_enforced": True,
    }
