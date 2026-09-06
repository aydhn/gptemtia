"""Phase 136: GPU ML Runtime Labels and Taxonomy.

Defines standardized domain, status, and backend capability labels.
"""

from typing import List


# Domain Labels
GPU_ML_RUNTIME_PROFILE_DOMAIN = "gpu_ml_runtime_profile_domain"
GPU_ML_RUNTIME_DOMAIN = "gpu_ml_runtime_domain"
LOCAL_HARDWARE_DOMAIN = "local_hardware_domain"
GPU_CAPABILITY_DOMAIN = "gpu_capability_domain"
CPU_CAPABILITY_DOMAIN = "cpu_capability_domain"
MEMORY_CAPABILITY_DOMAIN = "memory_capability_domain"
CUDA_CAPABILITY_DOMAIN = "cuda_capability_domain"
TORCH_CAPABILITY_DOMAIN = "torch_capability_domain"
SKLEARN_CAPABILITY_DOMAIN = "sklearn_capability_domain"
NUMPY_PANDAS_CAPABILITY_DOMAIN = "numpy_pandas_capability_domain"
OPTIONAL_DEPENDENCY_DOMAIN = "optional_dependency_domain"
ACCELERATOR_BACKEND_DOMAIN = "accelerator_backend_domain"
ENVIRONMENT_SNAPSHOT_DOMAIN = "environment_snapshot_domain"
RUNTIME_SAFETY_CONTRACT_DOMAIN = "runtime_safety_contract_domain"
EXPERIMENT_PERMISSION_DOMAIN = "experiment_permission_domain"
TRAINING_DISABLED_DOMAIN = "training_disabled_domain"
INFERENCE_DISABLED_DOMAIN = "inference_disabled_domain"
TARGET_LABEL_DISABLED_DOMAIN = "target_label_disabled_domain"
ARTIFACT_GOVERNANCE_PLACEHOLDER_DOMAIN = "artifact_governance_placeholder_domain"
REGIME_METADATA_INPUT_CONTRACT_DOMAIN = "regime_metadata_input_contract_domain"
FEATURESTORE_INPUT_CONTRACT_DOMAIN = "featurestore_input_contract_domain"
NO_LOOKAHEAD_INPUT_CONTRACT_DOMAIN = "no_lookahead_input_contract_domain"
METADATA_ONLY_NEWS_INPUT_CONTRACT_DOMAIN = "metadata_only_news_input_contract_domain"
SOURCE_PRESERVATION_INPUT_CONTRACT_DOMAIN = "source_preservation_input_contract_domain"
MANUAL_REVIEW_DOMAIN = "manual_review_domain"
FINDING_DOMAIN = "finding_domain"
READINESS_SCORE_DOMAIN = "readiness_score_domain"
MANIFEST_DOMAIN = "manifest_domain"
HEALTH_DOMAIN = "health_domain"
VALIDATION_DOMAIN = "validation_domain"
SAFETY_DOMAIN = "safety_domain"
PHASE_137_HANDOFF_DOMAIN = "phase_137_handoff_domain"
UNKNOWN_GPU_ML_RUNTIME_DOMAIN = "unknown_gpu_ml_runtime_domain"

ALL_DOMAINS: List[str] = [
    GPU_ML_RUNTIME_PROFILE_DOMAIN,
    GPU_ML_RUNTIME_DOMAIN,
    LOCAL_HARDWARE_DOMAIN,
    GPU_CAPABILITY_DOMAIN,
    CPU_CAPABILITY_DOMAIN,
    MEMORY_CAPABILITY_DOMAIN,
    CUDA_CAPABILITY_DOMAIN,
    TORCH_CAPABILITY_DOMAIN,
    SKLEARN_CAPABILITY_DOMAIN,
    NUMPY_PANDAS_CAPABILITY_DOMAIN,
    OPTIONAL_DEPENDENCY_DOMAIN,
    ACCELERATOR_BACKEND_DOMAIN,
    ENVIRONMENT_SNAPSHOT_DOMAIN,
    RUNTIME_SAFETY_CONTRACT_DOMAIN,
    EXPERIMENT_PERMISSION_DOMAIN,
    TRAINING_DISABLED_DOMAIN,
    INFERENCE_DISABLED_DOMAIN,
    TARGET_LABEL_DISABLED_DOMAIN,
    ARTIFACT_GOVERNANCE_PLACEHOLDER_DOMAIN,
    REGIME_METADATA_INPUT_CONTRACT_DOMAIN,
    FEATURESTORE_INPUT_CONTRACT_DOMAIN,
    NO_LOOKAHEAD_INPUT_CONTRACT_DOMAIN,
    METADATA_ONLY_NEWS_INPUT_CONTRACT_DOMAIN,
    SOURCE_PRESERVATION_INPUT_CONTRACT_DOMAIN,
    MANUAL_REVIEW_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_137_HANDOFF_DOMAIN,
]

# Status Labels
RUNTIME_READY = "runtime_ready"
RUNTIME_READY_WITH_WARNINGS = "runtime_ready_with_warnings"
RUNTIME_PLACEHOLDER_ONLY = "runtime_placeholder_only"
RUNTIME_MANUAL_REVIEW_REQUIRED = "runtime_manual_review_required"
RUNTIME_BLOCKED_BY_SAFETY = "runtime_blocked_by_safety"
RUNTIME_UNKNOWN = "runtime_unknown"

ALL_STATUSES: List[str] = [
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
    RUNTIME_PLACEHOLDER_ONLY,
    RUNTIME_MANUAL_REVIEW_REQUIRED,
    RUNTIME_BLOCKED_BY_SAFETY,
    RUNTIME_UNKNOWN,
]

# Backend Labels
BACKEND_CPU = "backend_cpu"
BACKEND_CUDA_GPU_AVAILABLE = "backend_cuda_gpu_available"
BACKEND_CUDA_GPU_UNAVAILABLE = "backend_cuda_gpu_unavailable"
BACKEND_TORCH_AVAILABLE = "backend_torch_available"
BACKEND_TORCH_UNAVAILABLE = "backend_torch_unavailable"
BACKEND_SKLEARN_AVAILABLE = "backend_sklearn_available"
BACKEND_OPTIONAL_DEPENDENCY_MISSING = "backend_optional_dependency_missing"
BACKEND_UNKNOWN = "backend_unknown"

ALL_BACKENDS: List[str] = [
    BACKEND_CPU,
    BACKEND_CUDA_GPU_AVAILABLE,
    BACKEND_CUDA_GPU_UNAVAILABLE,
    BACKEND_TORCH_AVAILABLE,
    BACKEND_TORCH_UNAVAILABLE,
    BACKEND_SKLEARN_AVAILABLE,
    BACKEND_OPTIONAL_DEPENDENCY_MISSING,
    BACKEND_UNKNOWN,
]


def list_gpu_ml_runtime_domain_labels() -> List[str]:
    """List all registered domain labels."""
    return list(ALL_DOMAINS)


def list_gpu_ml_runtime_status_labels() -> List[str]:
    """List all registered status labels."""
    return list(ALL_STATUSES)


def list_gpu_ml_backend_labels() -> List[str]:
    """List all registered backend labels."""
    return list(ALL_BACKENDS)


def validate_gpu_ml_runtime_domain_label(label: str) -> bool:
    """Validate whether domain label is recognized."""
    return label in ALL_DOMAINS


def validate_gpu_ml_runtime_status_label(label: str) -> bool:
    """Validate whether status label is recognized."""
    return label in ALL_STATUSES


def validate_gpu_ml_backend_label(label: str) -> bool:
    """Validate whether backend label is recognized."""
    return label in ALL_BACKENDS
