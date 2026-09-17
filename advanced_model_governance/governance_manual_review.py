# -*- coding: utf-8 -*-
"""Phase 144: Governance Manual Review Queue."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

MANUAL_REVIEW_QUEUE_ITEMS: List[Dict[str, Any]] = [
    {
        "queue_id": "MRQ-01",
        "component_name": "model_governance_contracts",
        "reason": "Verify alignment of baseline and candidate model specifications.",
        "recommended_action": "inspect model governance contracts",
        "blocked_actions": ["approve production", "auto-deploy model"],
    },
    {
        "queue_id": "MRQ-02",
        "component_name": "model_card_templates",
        "reason": "Verify completeness of 12 standard template sections.",
        "recommended_action": "inspect model card templates",
        "blocked_actions": ["auto-write model registry", "auto-save model artifact"],
    },
    {
        "queue_id": "MRQ-03",
        "component_name": "model_card_limitations",
        "reason": "Verify non-materialized weight constraints and offline scope.",
        "recommended_action": "inspect model card limitations",
        "blocked_actions": ["auto-run prediction", "auto-generate signal"],
    },
    {
        "queue_id": "MRQ-04",
        "component_name": "prohibited_use_registry",
        "reason": "Verify zero live trading, broker, or financial advice exposure.",
        "recommended_action": "inspect prohibited-use registry",
        "blocked_actions": ["approve broker readiness", "approve live trading"],
    },
    {
        "queue_id": "MRQ-05",
        "component_name": "risk_disclosures",
        "reason": "Verify concept drift and calibration degradation mitigations.",
        "recommended_action": "inspect risk disclosures",
        "blocked_actions": ["auto-run optimizer", "auto-run backtest"],
    },
    {
        "queue_id": "MRQ-06",
        "component_name": "validation_evidence",
        "reason": "Verify evidence chains from Phases 136-143.",
        "recommended_action": "inspect validation evidence",
        "blocked_actions": ["auto-delete", "auto-overwrite"],
    },
    {
        "queue_id": "MRQ-07",
        "component_name": "approval_boundaries",
        "reason": "Verify strict interception of production/broker requests.",
        "recommended_action": "inspect approval boundaries",
        "blocked_actions": ["approve production", "approve broker readiness"],
    },
    {
        "queue_id": "MRQ-08",
        "component_name": "audit_trail_placeholders",
        "reason": "Verify dry_run_only flag and non-production status.",
        "recommended_action": "inspect audit trail placeholders",
        "blocked_actions": ["auto-impute", "enable scraping"],
    },
    {
        "queue_id": "MRQ-09",
        "component_name": "disabled_execution_reports",
        "reason": "Verify all 10 execution disabled reports are actively enforced.",
        "recommended_action": "inspect disabled approval/deployment reports",
        "blocked_actions": ["download article body", "generate sentiment", "generate embedding"],
    },
    {
        "queue_id": "MRQ-10",
        "component_name": "phase_145_readiness",
        "reason": "Verify all handoff prerequisites before acceptance report.",
        "recommended_action": "inspect Phase 145 advanced ML acceptance blockers",
        "blocked_actions": ["auto-deploy model", "auto-generate signal"],
    },
]


def build_governance_manual_review_queue(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance manual review queue."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in MANUAL_REVIEW_QUEUE_ITEMS:
        row = dict(item)
        row["blocked_actions_csv"] = ",".join(item["blocked_actions"])
        row["resolved"] = False
        row["phase"] = prof.current_phase
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_manual_review_queue(df)
    return df, summary


def summarize_governance_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue."""
    return {
        "total_queue_items": len(df),
        "all_pending_review": not bool(df["resolved"].any()),
        "status": "MANUAL_REVIEW_QUEUE_READY",
    }
