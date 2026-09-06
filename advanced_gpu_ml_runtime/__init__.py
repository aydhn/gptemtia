"""Phase 136: GPU Acceleration and Advanced ML Runtime Foundation.

Provides hardware discovery, accelerator capabilities, safety contracts,
and Phase 137 handoff specifications for offline ML research.
"""

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
    get_default_gpu_ml_runtime_profile,
    list_gpu_ml_runtime_profiles,
    validate_gpu_ml_runtime_profiles,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    GPU_ML_RUNTIME_DOMAIN,
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
    RUNTIME_PLACEHOLDER_ONLY,
    RUNTIME_BLOCKED_BY_SAFETY,
    BACKEND_CPU,
    BACKEND_CUDA_GPU_AVAILABLE,
    BACKEND_CUDA_GPU_UNAVAILABLE,
    BACKEND_TORCH_AVAILABLE,
    BACKEND_TORCH_UNAVAILABLE,
    BACKEND_SKLEARN_AVAILABLE,
    list_gpu_ml_runtime_domain_labels,
    list_gpu_ml_runtime_status_labels,
    list_gpu_ml_backend_labels,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_pipeline import GpuMlRuntimePipeline

__all__ = [
    "GpuMlRuntimeProfile",
    "get_gpu_ml_runtime_profile",
    "get_default_gpu_ml_runtime_profile",
    "list_gpu_ml_runtime_profiles",
    "validate_gpu_ml_runtime_profiles",
    "GPU_ML_RUNTIME_DOMAIN",
    "RUNTIME_READY",
    "RUNTIME_READY_WITH_WARNINGS",
    "RUNTIME_PLACEHOLDER_ONLY",
    "RUNTIME_BLOCKED_BY_SAFETY",
    "BACKEND_CPU",
    "BACKEND_CUDA_GPU_AVAILABLE",
    "BACKEND_CUDA_GPU_UNAVAILABLE",
    "BACKEND_TORCH_AVAILABLE",
    "BACKEND_TORCH_UNAVAILABLE",
    "BACKEND_SKLEARN_AVAILABLE",
    "list_gpu_ml_runtime_domain_labels",
    "list_gpu_ml_runtime_status_labels",
    "list_gpu_ml_backend_labels",
    "GpuMlRuntimePipeline",
]
