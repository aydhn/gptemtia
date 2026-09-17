# -*- coding: utf-8 -*-
"""Phase 142: Model Drift Monitoring and Drift Linkage Data Models."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


class _DictAccessMixin:
    """Provides dictionary-style indexing and .get() method to dataclasses."""

    def __getitem__(self, key: str) -> Any:
        try:
            return getattr(self, key)
        except AttributeError:
            raise KeyError(key)

    def get(self, key: str, default: Any = None) -> Any:
        return getattr(self, key, default)

    def __contains__(self, key: str) -> bool:
        return hasattr(self, key)


@dataclass
class ModelDriftProfileItem(_DictAccessMixin):
    """Represents an active model drift configuration profile entry."""

    name: str = "default_profile"
    description: str = ""
    current_phase: int = 142
    target_final_phase: int = 160
    next_phase: int = 143
    dry_run: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    non_signal: bool = True
    drift_calculation_allowed: bool = False
    drift_metric_calculation_allowed: bool = False
    alerting_allowed: bool = False
    retraining_trigger_allowed: bool = False
    model_action_allowed: bool = False


@dataclass
class DriftMonitoringContract(_DictAccessMixin):
    """Contract definition for model, data, or feature drift monitoring."""

    contract_name: str = "default_drift_contract"
    drift_family: str = "general_drift"
    candidate_model_contract_ref: str = ""
    ensemble_contract_ref: str = ""
    calibration_contract_ref: str = ""
    uncertainty_contract_ref: str = ""
    dataset_contract_ref: str = ""
    featurestore_contract_ref: str = ""
    reference_window_policy_ref: str = ""
    current_window_policy_ref: str = ""
    threshold_placeholder_ref: str = ""
    required_no_lookahead_guard_ref: str = ""
    required_metadata_only_news_guard_ref: str = ""
    required_source_preservation_guard_ref: str = ""
    drift_calculation_allowed: bool = False
    metric_calculation_allowed: bool = False
    alerting_allowed: bool = False
    retraining_trigger_allowed: bool = False
    model_action_allowed: bool = False
    signal_generation_allowed: bool = False
    non_signal_required: bool = True
    manual_review_required: bool = True
    status: str = "drift_contract_ready"
    contract_id: Optional[str] = None
    domain: Optional[str] = None
    target_name: Optional[str] = None
    contract_version: str = "1.0.0"
    execution_mode: str = "non_executing_contract"
    reference_window: Optional[str] = None
    current_window: Optional[str] = None
    threshold_policy: Optional[Any] = None
    linkage_target: Optional[str] = None
    rules: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.contract_id and self.contract_name == "default_drift_contract":
            self.contract_name = self.contract_id
        elif not self.contract_id:
            self.contract_id = self.contract_name
        if self.domain and self.drift_family == "general_drift":
            self.drift_family = self.domain
        elif not self.domain:
            self.domain = self.drift_family
        if not self.target_name:
            self.target_name = self.drift_family
        if not self.reference_window:
            self.reference_window = self.reference_window_policy_ref
        if not self.current_window:
            self.current_window = self.current_window_policy_ref
        if not self.threshold_policy:
            self.threshold_policy = self.threshold_placeholder_ref


@dataclass
class DriftLinkageItem(_DictAccessMixin):
    """Linkage contract connecting drift monitoring to upstream quality, featurestore, or regime layers."""

    linkage_name: str = "default_linkage"
    linkage_type: str = "general_linkage"
    source_phase_ref: str = "Phase 123"
    upstream_contract_ref: str = ""
    target_drift_domain: str = ""
    metadata_fields: List[str] = field(default_factory=list)
    drift_calculation_allowed: bool = False
    model_action_allowed: bool = False
    non_signal: bool = True
    status: str = "drift_contract_ready"
    linkage_id: Optional[str] = None
    execution_enabled: bool = False
    drift_domain: Optional[str] = None
    source_component: Optional[str] = None
    target_model_or_dataset: Optional[str] = None

    def __post_init__(self):
        if self.linkage_id and self.linkage_name == "default_linkage":
            self.linkage_name = self.linkage_id
        elif not self.linkage_id:
            self.linkage_id = self.linkage_name
        if not self.drift_domain:
            self.drift_domain = self.target_drift_domain or self.linkage_type
        if not self.source_component:
            self.source_component = self.upstream_contract_ref or self.source_phase_ref
        if not self.target_model_or_dataset:
            self.target_model_or_dataset = self.target_drift_domain or self.linkage_name


@dataclass
class DriftWindowPolicy(_DictAccessMixin):
    """Specification of windowing policies (reference, current, rolling) for drift evaluation."""

    policy_name: str = "default_window_policy"
    window_type: str = "reference"
    window_size_description: str = ""
    min_observations_placeholder: int = 0
    alignment_method: str = "asof_backward"
    data_materialization_allowed: bool = False
    real_window_extraction_executed: bool = False
    non_signal: bool = True
    status: str = "drift_contract_ready"
    policy_id: Optional[str] = None
    window_size: Optional[str] = None
    stride: Optional[Any] = None
    min_observations: Optional[int] = None
    lookback_days: Optional[int] = None
    execution_enabled: bool = False
    parameters: Optional[Dict[str, Any]] = None

    def __post_init__(self):
        if self.policy_id and self.policy_name == "default_window_policy":
            self.policy_name = self.policy_id
        elif not self.policy_id:
            self.policy_id = self.policy_name
        if self.window_size and not self.window_size_description:
            self.window_size_description = str(self.window_size)
        if self.min_observations and not self.min_observations_placeholder:
            self.min_observations_placeholder = self.min_observations


@dataclass
class DriftThresholdPlaceholder(_DictAccessMixin):
    """Threshold placeholder policy for drift warning and critical boundaries."""

    threshold_name: str = "default_threshold_placeholder"
    drift_family: str = "distribution_stability"
    warning_threshold_placeholder: float = 0.10
    critical_threshold_placeholder: float = 0.25
    metric_type_ref: str = "psi"
    alerting_allowed: bool = False
    retraining_trigger_allowed: bool = False
    model_action_allowed: bool = False
    non_signal: bool = True
    status: str = "drift_contract_placeholder_only"
    threshold_id: Optional[str] = None
    threshold_type: Optional[str] = None
    execution_enabled: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)
    target_scope: Optional[str] = None
    warning_threshold_min: Optional[float] = None
    warning_threshold_max: Optional[float] = None
    breach_threshold: Optional[float] = None
    metric_type: Optional[str] = None

    def __post_init__(self):
        if self.threshold_id and self.threshold_name == "default_threshold_placeholder":
            self.threshold_name = self.threshold_id
        elif not self.threshold_id:
            self.threshold_id = self.threshold_name
        if not self.threshold_type:
            self.threshold_type = self.metric_type_ref
        if not self.metric_type:
            self.metric_type = self.threshold_type
        if self.warning_threshold_min is None:
            self.warning_threshold_min = 0.0
        if self.warning_threshold_max is None:
            self.warning_threshold_max = self.warning_threshold_placeholder
        if self.breach_threshold is None:
            self.breach_threshold = self.critical_threshold_placeholder
        if not self.target_scope:
            self.target_scope = self.drift_family


@dataclass
class DriftMetricPlaceholder(_DictAccessMixin):
    """Catalog entry for uncalculated drift metric definitions."""

    metric_name: str = "default_metric_placeholder"
    metric_family: str = "distribution_stability"
    statistical_method: str = "population_stability_index"
    formula_description: str = ""
    is_calculated: bool = False
    real_drift_calculation_allowed: bool = False
    performance_claim_allowed: bool = False
    non_signal: bool = True
    status: str = "drift_contract_placeholder_only"
    metric_id: Optional[str] = None
    metric_type: Optional[str] = None
    target_scope: Optional[str] = None
    calculation_enabled: bool = False
    threshold_placeholder: Optional[str] = None
    description: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.metric_id and self.metric_name == "default_metric_placeholder":
            self.metric_name = self.metric_id
        elif not self.metric_id:
            self.metric_id = self.metric_name
        if self.metric_type and not self.statistical_method:
            self.statistical_method = self.metric_type
        elif not self.metric_type:
            self.metric_type = self.statistical_method
        if self.description and not self.formula_description:
            self.formula_description = self.description
        elif not self.description:
            self.description = self.formula_description


@dataclass
class DriftDisabledExecutionItem(_DictAccessMixin):
    """Audit entry documenting an operation permanently disabled by policy."""

    operation_name: str = "default_operation"
    subsystem: str = "drift_safeguard"
    policy_enforced: str = "drift_safety_policy"
    execution_blocked: bool = True
    reason: str = "Blocked by safety policy in non-executing Phase 142 contracts layer."
    status: str = "execution_contract_only"
    execution_id: Optional[str] = None
    execution_type: Optional[str] = None
    target_component: Optional[str] = None
    is_disabled: bool = True
    disabled_reason: Optional[str] = None
    remediation_required: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.execution_id and self.operation_name == "default_operation":
            self.operation_name = self.execution_id
        elif not self.execution_id:
            self.execution_id = self.operation_name
        if self.target_component and self.subsystem == "drift_safeguard":
            self.subsystem = self.target_component
        if self.disabled_reason and self.reason == "Blocked by safety policy in non-executing Phase 142 contracts layer.":
            self.reason = self.disabled_reason


@dataclass
class DriftGuardItem(_DictAccessMixin):
    """Safety guard contract verifying boundary compliance."""

    guard_name: str = "default_guard"
    guard_type: str = "no_lookahead"
    enforced: bool = True
    blocked_patterns: List[str] = field(default_factory=list)
    non_signal: bool = True
    status: str = "drift_contract_ready"
    guard_id: Optional[str] = None
    is_active: bool = True
    description: Optional[str] = None
    validation_rule: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.guard_id and self.guard_name == "default_guard":
            self.guard_name = self.guard_id
        elif not self.guard_id:
            self.guard_id = self.guard_name


@dataclass
class DriftFinding(_DictAccessMixin):
    """Audit finding item generated during drift contract analysis."""

    finding_type: str = "audit"
    drift_domain: str = "general_drift"
    severity_label: str = "info"
    message: str = ""
    recommendation: str = ""
    manual_review_required: bool = True
    non_signal: bool = True
    finding_id: Optional[str] = None
    domain: Optional[str] = None
    target_name: Optional[str] = None
    severity: Optional[str] = None
    description: Optional[str] = None
    recommended_action: Optional[str] = None
    requires_human_review: bool = False
    execution_blocked: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.domain and self.drift_domain == "general_drift":
            self.drift_domain = self.domain
        elif not self.domain:
            self.domain = self.drift_domain
        if self.severity and self.severity_label == "info":
            self.severity_label = self.severity
        elif not self.severity:
            self.severity = self.severity_label
        if self.description and not self.message:
            self.message = self.description
        elif not self.description:
            self.description = self.message
        if self.recommended_action and not self.recommendation:
            self.recommendation = self.recommended_action
        elif not self.recommended_action:
            self.recommended_action = self.recommendation


@dataclass
class DriftReadinessScore(_DictAccessMixin):
    """Composite readiness score for Phase 142 drift monitoring contracts."""

    score: float = 1.0
    classification: str = "HIGH_READINESS"
    passed_gates: int = 5
    total_gates: int = 5
    findings_count: int = 0
    meets_threshold: bool = True
    non_signal: bool = True
    production_ready: bool = False
    broker_ready: bool = False
    official_approval: bool = False
    drift_calculation_approved: bool = False
    retraining_trigger_approved: bool = False
    domain: Optional[str] = None
    readiness_score: Optional[float] = None
    governance_status: str = "ready"
    blocker_count: int = 0
    warning_count: int = 0
    is_ready_for_review: bool = True
    details: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.readiness_score is not None and self.score == 1.0:
            self.score = self.readiness_score
        elif self.readiness_score is None:
            self.readiness_score = self.score


@dataclass
class DriftManualReviewItem(_DictAccessMixin):
    """Item placed into the manual inspection queue for human audit."""

    item_id: str = "review_item_001"
    domain: str = "general_drift"
    summary: str = ""
    review_reason: str = ""
    safe_recommendations: List[str] = field(default_factory=list)
    action_blocked: bool = True
    non_signal: bool = True
    review_id: Optional[str] = None
    target_name: Optional[str] = None
    drift_domain: Optional[str] = None
    status: str = "pending_review"
    findings_summary: Optional[str] = None
    required_signoffs: List[str] = field(default_factory=list)
    is_approved: bool = False
    notes: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.review_id and self.item_id == "review_item_001":
            self.item_id = self.review_id
        elif not self.review_id:
            self.review_id = self.item_id
        if self.drift_domain and self.domain == "general_drift":
            self.domain = self.drift_domain
        elif not self.drift_domain:
            self.drift_domain = self.domain
        if self.findings_summary and not self.summary:
            self.summary = self.findings_summary
        elif not self.findings_summary:
            self.findings_summary = self.summary


@dataclass
class ModelDriftMonitoringManifest(_DictAccessMixin):
    """Master manifest certifying the integrity of Phase 142 drift monitoring contracts."""

    manifest_id: str = "drift_manifest_p142"
    manifest_name: str = "model_drift_monitoring_manifest"
    generated_at: str = ""
    phase: int = 142
    current_phase: int = 142
    target_final_phase: int = 160
    next_phase: int = 143
    profile: Any = None
    contracts: List[DriftMonitoringContract] = field(default_factory=list)
    linkages: List[DriftLinkageItem] = field(default_factory=list)
    window_policies: List[DriftWindowPolicy] = field(default_factory=list)
    thresholds: List[DriftThresholdPlaceholder] = field(default_factory=list)
    metric_placeholders: List[DriftMetricPlaceholder] = field(default_factory=list)
    disabled_executions: List[DriftDisabledExecutionItem] = field(default_factory=list)
    guards: List[DriftGuardItem] = field(default_factory=list)
    findings: List[DriftFinding] = field(default_factory=list)
    readiness_scores: List[DriftReadinessScore] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    drift_contract_count: int = 0
    linkage_count: int = 0
    disabled_execution_report_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    readiness_score: float = 1.0

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
    data_drift_calculation_executed: bool = False
    feature_drift_calculation_executed: bool = False
    model_drift_calculation_executed: bool = False
    drift_metric_calculation_executed: bool = False
    live_monitoring_executed: bool = False
    alerting_executed: bool = False
    retraining_trigger_generated: bool = False
    model_action_generated: bool = False
    metric_calculation_executed: bool = False
    performance_claim_generated: bool = False
    artifact_persisted: bool = False
    model_registry_written: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    manual_review_required: bool = True

    def __post_init__(self):
        if not self.drift_contract_count and self.contracts:
            self.drift_contract_count = len(self.contracts)
        if not self.linkage_count and self.linkages:
            self.linkage_count = len(self.linkages)
        if not self.disabled_execution_report_count and self.disabled_executions:
            self.disabled_execution_report_count = len(self.disabled_executions)
        if not self.finding_count and self.findings:
            self.finding_count = len(self.findings)

