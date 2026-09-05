from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


QUALITY_FINDING_LINEAGE_ITEMS = [
    {
        "lineage_id": "qf_lin_001",
        "finding_type": "missing_bid_quote",
        "dataset_type": "dataset_fx_quote",
        "provider_name": "advanced_fx_providers_engine",
        "source_id": "prov_src_fx_fixture_provider_fx_dry_run_fixture_source",
        "quality_rule_ref": "fx_quote_sanity_rule",
        "severity": "lineage_manual_review_required",
        "provenance_impact": "Requires placeholder retention without row deletion",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": True,
    },
    {
        "lineage_id": "qf_lin_002",
        "finding_type": "negative_spread_anomaly",
        "dataset_type": "dataset_fx_quote",
        "provider_name": "advanced_fx_providers_engine",
        "source_id": "prov_src_fx_fixture_provider_fx_dry_run_fixture_source",
        "quality_rule_ref": "quote_spread_consistency_rule",
        "severity": "lineage_manual_review_required",
        "provenance_impact": "Flagged in lineage audit trail, raw values kept",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": True,
    },
    {
        "lineage_id": "qf_lin_003",
        "finding_type": "ohlc_high_low_inversion",
        "dataset_type": "dataset_commodity_ohlcv",
        "provider_name": "advanced_commodity_providers_engine",
        "source_id": "prov_src_commodity_fixture_provider_commodity_dry_run_fixture_source",
        "quality_rule_ref": "ohlc_geometry_consistency_rule",
        "severity": "lineage_manual_review_required",
        "provenance_impact": "Flagged in review queue, zero auto-overwrite",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": True,
    },
    {
        "lineage_id": "qf_lin_004",
        "finding_type": "unrecognized_macro_unit",
        "dataset_type": "dataset_macro_timeseries",
        "provider_name": "advanced_macro_providers_engine",
        "source_id": "prov_src_macro_fixture_provider_macro_dry_run_fixture_source",
        "quality_rule_ref": "frequency_unit_consistency_rule",
        "severity": "lineage_manual_review_required",
        "provenance_impact": "Forwarded to Phase 113 vocabulary standardizer",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": True,
    },
    {
        "lineage_id": "qf_lin_005",
        "finding_type": "scheduled_actual_time_gap",
        "dataset_type": "dataset_calendar_event",
        "provider_name": "advanced_economic_calendar_engine",
        "source_id": "prov_src_calendar_fixture_provider_calendar_dry_run_fixture_source",
        "quality_rule_ref": "event_release_consistency_rule",
        "severity": "lineage_manual_review_required",
        "provenance_impact": "Release delay recorded in audit trail",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "manual_review_required": False,
    },
]


def build_quality_finding_lineage_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(QUALITY_FINDING_LINEAGE_ITEMS)
    summary = summarize_quality_finding_lineage_registry(df)
    return df, summary


def summarize_quality_finding_lineage_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_quality_finding_lineage": len(df),
        "finding_types": df["finding_type"].tolist() if "finding_type" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
