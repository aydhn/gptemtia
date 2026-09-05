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

class NewsDryRunFixtureProvider(BaseNewsMetadataProvider):
    provider_name = "news_dry_run_fixture_provider"
    provider_type = "provider_dry_run_fixture"

    def metadata(self) -> NewsProviderMetadata:
        from advanced_news_metadata.news_provider_metadata import build_default_news_provider_metadata
        for m in build_default_news_provider_metadata(NewsProviderProfile("temp", "")):
            if m.provider_name == self.provider_name:
                return m
        return NewsProviderMetadata(
            self.provider_name, self.provider_name, self.provider_type,
            "Dry-run news metadata fixture provider", "local://dry_run", "none",
            "none", "strictly_no_scraping", "metadata_only_strict",
            "no_full_text", "global coverage", "news_provider_ready", []
        )

    def capabilities(self) -> List[NewsProviderCapability]:
        from advanced_news_metadata.news_provider_capabilities import build_default_news_provider_capabilities
        caps = []
        for c in build_default_news_provider_capabilities(NewsProviderProfile("temp", "")):
            if c.provider_name == self.provider_name:
                caps.append(c)
        return caps

    def validate_request(self, request: NewsProviderRequest) -> Dict:
        from advanced_news_metadata.news_provider_request import validate_news_provider_request
        return validate_news_provider_request(request, NewsProviderProfile("temp", ""))

    def fetch_news_metadata(self, request: NewsProviderRequest) -> NewsProviderResponse:
        region = request.region or "ALL"
        data_type = request.data_type or "news_data_metadata"
        output_uri = f"dry_run://news_metadata_fixture/{data_type}/{region}"
        return create_news_provider_response(
            request_id=request.request_id,
            provider_name=self.provider_name,
            data_type=data_type,
            status_label="news_provider_ready",
            output_ref=output_uri,
            row_count=5,
            schema_ref="news_metadata_schema_contract",
            warnings=["Synthetic dry-run metadata fixture; not a live signal or market direction claim."],
            manual_review_required=True
        )

    def health_check(self) -> Dict:
        return {"status": "healthy", "mode": "local-only dry-run", "scraping_enabled": False}

def build_news_dry_run_fixture_report(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    return run_news_dry_run_examples(profile)

def run_news_dry_run_examples(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    provider = NewsDryRunFixtureProvider()
    from advanced_news_metadata.news_provider_request import create_news_provider_request
    
    req1 = create_news_provider_request(
        provider.provider_name,
        "news_data_metadata",
        topics=["central_bank", "inflation"],
        asset_tags=["FX", "COMMODITIES"],
        region="US"
    )
    res1 = provider.fetch_news_metadata(req1)
    
    req2 = create_news_provider_request(
        provider.provider_name,
        "news_data_item_reference",
        topics=["energy"],
        asset_tags=["ENERGY"],
        region="GLOBAL"
    )
    res2 = provider.fetch_news_metadata(req2)
    
    df = pd.DataFrame([vars(res1), vars(res2)])
    summary = summarize_news_dry_run_fixture(df)
    return df, summary

def summarize_news_dry_run_fixture(df: pd.DataFrame) -> Dict:
    return {
        "total_requests": len(df),
        "providers": df["provider_name"].unique().tolist() if not df.empty else []
    }
