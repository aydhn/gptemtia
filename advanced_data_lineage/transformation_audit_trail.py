from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


TRANSFORMATION_AUDIT_ITEMS = [
    {
        "audit_id": "trans_aud_001",
        "dataset_type": "dataset_fx_quote",
        "transformation_rule": "fx_symbol_slashing",
        "source_field": "pair",
        "target_field": "normalized_pair",
        "input_sample": "EURUSD",
        "output_sample": "EUR/USD",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
    {
        "audit_id": "trans_aud_002",
        "dataset_type": "dataset_commodity_spot",
        "transformation_rule": "commodity_symbol_root_mapping",
        "source_field": "symbol",
        "target_field": "normalized_symbol",
        "input_sample": "GOLD",
        "output_sample": "XAU/USD",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
    {
        "audit_id": "trans_aud_003",
        "dataset_type": "dataset_macro_timeseries",
        "transformation_rule": "macro_indicator_slugification",
        "source_field": "indicator",
        "target_field": "normalized_indicator",
        "input_sample": "US10Y",
        "output_sample": "US_10Y_YIELD",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
    {
        "audit_id": "trans_aud_004",
        "dataset_type": "dataset_calendar_event",
        "transformation_rule": "calendar_event_name_normalization",
        "source_field": "event",
        "target_field": "normalized_event",
        "input_sample": "FOMC",
        "output_sample": "FOMC_RATE_DECISION",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
    {
        "audit_id": "trans_aud_005",
        "dataset_type": "dataset_news_metadata",
        "transformation_rule": "news_topic_tag_normalization",
        "source_field": "tags",
        "target_field": "normalized_tags",
        "input_sample": "['central bank']",
        "output_sample": "['CENTRAL_BANK']",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
    {
        "audit_id": "trans_aud_006",
        "dataset_type": "all",
        "transformation_rule": "timestamp_utc_iso8601_conversion",
        "source_field": "timestamp",
        "target_field": "normalized_timestamp",
        "input_sample": "2026-01-01 10:00:00+03:00",
        "output_sample": "2026-01-01T07:00:00Z",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
]


def build_transformation_audit_trail_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(TRANSFORMATION_AUDIT_ITEMS)
    summary = summarize_transformation_audit_trail(df)
    return df, summary


def summarize_transformation_audit_trail(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_transformation_audit_records": len(df),
        "transformation_rules": df["transformation_rule"].tolist() if "transformation_rule" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
