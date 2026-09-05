from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


NORMALIZATION_LINEAGE_ITEMS = [
    {
        "lineage_id": "norm_lin_fx_pair",
        "dataset_type": "dataset_fx_quote",
        "canonical_field": "normalized_pair",
        "phase_113_rule": "fx_symbol_normalization_enforcement",
        "source_expression": "pair.replace('/', '').upper()",
        "target_expression": "base + '/' + quote",
        "lineage_status": "lineage_complete",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": False,
    },
    {
        "lineage_id": "norm_lin_commodity_symbol",
        "dataset_type": "dataset_commodity_spot",
        "canonical_field": "normalized_symbol",
        "phase_113_rule": "commodity_symbol_normalization_enforcement",
        "source_expression": "symbol.strip().upper()",
        "target_expression": "commodity_root_map.get(raw, raw)",
        "lineage_status": "lineage_complete",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": False,
    },
    {
        "lineage_id": "norm_lin_macro_indicator",
        "dataset_type": "dataset_macro_timeseries",
        "canonical_field": "normalized_indicator",
        "phase_113_rule": "macro_indicator_normalization_enforcement",
        "source_expression": "indicator.strip()",
        "target_expression": "macro_vocabulary_map.get(raw, raw)",
        "lineage_status": "lineage_complete",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": False,
    },
    {
        "lineage_id": "norm_lin_calendar_event",
        "dataset_type": "dataset_calendar_event",
        "canonical_field": "normalized_event",
        "phase_113_rule": "calendar_event_normalization_enforcement",
        "source_expression": "event.strip()",
        "target_expression": "event_canonical_map.get(raw, raw)",
        "lineage_status": "lineage_complete",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": False,
    },
    {
        "lineage_id": "norm_lin_news_tags",
        "dataset_type": "dataset_news_metadata",
        "canonical_field": "normalized_tags",
        "phase_113_rule": "news_topic_tag_normalization_enforcement",
        "source_expression": "[t.lower() for t in raw_tags]",
        "target_expression": "[canonical_tag_map.get(t, t) for t in raw_tags]",
        "lineage_status": "lineage_complete",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": False,
    },
    {
        "lineage_id": "norm_lin_timestamp_utc",
        "dataset_type": "all",
        "canonical_field": "normalized_timestamp",
        "phase_113_rule": "timestamp_timezone_normalization",
        "source_expression": "timestamp_str_or_epoch",
        "target_expression": "iso8601_utc_format",
        "lineage_status": "lineage_complete",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": False,
    },
    {
        "lineage_id": "norm_lin_frequency",
        "dataset_type": "dataset_macro_timeseries",
        "canonical_field": "normalized_frequency",
        "phase_113_rule": "frequency_normalization",
        "source_expression": "freq_term.lower()",
        "target_expression": "standard_frequency_code",
        "lineage_status": "lineage_complete",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": False,
    },
    {
        "lineage_id": "norm_lin_unit",
        "dataset_type": "dataset_macro_timeseries",
        "canonical_field": "normalized_unit",
        "phase_113_rule": "unit_normalization",
        "source_expression": "unit_term.lower()",
        "target_expression": "standard_unit_slug",
        "lineage_status": "lineage_complete",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": False,
    },
    {
        "lineage_id": "norm_lin_duplicate_key",
        "dataset_type": "all",
        "canonical_field": "canonical_duplicate_key",
        "phase_113_rule": "duplicate_key_normalization",
        "source_expression": "tuple(primary_key_fields)",
        "target_expression": "hash_or_composite_slug",
        "lineage_status": "lineage_complete",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": False,
    },
]


def build_normalization_lineage_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(NORMALIZATION_LINEAGE_ITEMS)
    summary = summarize_normalization_lineage_registry(df)
    return df, summary


def summarize_normalization_lineage_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_normalization_lineage_records": len(df),
        "canonical_fields": df["canonical_field"].tolist() if "canonical_field" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
