"""Test suite for Phase 136 GPU ML Runtime Labels."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    GPU_ML_RUNTIME_DOMAIN,
    LOCAL_HARDWARE_DOMAIN,
    GPU_CAPABILITY_DOMAIN,
    CPU_CAPABILITY_DOMAIN,
    MEMORY_CAPABILITY_DOMAIN,
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
    RUNTIME_PLACEHOLDER_ONLY,
    RUNTIME_BLOCKED_BY_SAFETY,
    BACKEND_CPU,
    BACKEND_CUDA_GPU_AVAILABLE,
    BACKEND_CUDA_GPU_UNAVAILABLE,
    list_gpu_ml_runtime_domain_labels,
    list_gpu_ml_runtime_status_labels,
    list_gpu_ml_backend_labels,
    validate_gpu_ml_runtime_domain_label,
    validate_gpu_ml_runtime_status_label,
    validate_gpu_ml_backend_label,
)


def test_label_lists():
    domains = list_gpu_ml_runtime_domain_labels()
    assert len(domains) >= 20
    assert GPU_ML_RUNTIME_DOMAIN in domains
    assert LOCAL_HARDWARE_DOMAIN in domains
    assert GPU_CAPABILITY_DOMAIN in domains

    statuses = list_gpu_ml_runtime_status_labels()
    assert RUNTIME_READY in statuses
    assert RUNTIME_READY_WITH_WARNINGS in statuses
    assert RUNTIME_PLACEHOLDER_ONLY in statuses
    assert RUNTIME_BLOCKED_BY_SAFETY in statuses

    backends = list_gpu_ml_backend_labels()
    assert BACKEND_CPU in backends
    assert BACKEND_CUDA_GPU_AVAILABLE in backends


def test_label_validators():
    assert validate_gpu_ml_runtime_domain_label(GPU_ML_RUNTIME_DOMAIN) is True
    assert validate_gpu_ml_runtime_domain_label("non_existent_domain") is False

    assert validate_gpu_ml_runtime_status_label(RUNTIME_READY) is True
    assert validate_gpu_ml_runtime_status_label("unknown_status") is False

    assert validate_gpu_ml_backend_label(BACKEND_CPU) is True
    assert validate_gpu_ml_backend_label("unsupported_backend") is False
