"""Phase 134: Regime FeatureStore Read Contracts.

Governs read access to the FeatureStore, guaranteeing that all reads are local-only,
non-networked, non-broker, and free from trade signal or target queries.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    READ_CONTRACT_DOMAIN,
    REGIME_STORE_READY,
)

CANONICAL_READ_CONTRACTS: List[Dict[str, Any]] = [
    {
        "read_contract_name": "local_parquet_csv_read_contract",
        "allow_local_disk_read": True,
        "allow_network_calls": False,
        "allow_credentials_in_query": False,
        "allow_broker_integration": False,
        "allow_signal_queries": False,
        "allow_target_prediction_queries": False,
        "allow_production_approval_queries": False,
        "description": "Permits local read of structured CSV and JSON metadata from DataLake storage.",
        "non_signal": True,
    },
    {
        "read_contract_name": "catalog_metadata_lookup_contract",
        "allow_local_disk_read": True,
        "allow_network_calls": False,
        "allow_credentials_in_query": False,
        "allow_broker_integration": False,
        "allow_signal_queries": False,
        "allow_target_prediction_queries": False,
        "allow_production_approval_queries": False,
        "description": "Permits in-memory lookup of catalog items by entity type and component name.",
        "non_signal": True,
    },
]


def build_regime_featurestore_read_contract_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for read contracts."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_READ_CONTRACTS)
    summary = {
        "domain": READ_CONTRACT_DOMAIN,
        "total_read_contracts": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_network_forbidden": bool((df["allow_network_calls"] == False).all()),
        "all_signals_forbidden": bool((df["allow_signal_queries"] == False).all()),
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def validate_regime_featurestore_read_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that an incoming read request satisfies local non-signal constraints."""
    errors = []
    if request.get("network_call_requested", False):
        errors.append("Network calls are strictly prohibited for FeatureStore reads")
    if request.get("credential_provided", False):
        errors.append("Credentials must not be supplied or processed")
    if request.get("query_signal", False) or request.get("query_target", False):
        errors.append("Queries for trade signals, targets, or predictions are forbidden")
    if request.get("query_production_approval", False):
        errors.append("Production approval queries are unsupported and forbidden")

    return {
        "request_id": request.get("request_id", "read_req_default"),
        "is_valid": len(errors) == 0,
        "errors": errors,
        "non_signal": True,
    }


def summarize_regime_featurestore_read_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize read contract registry DataFrame."""
    return {
        "total_contracts": len(df),
        "contract_names": df["read_contract_name"].tolist() if not df.empty else [],
        "all_network_prohibited": bool((df["allow_network_calls"] == False).all()) if not df.empty else True,
    }
