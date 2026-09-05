"""Phase 124 Feature Store Write Contracts."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

WRITE_CONTRACTS = [
    {
        "contract_id": "WCON_001",
        "contract_name": "append_snapshot_write_contract",
        "write_mode": "append_or_snapshot_only",
        "source_overwrite_allowed": False,
        "destructive_cleaning_allowed": False,
        "auto_delete_allowed": False,
        "auto_impute_allowed": False,
        "auto_drop_allowed": False,
        "validation_metadata_required": True,
        "quality_drift_metadata_tracked": True,
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "contract_id": "WCON_002",
        "contract_name": "schema_conformance_write_contract",
        "write_mode": "schema_validated_only",
        "source_overwrite_allowed": False,
        "destructive_cleaning_allowed": False,
        "auto_delete_allowed": False,
        "auto_impute_allowed": False,
        "auto_drop_allowed": False,
        "validation_metadata_required": True,
        "quality_drift_metadata_tracked": True,
        "non_signal": True,
        "source_preserved": True,
    },
]


def validate_feature_store_write_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a write request against source preservation and write contracts."""
    mode = request.get("mode", "append").lower()
    issues = []

    if mode in ["overwrite", "replace", "delete"]:
        issues.append(f"Write mode '{mode}' violates immutable source preservation policy.")
    if request.get("auto_impute", False):
        issues.append("Automatic imputation is prohibited.")
    if request.get("auto_drop", False):
        issues.append("Automatic column dropping is prohibited.")
    if not request.get("has_validation_metadata", True):
        issues.append("Validation metadata must accompany every write operation.")

    return {
        "is_allowed": len(issues) == 0,
        "issues": issues,
        "source_preserved": len([i for i in issues if "source preservation" in i]) == 0,
        "non_signal": True,
    }


def build_feature_store_write_contract_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of write contracts."""
    records = list(WRITE_CONTRACTS)
    df = pd.DataFrame(records)
    summary = {
        "total_write_contracts": len(records),
        "source_overwrite_forbidden": True,
        "destructive_cleaning_forbidden": True,
        "auto_impute_forbidden": True,
        "auto_drop_forbidden": True,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_write_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize write contracts."""
    return {
        "total_contracts": len(df) if not df.empty else 0,
        "source_preserved": True,
        "non_signal": True,
    }
