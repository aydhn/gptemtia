import pandas as pd
from typing import Tuple, Dict, Optional
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_interfaces import BaseNewsMetadataProvider
from advanced_news_metadata.news_provider_registry import NewsMetadataProviderRegistry
from advanced_news_metadata.news_provider_models import NewsProviderRequest

def resolve_news_provider_for_request(
    request: NewsProviderRequest,
    registry: NewsMetadataProviderRegistry,
    profile: NewsProviderProfile,
) -> Optional[BaseNewsMetadataProvider]:
    if request.provider_name:
        provider = registry.get_provider(request.provider_name)
        if provider:
            return provider

    if request.dry_run:
        return registry.get_provider("news_dry_run_fixture_provider")
    
    return registry.get_provider("news_local_cache_provider_placeholder")

def build_news_provider_resolver_map(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    records = [
        {"data_type": "news_data_metadata", "default_provider": "news_dry_run_fixture_provider", "fallback_provider": "news_local_cache_provider_placeholder"},
        {"data_type": "news_data_item_reference", "default_provider": "news_dry_run_fixture_provider", "fallback_provider": "news_manual_file_provider_placeholder"},
        {"data_type": "news_data_source_metadata", "default_provider": "news_dry_run_fixture_provider", "fallback_provider": "news_local_cache_provider_placeholder"}
    ]
    df = pd.DataFrame(records)
    summary = summarize_news_provider_resolver_map(df)
    return df, summary

def summarize_news_provider_resolver_map(df: pd.DataFrame) -> Dict:
    return {
        "total_mappings": len(df),
        "data_types": df["data_type"].tolist() if not df.empty else []
    }
