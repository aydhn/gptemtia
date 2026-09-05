import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsProviderCapability, build_news_provider_capability_id

def build_default_news_provider_capabilities(profile: NewsProviderProfile) -> List[NewsProviderCapability]:
    caps = [
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_dry_run_fixture_provider", "news_data_metadata"),
            provider_name="news_dry_run_fixture_provider",
            provider_type="provider_dry_run_fixture",
            source_categories=["news_source_official_statement", "news_source_central_bank"],
            data_types=["news_data_metadata"],
            topic_support=["central_bank", "inflation", "growth", "energy", "metals", "fx"],
            region_support=["US", "EU", "TR", "GLOBAL"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_dry_run_fixture_provider", "news_data_item_reference"),
            provider_name="news_dry_run_fixture_provider",
            provider_type="provider_dry_run_fixture",
            source_categories=["news_source_official_statement", "news_source_central_bank"],
            data_types=["news_data_item_reference"],
            topic_support=["central_bank", "inflation", "growth", "energy", "metals", "fx"],
            region_support=["US", "EU", "TR", "GLOBAL"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_manual_file_provider_placeholder", "news_data_metadata"),
            provider_name="news_manual_file_provider_placeholder",
            provider_type="provider_manual_file",
            source_categories=["news_source_manual_research_note"],
            data_types=["news_data_metadata"],
            topic_support=["central_bank", "inflation", "energy", "metals", "fx"],
            region_support=["LOCAL", "GLOBAL"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_manual_file_provider_placeholder", "news_data_item_reference"),
            provider_name="news_manual_file_provider_placeholder",
            provider_type="provider_manual_file",
            source_categories=["news_source_manual_research_note"],
            data_types=["news_data_item_reference"],
            topic_support=["central_bank", "inflation", "energy", "metals", "fx"],
            region_support=["LOCAL", "GLOBAL"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_local_cache_provider_placeholder", "news_data_metadata"),
            provider_name="news_local_cache_provider_placeholder",
            provider_type="provider_local_cache",
            source_categories=["news_source_official_statement", "news_source_central_bank"],
            data_types=["news_data_metadata"],
            topic_support=["central_bank", "inflation", "growth", "energy", "fx"],
            region_support=["US", "EU", "TR", "GLOBAL"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_local_cache_provider_placeholder", "news_data_item_reference"),
            provider_name="news_local_cache_provider_placeholder",
            provider_type="provider_local_cache",
            source_categories=["news_source_official_statement", "news_source_central_bank"],
            data_types=["news_data_item_reference"],
            topic_support=["central_bank", "inflation", "growth", "energy", "fx"],
            region_support=["US", "EU", "TR", "GLOBAL"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_official_api_provider_placeholder", "news_source_official_statements"),
            provider_name="news_official_api_provider_placeholder",
            provider_type="provider_official_api_placeholder",
            source_categories=["news_source_official_statement"],
            data_types=["news_data_metadata"],
            topic_support=["central_bank", "growth"],
            region_support=["US", "EU", "TR"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_placeholder_only",
            warnings=["Offline placeholder; no live network call made."]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_official_api_provider_placeholder", "news_source_government_agency"),
            provider_name="news_official_api_provider_placeholder",
            provider_type="provider_official_api_placeholder",
            source_categories=["news_source_government_agency"],
            data_types=["news_data_metadata"],
            topic_support=["labor", "inflation", "growth"],
            region_support=["US", "EU", "TR"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_placeholder_only",
            warnings=["Offline placeholder; no live network call made."]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_official_api_provider_placeholder", "news_source_exchange_notice"),
            provider_name="news_official_api_provider_placeholder",
            provider_type="provider_official_api_placeholder",
            source_categories=["news_source_exchange_notice"],
            data_types=["news_data_metadata"],
            topic_support=["energy", "metals", "fx"],
            region_support=["US", "EU"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_placeholder_only",
            warnings=["Offline placeholder; no live network call made."]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_licensed_provider_placeholder", "news_data_metadata"),
            provider_name="news_licensed_provider_placeholder",
            provider_type="provider_licensed_placeholder",
            source_categories=["news_source_licensed_newswire_placeholder"],
            data_types=["news_data_metadata"],
            topic_support=["central_bank", "inflation", "energy", "fx", "risk_sentiment"],
            region_support=["GLOBAL"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_placeholder_only",
            warnings=["Licensing compliance verification required before connection."]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_licensed_provider_placeholder", "news_data_item_reference"),
            provider_name="news_licensed_provider_placeholder",
            provider_type="provider_licensed_placeholder",
            source_categories=["news_source_licensed_newswire_placeholder"],
            data_types=["news_data_item_reference"],
            topic_support=["central_bank", "inflation", "energy", "fx", "risk_sentiment"],
            region_support=["GLOBAL"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_placeholder_only",
            warnings=["Licensing compliance verification required before connection."]
        ),
        NewsProviderCapability(
            capability_id=build_news_provider_capability_id("news_public_dataset_placeholder", "news_data_metadata"),
            provider_name="news_public_dataset_provider_placeholder",
            provider_type="provider_public_dataset_placeholder",
            source_categories=["news_source_public_dataset_placeholder"],
            data_types=["news_data_metadata"],
            topic_support=["central_bank", "inflation", "growth", "energy", "metals", "fx"],
            region_support=["GLOBAL"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            metadata_only=True,
            no_scraping_compliant=True,
            copyright_safe=True,
            status_label="news_provider_placeholder_only",
            warnings=["Public dataset terms manual review required."]
        )
    ]
    return caps

def build_news_provider_capability_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_provider_capabilities(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_provider_capabilities(df)
    return df, summary

def summarize_news_provider_capabilities(df: pd.DataFrame) -> Dict:
    return {
        "total_capabilities": len(df),
        "providers": df["provider_name"].unique().tolist() if not df.empty else []
    }
