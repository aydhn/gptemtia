from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile
from advanced_data_lineage.data_lineage_models import (
    DatasetProvenance,
    build_dataset_provenance_id,
    build_source_reference_id,
    build_provenance_source_id,
    build_schema_provenance_id,
)


DATASET_SPECS = [
    ("fx_quote_contract_dataset", "dataset_fx_quote", "advanced_fx_providers_engine", "fx_dry_run_fixture_source", "fx_fixture_provider", "local_fixture_uri", "v1.0", "dry_run", "data/raw/fx/quotes_sample.csv", "data/lake/advanced_data_normalization/normalized_views/fx_quotes_normalized.parquet", True, False),
    ("fx_ohlcv_contract_dataset", "dataset_fx_ohlcv", "advanced_fx_providers_engine", "fx_dry_run_fixture_source", "fx_fixture_provider", "local_fixture_uri", "v1.0", "dry_run", "data/raw/fx/ohlcv_sample.csv", "data/lake/advanced_data_normalization/normalized_views/fx_ohlcv_normalized.parquet", True, False),
    ("commodity_spot_contract_dataset", "dataset_commodity_spot", "advanced_commodity_providers_engine", "commodity_dry_run_fixture_source", "commodity_fixture_provider", "local_fixture_uri", "v1.0", "dry_run", "data/raw/commodity/spot_sample.csv", "data/lake/advanced_data_normalization/normalized_views/commodity_spot_normalized.parquet", True, False),
    ("commodity_ohlcv_contract_dataset", "dataset_commodity_ohlcv", "advanced_commodity_providers_engine", "commodity_dry_run_fixture_source", "commodity_fixture_provider", "local_fixture_uri", "v1.0", "dry_run", "data/raw/commodity/ohlcv_sample.csv", "data/lake/advanced_data_normalization/normalized_views/commodity_ohlcv_normalized.parquet", True, False),
    ("macro_timeseries_contract_dataset", "dataset_macro_timeseries", "advanced_macro_providers_engine", "macro_dry_run_fixture_source", "macro_fixture_provider", "local_fixture_uri", "v1.0", "dry_run", "data/raw/macro/macro_sample.csv", "data/lake/advanced_data_normalization/normalized_views/macro_timeseries_normalized.parquet", True, False),
    ("calendar_event_contract_dataset", "dataset_calendar_event", "advanced_economic_calendar_engine", "calendar_dry_run_fixture_source", "calendar_fixture_provider", "local_fixture_uri", "v1.0", "dry_run", "data/raw/calendar/events_sample.csv", "data/lake/advanced_data_normalization/normalized_views/calendar_events_normalized.parquet", True, False),
    ("release_event_contract_dataset", "dataset_release_event", "advanced_economic_calendar_engine", "calendar_dry_run_fixture_source", "calendar_fixture_provider", "local_fixture_uri", "v1.0", "dry_run", "data/raw/calendar/releases_sample.csv", "data/lake/advanced_data_normalization/normalized_views/release_events_normalized.parquet", True, False),
    ("news_metadata_contract_dataset", "dataset_news_metadata", "advanced_news_metadata_engine", "news_metadata_dry_run_fixture_source", "news_fixture_provider", "metadata_only_uri", "v1.0", "dry_run", "data/raw/news/metadata_sample.csv", "data/lake/advanced_data_normalization/normalized_views/news_metadata_normalized.parquet", True, False),
    ("provider_metadata_contract_dataset", "dataset_provider_metadata", "advanced_data_providers_abstraction", "public_dataset_placeholder_source", "public_dataset_placeholder", "doi_or_urn", "v1.0", "dry_run", "data/raw/provider/metadata_sample.csv", "data/lake/advanced_data_normalization/normalized_views/provider_metadata_normalized.parquet", True, False),
    ("normalized_view_manifest_dataset", "dataset_unknown", "advanced_data_normalization_engine", "local_cache_placeholder_source", "local_cache_provider", "cache_manifest_key", "v1.0", "cache_read", "data/lake/advanced_data_normalization/output_manifest/output_manifest.csv", "data/lake/advanced_data_lineage/normalized_output_lineage/normalized_views_lineage.csv", True, False),
]


def build_default_dataset_provenance_records(
    profile: DataLineageProfile,
) -> List[DatasetProvenance]:
    records: List[DatasetProvenance] = []
    for d_name, d_type, provider, s_name, p_provider, r_type, ver, mode, orig, norm, pres, rev_req in DATASET_SPECS:
        prov_id = build_dataset_provenance_id(d_name, provider)
        s_id = build_provenance_source_id(s_name, p_provider)
        ref_id = build_source_reference_id(s_id, r_type)
        sch_id = build_schema_provenance_id(d_type, ver)
        records.append(
            DatasetProvenance(
                provenance_id=prov_id,
                dataset_name=d_name,
                dataset_type=d_type,
                provider_name=provider,
                source_reference_id=ref_id,
                schema_id=sch_id,
                retrieval_mode=mode,
                original_ref=orig,
                normalized_ref=norm,
                source_preserved=pres,
                manual_review_required=rev_req,
            )
        )
    return records


def build_dataset_provenance_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = build_default_dataset_provenance_records(profile)
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_dataset_provenance_registry(df)
    return df, summary


def summarize_dataset_provenance_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_datasets": len(df),
        "dataset_names": df["dataset_name"].tolist() if "dataset_name" in df.columns else [],
        "dataset_types": df["dataset_type"].unique().tolist() if "dataset_type" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
