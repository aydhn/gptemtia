"""Fusion Feature Metadata Registry.

Maintains comprehensive metadata definitions for all fused features across macro,
calendar, and news metadata domains.
Strictly non-signal, research use only.
"""

from typing import Any, Dict, List, Optional
from advanced_feature_fusion.fusion_feature_models import FusionFeatureMetadata


FEATURE_METADATA_ENTRIES: List[FusionFeatureMetadata] = [
    FusionFeatureMetadata(
        feature_id="macro_value_change",
        name="Macro Value Relative Change",
        domain="macroeconomic",
        feature_family="macro_lag",
        description="Period-over-period change in macroeconomic indicator value.",
        input_columns=["macro_value"],
        dtype="float64",
        is_placeholder=False,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="macro_surprise_placeholder",
        name="Macro Actual vs Forecast Surprise Placeholder",
        domain="macroeconomic",
        feature_family="macro_surprise",
        description="Normalized surprise magnitude placeholder (actual - forecast).",
        input_columns=["macro_actual_value", "macro_forecast_value"],
        dtype="float64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="macro_revision_flag",
        name="Macro Revision Flag Placeholder",
        domain="macroeconomic",
        feature_family="macro_revision",
        description="Binary flag indicating whether a macroeconomic figure was revised from its initial release.",
        input_columns=["macro_is_revised"],
        dtype="int64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="macro_frequency_flag",
        name="Macro Frequency Indicator Flag",
        domain="macroeconomic",
        feature_family="macro_lag",
        description="Categorical or one-hot flag indicating frequency cadence (monthly, quarterly, weekly).",
        input_columns=["macro_frequency"],
        dtype="object",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="pre_event_window_flag",
        name="Pre-Event Window Indicator",
        domain="calendar_events",
        feature_family="event_window",
        description="Binary indicator active within pre-event observation window before scheduled release.",
        input_columns=["timestamp", "scheduled_timestamp"],
        dtype="int64",
        is_placeholder=False,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="post_event_window_flag",
        name="Post-Event Window Indicator",
        domain="calendar_events",
        feature_family="event_window",
        description="Binary indicator active within post-event observation window following actual release.",
        input_columns=["timestamp", "actual_timestamp"],
        dtype="int64",
        is_placeholder=False,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="event_importance_weight",
        name="Event Importance Weight Placeholder",
        domain="calendar_events",
        feature_family="calendar_context",
        description="Ordinal or normalized importance scale (1-low to 3-high).",
        input_columns=["importance"],
        dtype="float64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="release_delay_placeholder",
        name="Release Delay Placeholder",
        domain="calendar_events",
        feature_family="event_window",
        description="Delay in minutes between scheduled release and actual availability timestamp.",
        input_columns=["scheduled_timestamp", "actual_timestamp"],
        dtype="float64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="release_has_actual_flag",
        name="Release Has Actual Figure Flag",
        domain="calendar_events",
        feature_family="calendar_context",
        description="Flag indicating whether an actual released value is currently available.",
        input_columns=["actual_value"],
        dtype="int64",
        is_placeholder=False,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="release_revised_previous_flag",
        name="Release Revised Previous Flag",
        domain="calendar_events",
        feature_family="calendar_context",
        description="Flag indicating whether previous period figure was revised in the current release.",
        input_columns=["revised_previous_value"],
        dtype="int64",
        is_placeholder=False,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="news_topic_flag",
        name="News Topic Presence Flag Placeholder",
        domain="news_metadata",
        feature_family="news_topic",
        description="Binary indicator of recent news metadata matching specified topic within lookback window.",
        input_columns=["news_topic"],
        dtype="int64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="news_topic_count",
        name="News Topic Occurrence Count Placeholder",
        domain="news_metadata",
        feature_family="news_topic",
        description="Count of distinct news metadata items associated with topic.",
        input_columns=["news_topic"],
        dtype="int64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="news_asset_tag_count",
        name="News Asset Tag Count Placeholder",
        domain="news_metadata",
        feature_family="news_asset_tag",
        description="Count of metadata tags referencing specific currency or commodity asset.",
        input_columns=["news_asset_tags"],
        dtype="int64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="news_macro_tag_count",
        name="News Macro Tag Count Placeholder",
        domain="news_metadata",
        feature_family="news_asset_tag",
        description="Count of metadata tags referencing macroeconomic themes (inflation, central bank, rate).",
        input_columns=["news_macro_tags"],
        dtype="int64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="news_event_linkage_flag",
        name="News Event Linkage Flag Placeholder",
        domain="news_metadata",
        feature_family="news_event_linkage",
        description="Indicator showing if news metadata references an identified economic calendar event.",
        input_columns=["event_id", "news_event_reference"],
        dtype="int64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="news_freshness_hours",
        name="News Freshness Elapsed Hours Placeholder",
        domain="news_metadata",
        feature_family="news_freshness",
        description="Elapsed hours since the most recent news metadata item prior to base timestamp.",
        input_columns=["timestamp", "news_published_timestamp"],
        dtype="float64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
    FusionFeatureMetadata(
        feature_id="news_freshness_decay_placeholder",
        name="News Freshness Exponential Decay Placeholder",
        domain="news_metadata",
        feature_family="news_freshness",
        description="Exponential recency factor placeholder for news metadata freshness.",
        input_columns=["news_freshness_hours"],
        dtype="float64",
        is_placeholder=True,
        is_signal=False,
        is_strictly_metadata=True,
    ),
]


def get_fusion_feature_metadata_registry() -> List[FusionFeatureMetadata]:
    """Return all registered fusion feature metadata entries."""
    return list(FEATURE_METADATA_ENTRIES)


def get_feature_metadata_by_id(feature_id: str) -> Optional[FusionFeatureMetadata]:
    """Retrieve metadata entry by feature_id."""
    for entry in FEATURE_METADATA_ENTRIES:
        if entry.feature_id == feature_id:
            return entry
    return None


def get_fusion_feature_metadata_summary() -> Dict[str, Any]:
    """Summary of metadata registry."""
    features = get_fusion_feature_metadata_registry()
    domains = sorted(list(set(f.domain for f in features)))
    families = sorted(list(set(f.feature_family for f in features)))
    return {
        "total_features": len(features),
        "domains": domains,
        "families": families,
        "zero_signal_guarantee": all(not f.is_signal for f in features),
        "strictly_metadata_only": all(f.is_strictly_metadata for f in features),
    }
