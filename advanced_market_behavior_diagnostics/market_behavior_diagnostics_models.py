"""Phase 129: Market Behavior Diagnostics and Regime Quality Models.

Defines dataclasses for profile items, metrics, thresholds, candidate quality items,
regime family items, findings, scores, manual reviews, and diagnostics manifests.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class MarketBehaviorDiagnosticsProfileItem:
    """Operational profile configuration record."""

    profile_name: str
    description: str
    current_phase: int = 129
    target_final_phase: int = 160
    next_phase: int = 130
    local_only: bool = True
    dry_run_default: bool = True
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    model_training_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False


@dataclass
class BehaviorQualityMetric:
    """Metric definition for behavior and candidate state quality."""

    metric_name: str
    domain: str
    description: str
    value_type: str = "float"
    min_value: float = 0.0
    max_value: float = 1.0
    target_direction: str = "higher_is_better"  # or lower_is_better
    is_blocking: bool = False
    non_signal: bool = True


CandidateStateQualityMetric = BehaviorQualityMetric



@dataclass
class BehaviorDiagnosticsMetric:
    """Metric definition for market behavior context diagnostics."""

    metric_name: str
    domain: str
    behavior_family: str
    description: str
    value_type: str = "float"
    coverage_ratio: float = 0.0
    is_ready: bool = True
    non_signal: bool = True


@dataclass
class BehaviorQualityThreshold:
    """Operational threshold for quality, coverage, or ambiguity metrics."""

    threshold_name: str
    metric_name: str
    warning_threshold: float
    critical_threshold: float
    evaluation_operator: str = "lt"  # lt, gt, le, ge, eq
    action_on_warning: str = "record_finding"
    action_on_critical: str = "manual_review_required"
    non_signal: bool = True


@dataclass
class CandidateStateQualityItem:
    """Quality diagnostic record for a candidate state contract."""

    candidate_state_name: str
    candidate_state_family: str
    schema_completeness: float
    assignment_policy_ref_available: bool
    source_matrix_ref_available: bool
    validation_dependency_passed: bool
    quality_dependency_passed: bool
    non_signal: bool = True
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    model_training_executed: bool = False
    clustering_executed: bool = False
    manual_review_required: bool = False
    quality_status: str = "behavior_quality_ready"


@dataclass
class RegimeFamilyQualityItem:
    """Quality diagnostic record for a regime family."""

    family_name: str
    source_features_available: bool
    source_factors_available: bool
    source_context_available: bool
    quality_drift_dependency_available: bool
    validation_dependency_available: bool
    coverage_ratio: float = 1.0
    consistency_score: float = 1.0
    manual_review_blocker_count: int = 0
    phase_130_readiness: bool = True
    non_signal: bool = True
    quality_status: str = "behavior_quality_ready"


@dataclass
class BehaviorQualityFinding:
    """Finding or anomaly detected during behavior and state diagnostics."""

    finding_id: str
    finding_type: str
    behavior_family: str
    severity: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    non_signal: bool = True
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


@dataclass
class BehaviorQualityScore:
    """Internal diagnostic quality score summary."""

    score_name: str
    overall_quality_score: float
    candidate_state_quality_score: float
    regime_family_quality_score: float
    behavior_context_quality_score: float
    transition_readiness_score: float
    stability_readiness_score: float
    quality_grade: str = "READY"
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_trading_recommendation: bool = False

    def __post_init__(self):
        for field_name, val in [
            ("overall_quality_score", self.overall_quality_score),
            ("candidate_state_quality_score", self.candidate_state_quality_score),
            ("regime_family_quality_score", self.regime_family_quality_score),
            ("behavior_context_quality_score", self.behavior_context_quality_score),
            ("transition_readiness_score", self.transition_readiness_score),
            ("stability_readiness_score", self.stability_readiness_score),
        ]:
            if not 0.0 <= val <= 1.0:
                raise ValueError(f"{field_name} must be between 0.0 and 1.0, got {val}")


@dataclass
class BehaviorDiagnosticsManifest:
    """Immutable audit manifest for Phase 129 outputs."""

    manifest_name: str
    current_phase: int = 129
    target_final_phase: int = 160
    next_phase: int = 130
    total_candidate_quality_reports: int = 0
    total_behavior_diagnostics_reports: int = 0
    total_findings_count: int = 0
    total_manual_review_count: int = 0
    overall_quality_score: float = 1.0
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    model_training_executed: bool = False
    model_fit_executed: bool = False
    model_predict_executed: bool = False
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    dimensionality_reduction_executed: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    manual_review_required: bool = True
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


@dataclass
class BehaviorManualReviewItem:
    """Non-destructive manual review item queued for analyst inspection."""

    item_id: str
    domain: str
    target_entity: str
    severity: str
    reason: str
    suggested_action: str
    blocking_for_phase_130: bool = False
    destructive_action_allowed: bool = False
    non_signal: bool = True
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
