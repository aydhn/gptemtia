import pandas as pd
from typing import Tuple, Dict, List, Optional
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_interfaces import BaseNewsMetadataProvider
from advanced_news_metadata.news_provider_models import NewsProviderCapability

class NewsMetadataProviderRegistry:
    def __init__(self):
        self._providers: Dict[str, BaseNewsMetadataProvider] = {}

    def register(self, provider: BaseNewsMetadataProvider) -> None:
        self._providers[provider.provider_name] = provider

    def list_providers(self) -> List[str]:
        return list(self._providers.keys())

    def get_provider(self, provider_name: str) -> Optional[BaseNewsMetadataProvider]:
        return self._providers.get(provider_name)

    def list_capabilities(self) -> List[NewsProviderCapability]:
        all_caps = []
        for p in self._providers.values():
            try:
                all_caps.extend(p.capabilities())
            except Exception:
                pass
        return all_caps

    def to_dataframe(self) -> pd.DataFrame:
        records = []
        for name, p in self._providers.items():
            try:
                meta = p.metadata()
                records.append({
                    "provider_name": name,
                    "provider_type": getattr(p, "provider_type", "unknown"),
                    "status_label": getattr(meta, "status_label", "news_provider_ready"),
                    "no_scraping_policy": getattr(meta, "no_scraping_policy", "strictly_no_scraping"),
                    "metadata_only_policy": getattr(meta, "metadata_only_policy", "metadata_only_strict")
                })
            except Exception:
                records.append({
                    "provider_name": name,
                    "provider_type": getattr(p, "provider_type", "unknown"),
                    "status_label": "news_provider_ready",
                    "no_scraping_policy": "strictly_no_scraping",
                    "metadata_only_policy": "metadata_only_strict"
                })
        return pd.DataFrame(records)

def build_default_news_provider_registry(profile: NewsProviderProfile) -> NewsMetadataProviderRegistry:
    reg = NewsMetadataProviderRegistry()
    from advanced_news_metadata.news_dry_run_fixture import NewsDryRunFixtureProvider
    from advanced_news_metadata.news_manual_file_provider import NewsManualFileProviderPlaceholder
    from advanced_news_metadata.news_local_cache_provider import NewsLocalCacheProviderPlaceholder
    from advanced_news_metadata.news_official_api_provider import NewsOfficialApiProviderPlaceholder
    from advanced_news_metadata.news_licensed_provider import NewsLicensedProviderPlaceholder
    from advanced_news_metadata.news_public_dataset_provider import NewsPublicDatasetProviderPlaceholder

    reg.register(NewsDryRunFixtureProvider())
    reg.register(NewsManualFileProviderPlaceholder())
    reg.register(NewsLocalCacheProviderPlaceholder())
    reg.register(NewsOfficialApiProviderPlaceholder())
    reg.register(NewsLicensedProviderPlaceholder())
    reg.register(NewsPublicDatasetProviderPlaceholder())
    return reg

def build_news_provider_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    reg = build_default_news_provider_registry(profile)
    df = reg.to_dataframe()
    summary = summarize_news_provider_registry(df)
    return df, summary

def summarize_news_provider_registry(df: pd.DataFrame) -> Dict:
    return {
        "total_providers": len(df),
        "providers": df["provider_name"].tolist() if not df.empty else []
    }
