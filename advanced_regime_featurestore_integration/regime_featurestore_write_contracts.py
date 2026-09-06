"""Phase 134: Regime FeatureStore Write Contracts.

Enforces write discipline: append/snapshot metadata only, absolute prohibition of
source overwrites and destructive cleaning, with mandatory validation acceptance references.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_STORE_READY,
    WRITE_CONTRACT_DOMAIN,
)

CANONICAL_WRITE_CONTRACTS: List[Dict[str, Any]] = [
    {
        "write_contract_name": "metadata_append_write_contract",
        "allow_append": True,
        "allow_source_overwrite": False,
        "allow_destructive_clean": False,
        "allow_file_deletion": False,
        "allow_auto_imputation": False,
        "allow_auto_feature_drop": False,
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": True,
        "non_signal_required": True,
        "description": "Appends new verified regime catalog metadata without mutating prior versions.",
    },
    {
        "write_contract_name": "metadata_snapshot_write_contract",
        "allow_append": False,
        "allow_source_overwrite": False,
        "allow_destructive_clean": False,
        "allow_file_deletion": False,
        "allow_auto_imputation": False,
        "allow_auto_feature_drop": False,
        "validation_acceptance_required": True,
        "no_lookahead_acceptance_required": True,
        "metadata_only_news_acceptance_required": True,
        "non_signal_required": True,
        "description": "Writes distinct timestamped snapshot files preserving historical data intact.",
    },
]


def build_regime_featurestore_write_contract_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for write contracts."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_WRITE_CONTRACTS)
    summary = {
        "domain": WRITE_CONTRACT_DOMAIN,
        "total_write_contracts": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_source_overwrites_forbidden": bool((df["allow_source_overwrite"] == False).all()),
        "all_destructive_cleans_forbidden": bool((df["allow_destructive_clean"] == False).all()),
        "all_non_signal_required": bool((df["non_signal_required"] == True).all()),
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def validate_regime_featurestore_write_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that a write request complies with non-destructive, acceptance-aware rules."""
    errors = []
    if request.get("attempt_source_overwrite", False):
        errors.append("Overwriting source datasets is strictly forbidden")
    if request.get("attempt_destructive_cleaning", False):
        errors.append("Destructive cleaning is prohibited")
    if request.get("attempt_auto_imputation", False):
        errors.append("Automatic imputation is prohibited")
    if not request.get("validation_acceptance_ref"):
        errors.append("Missing mandatory validation_acceptance_ref")
    if not request.get("no_lookahead_acceptance_ref"):
        errors.append("Missing mandatory no_lookahead_acceptance_ref")
    if request.get("has_news_context", False) and not request.get("metadata_only_news_acceptance_ref"):
        errors.append("News context requires verified metadata_only_news_acceptance_ref")
    if not request.get("non_signal", False):
        errors.append("Write payload must explicitly declare non_signal=True")

    return {
        "request_id": request.get("request_id", "write_req_default"),
        "is_valid": len(errors) == 0,
        "errors": errors,
        "non_signal": request.get("non_signal", False),
    }


def summarize_regime_featurestore_write_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize write contract registry DataFrame."""
    return {
        "total_contracts": len(df),
        "contract_names": df["write_contract_name"].tolist() if not df.empty else [],
        "all_overwrites_forbidden": bool((df["allow_source_overwrite"] == False).all()) if not df.empty else True,
    }
