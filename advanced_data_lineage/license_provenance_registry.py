from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


LICENSE_PROVENANCE_ITEMS = [
    {
        "license_id": "lic_prov_001",
        "provider_name": "advanced_fx_providers_engine",
        "source_id": "prov_src_fx_fixture_provider_fx_dry_run_fixture_source",
        "license_note": "Internal synthetic/dry-run fixture; non-commercial research use only",
        "manual_review_required": False,
        "usage_boundary": "research_only",
        "redistribution_allowed_placeholder": False,
        "commercial_use_review_required": True,
    },
    {
        "license_id": "lic_prov_002",
        "provider_name": "advanced_commodity_providers_engine",
        "source_id": "prov_src_commodity_fixture_provider_commodity_dry_run_fixture_source",
        "license_note": "Internal synthetic/dry-run fixture; non-commercial research use only",
        "manual_review_required": False,
        "usage_boundary": "research_only",
        "redistribution_allowed_placeholder": False,
        "commercial_use_review_required": True,
    },
    {
        "license_id": "lic_prov_003",
        "provider_name": "advanced_macro_providers_engine",
        "source_id": "prov_src_macro_fixture_provider_macro_dry_run_fixture_source",
        "license_note": "Open research baseline metadata; non-commercial research use only",
        "manual_review_required": False,
        "usage_boundary": "research_only",
        "redistribution_allowed_placeholder": False,
        "commercial_use_review_required": True,
    },
    {
        "license_id": "lic_prov_004",
        "provider_name": "advanced_economic_calendar_engine",
        "source_id": "prov_src_calendar_fixture_provider_calendar_dry_run_fixture_source",
        "license_note": "Event metadata placeholder; zero raw vendor scraping",
        "manual_review_required": False,
        "usage_boundary": "research_only",
        "redistribution_allowed_placeholder": False,
        "commercial_use_review_required": True,
    },
    {
        "license_id": "lic_prov_005",
        "provider_name": "advanced_news_metadata_engine",
        "source_id": "prov_src_news_fixture_provider_news_metadata_dry_run_fixture_source",
        "license_note": "Metadata-only and headline reference; zero article text copy",
        "manual_review_required": False,
        "usage_boundary": "metadata_only_research",
        "redistribution_allowed_placeholder": False,
        "commercial_use_review_required": True,
    },
    {
        "license_id": "lic_prov_006",
        "provider_name": "official_api_provider_placeholder",
        "source_id": "prov_src_official_api_placeholder_official_api_placeholder_source",
        "license_note": "Vendor API terms placeholder; contract review required before live keys",
        "manual_review_required": True,
        "usage_boundary": "contract_review_required",
        "redistribution_allowed_placeholder": False,
        "commercial_use_review_required": True,
    },
    {
        "license_id": "lic_prov_007",
        "provider_name": "licensed_vendor_provider_placeholder",
        "source_id": "prov_src_licensed_provider_placeholder_licensed_provider_placeholder_source",
        "license_note": "Commercial data license placeholder; strict vendor terms apply",
        "manual_review_required": True,
        "usage_boundary": "contract_review_required",
        "redistribution_allowed_placeholder": False,
        "commercial_use_review_required": True,
    },
]


def build_license_provenance_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(LICENSE_PROVENANCE_ITEMS)
    summary = summarize_license_provenance_registry(df)
    return df, summary


def summarize_license_provenance_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_license_records": len(df),
        "providers": df["provider_name"].tolist() if "provider_name" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "zero_unrestricted_redistribution": bool((~df["redistribution_allowed_placeholder"]).all()) if "redistribution_allowed_placeholder" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
