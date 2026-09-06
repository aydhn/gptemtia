"""Phase 136: ML Experiment Permission Policies.

Defines precise operational permissions for what actions are allowed now vs blocked now.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    EXPERIMENT_PERMISSION_DOMAIN,
    RUNTIME_READY,
    RUNTIME_BLOCKED_BY_SAFETY,
)


PERMISSION_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_id": "perm_runtime_capability_detection",
        "action_name": "runtime capability detection",
        "permission_state": "allowed_now",
        "reason": "Safe local query of CPU, GPU, memory, and package availability.",
        "status_label": RUNTIME_READY,
    },
    {
        "policy_id": "perm_contract_generation",
        "action_name": "contract generation",
        "permission_state": "allowed_now",
        "reason": "Safe schema, boundary, and input specification modeling.",
        "status_label": RUNTIME_READY,
    },
    {
        "policy_id": "perm_model_training",
        "action_name": "model training",
        "permission_state": "blocked_now",
        "reason": "Model training is prohibited in Phase 136 foundation.",
        "status_label": RUNTIME_BLOCKED_BY_SAFETY,
    },
    {
        "policy_id": "perm_model_prediction",
        "action_name": "model prediction",
        "permission_state": "blocked_now",
        "reason": "Inference and model prediction are prohibited in Phase 136.",
        "status_label": RUNTIME_BLOCKED_BY_SAFETY,
    },
    {
        "policy_id": "perm_target_label_generation",
        "action_name": "target label generation",
        "permission_state": "blocked_now",
        "reason": "Target and label synthesis is strictly blocked.",
        "status_label": RUNTIME_BLOCKED_BY_SAFETY,
    },
    {
        "policy_id": "perm_clustering_execution",
        "action_name": "clustering execution",
        "permission_state": "blocked_now",
        "reason": "Clustering execution is prohibited.",
        "status_label": RUNTIME_BLOCKED_BY_SAFETY,
    },
    {
        "policy_id": "perm_ensemble_execution",
        "action_name": "ensemble execution",
        "permission_state": "blocked_now",
        "reason": "Ensemble evaluation is prohibited.",
        "status_label": RUNTIME_BLOCKED_BY_SAFETY,
    },
    {
        "policy_id": "perm_calibration_execution",
        "action_name": "calibration execution",
        "permission_state": "blocked_now",
        "reason": "Probability calibration routines are prohibited.",
        "status_label": RUNTIME_BLOCKED_BY_SAFETY,
    },
    {
        "policy_id": "perm_artifact_persistence",
        "action_name": "artifact persistence",
        "permission_state": "blocked_now",
        "reason": "Serializing model artifacts or registry writes is blocked.",
        "status_label": RUNTIME_BLOCKED_BY_SAFETY,
    },
    {
        "policy_id": "perm_broker_live_integration",
        "action_name": "broker/live integration",
        "permission_state": "blocked_now",
        "reason": "Live trading and broker integration are permanently prohibited.",
        "status_label": RUNTIME_BLOCKED_BY_SAFETY,
    },
]


def validate_ml_experiment_permission(policy: Dict[str, Any]) -> Dict[str, Any]:
    """Validate permission policy structure and state."""
    state = policy.get("permission_state", "")
    is_valid = state in ("allowed_now", "blocked_now")
    return {
        "policy_id": policy.get("policy_id", "unknown"),
        "is_valid": is_valid,
        "permission_state": state,
        "non_signal": True,
        "source_preserved": True,
    }


def build_ml_experiment_permission_policy_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for experiment permission policies."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = []
    for p in PERMISSION_POLICIES:
        rows.append(
            {
                "policy_id": p["policy_id"],
                "action_name": p["action_name"],
                "permission_state": p["permission_state"],
                "reason": p["reason"],
                "status_label": p["status_label"],
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ml_experiment_permission_policies(df)
    summary["domain"] = EXPERIMENT_PERMISSION_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_ml_experiment_permission_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize experiment permission policies DataFrame."""
    allowed_count = int((df["permission_state"] == "allowed_now").sum()) if not df.empty and "permission_state" in df.columns else 0
    blocked_count = int((df["permission_state"] == "blocked_now").sum()) if not df.empty and "permission_state" in df.columns else 0
    return {
        "total_policies": len(df),
        "allowed_now_count": allowed_count,
        "blocked_now_count": blocked_count,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
