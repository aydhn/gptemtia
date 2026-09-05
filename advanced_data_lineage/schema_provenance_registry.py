from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile
from advanced_data_lineage.data_lineage_models import (
    SchemaProvenance,
    build_schema_provenance_id,
)


SCHEMA_SPECS = [
    ("dataset_fx_quote", "fx_quote_schema", "v1.0", "raw_schema://fx/quotes_raw_v1", "canonical://schema/fx_quote_canonical_v1", "Source raw columns mapped to canonical timestamp, pair, bid, ask", False),
    ("dataset_fx_ohlcv", "fx_ohlcv_schema", "v1.0", "raw_schema://fx/ohlcv_raw_v1", "canonical://schema/fx_ohlcv_canonical_v1", "Source raw OHLCV columns mapped to canonical OHLCV fields", False),
    ("dataset_commodity_spot", "commodity_spot_schema", "v1.0", "raw_schema://commodity/spot_raw_v1", "canonical://schema/commodity_spot_canonical_v1", "Source raw spot price mapped to canonical symbol, price, unit", False),
    ("dataset_commodity_ohlcv", "commodity_ohlcv_schema", "v1.0", "raw_schema://commodity/ohlcv_raw_v1", "canonical://schema/commodity_ohlcv_canonical_v1", "Source raw commodity OHLCV mapped to canonical commodity OHLCV", False),
    ("dataset_macro_timeseries", "macro_timeseries_schema", "v1.0", "raw_schema://macro/timeseries_raw_v1", "canonical://schema/macro_timeseries_canonical_v1", "Source indicator timeseries mapped to canonical indicator, value, frequency", False),
    ("dataset_calendar_event", "calendar_event_schema", "v1.0", "raw_schema://calendar/event_raw_v1", "canonical://schema/calendar_event_canonical_v1", "Source event mapped to canonical event, country, scheduled_time", False),
    ("dataset_release_event", "release_event_schema", "v1.0", "raw_schema://calendar/release_raw_v1", "canonical://schema/release_event_canonical_v1", "Source actual release mapped to canonical actual_time, actual_value", False),
    ("dataset_news_metadata", "news_metadata_schema", "v1.0", "raw_schema://news/metadata_raw_v1", "canonical://schema/news_metadata_canonical_v1", "Source headline, source, tags mapped to canonical tags - zero full text", False),
    ("dataset_provider_metadata", "provider_metadata_schema", "v1.0", "raw_schema://provider/meta_raw_v1", "canonical://schema/provider_metadata_canonical_v1", "Source provider identity mapped to canonical provider slug", False),
]


def build_default_schema_provenance_records(
    profile: DataLineageProfile,
) -> List[SchemaProvenance]:
    records: List[SchemaProvenance] = []
    for d_type, s_name, ver, src_ref, can_ref, note, rev_req in SCHEMA_SPECS:
        prov_id = build_schema_provenance_id(d_type, ver)
        records.append(
            SchemaProvenance(
                provenance_id=prov_id,
                dataset_type=d_type,
                schema_name=s_name,
                schema_version=ver,
                source_schema_ref=src_ref,
                canonical_schema_ref=can_ref,
                mapping_note=note,
                manual_review_required=rev_req,
            )
        )
    return records


def build_schema_provenance_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = build_default_schema_provenance_records(profile)
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_schema_provenance_registry(df)
    return df, summary


def summarize_schema_provenance_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_schemas": len(df),
        "schema_names": df["schema_name"].tolist() if "schema_name" in df.columns else [],
        "dataset_types": df["dataset_type"].unique().tolist() if "dataset_type" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
