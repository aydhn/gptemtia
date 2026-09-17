# -*- coding: utf-8 -*-
"""Phase 144: Governance Audit Trail Placeholders Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

AUDIT_TRAIL_ITEMS: List[Dict[str, str]] = [
    {"audit_id": "AUD-01", "event_type": "contract_registration", "description": "Baseline model contract registered in offline registry.", "actor": "system_governance"},
    {"audit_id": "AUD-02", "event_type": "model_card_template_instantiation", "description": "Model card template instantiated with standard 12 sections.", "actor": "system_governance"},
    {"audit_id": "AUD-03", "event_type": "boundary_check_enforced", "description": "Production approval and live trading blocked by policy.", "actor": "security_boundary"},
    {"audit_id": "AUD-04", "event_type": "readiness_evaluation", "description": "Readiness score computed across validation dependencies.", "actor": "governance_evaluator"},
]


def build_governance_audit_trail_placeholder_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance audit trail placeholders."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in AUDIT_TRAIL_ITEMS:
        row = dict(item)
        row["dry_run_only"] = True
        row["real_audit_log"] = False
        row["production_approved"] = False
        row["broker_ready_approved"] = False
        row["live_trading_approved"] = False
        row["phase"] = prof.current_phase
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_audit_trail_placeholders(df)
    return df, summary


def summarize_governance_audit_trail_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance audit trail placeholders."""
    return {
        "total_audit_placeholders": len(df),
        "all_dry_run_only": bool(df["dry_run_only"].all()),
        "all_real_audit_log_false": not bool(df["real_audit_log"].any()),
        "all_production_approved_false": not bool(df["production_approved"].any()),
        "status": "AUDIT_PLACEHOLDER_ONLY",
    }
