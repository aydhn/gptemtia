# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Manual Review Queue.

Queues manual inspection tasks for engineers/analysts to review baseline contracts
and dry-run harness configurations before proceeding to Phase 139.
Strictly prohibits automated training, predictions, signals, or destructive mutations.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

MANUAL_REVIEW_TASKS = [
    {
        "item_id": "review_baseline_contracts",
        "review_topic": "inspect baseline model contracts",
        "target_reference": "baseline_model_contracts_registry",
        "severity": "MEDIUM",
        "review_instructions": "Inspect that all 10 baseline model contracts specify zero training and non-signal flags.",
    },
    {
        "item_id": "review_dataset_contract_refs",
        "review_topic": "inspect dataset contract refs",
        "target_reference": "baseline_model_input_contracts",
        "severity": "MEDIUM",
        "review_instructions": "Verify that dataset contracts reference Phase 137 valid contracts without materializing data.",
    },
    {
        "item_id": "review_dry_run_policies",
        "review_topic": "inspect dry-run harness policies",
        "target_reference": "dry_run_training_policies",
        "severity": "HIGH",
        "review_instructions": "Verify zero real training, fit, and predict enforcement in dry-run trainers.",
    },
    {
        "item_id": "review_artifact_disabled_blockers",
        "review_topic": "inspect artifact disabled blockers",
        "target_reference": "model_artifact_disabled_report",
        "severity": "HIGH",
        "review_instructions": "Ensure binary model dumps, joblib, and model registry writes are strictly disabled.",
    },
    {
        "item_id": "review_phase_139_gpu_readiness",
        "review_topic": "inspect Phase 139 GPU resource governance blockers",
        "target_reference": "phase_139_handoff_report",
        "severity": "MEDIUM",
        "review_instructions": "Review GPU accelerator prerequisites and resource limits before Phase 139 handoff.",
    },
]


def build_baseline_model_manual_review_queue(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build manual review queue DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for t in MANUAL_REVIEW_TASKS:
        rows.append({
            "item_id": t["item_id"],
            "review_topic": t["review_topic"],
            "target_reference": t["target_reference"],
            "severity": t["severity"],
            "review_instructions": t["review_instructions"],
            "status": "PENDING_INSPECTION",
            "auto_execution_blocked": True,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_manual_review_queue(df)
    return df, summary


def summarize_baseline_model_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue."""
    return {
        "total_review_items": len(df),
        "all_auto_execution_blocked": bool(df["auto_execution_blocked"].all()) if not df.empty else True,
        "high_priority_items": int((df["severity"] == "HIGH").sum()) if not df.empty else 0,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
