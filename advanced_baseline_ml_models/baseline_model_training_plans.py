# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Training Plans Registry.

Defines dry-run training plan configurations that prohibit actual model fitting,
specifying simulated run constraints and safety limits.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_families import BASELINE_MODEL_FAMILIES_DATA


def build_baseline_model_training_plan_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build training plans registry DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for fam in BASELINE_MODEL_FAMILIES_DATA:
        rows.append({
            "plan_name": f"plan_{fam['family_id']}",
            "model_contract_ref": f"contract_{fam['family_id']}",
            "dataset_contract_ref": "ds_contract_balanced_commodity_fx",
            "split_policy_ref": "time_series_split_policy_walk_forward_v1",
            "runtime_profile_ref": "balanced_local_gpu_ml_runtime_foundation",
            "allowed_mode": "contract_only",
            "real_training_allowed": False,
            "dry_run_allowed": True,
            "target_label_required": False,
            "artifact_persistence_allowed": False,
            "manual_review_required": True,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_training_plans(df)
    return df, summary


def summarize_baseline_model_training_plans(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline model training plans."""
    return {
        "total_training_plans": len(df),
        "all_contract_only": bool((df["allowed_mode"] == "contract_only").all()) if not df.empty else True,
        "zero_real_training_allowed": bool((~df["real_training_allowed"]).all()) if not df.empty else True,
        "all_dry_run_allowed": bool(df["dry_run_allowed"].all()) if not df.empty else True,
        "zero_target_label_required": bool((~df["target_label_required"]).all()) if not df.empty else True,
        "zero_artifact_persistence": bool((~df["artifact_persistence_allowed"]).all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
