# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Dataclass Models."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class CalibrationUncertaintyProfileItem:
    """Represents an item in the profile registry."""
    profile_name: str
    description: str
    current_phase: int = 141
    target_final_phase: int = 160
    next_phase: int = 142
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    non_signal: bool = True
    source_preserved: bool = True


@dataclass
class ProbabilityCalibrationContract:
    """Contract defining probability calibration parameters without execution."""
    contract_name: str
    calibration_method_family: str
    candidate_model_contract_ref: str
    ensemble_contract_ref: str
    dataset_contract_ref: str
    experiment_registry_ref: str
    required_no_lookahead_guard_ref: str
    required_metadata_only_news_guard_ref: str
    required_source_preservation_guard_ref: str
    required_validation_dependency_ref: str
    required_quality_dependency_ref: str
    probability_prediction_allowed: bool = False
    calibration_fit_allowed: bool = False
    calibration_transform_allowed: bool = False
    metric_calculation_allowed: bool = False
    artifact_persistence_allowed: bool = False
    model_registry_write_allowed: bool = False
    signal_generation_allowed: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True


@dataclass
class CalibrationMethodPlaceholder:
    """Metadata placeholder for calibration method without instantiate/fit/transform."""
    method_name: str
    method_family: str
    description: str
    is_parametric: bool
    requires_optimization: bool = False
    execution_blocked: bool = True
    non_signal: bool = True


@dataclass
class CalibrationInputContract:
    """Specifies schema and source inputs for calibration."""
    input_name: str
    source_phase_ref: str
    allowed_types: List[str] = field(default_factory=lambda: ["float", "int"])
    allows_target: bool = False
    allows_prediction: bool = False
    non_signal: bool = True


@dataclass
class CalibrationOutputContract:
    """Specifies locked output schema for calibration without probabilities or signals."""
    output_name: str
    contains_probabilities: bool = False
    contains_confidence_scores: bool = False
    contains_signals: bool = False
    status_field: str = "calibration_contract_status"
    execution_blocked_field: str = "execution_blocked_by_policy"
    non_signal: bool = True


@dataclass
class UncertaintyEstimationContract:
    """Contract defining uncertainty estimation without execution."""
    contract_name: str
    uncertainty_method_family: str
    candidate_model_contract_ref: str
    ensemble_contract_ref: str
    calibration_contract_ref: str
    dataset_contract_ref: str
    required_no_lookahead_guard_ref: str
    required_metadata_only_news_guard_ref: str
    required_source_preservation_guard_ref: str
    uncertainty_estimation_allowed: bool = False
    prediction_interval_allowed: bool = False
    conformal_prediction_allowed: bool = False
    quantile_prediction_allowed: bool = False
    probability_prediction_allowed: bool = False
    metric_calculation_allowed: bool = False
    artifact_persistence_allowed: bool = False
    signal_generation_allowed: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True


@dataclass
class UncertaintyMethodPlaceholder:
    """Metadata placeholder for uncertainty estimation method."""
    method_name: str
    method_family: str
    description: str
    is_bayesian: bool
    requires_resampling: bool = False
    execution_blocked: bool = True
    non_signal: bool = True


@dataclass
class UncertaintyInputContract:
    """Specifies schema and source inputs for uncertainty estimation."""
    input_name: str
    source_phase_ref: str
    allowed_types: List[str] = field(default_factory=lambda: ["float", "int"])
    allows_target: bool = False
    allows_prediction: bool = False
    non_signal: bool = True


@dataclass
class UncertaintyOutputContract:
    """Specifies locked output schema for uncertainty estimation without intervals or risks."""
    output_name: str
    contains_uncertainty_values: bool = False
    contains_intervals: bool = False
    contains_risk_signals: bool = False
    status_field: str = "uncertainty_contract_status"
    execution_blocked_field: str = "execution_blocked_by_policy"
    non_signal: bool = True


@dataclass
class CalibrationUncertaintyGuardItem:
    """Guard rule item enforcing zero-execution and data hygiene invariants."""
    guard_id: str
    guard_name: str
    domain: str
    description: str
    is_active: bool = True
    blocking: bool = True
    non_signal: bool = True


@dataclass
class CalibrationUncertaintyFinding:
    """Represents a governance observation or finding."""
    finding_id: str
    finding_type: str
    calibration_domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    non_signal: bool = True


@dataclass
class CalibrationUncertaintyReadinessScore:
    """Readiness scoring bounded to [0, 1] with explicit non-production guarantees."""
    readiness_score: float
    classification: str
    meets_threshold: bool
    total_findings: int
    critical_blockers: int
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    official_approval: bool = False


@dataclass
class CalibrationUncertaintyManifest:
    """Master integrity manifest for Phase 141."""
    manifest_name: str
    current_phase: int = 141
    target_final_phase: int = 160
    next_phase: int = 142
    calibration_contract_count: int = 0
    uncertainty_contract_count: int = 0
    disabled_execution_report_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    readiness_score: float = 1.0
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
    real_training_executed: bool = False
    model_training_executed: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    model_inference_executed: bool = False
    probability_prediction_executed: bool = False
    confidence_score_calculated: bool = False
    calibration_executed: bool = False
    calibration_fit_executed: bool = False
    calibration_transform_executed: bool = False
    uncertainty_estimation_executed: bool = False
    prediction_interval_calculated: bool = False
    conformal_prediction_executed: bool = False
    metric_calculation_executed: bool = False
    performance_claim_generated: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False


@dataclass
class CalibrationUncertaintyManualReviewItem:
    """Item queued for operator review."""
    item_id: str
    item_type: str
    domain: str
    reason: str
    suggested_action: str
    auto_action_allowed: bool = False
    non_signal: bool = True
