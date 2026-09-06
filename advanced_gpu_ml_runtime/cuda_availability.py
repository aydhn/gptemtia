"""Phase 136: CUDA Availability Report.

Inspects CUDA driver and runtime status without training models,
allocating persistent memory, or calling remote endpoints.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    CUDA_CAPABILITY_DOMAIN,
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
    BACKEND_CUDA_GPU_AVAILABLE,
    BACKEND_CUDA_GPU_UNAVAILABLE,
)


def safe_detect_cuda_availability() -> Dict[str, Any]:
    """Safely detect CUDA driver and runtime version."""
    cuda_available = False
    cuda_version = "none"
    device_count = 0
    arch_list: List[str] = []

    try:
        import torch
        cuda_available = bool(torch.cuda.is_available())
        if cuda_available:
            cuda_version = str(torch.version.cuda or "unknown")
            device_count = torch.cuda.device_count()
            if hasattr(torch.cuda, "get_arch_list"):
                arch_list = torch.cuda.get_arch_list()
    except ImportError:
        pass
    except Exception:
        pass

    return {
        "cuda_available": cuda_available,
        "cuda_version": cuda_version,
        "device_count": device_count,
        "arch_list": arch_list[:5],
    }


def build_cuda_availability_report(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for CUDA availability."""
    active = profile or get_gpu_ml_runtime_profile()
    cuda_info = safe_detect_cuda_availability()

    status_label = RUNTIME_READY if cuda_info["cuda_available"] else RUNTIME_READY_WITH_WARNINGS
    backend_status = BACKEND_CUDA_GPU_AVAILABLE if cuda_info["cuda_available"] else BACKEND_CUDA_GPU_UNAVAILABLE

    rows: List[Dict[str, Any]] = [
        {
            "check_id": "cuda_is_available",
            "metric_name": "CUDA Available",
            "metric_value": str(cuda_info["cuda_available"]),
            "backend_label": backend_status,
            "status_label": status_label,
            "manual_review_required": not cuda_info["cuda_available"],
            "non_signal": True,
            "source_preserved": True,
            "details": "Indicates whether CUDA-capable device and driver are accessible to Python.",
        },
        {
            "check_id": "cuda_version",
            "metric_name": "CUDA Runtime Version",
            "metric_value": cuda_info["cuda_version"],
            "backend_label": backend_status,
            "status_label": status_label,
            "manual_review_required": False,
            "non_signal": True,
            "source_preserved": True,
            "details": "Linked CUDA toolkit version string.",
        },
        {
            "check_id": "cuda_device_count",
            "metric_name": "CUDA Device Count",
            "metric_value": str(cuda_info["device_count"]),
            "backend_label": backend_status,
            "status_label": status_label,
            "manual_review_required": False,
            "non_signal": True,
            "source_preserved": True,
            "details": "Number of recognized CUDA compute devices.",
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_cuda_availability(df)
    summary["domain"] = CUDA_CAPABILITY_DOMAIN
    summary["active_profile"] = active.profile_name
    summary["cuda_available"] = cuda_info["cuda_available"]
    return df, summary


def summarize_cuda_availability(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize CUDA availability DataFrame."""
    cuda_val = False
    if not df.empty and "metric_name" in df.columns:
        match = df[df["metric_name"] == "CUDA Available"]
        if not match.empty:
            cuda_val = match.iloc[0]["metric_value"] == "True"
    return {
        "total_checks": len(df),
        "cuda_available": cuda_val,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
