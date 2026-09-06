"""Phase 136: GPU Capability Registry.

Safely detects local NVIDIA/CUDA GPU availability, device counts, names, and VRAM
without executing model training, allocating persistent tensors, or making network calls.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    GPU_CAPABILITY_DOMAIN,
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
    BACKEND_CUDA_GPU_AVAILABLE,
    BACKEND_CUDA_GPU_UNAVAILABLE,
)


def safe_detect_gpu_capability() -> Dict[str, Any]:
    """Safely query torch/system GPU capability with graceful CPU fallback."""
    cuda_available = False
    device_count = 0
    devices: List[Dict[str, Any]] = []

    try:
        import torch
        cuda_available = bool(torch.cuda.is_available())
        if cuda_available:
            device_count = torch.cuda.device_count()
            for idx in range(device_count):
                name = torch.cuda.get_device_name(idx)
                # Query device properties safely
                try:
                    props = torch.cuda.get_device_properties(idx)
                    mem_mb = round(props.total_memory / (1024 * 1024), 2)
                except Exception:
                    mem_mb = 0.0
                devices.append({
                    "device_index": idx,
                    "name": name,
                    "total_memory_mb": mem_mb,
                })
    except ImportError:
        pass
    except Exception:
        pass

    return {
        "cuda_available": cuda_available,
        "device_count": device_count,
        "devices": devices,
    }


def build_gpu_capability_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for GPU capability registry."""
    active = profile or get_gpu_ml_runtime_profile()
    gpu_info = safe_detect_gpu_capability()

    rows: List[Dict[str, Any]] = []
    if gpu_info["cuda_available"] and gpu_info["devices"]:
        for dev in gpu_info["devices"]:
            rows.append({
                "gpu_id": f"gpu_{dev['device_index']}",
                "gpu_name": dev["name"],
                "cuda_available": True,
                "device_count": gpu_info["device_count"],
                "memory_total_mb": dev["total_memory_mb"],
                "capability_status": BACKEND_CUDA_GPU_AVAILABLE,
                "status_label": RUNTIME_READY,
                "manual_review_required": False,
                "non_signal": True,
                "source_preserved": True,
                "details": f"CUDA GPU {dev['device_index']} detected: {dev['name']}.",
            })
    else:
        rows.append({
            "gpu_id": "gpu_none",
            "gpu_name": "No CUDA GPU Detected / CPU Fallback",
            "cuda_available": False,
            "device_count": 0,
            "memory_total_mb": 0.0,
            "capability_status": BACKEND_CUDA_GPU_UNAVAILABLE,
            "status_label": RUNTIME_READY_WITH_WARNINGS,
            "manual_review_required": True,
            "non_signal": True,
            "source_preserved": True,
            "details": "GPU acceleration not present; CPU runtime fallback active.",
        })

    df = pd.DataFrame(rows)
    summary = summarize_gpu_capability(df)
    summary["domain"] = GPU_CAPABILITY_DOMAIN
    summary["active_profile"] = active.profile_name
    summary["cuda_available"] = gpu_info["cuda_available"]
    summary["device_count"] = gpu_info["device_count"]
    return df, summary


def summarize_gpu_capability(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize GPU capability DataFrame."""
    cuda_active = bool(df["cuda_available"].any()) if not df.empty and "cuda_available" in df.columns else False
    return {
        "total_records": len(df),
        "cuda_gpu_detected": cuda_active,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
