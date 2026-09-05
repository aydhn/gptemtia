import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def match_news_provider_capabilities(
    requested_data_type: str,
    requested_topic: str,
    requested_region: str,
    capability_df: pd.DataFrame,
) -> pd.DataFrame:
    if capability_df.empty:
        return pd.DataFrame()

    matches = []
    for _, row in capability_df.iterrows():
        d_types = row.get("data_types", [])
        topics = row.get("topic_support", [])
        regions = row.get("region_support", [])

        dt_match = requested_data_type in d_types or not requested_data_type
        topic_match = requested_topic in topics or not requested_topic
        region_match = requested_region in regions or "GLOBAL" in regions or not requested_region

        if dt_match and topic_match and region_match:
            matches.append(row.to_dict())

    return pd.DataFrame(matches)

def build_news_provider_capability_matcher_report(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    from advanced_news_metadata.news_provider_capabilities import build_news_provider_capability_registry
    cap_df, _ = build_news_provider_capability_registry(profile)
    matched = match_news_provider_capabilities("news_data_metadata", "central_bank", "US", cap_df)
    summary = summarize_news_provider_capability_matcher(matched)
    return matched, summary

def summarize_news_provider_capability_matcher(df: pd.DataFrame) -> Dict:
    return {
        "matched_capabilities_count": len(df),
        "matched_providers": df["provider_name"].unique().tolist() if not df.empty else []
    }
