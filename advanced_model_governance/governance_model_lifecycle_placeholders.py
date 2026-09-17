# -*- coding: utf-8 -*-
"""Phase 144: Governance Model Lifecycle Placeholders Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

LIFECYCLE_STAGES: List[Dict[str, str]] = [
    {"stage_id": "STG-01", "stage_name": "concept_and_contract", "description": "Formulate contract interfaces and dependency requirements.", "is_active": "YES"},
    {"stage_id": "STG-02", "stage_name": "dry_run_validation", "description": "Execute local offline mock test suites and harness checks.", "is_active": "YES"},
    {"stage_id": "STG-03", "stage_name": "model_card_authoring", "description": "Document limitations, intended/prohibited use, and risks.", "is_active": "YES"},
    {"stage_id": "STG-04", "stage_name": "governance_manual_review", "description": "Human inspection of contracts and boundaries before acceptance.", "is_active": "YES"},
    {"stage_id": "STG-05", "stage_name": "production_deployment", "description": "Production deployment is PERMANENTLY BLOCKED in this repo.", "is_active": "BLOCKED"},
]


def build_governance_model_lifecycle_placeholder_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model lifecycle placeholders."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in LIFECYCLE_STAGES:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["is_placeholder"] = True
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_model_lifecycle_placeholders(df)
    return df, summary


def summarize_governance_model_lifecycle_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model lifecycle placeholders."""
    return {
        "total_stages": len(df),
        "production_deployment_blocked": bool((df[df["stage_name"] == "production_deployment"]["is_active"] == "BLOCKED").all()),
        "status": "LIFECYCLE_PLACEHOLDER_READY",
    }
