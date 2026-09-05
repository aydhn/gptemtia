import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def build_default_news_deduplication_requirements(profile: NewsProviderProfile) -> pd.DataFrame:
    records = [
        {
            "requirement_id": "dedup_req_exact_hash",
            "duplicate_key_placeholder": "item_id_or_content_hash",
            "title_similarity_placeholder": "exact_match_threshold_1_0",
            "source_priority_placeholder": "official_statement > licensed_newswire > manual_note",
            "timestamp_window_placeholder": "24h",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": False
        },
        {
            "requirement_id": "dedup_req_topic_cluster",
            "duplicate_key_placeholder": "topic_event_date_key",
            "title_similarity_placeholder": "token_jaccard_placeholder_0_8",
            "source_priority_placeholder": "primary_regulatory_source_first",
            "timestamp_window_placeholder": "6h",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        }
    ]
    return pd.DataFrame(records)

def build_news_deduplication_requirement_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_news_deduplication_requirements(profile)
    summary = summarize_news_deduplication_requirements(df)
    return df, summary

def summarize_news_deduplication_requirements(df: pd.DataFrame) -> Dict:
    return {
        "total_requirements": len(df),
        "keys": df["duplicate_key_placeholder"].tolist() if not df.empty else []
    }
