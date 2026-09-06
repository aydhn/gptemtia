"""Phase 136: PyTorch Runtime Capability Report.

Safely detects PyTorch package availability, version, and backend device support
without executing tensor math, gradient computations, model initialization, or training.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    TORCH_CAPABILITY_DOMAIN,
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
    BACKEND_TORCH_AVAILABLE,
    BACKEND_TORCH_UNAVAILABLE,
)


def safe_detect_torch_runtime() -> Dict[str, Any]:
    """Safely check PyTorch import and capabilities without allocating memory."""
    installed = False
    version = "not_installed"
    cuda_available = False
    mps_available = False

    try:
        import torch
        installed = True
        version = str(getattr(torch, "__version__", "unknown"))
        if hasattr(torch, "cuda"):
            cuda_available = bool(torch.cuda.is_available())
        if hasattr(torch.backends, "mps"):
            mps_available = bool(torch.backends.mps.is_available())
    except ImportError:
        pass
    except Exception:
        pass

    return {
        "installed": installed,
        "version": version,
        "cuda_available": cuda_available,
        "mps_available": mps_available,
    }


def build_torch_runtime_capability_report(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for PyTorch capability."""
    active = profile or get_gpu_ml_runtime_profile()
    torch_info = safe_detect_torch_runtime()

    status = RUNTIME_READY if torch_info["installed"] else RUNTIME_READY_WITH_WARNINGS
    backend = BACKEND_TORCH_AVAILABLE if torch_info["installed"] else BACKEND_TORCH_UNAVAILABLE

    rows: List[Dict[str, Any]] = [
        {
            "check_id": "torch_installed",
            "property_name": "PyTorch Installed",
            "property_value": str(torch_info["installed"]),
            "backend_label": backend,
            "status_label": status,
            "manual_review_required": not torch_info["installed"],
            "non_signal": True,
            "source_preserved": True,
            "details": "Checks if PyTorch package is present in active environment.",
        },
        {
            "check_id": "torch_version",
            "property_name": "PyTorch Version",
            "property_value": torch_info["version"],
            "backend_label": backend,
            "status_label": status,
            "manual_review_required": False,
            "non_signal": True,
            "source_preserved": True,
            "details": "Installed PyTorch release version string.",
        },
        {
            "check_id": "torch_cuda_linked",
            "property_name": "PyTorch CUDA Support",
            "property_value": str(torch_info["cuda_available"]),
            "backend_label": backend,
            "status_label": RUNTIME_READY if torch_info["cuda_available"] else RUNTIME_READY_WITH_WARNINGS,
            "manual_review_required": False,
            "non_signal": True,
            "source_preserved": True,
            "details": "PyTorch CUDA accelerator device linkage status.",
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_torch_runtime_capability(df)
    summary["domain"] = TORCH_CAPABILITY_DOMAIN
    summary["active_profile"] = active.profile_name
    summary["torch_installed"] = torch_info["installed"]
    return df, summary


def summarize_torch_runtime_capability(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize PyTorch capability DataFrame."""
    installed = False
    if not df.empty and "property_name" in df.columns:
        m = df[df["property_name"] == "PyTorch Installed"]
        if not m.empty:
            installed = m.iloc[0]["property_value"] == "True"
    return {
        "total_checks": len(df),
        "torch_installed": installed,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
