"""Phase 136: ML Training Disabled Policies.

Enforces absolute prohibition of model training, fitting, and parameter optimization.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    TRAINING_DISABLED_DOMAIN,
    RUNTIME_BLOCKED_BY_SAFETY,
    RUNTIME_READY,
)


FORBIDDEN_TRAINING_KEYWORDS = [
    "fit",
    "train",
    "fine_tune",
    "backpropagation",
    "gradient_step",
    "epoch",
    "optimizer_step",
    "backward",
]


def validate_no_training_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect a request or query string and intercept any training attempts."""
    req_text = str(request).lower()
    violations: List[str] = []

    for kw in FORBIDDEN_TRAINING_KEYWORDS:
        if kw in req_text:
            violations.append(kw)

    blocked = len(violations) > 0
    return {
        "is_safe": not blocked,
        "blocked": blocked,
        "violations": violations,
        "reason": f"Training forbidden keyword(s) detected: {violations}" if blocked else "Compliant with training disabled policy.",
        "non_signal": True,
        "source_preserved": True,
    }


def build_ml_training_disabled_policy_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for training disabled policies."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = [
        {
            "policy_id": "policy_no_fit",
            "target_routine": "estimator.fit()",
            "enforced": True,
            "status_label": RUNTIME_BLOCKED_BY_SAFETY,
            "details": "Direct fitting on feature matrices is strictly prohibited.",
        },
        {
            "policy_id": "policy_no_train",
            "target_routine": "model.train() / training loop",
            "enforced": True,
            "status_label": RUNTIME_BLOCKED_BY_SAFETY,
            "details": "Running gradient descent or training epochs is prohibited.",
        },
        {
            "policy_id": "policy_no_optimizer_step",
            "target_routine": "optimizer.step()",
            "enforced": True,
            "status_label": RUNTIME_BLOCKED_BY_SAFETY,
            "details": "Weight updates and gradient optimization are prohibited.",
        },
    ]

    for r in rows:
        r["non_signal"] = True
        r["source_preserved"] = True
        r["official_approval"] = False
        r["production_ready"] = False
        r["broker_ready"] = False

    df = pd.DataFrame(rows)
    summary = summarize_ml_training_disabled_policies(df)
    summary["domain"] = TRAINING_DISABLED_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_ml_training_disabled_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize training disabled policies DataFrame."""
    all_enf = bool(df["enforced"].all()) if not df.empty and "enforced" in df.columns else False
    return {
        "total_policies": len(df),
        "all_enforced": all_enf,
        "training_blocked": True,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
