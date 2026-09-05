from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile
from advanced_data_lineage.data_lineage_models import (
    ProvenanceSource,
    build_provenance_source_id,
)


SOURCE_SPECS = [
    ("fx_dry_run_fixture_source", "dry_run_fixture", "fx_fixture_provider", "dataset_fx_quote", "Internal local research mock - non-commercial", "dry_run_offline", "Strict no-scraping", False),
    ("commodity_dry_run_fixture_source", "dry_run_fixture", "commodity_fixture_provider", "dataset_commodity_spot", "Internal local research mock - non-commercial", "dry_run_offline", "Strict no-scraping", False),
    ("macro_dry_run_fixture_source", "dry_run_fixture", "macro_fixture_provider", "dataset_macro_timeseries", "Internal local research mock - non-commercial", "dry_run_offline", "Strict no-scraping", False),
    ("calendar_dry_run_fixture_source", "dry_run_fixture", "calendar_fixture_provider", "dataset_calendar_event", "Internal local research mock - non-commercial", "dry_run_offline", "Strict no-scraping", False),
    ("news_metadata_dry_run_fixture_source", "dry_run_fixture", "news_fixture_provider", "dataset_news_metadata", "Internal local metadata mock - non-commercial, zero full text", "dry_run_offline", "Strict no-scraping", False),
    ("manual_file_placeholder_source", "manual_file", "manual_file_provider", "dataset_provider_metadata", "User-provided local flat file", "file_system", "Strict no-scraping", True),
    ("local_cache_placeholder_source", "local_cache", "local_cache_provider", "dataset_provider_metadata", "Cached offline snapshot", "file_cache", "Strict no-scraping", False),
    ("official_api_placeholder_source", "official_api", "official_api_placeholder", "dataset_provider_metadata", "Official REST/GraphQL endpoint contract placeholder", "api_placeholder", "Strict no-scraping", True),
    ("licensed_provider_placeholder_source", "licensed_provider", "licensed_provider_placeholder", "dataset_provider_metadata", "Commercial vendor contract placeholder", "licensed_placeholder", "Strict no-scraping", True),
    ("public_dataset_placeholder_source", "public_dataset", "public_dataset_placeholder", "dataset_provider_metadata", "Public domain / open research archive placeholder", "public_placeholder", "Strict no-scraping", False),
]


def build_default_provenance_sources(
    profile: DataLineageProfile,
) -> List[ProvenanceSource]:
    sources: List[ProvenanceSource] = []
    for name, stype, provider, ds_type, license_note, mode, no_scraping, rev_req in SOURCE_SPECS:
        s_id = build_provenance_source_id(name, provider)
        sources.append(
            ProvenanceSource(
                source_id=s_id,
                source_name=name,
                source_type=stype,
                provider_name=provider,
                dataset_type=ds_type,
                license_note=license_note,
                retrieval_mode=mode,
                no_scraping_policy=no_scraping,
                manual_review_required=rev_req,
            )
        )
    return sources


def build_provenance_source_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    sources = build_default_provenance_sources(profile)
    records = [s.to_dict() for s in sources]
    df = pd.DataFrame.from_records(records)
    summary = summarize_provenance_source_registry(df)
    return df, summary


def summarize_provenance_source_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_sources": len(df),
        "source_names": df["source_name"].tolist() if "source_name" in df.columns else [],
        "source_types": df["source_type"].unique().tolist() if "source_type" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "all_no_scraping": bool((df["no_scraping_policy"] == "Strict no-scraping").all()) if "no_scraping_policy" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
