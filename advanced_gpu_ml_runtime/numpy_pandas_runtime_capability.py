"""Phase 136: NumPy and Pandas Runtime Capability Report.

Inspects core array and dataframe runtime capabilities, versions,
and hardware acceleration linkage without modifying tables or calculating signals.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    NUMPY_PANDAS_CAPABILITY_DOMAIN,
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
    BACKEND_CPU,
)


def safe_detect_numpy_pandas_runtime() -> Dict[str, Any]:
    """Safely detect NumPy and Pandas installation and versions."""
    np_installed = False
    np_version = "not_installed"
    pd_installed = False
    pd_version = "not_installed"

    try:
        import numpy as np
        np_installed = True
        np_version = str(getattr(np, "__version__", "unknown"))
    except ImportError:
        pass
    except Exception:
        pass

    try:
        import pandas as pnd
        pd_installed = True
        pd_version = str(getattr(pnd, "__version__", "unknown"))
    except ImportError:
        pass
    except Exception:
        pass

    return {
        "numpy_installed": np_installed,
        "numpy_version": np_version,
        "pandas_installed": pd_installed,
        "pandas_version": pd_version,
    }


def build_numpy_pandas_runtime_capability_report(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for NumPy and Pandas runtime capability."""
    active = profile or get_gpu_ml_runtime_profile()
    core_info = safe_detect_numpy_pandas_runtime()

    rows: List[Dict[str, Any]] = [
        {
            "check_id": "numpy_version",
            "package_name": "numpy",
            "installed": core_info["numpy_installed"],
            "version": core_info["numpy_version"],
            "backend_label": BACKEND_CPU,
            "status_label": RUNTIME_READY if core_info["numpy_installed"] else RUNTIME_READY_WITH_WARNINGS,
            "manual_review_required": not core_info["numpy_installed"],
            "non_signal": True,
            "source_preserved": True,
            "details": "Core tensor/array mathematical operations foundation.",
        },
        {
            "check_id": "pandas_version",
            "package_name": "pandas",
            "installed": core_info["pandas_installed"],
            "version": core_info["pandas_version"],
            "backend_label": BACKEND_CPU,
            "status_label": RUNTIME_READY if core_info["pandas_installed"] else RUNTIME_READY_WITH_WARNINGS,
            "manual_review_required": not core_info["pandas_installed"],
            "non_signal": True,
            "source_preserved": True,
            "details": "Tabular dataframe manipulation foundation.",
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_numpy_pandas_runtime_capability(df)
    summary["domain"] = NUMPY_PANDAS_CAPABILITY_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_numpy_pandas_runtime_capability(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize NumPy and Pandas runtime capability DataFrame."""
    all_inst = bool(df["installed"].all()) if not df.empty and "installed" in df.columns else False
    return {
        "total_packages": len(df),
        "all_installed": all_inst,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
