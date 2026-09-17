# -*- coding: utf-8 -*-
"""Phase 144: Model Card Prohibited Use Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

PROHIBITED_USE_ITEMS: List[Dict[str, str]] = [
    {
        "prohibition_id": "PROH-001",
        "action_name": "live_trading",
        "reason": "Direct submission of orders to real exchanges or accounts is strictly prohibited.",
        "severity": "CRITICAL",
    },
    {
        "prohibition_id": "PROH-002",
        "action_name": "broker_execution",
        "reason": "Connecting broker APIs or executing automated broker orders is prohibited.",
        "severity": "CRITICAL",
    },
    {
        "prohibition_id": "PROH-003",
        "action_name": "investment_advice",
        "reason": "Generating financial advice, directional buy/sell claims, or position sizing is prohibited.",
        "severity": "CRITICAL",
    },
    {
        "prohibition_id": "PROH-004",
        "action_name": "guaranteed_signal",
        "reason": "Treating governance scores, readiness, or contracts as predictive market signals is prohibited.",
        "severity": "CRITICAL",
    },
    {
        "prohibition_id": "PROH-005",
        "action_name": "production_approval",
        "reason": "Signing off production deployment without formal multi-phase governance completion is prohibited.",
        "severity": "HIGH",
    },
    {
        "prohibition_id": "PROH-006",
        "action_name": "broker_ready_approval",
        "reason": "Claiming broker readiness or live gateway compatibility is prohibited.",
        "severity": "HIGH",
    },
    {
        "prohibition_id": "PROH-007",
        "action_name": "automatic_retraining",
        "reason": "Unsupervised autonomous retraining on production market feeds is prohibited.",
        "severity": "HIGH",
    },
    {
        "prohibition_id": "PROH-008",
        "action_name": "automatic_deployment",
        "reason": "Autonomous continuous deployment of models into execution runtime is prohibited.",
        "severity": "HIGH",
    },
    {
        "prohibition_id": "PROH-009",
        "action_name": "model_registry_write",
        "reason": "Writing weights, checkpoints, or artifacts to production model registries (e.g. MLflow) is prohibited.",
        "severity": "HIGH",
    },
    {
        "prohibition_id": "PROH-010",
        "action_name": "source_overwrite",
        "reason": "Overwriting, mutating, or destructively cleaning raw Lake/Store data is prohibited.",
        "severity": "CRITICAL",
    },
    {
        "prohibition_id": "PROH-011",
        "action_name": "article_scraping",
        "reason": "Scraping copyrighted full-text articles or storing raw HTML bodies is prohibited.",
        "severity": "HIGH",
    },
]


def build_model_card_prohibited_use_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card prohibited uses."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in PROHIBITED_USE_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["is_prohibited"] = True
        row["status"] = "BLOCKED_BY_POLICY"
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_prohibited_use(df)
    return df, summary


def summarize_model_card_prohibited_use(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card prohibited uses."""
    return {
        "total_prohibitions": len(df),
        "all_prohibited": bool(df["is_prohibited"].all()),
        "all_blocked": bool((df["status"] == "BLOCKED_BY_POLICY").all()),
    }
