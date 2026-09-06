"""Phase 132: Macro/Event/News Regime Context Expansion Data Models.

Defines dataclasses ensuring non-signal, metadata-only, lookahead-free guarantees.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class MacroEventNewsRegimeProfileItem:
    """Represents a registered operational profile item."""

    profile_name: str
    description: str
    current_phase: int = 132
    target_final_phase: int = 160
    next_phase: int = 133
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    min_context_score: float = 0.45
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class MacroRegimeEntity:
    """Represents a macro regime indicator or release entity."""

    entity_id: str
    entity_name: str
    entity_type: str  # e.g., inflation_indicator, rate_indicator, growth_indicator
    country_code: str
    currency_code: str
    source_provider: str
    release_frequency: str
    nominal_lag_days: int
    revision_tracked: bool = True
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class EventRegimeEntity:
    """Represents an economic calendar or scheduled release event entity."""

    event_id: str
    event_name: str
    entity_type: str  # calendar_event, scheduled_release, event_window
    country_code: str
    currency_code: str
    importance_level: str  # low, medium, high, critical
    pre_event_window_minutes: int
    post_event_window_minutes: int
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class NewsMetadataRegimeEntity:
    """Represents metadata-only news tag, topic, or reference entity (zero full article)."""

    entity_id: str
    entity_name: str
    entity_type: str  # news_topic_tag, news_asset_tag, news_macro_tag, news_event_reference
    tag_category: str
    source_system: str
    freshness_window_hours: int = 24
    contains_full_article_text: bool = False
    contains_article_body: bool = False
    contains_raw_content: bool = False
    contains_scraped_html: bool = False
    contains_embedding: bool = False
    contains_vector: bool = False
    sentiment_model_output: bool = False
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class MacroEventNewsContextTaxonomyItem:
    """Taxonomy categorization item for macro, event, or news regime context."""

    taxonomy_id: str
    taxonomy_name: str
    domain: str
    description: str
    parent_category: str
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class MacroEventNewsContextContract:
    """Contract binding macro/event/news context metadata to alignment and safety invariants."""

    contract_name: str
    context_type: str
    entity_type: str
    timestamp_policy_ref: str
    asof_policy_ref: str
    validation_dependency_ref: str
    quality_dependency_ref: str
    source_phase_refs: List[str] = field(default_factory=list)
    metadata_only_news_required: bool = True
    no_lookahead_required: bool = True
    non_signal_required: bool = True
    manual_review_required: bool = False
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class MetadataOnlyNewsBoundaryItem:
    """Metadata-only news boundary rule definition ensuring zero raw article/sentiment leaks."""

    rule_id: str
    forbidden_field: str
    description: str
    remediation_action: str = "exclude_from_feature_lake"
    is_active: bool = True
    strictly_enforced: bool = True
    non_signal: bool = True


@dataclass
class MacroEventNewsContextFinding:
    """Diagnostic finding identified during macro/event/news context expansion."""

    finding_id: str
    finding_type: str
    context_type: str
    severity_label: str  # info, warning, error, blocker
    message: str
    recommendation: str
    manual_review_required: bool = True
    destructive_action_allowed: bool = False
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class MacroEventNewsContextScore:
    """Overall scoring of macro/event/news regime context integrity."""

    context_score: float  # 0.0 to 1.0
    classification: str
    total_findings: int
    blocker_count: int
    warning_count: int
    manual_review_count: int
    non_signal: bool = True
    source_preserved: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False


@dataclass
class MacroEventNewsRegimeManifest:
    """Comprehensive manifest asserting Phase 132 state, counts, and safety guarantees."""

    manifest_name: str
    current_phase: int = 132
    target_final_phase: int = 160
    next_phase: int = 133
    macro_entity_count: int = 0
    event_entity_count: int = 0
    news_metadata_entity_count: int = 0
    context_report_count: int = 0
    finding_count: int = 0
    manual_review_count: int = 0
    context_score: float = 1.0
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
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class MacroEventNewsManualReviewItem:
    """Manual review entry for offline governance."""

    item_id: str
    category: str
    issue_description: str
    safe_recommendation: str
    status: str = "pending"
    prohibited_actions: List[str] = field(
        default_factory=lambda: [
            "auto-delete",
            "auto-overwrite",
            "auto-impute",
            "enable scraping",
            "download article body",
            "generate sentiment",
            "generate embedding",
            "generate signal",
            "train model",
            "approve production",
            "approve broker readiness",
        ]
    )
