# -*- coding: utf-8 -*-
"""Phase 138 Dry-Run Trainer Stubs.

Provides stub implementations for baseline model trainers. Ensures no model
is instantiated or fitted, returning safe blocked execution metadata.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_families import BASELINE_MODEL_FAMILIES_DATA


def build_dry_run_trainer_stub_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build trainer stubs registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for fam in BASELINE_MODEL_FAMILIES_DATA:
        rows.append({
            "stub_id": f"trainer_stub_{fam['family_id']}",
            "trainer_name": f"DryRun{fam['family_name'].replace(' ', '')}Stub",
            "model_family_ref": fam["family_id"],
            "harness_contract_ref": "harness_contract_standard_linear",
            "is_active_stub": True,
            "execution_status": "execution_blocked_no_real_training",
            "blocked_reason": "Zero-training policy active in Phase 138 baseline model contracts",
            "manual_review_required": True,
            "real_training_executed": False,
            "model_fit_executed": False,
            "model_predict_executed": False,
            "target_label_generated": False,
            "artifact_persisted": False,
            "non_signal": True,
        })

    df = pd.DataFrame(rows)
    summary = summarize_dry_run_trainer_stubs(df)
    return df, summary


def dry_run_train_stub(request: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a simulated dry-run training request.

    Strictly guarantees that no real training, fit, prediction, dataset materialization,
    target/label generation, or artifact persistence occurs.
    """
    model_family = request.get("model_family", "unknown_baseline_model_family")
    plan_name = request.get("plan_name", "unspecified_dry_run_plan")

    return {
        "dry_run": True,
        "request_plan_name": plan_name,
        "model_family": model_family,
        "real_training_executed": False,
        "model_training_executed": False,
        "model_fit_executed": False,
        "model_predict_executed": False,
        "model_inference_executed": False,
        "model_transform_executed": False,
        "target_label_generated": False,
        "artifact_persisted": False,
        "model_registry_written": False,
        "blocked_by_policy": True,
        "blocked_reason": "Real model training, fitting, and prediction are strictly blocked by Phase 138 policy.",
        "manual_review_required": True,
        "execution_label": "execution_blocked_no_real_training",
        "execution_status": "no_real_training_executed",
        "status": "execution_blocked_by_policy",
        "contract_validated": True,
        "would_run": False,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }


def summarize_dry_run_trainer_stubs(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize trainer stubs registry."""
    return {
        "total_trainer_stubs": len(df),
        "all_stubs_active": bool(df["is_active_stub"].all()) if not df.empty else True,
        "all_active_stubs": bool(df["is_active_stub"].all()) if not df.empty else True,
        "all_real_training_blocked": bool((~df["real_training_executed"]).all()) if not df.empty else True,
        "all_model_fit_blocked": bool((~df["model_fit_executed"]).all()) if not df.empty else True,
        "all_fit_blocked": bool((~df["model_fit_executed"]).all()) if not df.empty else True,
        "all_predict_blocked": bool((~df["model_predict_executed"]).all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
