# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Testing and Drawdown Control Data Models."""

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ScenarioTestingContract:
    contract_id: str
    scenario_type: str
    name: str
    description: str
    shock_scope: str
    severity_level: str
    target_asset_classes: List[str]
    offline_simulation_hook: str
    contract_status: str = "CONTRACT_ONLY"
    execution_allowed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ScenarioLibraryContract:
    library_id: str
    library_name: str
    category: str
    scenario_count: int
    historical_count: int
    hypothetical_count: int
    dry_run_fixture: str
    contract_status: str = "CONTRACT_ONLY"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class HistoricalScenarioContract:
    scenario_id: str
    historical_event: str
    period_start: str
    period_end: str
    macro_backdrop: str
    observed_market_shock: str
    contract_status: str = "CONTRACT_ONLY"
    execution_allowed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class HypotheticalScenarioContract:
    scenario_id: str
    scenario_title: str
    rationale: str
    shock_vector: str
    extreme_tail_probability: str
    contract_status: str = "CONTRACT_ONLY"
    execution_allowed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class RegimeShiftScenarioContract:
    scenario_id: str
    transition_name: str
    source_regime: str
    target_regime: str
    volatility_multiplier: float
    correlation_shift: str
    contract_status: str = "CONTRACT_ONLY"
    execution_allowed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DrawdownControlContract:
    contract_id: str
    control_name: str
    drawdown_metric_target: str
    warning_threshold_pct: float
    breach_threshold_pct: float
    critical_threshold_pct: float
    control_policy: str
    contract_status: str = "CONTRACT_ONLY"
    execution_allowed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DrawdownThresholdContract:
    threshold_id: str
    tier_name: str
    drawdown_lower_pct: float
    drawdown_upper_pct: float
    mandatory_action: str
    contract_status: str = "CONTRACT_ONLY"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ControlActionPlaceholder:
    placeholder_id: str
    action_type: str
    target_scope: str
    reduction_target_pct: float
    activation_trigger: str
    execution_enabled: bool = False
    status: str = "PLACEHOLDER_ONLY"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ScenarioOutputContract:
    output_contract_id: str
    output_name: str
    schema_fields: List[str]
    frequency: str
    storage_format: str = "csv_json"
    materialization_allowed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ScenarioMetricPlaceholder:
    metric_id: str
    metric_name: str
    metric_category: str
    formula_spec: str
    is_calculated: bool = False
    status: str = "PLACEHOLDER_ONLY"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PortfolioScenarioFinding:
    finding_id: str
    domain: str
    severity: str
    description: str
    manual_review_required: bool
    status: str = "REGISTERED"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PortfolioScenarioReadinessScore:
    score_id: str
    overall_score: float
    classification: str
    meets_threshold: bool
    is_trading_signal: bool = False
    production_ready: bool = False
    broker_ready: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PortfolioScenarioControlManifest:
    manifest_id: str
    current_phase: int = 156
    target_final_phase: int = 160
    next_phase: int = 157
    scenario_contracts_count: int = 0
    drawdown_contracts_count: int = 0
    control_placeholders_count: int = 0
    scenario_executed: bool = False
    drawdown_control_executed: bool = False
    portfolio_adjustment_generated: bool = False
    broker_order_sent: bool = False
    live_order_sent: bool = False
    status: str = "READY"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
