from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


CALENDAR_LINEAGE_ITEMS = [
    {
        "lineage_item_id": "cal_lin_event_norm",
        "domain": "calendar_lineage_domain",
        "provider_profile": "balanced_no_scraping_calendar_provider",
        "raw_field": "event",
        "canonical_field": "normalized_event",
        "schema_ref": "canonical://schema/calendar_event_canonical_v1",
        "normalization_rule": "calendar_event_normalization_enforcement",
        "quality_rule_ref": "calendar_event_sanity_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Event standardized (e.g. FOMC -> FOMC_RATE_DECISION, NFP -> US_NONFARM_PAYROLLS_RELEASE)",
    },
    {
        "lineage_item_id": "cal_lin_time_split",
        "domain": "calendar_lineage_domain",
        "provider_profile": "balanced_no_scraping_calendar_provider",
        "raw_field": "scheduled_time, actual_time",
        "canonical_field": "normalized_scheduled_time, actual_release_time",
        "schema_ref": "canonical://schema/release_event_canonical_v1",
        "normalization_rule": "timestamp_timezone_normalization",
        "quality_rule_ref": "event_release_consistency_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Scheduled and actual release times tracked separately with UTC timestamps",
    },
    {
        "lineage_item_id": "cal_lin_surprise_req",
        "domain": "calendar_lineage_domain",
        "provider_profile": "balanced_no_scraping_calendar_provider",
        "raw_field": "forecast, actual",
        "canonical_field": "canonical_surprise_requirement",
        "schema_ref": "canonical://schema/release_event_canonical_v1",
        "normalization_rule": "numeric_type_normalization",
        "quality_rule_ref": "event_release_consistency_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Surprise requirement tracked as diagnostic placeholder; no directional trade claims",
    },
]


def build_calendar_lineage_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(CALENDAR_LINEAGE_ITEMS)
    summary = summarize_calendar_lineage_registry(df)
    return df, summary


def summarize_calendar_lineage_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_calendar_lineage_items": len(df),
        "canonical_fields": df["canonical_field"].tolist() if "canonical_field" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
