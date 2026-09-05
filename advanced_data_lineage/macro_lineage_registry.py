from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


MACRO_LINEAGE_ITEMS = [
    {
        "lineage_item_id": "mac_lin_indicator_norm",
        "domain": "macro_lineage_domain",
        "provider_profile": "balanced_no_scraping_macro_provider",
        "raw_field": "indicator",
        "canonical_field": "normalized_indicator",
        "schema_ref": "canonical://schema/macro_timeseries_canonical_v1",
        "normalization_rule": "macro_indicator_normalization_enforcement",
        "quality_rule_ref": "macro_indicator_sanity_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Indicator standardized (e.g. US10Y -> US_10Y_YIELD); raw value preserved",
    },
    {
        "lineage_item_id": "mac_lin_frequency_norm",
        "domain": "macro_lineage_domain",
        "provider_profile": "balanced_no_scraping_macro_provider",
        "raw_field": "frequency",
        "canonical_field": "normalized_frequency",
        "schema_ref": "canonical://schema/macro_timeseries_canonical_v1",
        "normalization_rule": "frequency_normalization",
        "quality_rule_ref": "frequency_unit_consistency_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Code standardized to standard vocabulary ('1d', '1mo', '1q', '1y')",
    },
    {
        "lineage_item_id": "mac_lin_unit_norm",
        "domain": "macro_lineage_domain",
        "provider_profile": "balanced_no_scraping_macro_provider",
        "raw_field": "unit",
        "canonical_field": "normalized_unit",
        "schema_ref": "canonical://schema/macro_timeseries_canonical_v1",
        "normalization_rule": "unit_normalization",
        "quality_rule_ref": "frequency_unit_consistency_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Unit vocabulary mapped ('percent', 'index_points', 'bps'); multipliers not applied",
    },
    {
        "lineage_item_id": "mac_lin_revision_prov",
        "domain": "macro_lineage_domain",
        "provider_profile": "balanced_no_scraping_macro_provider",
        "raw_field": "revision_date, revision_status",
        "canonical_field": "canonical_revision_metadata",
        "schema_ref": "canonical://schema/macro_timeseries_canonical_v1",
        "normalization_rule": "macro_revision_policy_enforcement",
        "quality_rule_ref": "macro_revision_consistency_rule",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "notes": "Vintage and revision history tracked without destructive overwrite",
    },
]


def build_macro_lineage_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(MACRO_LINEAGE_ITEMS)
    summary = summarize_macro_lineage_registry(df)
    return df, summary


def summarize_macro_lineage_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_macro_lineage_items": len(df),
        "canonical_fields": df["canonical_field"].tolist() if "canonical_field" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
