import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import (
    NewsProviderMetadata,
    NewsProviderCapability,
    NewsProviderRequest,
    NewsProviderResponse
)

class BaseNewsMetadataProvider:
    provider_name: str = "base_news_provider"
    provider_type: str = "base"

    def metadata(self) -> NewsProviderMetadata:
        raise NotImplementedError

    def capabilities(self) -> List[NewsProviderCapability]:
        raise NotImplementedError

    def validate_request(self, request: NewsProviderRequest) -> Dict:
        raise NotImplementedError

    def fetch_news_metadata(self, request: NewsProviderRequest) -> NewsProviderResponse:
        raise NotImplementedError

    def health_check(self) -> Dict:
        raise NotImplementedError

def build_news_provider_interface_contract(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    contract_methods = [
        {"method_name": "metadata", "return_type": "NewsProviderMetadata", "description": "Returns descriptive provider catalog metadata without credentials."},
        {"method_name": "capabilities", "return_type": "list[NewsProviderCapability]", "description": "Returns supported data types, topics, regions, and compliance flags."},
        {"method_name": "validate_request", "return_type": "dict", "description": "Validates request parameters against no-scraping and metadata-only boundaries."},
        {"method_name": "fetch_news_metadata", "return_type": "NewsProviderResponse", "description": "Retrieves news metadata or returns synthetic/cached records offline."},
        {"method_name": "health_check", "return_type": "dict", "description": "Evaluates local adapter operational readiness."}
    ]
    df = pd.DataFrame(contract_methods)
    summary = summarize_news_provider_interface_contract(df)
    return df, summary

def summarize_news_provider_interface_contract(df: pd.DataFrame) -> Dict:
    return {
        "total_methods": len(df),
        "methods": df["method_name"].tolist() if not df.empty else []
    }
