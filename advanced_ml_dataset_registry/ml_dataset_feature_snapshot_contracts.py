import pandas as pd
from typing import Dict, List, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_SNAPSHOT_CONTRACTS = [
    {"contract_name": "featurestore_snapshot_contract", "dataset_family": "featurestore"},
    {"contract_name": "regime_metadata_snapshot_contract", "dataset_family": "regime_metadata"},
    {"contract_name": "technical_feature_snapshot_contract", "dataset_family": "technical_features"},
    {"contract_name": "factor_feature_snapshot_contract", "dataset_family": "factor_features"},
    {"contract_name": "macro_event_news_metadata_snapshot_contract", "dataset_family": "macro_event_news_metadata"},
    {"contract_name": "no_lookahead_accepted_snapshot_contract", "dataset_family": "validation_accepted"},
]

def build_ml_dataset_feature_snapshot_contract_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for c in _SNAPSHOT_CONTRACTS:
        rows.append({
            "contract_name": c["contract_name"],
            "dataset_family": c["dataset_family"],
            "materialized": False,
            "production_ready": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
            "placeholder_only": True,
            "snapshot_for_phase": 138,
        })
    df = pd.DataFrame(rows)
    summary = {"total_snapshot_contracts": len(rows), "current_phase": 137, "non_signal": True, "materialized": False, "status": "READY"}
    return df, summary

def validate_feature_snapshot_contract(contract: Dict) -> Dict:
    issues = []
    if contract.get("materialized", False):
        issues.append("materialized must be False")
    if contract.get("production_ready", False):
        issues.append("production_ready must be False")
    return {"valid": len(issues) == 0, "issues": issues, "non_signal": True}

def summarize_feature_snapshot_contracts(df: pd.DataFrame) -> Dict:
    return {"total_snapshot_contracts": len(df), "current_phase": 137, "non_signal": True, "status": "READY"}
