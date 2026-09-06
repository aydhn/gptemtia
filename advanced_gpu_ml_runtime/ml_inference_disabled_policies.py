"""Phase 136: ML Inference Disabled Policies.

Enforces absolute prohibition of model inference, forward passes, predictions, and transforms.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    INFERENCE_DISABLED_DOMAIN,
    RUNTIME_BLOCKED_BY_SAFETY,
)


FORBIDDEN_INFERENCE_KEYWORDS = [
    "predict",
    "predict_proba",
    "inference",
    "transform",
    "forward",
    "score_samples",
    "decision_function",
]


def validate_no_inference_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect a request or query string and intercept any inference attempts."""
    req_text = str(request).lower()
    violations: List[str] = []

    for kw in FORBIDDEN_INFERENCE_KEYWORDS:
        if kw in req_text:
            violations.append(kw)

    blocked = len(violations) > 0
    return {
        "is_safe": not blocked,
        "blocked": blocked,
        "violations": violations,
        "reason": f"Inference forbidden keyword(s) detected: {violations}" if blocked else "Compliant with inference disabled policy.",
        "non_signal": True,
        "source_preserved": True,
    }


def build_ml_inference_disabled_policy_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for inference disabled policies."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = [
        {
            "policy_id": "policy_no_predict",
            "target_routine": "estimator.predict() / model.forward()",
            "enforced": True,
            "status_label": RUNTIME_BLOCKED_BY_SAFETY,
            "details": "Model prediction and scoring on datasets are prohibited.",
        },
        {
            "policy_id": "policy_no_predict_proba",
            "target_routine": "estimator.predict_proba()",
            "enforced": True,
            "status_label": RUNTIME_BLOCKED_BY_SAFETY,
            "details": "Probability output calculation is prohibited.",
        },
        {
            "policy_id": "policy_no_transform",
            "target_routine": "transformer.transform()",
            "enforced": True,
            "status_label": RUNTIME_BLOCKED_BY_SAFETY,
            "details": "Data transformation via fitted models is prohibited.",
        },
    ]

    for r in rows:
        r["non_signal"] = True
        r["source_preserved"] = True
        r["official_approval"] = False
        r["production_ready"] = False
        r["broker_ready"] = False

    df = pd.DataFrame(rows)
    summary = summarize_ml_inference_disabled_policies(df)
    summary["domain"] = INFERENCE_DISABLED_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_ml_inference_disabled_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize inference disabled policies DataFrame."""
    all_enf = bool(df["enforced"].all()) if not df.empty and "enforced" in df.columns else False
    return {
        "total_policies": len(df),
        "all_enforced": all_enf,
        "inference_blocked": True,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
