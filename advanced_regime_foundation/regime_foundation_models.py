"""Phase 126: Regime Classification and Market Behavior Foundation Models.

Data models representing taxonomies, contracts, dependencies, and manifests.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class RegimeFoundationProfileItem:
    """Represents an active operational profile entry."""

    profile_name: str
    description: str
    current_phase: int = 126
    target_final_phase: int = 160
    next_phase: int = 127
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    min_readiness_score: float = 0.45
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class MarketBehaviorTaxonomyItem:
    """Represents a canonical market behavior classification."""

    behavior_id: str
    behavior_name: str
    behavior_category: str
    description: str
    associated_regime_family: str
    key_characteristics: List[str] = field(default_factory=list)
    non_signal: bool = True
    contains_trading_recommendation: bool = False
    status: str = "regime_ready"


@dataclass
class RegimeStateTaxonomyItem:
    """Represents a discrete or continuous regime state definition."""

    state_id: str
    regime_state_name: str
    regime_family: str
    state_description: str
    source_feature_contract: str
    validation_dependency: str
    quality_dependency: str
    non_signal: bool = True
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    status: str = "regime_ready"


@dataclass
class RegimeFamilyItem:
    """Represents a primary regime family definition."""

    family_id: str
    family_name: str
    family_category: str
    description: str
    primary_indicators: List[str] = field(default_factory=list)
    source_phases: List[int] = field(default_factory=list)
    non_signal: bool = True
    model_training_executed: bool = False
    clustering_executed: bool = False
    status: str = "regime_ready"


@dataclass
class RegimeInputFeatureContract:
    """Represents input feature and factor contract requirements for regimes."""

    contract_name: str
    regime_family: str
    required_feature_families: List[str] = field(default_factory=list)
    required_factor_families: List[str] = field(default_factory=list)
    source_phase_refs: List[int] = field(default_factory=list)
    validation_required: bool = True
    quality_required: bool = True
    no_lookahead_required: bool = True
    non_signal_required: bool = True
    manual_review_required: bool = True
    status: str = "regime_ready"


@dataclass
class RegimeDependencyItem:
    """Represents an upstream dependency (factor, validation, quality, feature store)."""

    dependency_id: str
    dependency_type: str  # factor, validation, quality, feature_store
    target_regime_family: str
    source_phase: int
    prerequisite_name: str
    verification_status: str = "VERIFIED"
    non_signal: bool = True
    blocking: bool = True


@dataclass
class RegimeStateOutputSchema:
    """Represents the canonical schema for non-signal regime state outputs."""

    field_name: str
    data_type: str
    regime_family: str
    description: str
    source_feature_contract: str
    validation_dependency: str
    quality_dependency: str
    non_signal: bool = True
    model_training_required_future_phase: bool = True
    manual_review_required: bool = True
    forbidden_field: bool = False


@dataclass
class RegimeFoundationManifest:
    """Master governance manifest for Phase 126 Regime Foundation."""

    foundation_name: str = "advanced_regime_foundation"
    current_phase: int = 126
    target_final_phase: int = 160
    next_phase: int = 127
    regime_family_count: int = 0
    regime_state_count: int = 0
    dependency_count: int = 0
    validation_dependency_count: int = 0
    quality_dependency_count: int = 0
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    model_training_executed: bool = False
    clustering_executed: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    contains_full_article_text: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    manual_review_required: bool = True
    extra_metadata: Dict[str, Any] = field(default_factory=dict)
