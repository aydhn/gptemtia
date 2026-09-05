from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile
from advanced_data_lineage.data_lineage_models import (
    ProviderProvenance,
    build_provider_provenance_id,
    build_provenance_source_id,
)


PROVIDER_SPECS = [
    ("advanced_data_providers_abstraction", "data_abstraction", "public_dataset_placeholder_source", "public_dataset_placeholder", "capability:multi_provider_router", "Open research baseline", "No credentials required / offline", "Strict no-scraping", "provenance_high_confidence", False),
    ("advanced_fx_providers_engine", "fx_provider", "fx_dry_run_fixture_source", "fx_fixture_provider", "capability:fx_quotes_and_ohlcv", "Local dry-run mock", "No credentials required / offline", "Strict no-scraping", "provenance_high_confidence", False),
    ("advanced_commodity_providers_engine", "commodity_provider", "commodity_dry_run_fixture_source", "commodity_fixture_provider", "capability:commodity_spot_and_futures", "Local dry-run mock", "No credentials required / offline", "Strict no-scraping", "provenance_high_confidence", False),
    ("advanced_macro_providers_engine", "macro_provider", "macro_dry_run_fixture_source", "macro_fixture_provider", "capability:macro_indicators_and_rates", "Local dry-run mock", "No credentials required / offline", "Strict no-scraping", "provenance_high_confidence", False),
    ("advanced_economic_calendar_engine", "calendar_provider", "calendar_dry_run_fixture_source", "calendar_fixture_provider", "capability:calendar_events_and_releases", "Local dry-run mock", "No credentials required / offline", "Strict no-scraping", "provenance_high_confidence", False),
    ("advanced_news_metadata_engine", "news_provider", "news_metadata_dry_run_fixture_source", "news_fixture_provider", "capability:news_metadata_and_taxonomies", "Local metadata mock - zero full text", "No credentials required / offline", "Strict no-scraping", "provenance_high_confidence", False),
    ("manual_file_provider_adapter", "file_adapter", "manual_file_placeholder_source", "manual_file_provider", "capability:manual_file_dropzone", "User-provided files", "Local filesystem permissions only", "Strict no-scraping", "provenance_medium_confidence", True),
    ("local_cache_provider_adapter", "cache_adapter", "local_cache_placeholder_source", "local_cache_provider", "capability:local_cache_reader", "Local snapshot data", "No external credentials", "Strict no-scraping", "provenance_high_confidence", False),
    ("official_api_provider_placeholder", "api_placeholder", "official_api_placeholder_source", "official_api_placeholder", "capability:official_api_dry_run", "Vendor public terms placeholder", "Dry-run only / zero live keys", "Strict no-scraping", "provenance_medium_confidence", True),
    ("licensed_vendor_provider_placeholder", "licensed_placeholder", "licensed_provider_placeholder_source", "licensed_provider_placeholder", "capability:licensed_market_data", "Commercial license placeholder", "Dry-run only / zero live keys", "Strict no-scraping", "provenance_low_confidence", True),
]


def build_default_provider_provenance_records(
    profile: DataLineageProfile,
) -> List[ProviderProvenance]:
    records: List[ProviderProvenance] = []
    for p_name, p_type, s_name, provider, cap, lic, cred, no_scrap, conf, rev_req in PROVIDER_SPECS:
        prov_id = build_provider_provenance_id(p_name)
        s_id = build_provenance_source_id(s_name, provider)
        records.append(
            ProviderProvenance(
                provenance_id=prov_id,
                provider_name=p_name,
                provider_type=p_type,
                source_id=s_id,
                capability_ref=cap,
                license_note=lic,
                credential_policy=cred,
                no_scraping_policy=no_scrap,
                confidence_label=conf,
                manual_review_required=rev_req,
            )
        )
    return records


def build_provider_provenance_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = build_default_provider_provenance_records(profile)
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_provenance_registry(df)
    return df, summary


def summarize_provider_provenance_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_providers": len(df),
        "provider_names": df["provider_name"].tolist() if "provider_name" in df.columns else [],
        "provider_types": df["provider_type"].unique().tolist() if "provider_type" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "high_confidence_count": int((df["confidence_label"] == "provenance_high_confidence").sum()) if "confidence_label" in df.columns else 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
