# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Experiment Linkage Registry.

Connects Phase 137 Experiment Registry and templates with Phase 138 baseline model
contracts and Phase 139 GPU harness resource governance.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

EXPERIMENT_LINKAGES = [
    {
        "linkage_id": "linkage_exp_baseline_linear",
        "experiment_template_ref": "exp_template_linear_baseline_v1",
        "model_contract_ref": "contract_logistic_regression_baseline_contract",
        "phase_137_run_plan_ref": "run_plan_placeholder_linear_models",
        "phase_139_resource_governance_ref": "gpu_resource_governance_standard",
    },
    {
        "linkage_id": "linkage_exp_baseline_trees",
        "experiment_template_ref": "exp_template_tree_baseline_v1",
        "model_contract_ref": "contract_random_forest_baseline_contract",
        "phase_137_run_plan_ref": "run_plan_placeholder_tree_models",
        "phase_139_resource_governance_ref": "gpu_resource_governance_multi_thread",
    },
    {
        "linkage_id": "linkage_exp_baseline_boosting",
        "experiment_template_ref": "exp_template_boosting_baseline_v1",
        "model_contract_ref": "contract_xgboost_baseline_contract",
        "phase_137_run_plan_ref": "run_plan_placeholder_boosting_models",
        "phase_139_resource_governance_ref": "gpu_resource_governance_cuda_pinned",
    },
    {
        "linkage_id": "linkage_exp_baseline_neural",
        "experiment_template_ref": "exp_template_neural_baseline_v1",
        "model_contract_ref": "contract_shallow_mlp_baseline_contract",
        "phase_137_run_plan_ref": "run_plan_placeholder_neural_models",
        "phase_139_resource_governance_ref": "gpu_resource_governance_vram_capped",
    },
]


def build_baseline_model_experiment_linkage_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build experiment linkage registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for item in EXPERIMENT_LINKAGES:
        rows.append({
            "linkage_id": item["linkage_id"],
            "experiment_template_ref": item["experiment_template_ref"],
            "model_contract_ref": item["model_contract_ref"],
            "phase_137_run_plan_ref": item["phase_137_run_plan_ref"],
            "phase_139_resource_governance_ref": item["phase_139_resource_governance_ref"],
            "is_run_executed": False,
            "training_job_active": False,
            "prediction_active": False,
            "artifact_saved": False,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_experiment_linkage(df)
    return df, summary


def summarize_baseline_model_experiment_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize experiment linkages."""
    return {
        "total_linkages": len(df),
        "zero_runs_executed": bool((~df["is_run_executed"]).all()) if not df.empty else True,
        "zero_training_jobs": bool((~df["training_job_active"]).all()) if not df.empty else True,
        "zero_predictions": bool((~df["prediction_active"]).all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
