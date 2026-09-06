"""Phase 136: GPU ML Runtime Data Models.

Defines dataclasses for hardware capabilities, dependencies, safety contracts,
input contracts, findings, manifests, and review queues.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class GpuMlRuntimeProfileItem:
    profile_name: str
    description: str
    current_phase: int = 136
    target_final_phase: int = 160
    next_phase: int = 137
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    non_signal: bool = True
    min_readiness_score: float = 0.45


@dataclass(frozen=True)
class HardwareDiscoveryItem:
    item_id: str
    category: str
    property_name: str
    property_value: str
    status_label: str
    non_signal: bool = True
    source_preserved: bool = True
    manual_review_required: bool = False
    details: str = ""


@dataclass(frozen=True)
class GpuCapabilityItem:
    gpu_id: str
    gpu_name: str
    cuda_available: bool
    device_count: int
    memory_total_mb: float
    capability_status: str
    non_signal: bool = True
    source_preserved: bool = True
    manual_review_required: bool = False
    details: str = ""


@dataclass(frozen=True)
class CpuCapabilityItem:
    cpu_id: str
    architecture: str
    physical_cores: int
    logical_cores: int
    cpu_freq_mhz: float
    capability_status: str
    non_signal: bool = True
    source_preserved: bool = True
    manual_review_required: bool = False
    details: str = ""


@dataclass(frozen=True)
class MemoryCapabilityItem:
    memory_id: str
    total_ram_gb: float
    available_ram_gb: float
    swap_total_gb: float
    capability_status: str
    non_signal: bool = True
    source_preserved: bool = True
    manual_review_required: bool = False
    details: str = ""


@dataclass(frozen=True)
class RuntimeDependencyCapabilityItem:
    dependency_id: str
    package_name: str
    installed: bool
    version: str
    accelerated: bool
    backend_label: str
    status_label: str
    non_signal: bool = True
    source_preserved: bool = True
    manual_review_required: bool = False
    details: str = ""


@dataclass(frozen=True)
class AcceleratorBackendItem:
    backend_id: str
    backend_name: str
    backend_type: str
    available: bool
    priority_order: int
    status_label: str
    non_signal: bool = True
    source_preserved: bool = True
    details: str = ""


@dataclass(frozen=True)
class MlRuntimeSafetyContract:
    contract_id: str
    topic: str
    enforced: bool
    prohibition_rule: str
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    details: str = ""


@dataclass(frozen=True)
class MlExperimentPermissionPolicy:
    policy_id: str
    action_name: str
    permission_state: str  # allowed_now or blocked_now
    reason: str
    non_signal: bool = True
    source_preserved: bool = True
    details: str = ""


@dataclass(frozen=True)
class MlInputContract:
    contract_id: str
    source_component: str
    source_phase: int
    dataset_entity: str
    accepted_reference_required: bool
    no_lookahead_accepted_required: bool
    metadata_only_news_accepted_required: bool
    source_preserved_required: bool
    non_signal_required: bool
    target_label_forbidden: bool = True
    prediction_forbidden: bool = True
    model_training_allowed: bool = False
    manual_review_required: bool = False
    details: str = ""


@dataclass(frozen=True)
class MlRuntimeFinding:
    finding_id: str
    finding_type: str
    runtime_domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    non_signal: bool = True


@dataclass(frozen=True)
class MlRuntimeReadinessScore:
    readiness_score: float
    score_label: str
    is_ready: bool
    hardware_discovery_count: int
    gpu_capability_count: int
    cpu_capability_count: int
    memory_capability_count: int
    dependency_count: int
    safety_contract_count: int
    permission_policy_count: int
    input_contract_count: int
    finding_count: int
    manual_review_count: int
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False

    def __post_init__(self):
        if not 0.0 <= self.readiness_score <= 1.0:
            raise ValueError(f"Readiness score must be between 0.0 and 1.0, got {self.readiness_score}")


@dataclass(frozen=True)
class GpuMlRuntimeManifest:
    manifest_name: str
    current_phase: int = 136
    target_final_phase: int = 160
    next_phase: int = 137
    non_signal: bool = True
    source_preserved: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    contains_article_body: bool = False
    contains_raw_content: bool = False
    contains_scraped_html: bool = False
    contains_embedding: bool = False
    contains_vector: bool = False
    sentiment_model_output: bool = False
    model_training_executed: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    model_inference_executed: bool = False
    model_transform_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    ensemble_executed: bool = False
    calibration_executed: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    capability_report_count: int = 0
    safety_contract_count: int = 0
    input_contract_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    readiness_score: float = 0.0
    manual_review_required: bool = True


@dataclass(frozen=True)
class MlRuntimeManualReviewItem:
    review_id: str
    domain: str
    topic: str
    recommended_action: str
    forbidden_action_warning: str
    non_signal: bool = True
    source_preserved: bool = True
    details: str = ""
