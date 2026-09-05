"""Phase 131: Cross-Asset Regime Context Models.

Defines non-signal, zero-execution dataclass models for cross-asset profiles,
entities, pairs, taxonomy items, contracts, findings, scores, manifests, and review items.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class CrossAssetRegimeProfileItem:
    """Registered profile item with explicit safety boundary flags."""

    profile_name: str
    description: str
    current_phase: int = 131
    target_final_phase: int = 160
    next_phase: int = 132
    min_context_score: float = 0.45
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
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
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False


@dataclass
class CrossAssetRegimeEntity:
    """Cross-asset regime entity metadata item."""

    entity_id: str
    entity_name: str
    entity_type: str  # fx_pair, commodity_symbol, macro_indicator, calendar_event, news_metadata_tag, regime_family, candidate_state_context, transition_context
    domain: str
    base_currency_or_asset: str
    quote_or_benchmark: str
    source_phase: int
    readiness_status: str
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False


@dataclass
class CrossAssetRegimePair:
    """Cross-asset entity pair relationship definition."""

    pair_id: str
    left_entity_id: str
    left_entity_type: str
    right_entity_id: str
    right_entity_type: str
    relationship_category: str
    timestamp_alignment_policy: str
    asof_join_policy: str
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False


@dataclass
class CrossAssetRelationshipTaxonomyItem:
    """Taxonomy catalog item defining relationship nature."""

    taxonomy_id: str
    taxonomy_name: str
    relationship_type: str
    description: str
    diagnostic_role: str
    allows_trading_signal: bool = False
    allows_prediction: bool = False
    requires_no_lookahead: bool = True
    non_signal: bool = True
    source_preserved: bool = True


@dataclass
class CrossAssetContextContract:
    """Cross-asset context contract defining join, alignment, and guard rules."""

    contract_name: str
    relationship_type: str
    left_entity_type: str
    right_entity_type: str
    timestamp_policy_ref: str
    asof_policy_ref: str
    validation_dependency_ref: str
    quality_dependency_ref: str
    source_phase_refs: List[str] = field(default_factory=list)
    metadata_only_news_required: bool = True
    no_lookahead_required: bool = True
    non_signal_required: bool = True
    manual_review_required: bool = False
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False


@dataclass
class CrossAssetContextFinding:
    """Diagnostic finding discovered during cross-asset context evaluation."""

    finding_id: str
    finding_type: str
    relationship_type: str
    severity_label: str
    message: str
    recommendation: str
    manual_review_required: bool = True
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    timestamp_utc: str = field(default_factory=_utc_now_iso)


@dataclass
class CrossAssetContextScore:
    """Internal diagnostic score measuring cross-asset context completeness and integrity."""

    score_id: str
    context_score: float  # 0.0 to 1.0
    classification: str
    active_profile: str
    entity_count: int
    pair_count: int
    contract_count: int
    findings_count: int
    manual_review_count: int
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    contains_target_or_prediction: bool = False
    contains_trading_recommendation: bool = False
    timestamp_utc: str = field(default_factory=_utc_now_iso)

    def __post_init__(self):
        if not (0.0 <= self.context_score <= 1.0):
            raise ValueError(f"context_score must be between 0.0 and 1.0, got {self.context_score}")


@dataclass
class CrossAssetRegimeManifest:
    """Master audit manifest certifying non-signal, zero-execution compliance."""

    manifest_name: str
    current_phase: int = 131
    target_final_phase: int = 160
    next_phase: int = 132
    entity_count: int = 0
    pair_count: int = 0
    context_report_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    context_score: float = 0.85
    manifest_status: str = "MANIFEST_VALID"
    manual_review_required: bool = False
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
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    timestamp_utc: str = field(default_factory=_utc_now_iso)

    def __post_init__(self):
        if not (0.0 <= self.context_score <= 1.0):
            raise ValueError(f"context_score must be between 0.0 and 1.0, got {self.context_score}")


@dataclass
class CrossAssetManualReviewItem:
    """Non-destructive review queue item requiring human analyst inspection."""

    item_id: str
    category: str
    severity: str
    title: str
    description: str
    suggested_action: str
    blocking_for_phase_132: bool = False
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    timestamp_utc: str = field(default_factory=_utc_now_iso)
