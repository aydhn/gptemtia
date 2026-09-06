"""Phase 136: CPU Capability Registry.

Safely inspects CPU architecture, physical/logical core counts, and frequency
without executing benchmarks, model training, or secret leakage.
"""

import os
import platform
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    CPU_CAPABILITY_DOMAIN,
    RUNTIME_READY,
    BACKEND_CPU,
)


def safe_detect_cpu_capability() -> Dict[str, Any]:
    """Safely query CPU architecture and core details with graceful psutil fallback."""
    arch = platform.machine()
    logical_cores = os.cpu_count() or 1
    physical_cores = logical_cores // 2 or 1
    freq_mhz = 0.0

    try:
        import psutil
        p_count = psutil.cpu_count(logical=False)
        if p_count:
            physical_cores = p_count
        l_count = psutil.cpu_count(logical=True)
        if l_count:
            logical_cores = l_count
        cpu_freq = psutil.cpu_freq()
        if cpu_freq:
            freq_mhz = float(cpu_freq.current or cpu_freq.max or 0.0)
    except ImportError:
        pass
    except Exception:
        pass

    return {
        "architecture": arch,
        "physical_cores": physical_cores,
        "logical_cores": logical_cores,
        "freq_mhz": freq_mhz,
    }


def build_cpu_capability_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for CPU capability registry."""
    active = profile or get_gpu_ml_runtime_profile()
    cpu_info = safe_detect_cpu_capability()

    rows: List[Dict[str, Any]] = [
        {
            "cpu_id": "cpu_host_primary",
            "architecture": cpu_info["architecture"],
            "physical_cores": cpu_info["physical_cores"],
            "logical_cores": cpu_info["logical_cores"],
            "cpu_freq_mhz": cpu_info["freq_mhz"],
            "capability_status": BACKEND_CPU,
            "status_label": RUNTIME_READY,
            "manual_review_required": False,
            "non_signal": True,
            "source_preserved": True,
            "details": f"Local host CPU: {cpu_info['physical_cores']} phys / {cpu_info['logical_cores']} log cores ({cpu_info['architecture']}).",
        }
    ]

    df = pd.DataFrame(rows)
    summary = summarize_cpu_capability(df)
    summary["domain"] = CPU_CAPABILITY_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_cpu_capability(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize CPU capability DataFrame."""
    return {
        "total_cpus": len(df),
        "status_label": RUNTIME_READY,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
