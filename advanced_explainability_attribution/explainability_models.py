# -*- coding: utf-8 -*-
"""Phase 143: Explainability and Feature Attribution Data Models."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ExplainabilityProfileItem:
    """Represents an explainability configuration profile item."""

    profile_name: str
    display_name: str
    description: str
    current_phase: int = 143
    target_final_phase: int = 160
    next_phase: int = 144
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class ExplainabilityReportContract:
    """Represents an explainability report contract definition."""

    contract_name: str
    explanation_family: str
    candidate_model_contract_ref: str
    ensemble_contract_ref: str
    dataset_contract_ref: str
    featurestore_contract_ref: str
    drift_contract_ref: str
    calibration_uncertainty_contract_ref: str
    required_no_lookahead_guard_ref: str
    required_metadata_only_news_guard_ref: str
    required_source_preservation_guard_ref: str
    explainability_calculation_allowed: bool = False
    attribution_calculation_allowed: bool = False
    metric_calculation_allowed: bool = False
    model_action_allowed: bool = False
    signal_generation_allowed: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class FeatureAttributionContract:
    """Represents a feature attribution contract specification."""

    contract_name: str
    method_name: str
    attribution_scope: str
    target_feature_set_ref: str
    attribution_calculation_allowed: bool = False
    shap_execution_allowed: bool = False
    lime_execution_allowed: bool = False
    permutation_importance_allowed: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class ExplanationPlaceholderItem:
    """Represents an explanation or attribution placeholder item."""

    placeholder_id: str
    placeholder_type: str
    target_component: str
    description: str
    calculation_allowed: bool = False
    is_placeholder_only: bool = True
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class AttributionMethodPolicy:
    """Represents an attribution method policy."""

    policy_name: str
    method_family: str
    description: str
    execution_blocked: bool = True
    policy_status: str = "execution_blocked_by_policy"
    non_signal: bool = True
    manual_review_required: bool = True


@dataclass
class AttributionInputContract:
    """Represents an attribution input contract."""

    input_name: str
    source_reference: str
    description: str
    no_lookahead_enforced: bool = True
    metadata_only_enforced: bool = True
    source_preserved: bool = True
    non_signal: bool = True


@dataclass
class AttributionOutputContract:
    """Represents an attribution output contract."""

    output_name: str
    output_schema_ref: str
    contains_signal: bool = False
    contains_real_attribution: bool = False
    contains_prediction: bool = False
    is_contract_only: bool = True
    non_signal: bool = True


@dataclass
class ExplainabilityDisabledExecutionItem:
    """Represents a disabled execution safeguard verification."""

    action_name: str
    blocked_reason: str
    is_disabled: bool = True
    execution_attempted: bool = False
    policy_enforced: bool = True
    non_signal: bool = True


@dataclass
class ExplainabilityGuardItem:
    """Represents a guard or boundary verification item."""

    guard_name: str
    guard_type: str
    status: str
    violation_count: int = 0
    is_active: bool = True
    non_signal: bool = True


@dataclass
class ExplainabilityFinding:
    """Represents an explainability finding or discrepancy."""

    finding_id: str
    finding_type: str
    explainability_domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class ExplainabilityReadinessScore:
    """Represents explainability readiness score and classification."""

    score_id: str
    readiness_score: float
    classification: str
    findings_count: int = 0
    manual_review_count: int = 0
    meets_threshold: bool = True
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False

    def __post_init__(self):
        if not (0.0 <= self.readiness_score <= 1.0):
            raise ValueError(f"Readiness score must be between 0.0 and 1.0, got {self.readiness_score}")


@dataclass
class ExplainabilityManifest:
    """Comprehensive manifest of Phase 143 Explainability Layer."""

    manifest_id: str
    current_phase: int = 143
    target_final_phase: int = 160
    next_phase: int = 144
    explainability_contract_count: int = 0
    attribution_contract_count: int = 0
    disabled_execution_report_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    readiness_score: float = 1.0
    manual_review_required: bool = True

    # Invariant safety flags
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
    calibration_executed: bool = False
    uncertainty_estimation_executed: bool = False
    drift_calculation_executed: bool = False
    explainability_calculation_executed: bool = False
    feature_attribution_calculation_executed: bool = False
    feature_importance_calculation_executed: bool = False
    shap_executed: bool = False
    lime_executed: bool = False
    permutation_importance_executed: bool = False
    pdp_executed: bool = False
    ice_executed: bool = False
    surrogate_model_executed: bool = False
    counterfactual_generated: bool = False
    explanation_model_action_generated: bool = False
    metric_calculation_executed: bool = False
    performance_claim_generated: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False


@dataclass
class ExplainabilityManualReviewItem:
    """Represents a human manual review item in queue."""

    review_id: str
    item_type: str
    domain: str
    reason: str
    required_action: str
    urgency: str = "medium"
    status: str = "pending"
    non_signal: bool = True
