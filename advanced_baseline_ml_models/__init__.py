# -*- coding: utf-8 -*-
"""Phase 138: Baseline ML Model Contracts and Dry-Run Training Harness.

Defines baseline model families, contracts, input/output constraints,
dry-run training harness interfaces, trainer stubs, and Phase 139 handoff.
"""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_baseline_ml_model_profile,
    list_baseline_ml_model_profiles,
    validate_baseline_ml_model_profiles,
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_profile_registry import (
    build_baseline_ml_model_profile_registry,
    summarize_baseline_ml_model_profiles,
)
from advanced_baseline_ml_models.baseline_ml_model_pipeline import (
    BaselineMlModelPipeline,
)
from advanced_baseline_ml_models.baseline_ml_model_manifest import (
    build_baseline_ml_model_manifest,
    create_baseline_ml_model_manifest,
    summarize_baseline_ml_model_manifest,
)
from advanced_baseline_ml_models.baseline_ml_model_health import (
    build_baseline_ml_model_health_check,
    summarize_baseline_ml_model_health,
)
from advanced_baseline_ml_models.baseline_ml_model_validation import (
    build_baseline_ml_model_validation_report,
    validate_no_forbidden_baseline_ml_claims,
)
from advanced_baseline_ml_models.baseline_ml_model_safety_boundary import (
    build_baseline_ml_model_safety_boundary,
    build_baseline_ml_model_no_go_conditions,
    build_baseline_ml_model_safe_go_conditions,
)
from advanced_baseline_ml_models.phase_139_handoff import (
    build_phase_139_gpu_training_harness_resource_governance_handoff_report,
    summarize_phase_139_handoff,
)

__all__ = [
    "BaselineMlModelProfile",
    "get_baseline_ml_model_profile",
    "list_baseline_ml_model_profiles",
    "validate_baseline_ml_model_profiles",
    "get_default_baseline_ml_model_profile",
    "build_baseline_ml_model_profile_registry",
    "summarize_baseline_ml_model_profiles",
    "BaselineMlModelPipeline",
    "build_baseline_ml_model_manifest",
    "create_baseline_ml_model_manifest",
    "summarize_baseline_ml_model_manifest",
    "build_baseline_ml_model_health_check",
    "summarize_baseline_ml_model_health",
    "build_baseline_ml_model_validation_report",
    "validate_no_forbidden_baseline_ml_claims",
    "build_baseline_ml_model_safety_boundary",
    "build_baseline_ml_model_no_go_conditions",
    "build_baseline_ml_model_safe_go_conditions",
    "build_phase_139_gpu_training_harness_resource_governance_handoff_report",
    "summarize_phase_139_handoff",
]
