import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsProviderError, build_news_provider_error_id, to_dict

def create_news_provider_error(
    provider_name: str,
    error_type: str,
    message: str,
    retryable: bool = False,
    blocked_by_safety: bool = False,
    recommendation: str = ""
) -> NewsProviderError:
    err_id = build_news_provider_error_id(provider_name, error_type)
    return NewsProviderError(
        error_id=err_id,
        provider_name=provider_name,
        error_type=error_type,
        message=message,
        retryable=retryable,
        blocked_by_safety=blocked_by_safety,
        recommendation=recommendation
    )

def news_provider_error_to_dict(error: NewsProviderError) -> Dict:
    return to_dict(error)

def build_news_provider_error_schema(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    error_types = [
        {"error_type": "news_provider_not_found", "description": "Requested news provider is not registered.", "retryable": False, "blocked_by_safety": False},
        {"error_type": "unsupported_news_topic", "description": "Requested news topic is not supported.", "retryable": False, "blocked_by_safety": False},
        {"error_type": "unsupported_news_data_type", "description": "Data type is not supported by the provider.", "retryable": False, "blocked_by_safety": False},
        {"error_type": "unsupported_region", "description": "Region is outside provider coverage.", "retryable": False, "blocked_by_safety": False},
        {"error_type": "unsupported_time_range", "description": "Specified time range is invalid or out of bounds.", "retryable": False, "blocked_by_safety": False},
        {"error_type": "blocked_by_no_scraping_boundary", "description": "Operation attempted web or HTML scraping, which is strictly prohibited.", "retryable": False, "blocked_by_safety": True},
        {"error_type": "blocked_by_copyright_boundary", "description": "Operation attempted full-text article copying, violating copyright boundaries.", "retryable": False, "blocked_by_safety": True},
        {"error_type": "full_article_download_blocked", "description": "Full article download requested but disabled.", "retryable": False, "blocked_by_safety": True},
        {"error_type": "credential_not_available", "description": "Provider credentials are not stored or available.", "retryable": False, "blocked_by_safety": False},
        {"error_type": "network_disabled", "description": "Live network access disabled; offline dry-run only.", "retryable": False, "blocked_by_safety": False},
        {"error_type": "schema_mismatch", "description": "Input or output schema does not conform to contract.", "retryable": False, "blocked_by_safety": False},
        {"error_type": "sentiment_not_available", "description": "Live NLP sentiment model is disabled and not available as a signal.", "retryable": False, "blocked_by_safety": False},
        {"error_type": "impact_placeholder_not_available", "description": "Impact placeholder calculation cannot be generated.", "retryable": False, "blocked_by_safety": False},
        {"error_type": "manual_review_required", "description": "Provider response requires manual compliance review.", "retryable": False, "blocked_by_safety": False}
    ]
    df = pd.DataFrame(error_types)
    summary = summarize_news_provider_errors(df)
    return df, summary

def summarize_news_provider_errors(df: pd.DataFrame) -> Dict:
    return {
        "total_error_types": len(df),
        "safety_blocked_types": df[df["blocked_by_safety"]]["error_type"].tolist() if not df.empty else []
    }
