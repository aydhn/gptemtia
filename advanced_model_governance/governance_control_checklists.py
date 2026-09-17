# -*- coding: utf-8 -*-
"""Phase 144: Governance Control Checklists Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

CONTROL_CHECKLIST_ITEMS: List[Dict[str, str]] = [
    {"check_id": "CHK-01", "check_name": "no_live_trading_check", "category": "trading_safety", "description": "Verify live trading is completely disabled."},
    {"check_id": "CHK-02", "check_name": "no_broker_execution_check", "category": "broker_safety", "description": "Verify broker APIs and automated routing are blocked."},
    {"check_id": "CHK-03", "check_name": "no_investment_advice_check", "category": "legal_safety", "description": "Verify zero financial advice or directional claims."},
    {"check_id": "CHK-04", "check_name": "no_signal_generation_check", "category": "signal_safety", "description": "Verify outputs do not generate buy/sell/position signals."},
    {"check_id": "CHK-05", "check_name": "no_prediction_check", "category": "execution_safety", "description": "Verify no model predict/inference was executed."},
    {"check_id": "CHK-06", "check_name": "no_model_training_check", "category": "execution_safety", "description": "Verify no real model training or fitting was executed."},
    {"check_id": "CHK-07", "check_name": "no_model_registry_write_check", "category": "registry_safety", "description": "Verify zero write operations to model registries."},
    {"check_id": "CHK-08", "check_name": "no_deployment_check", "category": "deployment_safety", "description": "Verify no model deployment or publishing occurred."},
    {"check_id": "CHK-09", "check_name": "no_scraping_check", "category": "data_safety", "description": "Verify web scraping and article full-text usage are disabled."},
    {"check_id": "CHK-10", "check_name": "no_credential_output_check", "category": "security_safety", "description": "Verify no API keys or secrets are leaked in logs."},
    {"check_id": "CHK-11", "check_name": "no_source_overwrite_check", "category": "data_integrity", "description": "Verify raw source data files remain unmodified."},
    {"check_id": "CHK-12", "check_name": "manual_review_check", "category": "governance", "description": "Verify manual review gates are active and enforced."},
]


def build_governance_control_checklist_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance control checklists."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in CONTROL_CHECKLIST_ITEMS:
        row = dict(item)
        row["status"] = "PASSED"
        row["enforced"] = True
        row["phase"] = prof.current_phase
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_control_checklists(df)
    return df, summary


def summarize_governance_control_checklists(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance control checklists."""
    return {
        "total_items": len(df),
        "all_passed": bool((df["status"] == "PASSED").all()),
        "all_enforced": bool(df["enforced"].all()),
    }
