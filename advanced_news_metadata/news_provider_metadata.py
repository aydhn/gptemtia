import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsProviderMetadata, build_news_provider_metadata_id

def build_default_news_provider_metadata(profile: NewsProviderProfile) -> List[NewsProviderMetadata]:
    providers = [
        NewsProviderMetadata(
            provider_id=build_news_provider_metadata_id("news_dry_run_fixture_provider"),
            provider_name="news_dry_run_fixture_provider",
            provider_type="provider_dry_run_fixture",
            description="Synthetic dry-run news metadata provider for local contract testing.",
            homepage_ref="local://dry_run_fixture",
            license_note="Open-source internal test fixture; no third-party restrictions.",
            credential_policy="no_credentials_required_or_stored",
            no_scraping_policy="strictly_no_scraping_offline_only",
            metadata_only_policy="metadata_only_strict",
            copyright_policy="no_full_text_copied_synthetic_references_only",
            news_coverage_note="Synthetic representative news metadata across G10 and commodities.",
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsProviderMetadata(
            provider_id=build_news_provider_metadata_id("news_manual_file_provider_placeholder"),
            provider_name="news_manual_file_provider_placeholder",
            provider_type="provider_manual_file",
            description="User-supplied offline file ingestion provider for news metadata.",
            homepage_ref="file://local_user_files",
            license_note="User responsibility to respect source copyright; metadata-only ingestion.",
            credential_policy="no_credentials_required_local_filesystem_only",
            no_scraping_policy="strictly_no_scraping_manual_files_only",
            metadata_only_policy="metadata_only_strict",
            copyright_policy="full_article_ingestion_blocked_metadata_fields_only",
            news_coverage_note="Covers whatever valid metadata files are placed in user storage.",
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsProviderMetadata(
            provider_id=build_news_provider_metadata_id("news_local_cache_provider_placeholder"),
            provider_name="news_local_cache_provider_placeholder",
            provider_type="provider_local_cache",
            description="Local filesystem cached news metadata provider adapter.",
            homepage_ref="data/lake/advanced_news_metadata/placeholders/",
            license_note="Cached metadata under local repository governance.",
            credential_policy="no_credentials_required_local_cache_only",
            no_scraping_policy="strictly_no_scraping_offline_cache_only",
            metadata_only_policy="metadata_only_strict",
            copyright_policy="cached_records_contain_only_metadata_no_raw_articles",
            news_coverage_note="Local cached historical metadata for regression testing.",
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsProviderMetadata(
            provider_id=build_news_provider_metadata_id("news_official_api_provider_placeholder"),
            provider_name="news_official_api_provider_placeholder",
            provider_type="provider_official_api_placeholder",
            description="Future adapter placeholder for public sovereign and exchange announcement APIs.",
            homepage_ref="https://example.org/official_api_placeholder",
            license_note="Public data terms apply upon activation; manual review required.",
            credential_policy="credentials_managed_externally_never_printed_or_persisted_in_code",
            no_scraping_policy="strictly_no_scraping_official_endpoints_only",
            metadata_only_policy="metadata_only_strict",
            copyright_policy="only_official_headline_metadata_ingested",
            news_coverage_note="Official central bank, treasury, and exchange communiques.",
            status_label="news_provider_placeholder_only",
            warnings=["Offline adapter placeholder; no live network calls enabled."]
        ),
        NewsProviderMetadata(
            provider_id=build_news_provider_metadata_id("news_licensed_provider_placeholder"),
            provider_name="news_licensed_provider_placeholder",
            provider_type="provider_licensed_placeholder",
            description="Future institutional adapter placeholder for licensed financial newswires.",
            homepage_ref="https://example.com/licensed_newswire_placeholder",
            license_note="Requires commercial enterprise subscription and legal compliance review.",
            credential_policy="strict_secrets_hygiene_no_credential_stored_or_printed",
            no_scraping_policy="strictly_no_scraping_licensed_api_feed_only",
            metadata_only_policy="metadata_only_strict",
            copyright_policy="strictly_metadata_only_no_full_article_copying",
            news_coverage_note="Global financial and economic news metadata coverage.",
            status_label="news_provider_placeholder_only",
            warnings=["Commercial licensing and manual review required prior to live use."]
        ),
        NewsProviderMetadata(
            provider_id=build_news_provider_metadata_id("news_public_dataset_provider_placeholder"),
            provider_name="news_public_dataset_provider_placeholder",
            provider_type="provider_public_dataset_placeholder",
            description="Future adapter placeholder for academic and open research news headline datasets.",
            homepage_ref="https://example.org/public_news_dataset_placeholder",
            license_note="Academic/research terms; compliance verification required.",
            credential_policy="no_credentials_required_for_public_datasets",
            no_scraping_policy="strictly_no_scraping_dataset_archive_only",
            metadata_only_policy="metadata_only_strict",
            copyright_policy="open_metadata_attributes_only",
            news_coverage_note="Historical benchmark news metadata for backtest regimes.",
            status_label="news_provider_placeholder_only",
            warnings=["Research terms of use manual review required."]
        )
    ]
    return providers

def validate_news_provider_metadata_item(item: NewsProviderMetadata, profile: NewsProviderProfile) -> Dict:
    errors = []
    if not item.provider_id:
        errors.append("provider_id must not be empty")
    if not item.provider_name:
        errors.append("provider_name must not be empty")
    if item.no_scraping_policy == "":
        errors.append("no_scraping_policy must be declared")
    if item.metadata_only_policy == "":
        errors.append("metadata_only_policy must be declared")
    return {"valid": len(errors) == 0, "errors": errors}

def build_news_provider_metadata_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_provider_metadata(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_provider_metadata(df)
    return df, summary

def summarize_news_provider_metadata(df: pd.DataFrame) -> Dict:
    return {
        "total_providers": len(df),
        "providers": df["provider_name"].tolist() if not df.empty else []
    }
