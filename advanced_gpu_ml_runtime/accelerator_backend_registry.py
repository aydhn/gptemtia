"""Phase 136: Accelerator Backend Registry.

Catalogs active compute engines and future accelerator backend placeholders.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    ACCELERATOR_BACKEND_DOMAIN,
    RUNTIME_READY,
    RUNTIME_PLACEHOLDER_ONLY,
    BACKEND_CPU,
    BACKEND_CUDA_GPU_AVAILABLE,
    BACKEND_CUDA_GPU_UNAVAILABLE,
)
from advanced_gpu_ml_runtime.gpu_capability_registry import safe_detect_gpu_capability
from advanced_gpu_ml_runtime.torch_runtime_capability import safe_detect_torch_runtime
from advanced_gpu_ml_runtime.sklearn_runtime_capability import safe_detect_sklearn_runtime


def build_accelerator_backend_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for accelerator backend registry."""
    active = profile or get_gpu_ml_runtime_profile()

    gpu_info = safe_detect_gpu_capability()
    torch_info = safe_detect_torch_runtime()
    sk_info = safe_detect_sklearn_runtime()

    rows: List[Dict[str, Any]] = [
        {
            "backend_id": "backend_cpu",
            "backend_name": "CPU Host Execution Backend",
            "backend_type": "cpu",
            "available": True,
            "priority_order": 1,
            "status_label": RUNTIME_READY,
            "non_signal": True,
            "source_preserved": True,
            "details": "Standard CPU host execution with numpy/scipy/pandas.",
        },
        {
            "backend_id": "backend_cuda",
            "backend_name": "NVIDIA CUDA Accelerator Backend",
            "backend_type": "cuda",
            "available": gpu_info["cuda_available"],
            "priority_order": 2,
            "status_label": RUNTIME_READY if gpu_info["cuda_available"] else RUNTIME_PLACEHOLDER_ONLY,
            "non_signal": True,
            "source_preserved": True,
            "details": "NVIDIA CUDA hardware accelerator backend." if gpu_info["cuda_available"] else "CUDA backend unavailable in local host.",
        },
        {
            "backend_id": "backend_torch",
            "backend_name": "PyTorch Compute Backend",
            "backend_type": "framework",
            "available": torch_info["installed"],
            "priority_order": 3,
            "status_label": RUNTIME_READY if torch_info["installed"] else RUNTIME_PLACEHOLDER_ONLY,
            "non_signal": True,
            "source_preserved": True,
            "details": f"PyTorch tensor framework ({torch_info['version']}).",
        },
        {
            "backend_id": "backend_sklearn",
            "backend_name": "Scikit-Learn Backend",
            "backend_type": "framework",
            "available": sk_info["installed"],
            "priority_order": 4,
            "status_label": RUNTIME_READY if sk_info["installed"] else RUNTIME_PLACEHOLDER_ONLY,
            "non_signal": True,
            "source_preserved": True,
            "details": f"Scikit-learn classical ML foundation ({sk_info['version']}).",
        },
        {
            "backend_id": "optional_gradient_boosting_backend_placeholder",
            "backend_name": "Gradient Boosting Backend Placeholder",
            "backend_type": "placeholder",
            "available": False,
            "priority_order": 5,
            "status_label": RUNTIME_PLACEHOLDER_ONLY,
            "non_signal": True,
            "source_preserved": True,
            "details": "Placeholder for upcoming LightGBM/XGBoost/CatBoost accelerators.",
        },
        {
            "backend_id": "future_gpu_dataframe_backend_placeholder",
            "backend_name": "GPU DataFrame (cuDF/Polars) Backend Placeholder",
            "backend_type": "placeholder",
            "available": False,
            "priority_order": 6,
            "status_label": RUNTIME_PLACEHOLDER_ONLY,
            "non_signal": True,
            "source_preserved": True,
            "details": "Placeholder for accelerated GPU-memory dataframe joins.",
        },
        {
            "backend_id": "future_onnx_runtime_placeholder",
            "backend_name": "ONNX Runtime Acceleration Placeholder",
            "backend_type": "placeholder",
            "available": False,
            "priority_order": 7,
            "status_label": RUNTIME_PLACEHOLDER_ONLY,
            "non_signal": True,
            "source_preserved": True,
            "details": "Placeholder for cross-platform model graph evaluation.",
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_accelerator_backends(df)
    summary["domain"] = ACCELERATOR_BACKEND_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_accelerator_backends(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize accelerator backend DataFrame."""
    avail_count = int(df["available"].sum()) if not df.empty and "available" in df.columns else 0
    return {
        "total_backends": len(df),
        "available_backends": avail_count,
        "placeholder_backends": len(df) - avail_count,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
