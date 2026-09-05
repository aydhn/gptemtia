import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_interfaces import BaseNewsMetadataProvider
from advanced_news_metadata.news_provider_response import create_news_provider_response
from advanced_news_metadata.news_provider_models import (
    NewsProviderMetadata,
    NewsProviderCapability,
    NewsProviderRequest,
    NewsProviderResponse
)

class NewsManualFileProviderPlaceholder(BaseNewsMetadataProvider):
    provider_name = "news_manual_file_provider_placeholder"
    provider_type = "provider_manual_file"

    def metadata(self) -> NewsProviderMetadata:
        from advanced_news_metadata.news_provider_metadata import build_default_news_provider_metadata
        for m in build_default_news_provider_metadata(NewsProviderProfile("temp", "")):
            if m.provider_name == self.provider_name:
                return m
        return NewsProviderMetadata(
            self.provider_name, self.provider_name, self.provider_type,
            "Manual file news metadata provider", "file://local", "user",
            "none", "strictly_no_scraping", "metadata_only_strict",
            "no_full_text", "local", "news_provider_ready", []
        )

    def capabilities(self) -> List[NewsProviderCapability]:
        from advanced_news_metadata.news_provider_capabilities import build_default_news_provider_capabilities
        return [c for c in build_default_news_provider_capabilities(NewsProviderProfile("temp", "")) if c.provider_name == self.provider_name]

    def validate_request(self, request: NewsProviderRequest) -> Dict:
        return {"valid": True, "errors": []}

    def fetch_news_metadata(self, request: NewsProviderRequest) -> NewsProviderResponse:
        return create_news_provider_response(
            request_id=request.request_id,
            provider_name=self.provider_name,
            data_type=request.data_type,
            status_label="news_provider_ready",
            output_ref="file://data/lake/advanced_news_metadata/placeholders/manual_news.csv",
            row_count=0,
            schema_ref="news_metadata_schema_contract",
            warnings=["Manual file placeholder; no filesystem modification or full article ingestion."],
            manual_review_required=True
        )

    def health_check(self) -> Dict:
        return {"status": "healthy", "mode": "manual-file-placeholder"}

def build_news_manual_file_provider_placeholder(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    provider = NewsManualFileProviderPlaceholder()
    from advanced_news_metadata.news_provider_request import create_news_provider_request
    req = create_news_provider_request(provider.provider_name, "news_data_metadata", region="LOCAL")
    res = provider.fetch_news_metadata(req)
    df = pd.DataFrame([vars(res)])
    summary = {"provider_name": provider.provider_name, "status": "ready"}
    return df, summary
