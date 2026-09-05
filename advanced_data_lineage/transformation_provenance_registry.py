from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile
from advanced_data_lineage.data_lineage_models import (
    TransformationProvenance,
    build_transformation_provenance_id,
)


TRANSFORMATION_SPECS = [
    ("dataset_fx_quote", "fx_symbol_slashing", "pair", "normalized_pair", "'EURUSD'", "'EUR/USD'", True, False, False),
    ("dataset_commodity_spot", "commodity_symbol_root_mapping", "symbol", "normalized_symbol", "'GOLD'", "'XAU/USD'", True, False, False),
    ("dataset_macro_timeseries", "macro_indicator_slugification", "indicator", "normalized_indicator", "'US10Y'", "'US_10Y_YIELD'", True, False, False),
    ("dataset_calendar_event", "calendar_event_name_normalization", "event", "normalized_event", "'FOMC'", "'FOMC_RATE_DECISION'", True, False, False),
    ("dataset_news_metadata", "news_topic_tag_normalization", "tags", "normalized_tags", "['central bank', 'inflation']", "['CENTRAL_BANK', 'INFLATION']", True, False, False),
    ("dataset_provider_metadata", "provider_name_slugification", "provider_name", "normalized_provider_name", "'Provider A'", "'provider_a'", True, False, False),
    ("dataset_provider_metadata", "schema_version_normalization", "schema_version", "normalized_schema_version", "'1.0'", "'v1.0'", True, False, False),
    ("dataset_fx_ohlcv", "timestamp_utc_iso8601_conversion", "timestamp", "normalized_timestamp", "'2026-01-01 10:00:00+03:00'", "'2026-01-01T07:00:00Z'", True, False, False),
    ("dataset_macro_timeseries", "frequency_vocabulary_standardization", "frequency", "normalized_frequency", "'Daily'", "'1d'", True, False, False),
    ("dataset_macro_timeseries", "unit_vocabulary_standardization", "unit", "normalized_unit", "'Percent'", "'percent'", True, False, False),
    ("dataset_calendar_event", "region_country_iso_normalization", "country", "normalized_region", "'United States'", "'US'", True, False, False),
    ("dataset_fx_quote", "duplicate_key_composite_derivation", "pair, timestamp", "canonical_duplicate_key", "('EUR/USD', '2026-01-01T00:00:00Z')", "'EUR/USD_2026-01-01T00:00:00Z'", True, False, False),
]


def build_default_transformation_provenance_records(
    profile: DataLineageProfile,
) -> List[TransformationProvenance]:
    records: List[TransformationProvenance] = []
    for d_type, rule, sf, tf, orig_repr, norm_repr, pres, dest, rev_req in TRANSFORMATION_SPECS:
        prov_id = build_transformation_provenance_id(d_type, sf, tf)
        records.append(
            TransformationProvenance(
                provenance_id=prov_id,
                dataset_type=d_type,
                transformation_rule=rule,
                source_field=sf,
                target_field=tf,
                original_value_repr=orig_repr,
                normalized_value_repr=norm_repr,
                source_preserved=pres,
                destructive_action_allowed=dest,
                manual_review_required=rev_req,
            )
        )
    return records


def build_transformation_provenance_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = build_default_transformation_provenance_records(profile)
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_transformation_provenance_registry(df)
    return df, summary


def summarize_transformation_provenance_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_transformations": len(df),
        "transformation_rules": df["transformation_rule"].tolist() if "transformation_rule" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
