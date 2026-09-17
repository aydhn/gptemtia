# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Model Contracts & Candidate Registry Data Models."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class EnsembleModelProfileItem:
    """Ensemble model profile item metadata."""

    profile_name: str
    description: str
    current_phase: int = 140
    target_final_phase: int = 160
    next_phase: int = 141
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    non_signal: bool = True
    source_preserved: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    official_approval: bool = False


@dataclass
class CandidateModelFamilyItem:
    """Candidate model family metadata placeholder."""

    family_id: str
    family_name: str
    family_category: str  # linear, tree, boosting, neural, sequence, unsupervised_placeholder
    description: str
    baseline_contract_ref: str
    dataset_contract_ref: str
    is_placeholder: bool = True
    model_instantiated: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class CandidateModelContract:
    """Candidate model contract definition."""

    contract_name: str
    candidate_family: str
    baseline_contract_ref: str
    dataset_contract_ref: str
    feature_snapshot_contract_ref: str
    experiment_registry_ref: str
    gpu_resource_policy_ref: str
    required_no_lookahead_guard_ref: str
    required_metadata_only_news_guard_ref: str
    required_source_preservation_guard_ref: str
    required_validation_dependency_ref: str
    required_quality_dependency_ref: str
    real_training_allowed: bool = False
    model_fit_allowed: bool = False
    model_predict_allowed: bool = False
    inference_allowed: bool = False
    ensemble_execution_allowed: bool = False
    calibration_allowed: bool = False
    target_label_generation_allowed: bool = False
    artifact_persistence_allowed: bool = False
    model_registry_write_allowed: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True
    status: str = "ensemble_contract_placeholder_only"


@dataclass
class CandidateModelInputContract:
    """Candidate model input contract definition."""

    contract_name: str
    candidate_family: str
    dataset_source: str
    input_feature_count: int
    no_lookahead_guaranteed: bool = True
    metadata_only_news_guaranteed: bool = True
    source_preserved: bool = True
    contains_target: bool = False
    contains_signal: bool = False
    non_signal: bool = True


@dataclass
class CandidateModelOutputContract:
    """Candidate model output contract definition."""

    contract_name: str
    candidate_family: str
    prediction_output_allowed: bool = False
    probability_output_allowed: bool = False
    class_label_allowed: bool = False
    regression_output_allowed: bool = False
    ensemble_vote_allowed: bool = False
    trade_signal_allowed: bool = False
    performance_metric_allowed: bool = False
    candidate_contract_status: str = "contract_registered"
    eligibility_status: str = "candidate_metadata_ready"
    compatibility_status: str = "compatible_contract_only"
    blocked_reason: str = "execution_blocked_by_policy"
    manual_review_required: bool = True
    non_signal: bool = True


@dataclass
class CandidateModelEligibilityGate:
    """Candidate model eligibility gate definition."""

    gate_name: str
    gate_category: str
    description: str
    status: str = "GATE_ACTIVE"
    passed: bool = True
    blocks_execution: bool = True
    non_signal: bool = True
    manual_review_required: bool = True


@dataclass
class CandidateCompatibilityMatrixItem:
    """Candidate model compatibility matrix placeholder item."""

    matrix_id: str
    candidate_family: str
    compatible_dataset_family_placeholder: str
    compatible_runtime_backend_placeholder: str
    compatible_resource_policy_placeholder: str
    compatible_ensemble_strategy_placeholder: str
    compatibility_score_placeholder: float = 1.0
    compatibility_score_is_signal: bool = False
    compatibility_score_is_performance: bool = False
    manual_review_required: bool = True
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class EnsembleStrategyContract:
    """Ensemble strategy contract definition."""

    ensemble_strategy_name: str
    strategy_type: str  # voting, blending, stacking, averaging, rank_aggregation, meta_model
    required_candidate_contract_refs: List[str] = field(default_factory=list)
    required_candidate_eligibility_refs: List[str] = field(default_factory=list)
    required_compatibility_matrix_ref: str = "compatibility_matrix_v140"
    required_resource_policy_ref: str = "default_ensemble_resource_policy"
    required_no_lookahead_guard_ref: str = "ensemble_no_lookahead_guard"
    required_metadata_only_news_guard_ref: str = "ensemble_metadata_only_news_guard"
    ensemble_execution_allowed: bool = False
    voting_execution_allowed: bool = False
    blending_execution_allowed: bool = False
    stacking_execution_allowed: bool = False
    calibration_allowed: bool = False
    prediction_allowed: bool = False
    signal_generation_allowed: bool = False
    artifact_persistence_allowed: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True
    status: str = "ensemble_contract_placeholder_only"


@dataclass
class EnsemblePlaceholderItem:
    """Ensemble placeholder item for voting, blending, stacking, weighting, or meta-models."""

    placeholder_id: str
    placeholder_type: str  # voting, blending, stacking, weighting_policy, meta_model
    description: str
    execution_blocked: bool = True
    computation_executed: bool = False
    non_signal: bool = True
    manual_review_required: bool = True


@dataclass
class EnsembleFinding:
    """Finding regarding candidate or ensemble contract anomaly or blocked execution."""

    finding_id: str
    finding_type: str
    ensemble_domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    non_signal: bool = True
    auto_fix_prohibited: bool = True


@dataclass
class EnsembleReadinessScore:
    """Readiness scoring evaluation for Phase 140."""

    score_name: str
    readiness_score: float  # 0.0 to 1.0
    classification: str
    meets_threshold: bool
    source_phase: int = 140
    target_final_phase: int = 160
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    official_approval: bool = False

    def __post_init__(self):
        if self.readiness_score < 0.0 or self.readiness_score > 1.0:
            raise ValueError(f"readiness_score must be in [0, 1], got {self.readiness_score}")


@dataclass
class EnsembleManualReviewItem:
    """Manual review queue item for candidate and ensemble governance."""

    review_id: str
    finding_ref: str
    ensemble_domain: str
    severity: str
    description: str
    recommended_action: str
    non_signal: bool = True
    auto_fix_allowed: bool = False
    destructive_action_allowed: bool = False


@dataclass
class EnsembleModelManifest:
    """Consolidated manifest for Phase 140 Ensemble Model Contracts."""

    manifest_name: str = "ensemble_model_manifest_v140"
    current_phase: int = 140
    target_final_phase: int = 160
    next_phase: int = 141
    candidate_contract_count: int = 0
    ensemble_contract_count: int = 0
    disabled_execution_report_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    readiness_score: float = 1.0

    # Invariant flags
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
    voting_executed: bool = False
    blending_executed: bool = False
    stacking_executed: bool = False
    calibration_executed: bool = False
    uncertainty_estimation_executed: bool = False
    metric_calculation_executed: bool = False
    performance_claim_generated: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    manual_review_required: bool = True

    def __post_init__(self):
        if self.readiness_score < 0.0 or self.readiness_score > 1.0:
            raise ValueError(f"readiness_score must be in [0, 1], got {self.readiness_score}")
