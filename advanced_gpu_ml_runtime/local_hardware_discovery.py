"""Phase 136: Local Hardware Discovery.

Inspects local operating system, architecture, Python environment, and hardware capabilities
strictly offline without network calls, secret leakage, or model execution.
"""

import os
import platform
import sys
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    LOCAL_HARDWARE_DOMAIN,
    RUNTIME_READY,
)


def safe_collect_platform_info() -> Dict[str, str]:
    """Safely gather platform metadata without leaking private paths or credentials."""
    return {
        "os_name": platform.system(),
        "os_release": platform.release(),
        "os_version": platform.version()[:50] if platform.version() else "unknown",
        "architecture": platform.machine(),
        "processor": platform.processor()[:50] if platform.processor() else "unknown",
    }


def safe_collect_python_info() -> Dict[str, str]:
    """Safely gather Python interpreter metadata without leaking user paths or virtualenv secrets."""
    return {
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "python_compiler": platform.python_compiler()[:50] if platform.python_compiler() else "unknown",
        "byteorder": sys.byteorder,
    }


def build_local_hardware_discovery_report(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for local hardware discovery."""
    active = profile or get_gpu_ml_runtime_profile()

    plat_info = safe_collect_platform_info()
    py_info = safe_collect_python_info()

    rows: List[Dict[str, Any]] = [
        {
            "item_id": "hw_os_system",
            "category": "operating_system",
            "property_name": "system",
            "property_value": plat_info["os_name"],
            "status_label": RUNTIME_READY,
            "non_signal": True,
            "source_preserved": True,
            "manual_review_required": False,
            "details": "Operating system family safely discovered.",
        },
        {
            "item_id": "hw_os_release",
            "category": "operating_system",
            "property_name": "release",
            "property_value": plat_info["os_release"],
            "status_label": RUNTIME_READY,
            "non_signal": True,
            "source_preserved": True,
            "manual_review_required": False,
            "details": "OS release version.",
        },
        {
            "item_id": "hw_cpu_arch",
            "category": "cpu_hardware",
            "property_name": "machine_arch",
            "property_value": plat_info["architecture"],
            "status_label": RUNTIME_READY,
            "non_signal": True,
            "source_preserved": True,
            "manual_review_required": False,
            "details": "Machine instruction architecture.",
        },
        {
            "item_id": "hw_cpu_proc",
            "category": "cpu_hardware",
            "property_name": "processor",
            "property_value": plat_info["processor"],
            "status_label": RUNTIME_READY,
            "non_signal": True,
            "source_preserved": True,
            "manual_review_required": False,
            "details": "Processor identification string.",
        },
        {
            "item_id": "hw_py_version",
            "category": "python_runtime",
            "property_name": "python_version",
            "property_value": py_info["python_version"],
            "status_label": RUNTIME_READY,
            "non_signal": True,
            "source_preserved": True,
            "manual_review_required": False,
            "details": "Python runtime version.",
        },
        {
            "item_id": "hw_py_impl",
            "category": "python_runtime",
            "property_name": "python_implementation",
            "property_value": py_info["python_implementation"],
            "status_label": RUNTIME_READY,
            "non_signal": True,
            "source_preserved": True,
            "manual_review_required": False,
            "details": "Python implementation type.",
        },
    ]

    # CPU core count inspection
    cpu_count = os.cpu_count() or 1
    rows.append(
        {
            "item_id": "hw_cpu_cores",
            "category": "cpu_hardware",
            "property_name": "logical_cores",
            "property_value": str(cpu_count),
            "status_label": RUNTIME_READY,
            "non_signal": True,
            "source_preserved": True,
            "manual_review_required": False,
            "details": "Logical CPU core count available.",
        }
    )

    df = pd.DataFrame(rows)
    summary = summarize_local_hardware_discovery(df)
    summary["domain"] = LOCAL_HARDWARE_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_local_hardware_discovery(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize local hardware discovery DataFrame."""
    return {
        "total_items": len(df),
        "all_ready": bool((df["status_label"] == RUNTIME_READY).all()) if not df.empty else True,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
