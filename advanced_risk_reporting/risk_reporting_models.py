# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting, Exposure Attribution and Limit Monitoring Data Models.

Defines Pydantic / dataclass models for profiles, risk report contracts,
exposure attribution contracts, limit monitoring contracts, placeholders, guards,
findings, readiness score, manifest, and manual review items.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, field_validator


class RiskReportingProfileItem(BaseModel):
    """Pydantic model for a registered risk reporting profile."""
    profile_name: str
    description: str
    current_phase: int = 155
    target_final_phase: int = 160
    next_phase: int = 156
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_signal_generation: bool = False
    allow_risk_reporting_execution: bool = False
    allow_exposure_attribution_execution: bool = False
    allow_limit_monitoring_execution: bool = False
    allow_metric_calculation: bool = False
    min_readiness_score: float = Field(default=0.50, ge=0.0, le=1.0)


class RiskReportContract(BaseModel):
    """Model representing an offline/local risk report contract specification."""
    contract_name: str
    report_family: str
    portfolio_construction_ref: str
    portfolio_optimization_ref: str
    backtest_acceptance_ref: str
    model_governance_ref: str
    regime_context_ref: str
    featurestore_ref: str
    no_lookahead_guard_ref: str
    investment_advice_guard_ref: str
    risk_reporting_execution_allowed: bool = False
    exposure_attribution_allowed: bool = False
    limit_monitoring_allowed: bool = False
    metric_calculation_allowed: bool = False
    alert_generation_allowed: bool = False
    dashboard_generation_allowed: bool = False
    portfolio_adjustment_allowed: bool = False
    live_trading_allowed: bool = False
    broker_execution_allowed: bool = False
    signal_generation_allowed: bool = False
    manual_review_required: bool = True


class ExposureAttributionContract(BaseModel):
    """Model representing an exposure attribution contract specification."""
    contract_name: str
    exposure_family: str
    description: str
    mathematical_formulation: str
    is_placeholder: bool = True
    exposure_calculated: bool = False
    allows_execution: bool = False


class LimitMonitoringContract(BaseModel):
    """Model representing a limit monitoring contract specification."""
    contract_name: str
    limit_family: str
    description: str
    limit_type: str  # "hard_limit", "soft_warning", "monitor_only"
    threshold_metadata: str
    is_placeholder: bool = True
    is_enforced_live: bool = False
    allows_execution: bool = False
    allows_alerting: bool = False


class RiskMetricPlaceholder(BaseModel):
    """Model representing a risk metric placeholder with formula metadata."""
    metric_name: str
    metric_domain: str
    formula_description: str
    unit: str
    is_placeholder: bool = True
    actual_value: Optional[float] = None
    is_calculated: bool = False


class ExposurePlaceholder(BaseModel):
    """Model representing an exposure placeholder with formula metadata."""
    placeholder_name: str
    exposure_type: str
    formula_description: str
    dimension: str
    is_placeholder: bool = True
    is_calculated: bool = False


class LimitMonitoringPlaceholder(BaseModel):
    """Model representing a limit monitoring placeholder."""
    placeholder_name: str
    limit_type: str
    description: str
    is_placeholder: bool = True
    is_enforced: bool = False


class RiskReportingGuardItem(BaseModel):
    """Model for a risk reporting safety guard policy."""
    guard_name: str
    domain: str
    guard_rule: str
    is_active: bool = True
    action_on_violation: str = "BLOCK"


class RiskReportingDisabledExecutionItem(BaseModel):
    """Model documenting a strictly disabled execution component."""
    component_name: str
    prohibited_actions: List[str]
    enforcement_mechanism: str
    is_disabled: bool = True
    status: str = "execution_contract_only"


class RiskReportingFinding(BaseModel):
    """Diagnostic finding item."""
    finding_id: str
    finding_type: str
    domain: str
    severity_label: str  # "INFO", "WARNING", "BLOCKER"
    message: str
    recommendation: str
    manual_review_required: bool = True

    @field_validator("recommendation")
    @classmethod
    def validate_no_prohibited_actions(cls, v: str) -> str:
        prohibited = [
            "auto-generate live risk report",
            "auto-calculate exposure",
            "auto-calculate var/es",
            "auto-calculate var",
            "auto-monitor limits",
            "auto-send alert",
            "auto-generate dashboard",
            "auto-adjust portfolio",
            "auto-rebalance",
            "auto-hedge",
            "auto-send broker order",
            "auto-generate signal",
            "auto-run prediction",
            "approve production",
            "approve broker readiness",
            "auto-deploy",
            "auto-write model registry",
            "auto-overwrite",
            "auto-delete",
            "auto-impute",
            "enable scraping",
        ]
        for p in prohibited:
            if p.lower() in v.lower():
                raise ValueError(f"Prohibited automatic remediation phrase detected: '{p}'")
        return v


class RiskReportingReadinessScore(BaseModel):
    """Readiness scoring model for Phase 155."""
    readiness_score: float = Field(..., ge=0.0, le=1.0)
    classification: str
    is_contract_ready: bool
    summary_text: str
    current_phase: int = 155
    target_final_phase: int = 160
    next_phase: int = 156
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False


class RiskReportingManifest(BaseModel):
    """Master Phase 155 risk reporting manifest."""
    manifest_name: str = "Phase 155 Risk Reporting, Exposure Attribution and Limit Monitoring Manifest"
    current_phase: int = 155
    target_final_phase: int = 160
    next_phase: int = 156
    non_signal: bool = True
    local_only: bool = True
    dry_run: bool = True
    non_production: bool = True
    research_only: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    live_trading_ready: bool = False
    official_approval: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    risk_report_generated: bool = False
    exposure_attribution_generated: bool = False
    limit_monitoring_executed: bool = False
    metric_calculated: bool = False
    var_calculated: bool = False
    expected_shortfall_calculated: bool = False
    exposure_calculated: bool = False
    limit_breach_generated: bool = False
    alert_generated: bool = False
    dashboard_generated: bool = False
    portfolio_adjustment_generated: bool = False
    rebalance_generated: bool = False
    orders_generated: bool = False
    optimizer_executed: bool = False
    model_training_executed: bool = False
    model_predict_executed: bool = False
    prediction_generated: bool = False
    target_label_generated: bool = False
    broker_order_sent: bool = False
    live_order_sent: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    model_deployed: bool = False
    production_deployed: bool = False
    source_preserved: bool = True
    manual_review_required: bool = True
    phase_156_handoff_ready: bool = True


class RiskReportingManualReviewItem(BaseModel):
    """Manual review queue checkpoint."""
    checkpoint_id: str
    domain: str
    review_target: str
    description: str
    status: str = "PENDING_OPERATOR_REVIEW"
    recommendation: str
