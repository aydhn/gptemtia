"""Phase 133: Regime Validation Acceptance Data Models.

Defines typed dataclasses for profiles, gates, check items, findings,
scoring, manifests, and manual review queues.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class RegimeValidationAcceptanceProfileItem:
    """Registry entry for a validation acceptance profile."""

    profile_name: str
    description: str
    current_phase: int = 133
    target_final_phase: int = 160
    next_phase: int = 134
    min_score: float = 0.45
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
class RegimeValidationGate:
    """Represents a safety and integrity gate in the acceptance subsystem."""

    gate_id: str
    gate_name: str
    domain: str
    description: str
    status: str = "acceptance_pass"
    score_weight: float = 1.0
    passed: bool = True
    details: str = ""
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class RegimeAcceptanceCheckItem:
    """Individual item verification record."""

    check_id: str
    check_name: str
    domain: str
    target_component: str
    passed: bool = True
    status: str = "acceptance_pass"
    details: str = ""
    non_signal: bool = True
    source_preserved: bool = True
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
    clustering_executed: bool = False
    unsupervised_execution: bool = False


@dataclass
class RegimeValidationFinding:
    """Diagnostic finding produced during validation checks."""

    finding_id: str
    finding_type: str
    acceptance_domain: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    non_signal: bool = True


@dataclass
class RegimeAcceptanceScore:
    """Overall calculated acceptance score."""

    overall_score: float
    score_tier: str
    total_checks: int
    passed_checks: int
    failed_checks: int
    warning_checks: int
    manual_review_required: bool
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False

    def __post_init__(self):
        if not (0.0 <= self.overall_score <= 1.0):
            raise ValueError(f"Score must be between 0.0 and 1.0, got: {self.overall_score}")


@dataclass
class RegimeValidationAcceptanceManifest:
    """Master acceptance manifest certifying Phase 133 boundaries and integrity."""

    manifest_name: str
    current_phase: int = 133
    target_final_phase: int = 160
    next_phase: int = 134
    gate_count: int = 19
    acceptance_report_count: int = 15
    finding_count: int = 0
    manual_review_count: int = 0
    acceptance_score: float = 1.0
    manual_review_required: bool = False
    non_signal: bool = True
    source_preserved: bool = True
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
    clustering_executed: bool = False
    unsupervised_execution: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    extra_metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not (0.0 <= self.acceptance_score <= 1.0):
            raise ValueError(f"Acceptance score must be between 0.0 and 1.0, got: {self.acceptance_score}")


@dataclass
class RegimeAcceptanceManualReviewItem:
    """Queue entry for items requiring manual human review."""

    review_id: str
    domain: str
    subject_component: str
    review_reason: str
    severity: str
    suggested_action: str
    status: str = "PENDING"
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    non_signal: bool = True
