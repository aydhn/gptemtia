"""Phase 136: ML Runtime Manual Review Queue.

Provides actionable operator review items strictly avoiding destructive actions,
auto-installs, model training, or trading signals.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    MANUAL_REVIEW_DOMAIN,
    RUNTIME_READY,
)
from advanced_gpu_ml_runtime.gpu_capability_registry import safe_detect_gpu_capability
from advanced_gpu_ml_runtime.torch_runtime_capability import safe_detect_torch_runtime
from advanced_gpu_ml_runtime.sklearn_runtime_capability import safe_detect_sklearn_runtime
from advanced_gpu_ml_runtime.memory_capability_registry import safe_detect_memory_capability


REVIEW_ITEMS: List[Dict[str, Any]] = [
    {
        "review_id": "review_gpu_cuda",
        "domain": "gpu_capability",
        "topic": "Inspect GPU and CUDA Hardware Availability",
        "recommended_action": "Verify if local host has supported NVIDIA hardware and matching CUDA runtime installed.",
        "forbidden_action_warning": "Do not attempt model training or benchmark stress-testing.",
    },
    {
        "review_id": "review_framework_pkgs",
        "domain": "dependencies",
        "topic": "Inspect PyTorch and Scikit-Learn Packages",
        "recommended_action": "Check if required ML packages are available in the virtualenv; install offline if needed.",
        "forbidden_action_warning": "Do not auto-install unvetted third-party packages or run auto-scrapers.",
    },
    {
        "review_id": "review_memory_limits",
        "domain": "memory_capability",
        "topic": "Inspect System Host RAM Capacity",
        "recommended_action": "Verify host memory meets minimum thresholds for feature matrix loading.",
        "forbidden_action_warning": "Do not delete or truncate historical DataLake records to save disk space.",
    },
    {
        "review_id": "review_no_training_policy",
        "domain": "safety_policies",
        "topic": "Verify No-Training and No-Inference Enforcement",
        "recommended_action": "Audit codebase to ensure all model training and prediction routines remain disabled in Phase 136.",
        "forbidden_action_warning": "Do not enable model training or inference loops.",
    },
    {
        "review_id": "review_input_accepted_refs",
        "domain": "input_contracts",
        "topic": "Inspect Regime and FeatureStore Accepted References",
        "recommended_action": "Verify that input matrices source exclusively from Phase 133-135 accepted catalogs.",
        "forbidden_action_warning": "Do not inject forward returns, future targets, raw article bodies, or trade signals.",
    },
    {
        "review_id": "review_phase_137_blockers",
        "domain": "handoff",
        "topic": "Inspect Phase 137 Dataset and Experiment Blockers",
        "recommended_action": "Ensure dataset contract requirements and experiment schemas are fully specified before Phase 137.",
        "forbidden_action_warning": "Do not approve production deployment or broker connectivity.",
    },
]


def build_ml_runtime_manual_review_queue(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for manual review queue."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = []
    for item in REVIEW_ITEMS:
        rows.append(
            {
                "review_id": item["review_id"],
                "domain": item["domain"],
                "topic": item["topic"],
                "recommended_action": item["recommended_action"],
                "forbidden_action_warning": item["forbidden_action_warning"],
                "status_label": RUNTIME_READY,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ml_runtime_manual_review_queue(df)
    summary["domain"] = MANUAL_REVIEW_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_ml_runtime_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue DataFrame."""
    return {
        "total_review_items": len(df),
        "status_label": RUNTIME_READY,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
