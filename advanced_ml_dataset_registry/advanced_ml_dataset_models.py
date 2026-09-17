"""
advanced_ml_dataset_models.py
Phase 137 — Advanced ML Dataset Contracts and Experiment Registry: Data Models

current_phase=137 | target_final_phase=160 | next_phase=138
dry_run=True | local_only=True | non_production=True | research_only=True

All live/broker/signal/training/prediction/materialization/artifact flags=False.
No dataset materialization, no feature snapshot materialization.
No model training/fit/predict/inference/transform.
No target/label/prediction generation.
No clustering/ensemble/calibration execution.
No full article/article_body/raw_content/scraped_html/embedding/vector.
No sentiment model output, no credential/API key output.
No source overwrite/destructive cleaning/auto-imputation/auto-feature-drop.
No official approval/production-ready/broker-ready claim.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any


@dataclass
class AdvancedMlDatasetProfileItem:
    """Runtime profile descriptor for a single Advanced ML Dataset profile slot."""

    profile_name: str
    description: str
    current_phase: int = 137
    target_final_phase: int = 160
    next_phase: int = 138
    enabled: bool = True
    dry_run: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    non_signal: bool = True
    source_preserved: bool = True
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
    score: float = 0.0  # 0-1 arasında
    status: str = "dataset_contract_placeholder_only"


@dataclass
class MlDatasetContract:
    """Contract definition for a single ML dataset family."""

    contract_name: str
    dataset_family: str
    source_phase_refs: List[str] = field(default_factory=list)
    source_catalog_refs: List[str] = field(default_factory=list)
    required_schema_ref: str = ""
    required_time_index_policy_ref: str = ""
    required_split_policy_ref: str = ""
    required_no_lookahead_guard_ref: str = ""
    required_metadata_only_news_guard_ref: str = ""
    required_source_preservation_guard_ref: str = ""
    required_validation_dependency_ref: str = ""
    required_quality_dependency_ref: str = ""
    target_label_generation_allowed: bool = False
    dataset_materialization_allowed: bool = False
    model_training_allowed: bool = False
    prediction_allowed: bool = False
    artifact_persistence_allowed: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True
    status: str = "dataset_contract_placeholder_only"


@dataclass
class MlDatasetSourceCatalogItem:
    """Catalog entry describing a single metadata-reference source."""

    source_key: str
    source_phase: str
    description: str
    source_type: str = "metadata_reference"
    materialized: bool = False
    contains_target: bool = False
    contains_label: bool = False
    contains_prediction: bool = False
    contains_full_article: bool = False
    contains_embedding: bool = False
    non_signal: bool = True
    manual_review_required: bool = True


@dataclass
class MlDatasetSchemaItem:
    """Schema definition associated with a dataset contract."""

    schema_key: str
    dataset_contract_key: str
    required_columns: List[str] = field(default_factory=list)
    forbidden_columns: List[str] = field(default_factory=list)
    timestamp_field: str = "timestamp_utc"
    manual_review_required: bool = True
    non_signal: bool = True


@dataclass
class MlDatasetSplitPolicy:
    """Placeholder split policy for a dataset family (no execution allowed)."""

    policy_name: str
    split_type: str
    description: str
    materialized: bool = False
    target_label_generated: bool = False
    train_test_split_executed: bool = False
    backtest_executed: bool = False
    optimizer_executed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    placeholder_only: bool = True


@dataclass
class MlDatasetGuardItem:
    """Guard definition that enforces dataset safety constraints."""

    guard_name: str
    guard_type: str
    description: str
    blocked_keywords: List[str] = field(default_factory=list)
    non_signal: bool = True
    manual_review_required: bool = True


@dataclass
class MlFeatureSnapshotContract:
    """Contract for a feature snapshot (materialization is always blocked)."""

    contract_name: str
    dataset_family: str
    source_catalog_refs: List[str] = field(default_factory=list)
    schema_ref: str = ""
    validation_acceptance_refs: List[str] = field(default_factory=list)
    no_lookahead_refs: List[str] = field(default_factory=list)
    metadata_only_news_refs: List[str] = field(default_factory=list)
    source_preservation_refs: List[str] = field(default_factory=list)
    quality_dependency_refs: List[str] = field(default_factory=list)
    manual_review_required: bool = True
    materialized: bool = False
    non_signal: bool = True
    production_ready: bool = False


@dataclass
class MlExperimentRegistryItem:
    """Registry entry for a single ML experiment (training always blocked)."""

    experiment_key: str
    experiment_family: str
    dataset_contract_ref: str = ""
    feature_snapshot_contract_ref: str = ""
    runtime_profile_ref: str = ""
    permission_policy_ref: str = ""
    no_training_required: bool = True
    no_prediction_required: bool = True
    target_label_forbidden: bool = True
    artifact_persistence_allowed: bool = False
    model_registry_write_allowed: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    status: str = "experiment_training_blocked"


@dataclass
class MlExperimentTemplate:
    """Template describing the allowed/blocked action surface for an experiment family."""

    template_name: str
    experiment_family: str
    dataset_contract_refs: List[str] = field(default_factory=list)
    allowed_actions: List[str] = field(default_factory=list)
    blocked_actions: List[str] = field(default_factory=list)
    required_guards: List[str] = field(default_factory=list)
    required_acceptance_refs: List[str] = field(default_factory=list)
    handoff_phase: int = 138
    non_signal: bool = True


@dataclass
class MlExperimentPermission:
    """Permission descriptor for a named experiment action."""

    permission_name: str
    description: str
    allowed: bool = True
    blocked_keywords: List[str] = field(default_factory=list)
    non_signal: bool = True


@dataclass
class MlDatasetFinding:
    """A single audit finding surfaced during dataset contract review."""

    finding_id: str
    finding_type: str
    dataset_domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    non_signal: bool = True
    auto_fix_forbidden: bool = True


@dataclass
class MlDatasetReadinessScore:
    """Composite readiness score for a dataset domain (never production-ready here)."""

    score: float  # 0-1
    label: str
    total_findings: int = 0
    critical_findings: int = 0
    warning_findings: int = 0
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    training_approved: bool = False
    dataset_materialization_approved: bool = False


@dataclass
class AdvancedMlDatasetManifest:
    """Top-level manifest aggregating all dataset contract metadata for Phase 137."""

    manifest_name: str
    current_phase: int = 137
    target_final_phase: int = 160
    next_phase: int = 138
    dataset_contract_count: int = 0
    experiment_count: int = 0
    guard_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    readiness_score: float = 0.0
    manual_review_required: bool = True
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
    status: str = "dataset_contract_placeholder_only"


@dataclass
class MlDatasetManualReviewItem:
    """Manual review action item produced during dataset contract audit."""

    review_id: str
    domain: str
    description: str
    recommendation: str
    priority: str = "medium"
    auto_fix_forbidden: bool = True
    non_signal: bool = True
