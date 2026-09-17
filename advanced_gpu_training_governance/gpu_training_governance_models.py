# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Governance Data Models.

Defines dataclasses for resource governance policies, device selection,
memory budget, CPU fallback, training loop stubs, harness stubs, findings,
readiness scores, manifest, and review queues.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class GpuTrainingGovernanceProfileItem:
    """Represents a GPU training governance profile item."""

    profile_name: str
    description: str
    current_phase: int = 139
    target_final_phase: int = 160
    next_phase: int = 140
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    non_signal: bool = True
    real_training_allowed: bool = False
    prediction_allowed: bool = False
    artifact_persistence_allowed: bool = False
    model_registry_write_allowed: bool = False
    tags: List[str] = field(default_factory=list)


@dataclass
class GpuTrainingResourcePolicy:
    """Represents a resource governance policy for GPU training harness."""

    policy_id: str
    policy_name: str
    resource_type: str  # "gpu", "cpu", "memory", "timeout"
    allowed_mode: str = "contract_only"
    dry_run_required: bool = True
    local_only: bool = True
    non_production: bool = True
    real_training_allowed: bool = False
    prediction_allowed: bool = False
    artifact_persistence_allowed: bool = False
    model_registry_write_allowed: bool = False
    max_runtime_seconds_placeholder: int = 3600
    max_memory_fraction_placeholder: float = 0.80
    manual_review_required: bool = True
    description: str = ""
    status: str = "gpu_governance_ready"


@dataclass
class GpuDeviceSelectionPolicy:
    """Represents a policy for device selection without real allocation."""

    policy_id: str
    device_preference: str  # "cuda_if_available", "cpu_fallback", "mps_if_available"
    fallback_allowed: bool = True
    allow_real_cuda_initialization: bool = False
    dry_run_mode: bool = True
    non_signal: bool = True
    description: str = ""
    status: str = "gpu_governance_ready"


@dataclass
class GpuMemoryBudgetPolicy:
    """Represents a memory budget policy guarding against OOM."""

    policy_id: str
    max_memory_fraction: float = 0.80
    reserved_system_mb: int = 2048
    enable_memory_guard: bool = True
    dry_run_only: bool = True
    non_signal: bool = True
    description: str = ""
    status: str = "gpu_governance_ready"


@dataclass
class CpuFallbackPolicy:
    """Represents CPU fallback rules when GPU is unavailable or restricted."""

    policy_id: str
    allow_cpu_fallback: bool = True
    fallback_priority: str = "cpu"
    max_cpu_threads_placeholder: int = 4
    dry_run_only: bool = True
    non_signal: bool = True
    description: str = ""
    status: str = "gpu_governance_ready"


@dataclass
class TrainingTimeoutPolicy:
    """Represents timeout bounds for training loop stubs."""

    policy_id: str
    max_timeout_seconds: int = 3600
    heartbeat_interval_seconds: int = 60
    terminate_on_timeout: bool = True
    dry_run_only: bool = True
    non_signal: bool = True
    description: str = ""
    status: str = "gpu_governance_ready"


@dataclass
class TrainingLoopStubContract:
    """Contract defining stubbed training loop behavior with blocked execution."""

    contract_id: str
    contract_name: str
    allowed_execution: bool = False
    blocked_keywords: List[str] = field(
        default_factory=lambda: [
            "fit",
            "train",
            "predict",
            "inference",
            "transform",
            "backward",
            "optimizer_step",
            "save_model",
            "write_model_registry",
            "generate_signal",
        ]
    )
    dry_run_only: bool = True
    non_signal: bool = True
    description: str = ""
    status: str = "execution_contract_only"


@dataclass
class GpuTrainingHarnessStub:
    """Represents harness stub metadata."""

    stub_id: str
    stub_name: str
    dry_run: bool = True
    resource_policy_validated: bool = True
    device_selection_dry_run: bool = True
    real_training_executed: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    target_label_generated: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    blocked_by_policy: bool = True
    blocked_reason: str = "Phase 139 strict dry-run resource governance boundary"
    manual_review_required: bool = True
    status: str = "execution_blocked_no_real_training"


@dataclass
class DryRunResourceCheckItem:
    """Represents an individual dry-run resource check item."""

    check_id: str
    check_name: str
    check_type: str
    result: str  # "PASS", "WARN", "BLOCKED"
    details: str
    dry_run_only: bool = True
    non_signal: bool = True


@dataclass
class GpuTrainingFinding:
    """Represents an audit finding or observation."""

    finding_id: str
    finding_type: str
    governance_domain: str
    severity_label: str  # "INFO", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    message: str
    recommendation: str
    manual_review_required: bool = True
    non_signal: bool = True
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


@dataclass
class GpuTrainingReadinessScore:
    """Represents readiness score for Phase 139 GPU training governance."""

    score: float
    classification: str
    meets_threshold: bool
    current_phase: int = 139
    target_final_phase: int = 160
    next_phase: int = 140
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    official_approval: bool = False
    real_training_approved: bool = False
    performance_claim_generated: bool = False
    details: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not (0.0 <= self.score <= 1.0):
            raise ValueError(f"Score must be between 0.0 and 1.0, got {self.score}")


@dataclass
class GpuTrainingManualReviewItem:
    """Represents an item in the manual review queue."""

    item_id: str
    domain: str
    description: str
    recommended_action: str
    priority: str = "NORMAL"
    manual_review_required: bool = True
    non_destructive: bool = True
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


@dataclass
class GpuTrainingGovernanceManifest:
    """Immutable manifest declaring all Phase 139 execution states and safety boundaries."""

    manifest_name: str
    current_phase: int = 139
    target_final_phase: int = 160
    next_phase: int = 140
    active_profile: str = "balanced_local_gpu_training_governance"
    non_signal: bool = True
    source_preserved: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    dataset_materialized: bool = False
    feature_snapshot_materialized: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    contains_article_body: bool = False
    contains_raw_content: bool = False
    contains_scraped_html: bool = False
    contains_embedding: bool = False
    contains_vector: bool = False
    sentiment_model_output: bool = False
    real_training_executed: bool = False
    model_training_executed: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    model_inference_executed: bool = False
    model_transform_executed: bool = False
    clustering_executed: bool = False
    supervised_execution: bool = False
    unsupervised_execution: bool = False
    ensemble_executed: bool = False
    calibration_executed: bool = False
    metric_calculation_executed: bool = False
    performance_claim_generated: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    resource_policy_count: int = 0
    harness_contract_count: int = 0
    disabled_execution_report_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    readiness_score: float = 1.0
    manual_review_required: bool = True
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
