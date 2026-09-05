import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def build_default_news_freshness_requirements(profile: NewsProviderProfile) -> pd.DataFrame:
    records = [
        {
            "requirement_id": "fresh_req_breaking",
            "timestamp_field": "timestamp",
            "freshness_window_placeholder": "1h",
            "stale_threshold_placeholder": "24h",
            "timezone_policy": "UTC_iso8601_strict",
            "future_phase_owner": "Phase 112 Data Quality Engine",
            "manual_review_required": False
        },
        {
            "requirement_id": "fresh_req_daily_summary",
            "timestamp_field": "timestamp",
            "freshness_window_placeholder": "24h",
            "stale_threshold_placeholder": "72h",
            "timezone_policy": "UTC_iso8601_strict",
            "future_phase_owner": "Phase 112 Data Quality Engine",
            "manual_review_required": False
        },
        {
            "requirement_id": "fresh_req_weekly_macro",
            "timestamp_field": "timestamp",
            "freshness_window_placeholder": "7d",
            "stale_threshold_placeholder": "30d",
            "timezone_policy": "UTC_iso8601_strict",
            "future_phase_owner": "Phase 112 Data Quality Engine",
            "manual_review_required": False
        }
    ]
    return pd.DataFrame(records)

def build_news_freshness_staleness_requirement_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_news_freshness_requirements(profile)
    summary = summarize_news_freshness_requirements(df)
    return df, summary

def summarize_news_freshness_requirements(df: pd.DataFrame) -> Dict:
    return {
        "total_requirements": len(df),
        "windows": df["freshness_window_placeholder"].tolist() if not df.empty else []
    }
