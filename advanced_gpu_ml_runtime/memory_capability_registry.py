"""Phase 136: Memory Capability Registry.

Safely inspects system RAM and swap capacity without leaking process data,
secrets, or user file paths.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    MEMORY_CAPABILITY_DOMAIN,
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
)


def safe_detect_memory_capability() -> Dict[str, float]:
    """Safely query system memory with graceful fallback."""
    total_ram_gb = 8.0
    available_ram_gb = 4.0
    swap_total_gb = 0.0

    try:
        import psutil
        vm = psutil.virtual_memory()
        total_ram_gb = round(vm.total / (1024 ** 3), 2)
        available_ram_gb = round(vm.available / (1024 ** 3), 2)
        sm = psutil.swap_memory()
        swap_total_gb = round(sm.total / (1024 ** 3), 2)
    except ImportError:
        pass
    except Exception:
        pass

    return {
        "total_ram_gb": total_ram_gb,
        "available_ram_gb": available_ram_gb,
        "swap_total_gb": swap_total_gb,
    }


def build_memory_capability_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for memory capability registry."""
    active = profile or get_gpu_ml_runtime_profile()
    mem_info = safe_detect_memory_capability()

    is_low = mem_info["total_ram_gb"] < 4.0
    status = RUNTIME_READY_WITH_WARNINGS if is_low else RUNTIME_READY

    rows: List[Dict[str, Any]] = [
        {
            "memory_id": "mem_system_ram",
            "total_ram_gb": mem_info["total_ram_gb"],
            "available_ram_gb": mem_info["available_ram_gb"],
            "swap_total_gb": mem_info["swap_total_gb"],
            "capability_status": "sufficient" if not is_low else "low_memory",
            "status_label": status,
            "manual_review_required": is_low,
            "non_signal": True,
            "source_preserved": True,
            "details": f"Total RAM: {mem_info['total_ram_gb']} GB, Available: {mem_info['available_ram_gb']} GB, Swap: {mem_info['swap_total_gb']} GB.",
        }
    ]

    df = pd.DataFrame(rows)
    summary = summarize_memory_capability(df)
    summary["domain"] = MEMORY_CAPABILITY_DOMAIN
    summary["active_profile"] = active.profile_name
    summary["total_ram_gb"] = mem_info["total_ram_gb"]
    summary["available_ram_gb"] = mem_info["available_ram_gb"]
    return df, summary


def summarize_memory_capability(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize memory capability DataFrame."""
    return {
        "total_records": len(df),
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
