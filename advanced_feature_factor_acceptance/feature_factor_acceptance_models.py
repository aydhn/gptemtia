"""Phase 125: Feature/Factor Engine Acceptance Data Models.

Defines typed dataclasses for profiles, block inventory, dependency graphs,
acceptance gates, acceptance scoring, manual reviews, compliance items, and manifests.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class FeatureFactorAcceptanceProfileItem:
    """Represents an acceptance profile record in the registry."""
    profile_name: str
    description: str
    current_phase: int = 125
    target_final_phase: int = 160
    next_phase: int = 126
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    min_score: float = 0.45
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class FeatureEngineBlockInventoryItem:
    """Represents a module inventory record in the Phase 116-125 feature engine block."""
    phase_number: int
    module_name: str
    package_name: str
    description: str
    expected_scripts: int
    expected_tests: int
    expected_reports: int
    expected_datalake_outputs: int
    expected_docs: int
    status_label: str
    manual_review_required: bool = False
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class FeatureEngineBlockDependencyItem:
    """Represents a dependency connection between phases in the feature block."""
    source_phase: int
    source_module: str
    target_phase: int
    target_module: str
    dependency_type: str
    contract_satisfied: bool = True
    notes: str = ""
    non_signal: bool = True


@dataclass
class FeatureEngineAcceptanceGate:
    """Represents a single acceptance evaluation gate."""
    gate_id: str
    gate_name: str
    category: str
    description: str
    status: str
    score_weight: float
    passed: bool
    details: str = ""
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class FeatureEngineAcceptanceScore:
    """Aggregated acceptance score for the feature engine block."""
    overall_score: float
    score_tier: str
    total_gates: int
    passed_gates: int
    failed_gates: int
    warning_gates: int
    manual_review_required: bool
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class FeatureEngineManualReviewItem:
    """Queue entry for items requiring manual inspection."""
    review_id: str
    phase_number: int
    module_name: str
    review_reason: str
    severity: str
    suggested_action: str
    status: str = "PENDING"
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    non_signal: bool = True


@dataclass
class FeatureEngineComplianceItem:
    """Compliance verification entry for governance requirements."""
    compliance_id: str
    compliance_type: str
    subject_module: str
    verified: bool
    rule_description: str
    findings: str = "COMPLIANT"
    non_signal: bool = True
    source_preserved: bool = True
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False


@dataclass
class FeatureEngineBlockStatusItem:
    """Summary record for overall block status."""
    phase_start: int = 116
    phase_end: int = 125
    overall_status: str = "ACCEPTANCE_PASS"
    acceptance_score: float = 1.0
    total_modules: int = 10
    total_gates: int = 16
    manual_review_count: int = 0
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class Phase116125AcceptanceManifest:
    """Official Phase 116-125 Acceptance Manifest."""
    block_name: str
    phase_start: int = 116
    phase_end: int = 125
    target_final_phase: int = 160
    next_phase: int = 126
    module_count: int = 10
    gate_count: int = 16
    manual_review_count: int = 0
    acceptance_score: float = 1.0
    manual_review_required: bool = False
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    source_preserved: bool = True
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)
