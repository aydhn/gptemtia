# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Dataclasses and Data Models.

Defines all core dataclasses with strict non-signal, zero-training,
and safety constraints.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class BaselineMlModelProfileItem:
    """Represents a profile entry in the baseline ML model registry."""

    profile_name: str
    description: str
    current_phase: int = 138
    target_final_phase: int = 160
    next_phase: int = 139
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class BaselineModelFamilyItem:
    """Represents a baseline model family contract definition."""

    family_id: str
    family_name: str
    algorithm_category: str
    library_name: str
    description: str
    is_contract_only: bool = True
    real_training_allowed: bool = False
    model_fit_allowed: bool = False
    model_predict_allowed: bool = False
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    official_approval: bool = False
    tags: List[str] = field(default_factory=list)


@dataclass
class BaselineModelContract:
    """Formal specification of a baseline ML model contract."""

    contract_name: str
    model_family: str
    dataset_contract_ref: str
    feature_snapshot_contract_ref: str
    experiment_registry_ref: str
    runtime_profile_ref: str
    required_no_lookahead_guard_ref: str
    required_metadata_only_news_guard_ref: str
    required_source_preservation_guard_ref: str
    required_validation_dependency_ref: str
    required_quality_dependency_ref: str
    status: str = "baseline_contract_placeholder_only"
    real_training_allowed: bool = False
    model_fit_allowed: bool = False
    model_predict_allowed: bool = False
    inference_allowed: bool = False
    target_label_generation_allowed: bool = False
    artifact_persistence_allowed: bool = False
    model_registry_write_allowed: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    official_approval: bool = False


@dataclass
class BaselineModelInputContract:
    """Defines the input contract connecting FeatureStore, regimes, and datasets."""

    input_contract_id: str
    dataset_contract_ref: str
    feature_snapshot_contract_ref: str
    runtime_input_ref: str
    regime_acceptance_ref: str
    feature_store_catalog_ref: str
    quality_drift_ref: str
    validation_no_lookahead_ref: str
    is_validated: bool = True
    dataset_materialized: bool = False
    feature_snapshot_materialized: bool = False
    non_signal: bool = True


@dataclass
class BaselineModelOutputContract:
    """Defines the dry-run output contract strictly blocking real predictions."""

    output_contract_id: str
    model_contract_ref: str
    allowed_output_types: List[str] = field(default_factory=lambda: [
        "dry_run_status",
        "blocked_reason",
        "contract_validation_status",
        "manual_review_required",
    ])
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_probabilities: bool = False
    contains_class_labels: bool = False
    contains_regression_outputs: bool = False
    contains_performance_metrics: bool = False
    non_signal: bool = True


@dataclass
class DryRunHarnessContract:
    """Contract for the dry-run training harness."""

    harness_id: str
    harness_name: str
    allowed_mode: str = "contract_only"
    simulation_mode: str = "no_op_dry_run"
    real_training_allowed: bool = False
    model_fit_allowed: bool = False
    model_predict_allowed: bool = False
    artifact_persistence_allowed: bool = False
    model_registry_write_allowed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True


@dataclass
class DryRunTrainerStub:
    """Metadata representation of a dry-run trainer stub."""

    stub_id: str
    trainer_name: str
    model_family_ref: str
    harness_contract_ref: str
    is_active_stub: bool = True
    execution_status: str = "execution_blocked_no_real_training"
    blocked_reason: str = "Zero-training policy active in Phase 138"
    manual_review_required: bool = True


@dataclass
class BaselineModelFinding:
    """Represents an audit finding or safety blocker."""

    finding_id: str
    finding_type: str
    model_domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    blocking_status: bool = True
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class BaselineModelReadinessScore:
    """Readiness scoring for Phase 138 baseline model contracts."""

    score: float
    score_tier: str
    critical_blockers: int
    total_findings: int
    classification: str
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    official_approval: bool = False
    real_training_approved: bool = False
    dataset_materialization_approved: bool = False

    def __post_init__(self):
        if not (0.0 <= self.score <= 1.0):
            raise ValueError(f"Readiness score must be between 0.0 and 1.0, got {self.score}")


@dataclass
class BaselineModelManualReviewItem:
    """An item queued for manual analyst/engineer inspection."""

    item_id: str
    review_topic: str
    target_reference: str
    severity: str
    review_instructions: str
    prohibited_auto_actions: List[str] = field(default_factory=lambda: [
        "auto_materialize_dataset",
        "auto_generate_target_labels",
        "auto_train_model",
        "auto_run_prediction",
        "auto_persist_artifact",
        "auto_write_model_registry",
        "auto_delete",
        "auto_overwrite",
        "auto_impute",
        "generate_signal",
    ])
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class BaselineMlModelManifest:
    """Comprehensive integrity manifest for Phase 138."""

    manifest_name: str = "baseline_ml_model_manifest"
    current_phase: int = 138
    target_final_phase: int = 160
    next_phase: int = 139
    model_contract_count: int = 10
    harness_contract_count: int = 5
    disabled_execution_report_count: int = 5
    finding_count: int = 0
    manual_review_count: int = 0
    readiness_score: float = 1.0
    status: str = "baseline_contract_placeholder_only"
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
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def __post_init__(self):
        if not (0.0 <= self.readiness_score <= 1.0):
            raise ValueError(f"Readiness score must be between 0.0 and 1.0, got {self.readiness_score}")
