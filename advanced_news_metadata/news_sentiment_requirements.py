import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def build_default_news_sentiment_requirements(profile: NewsProviderProfile) -> pd.DataFrame:
    allowed_values_str = "positive_placeholder, negative_placeholder, neutral_placeholder, mixed_placeholder, unknown"
    records = [
        {
            "requirement_id": "sent_req_central_bank",
            "topic_category": "central_bank",
            "sentiment_placeholder_method": "categorical_placeholder_only",
            "allowed_values": allowed_values_str,
            "limitation_note": "Placeholder only; strictly NOT an NLP classification or directional trade signal.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        },
        {
            "requirement_id": "sent_req_inflation",
            "topic_category": "inflation",
            "sentiment_placeholder_method": "categorical_placeholder_only",
            "allowed_values": allowed_values_str,
            "limitation_note": "Does not infer price momentum or market direction; schema placeholder requirement.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        },
        {
            "requirement_id": "sent_req_growth",
            "topic_category": "growth",
            "sentiment_placeholder_method": "categorical_placeholder_only",
            "allowed_values": allowed_values_str,
            "limitation_note": "Macro growth tone placeholder; external LLM or neural sentiment models prohibited.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        },
        {
            "requirement_id": "sent_req_energy",
            "topic_category": "energy",
            "sentiment_placeholder_method": "categorical_placeholder_only",
            "allowed_values": allowed_values_str,
            "limitation_note": "Commodity supply/demand balance placeholder; strictly non-actionable.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        },
        {
            "requirement_id": "sent_req_metals",
            "topic_category": "metals",
            "sentiment_placeholder_method": "categorical_placeholder_only",
            "allowed_values": allowed_values_str,
            "limitation_note": "Metals market placeholder; strictly non-actionable.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        },
        {
            "requirement_id": "sent_req_fx",
            "topic_category": "fx",
            "sentiment_placeholder_method": "categorical_placeholder_only",
            "allowed_values": allowed_values_str,
            "limitation_note": "Currency news placeholder; does not imply buy/sell pressure.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        },
        {
            "requirement_id": "sent_req_risk_sentiment",
            "topic_category": "risk_sentiment",
            "sentiment_placeholder_method": "categorical_placeholder_only",
            "allowed_values": allowed_values_str,
            "limitation_note": "Systemic sentiment placeholder; strictly informational.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        }
    ]
    return pd.DataFrame(records)

def build_news_sentiment_placeholder_requirement_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_news_sentiment_requirements(profile)
    summary = summarize_news_sentiment_requirements(df)
    return df, summary

def summarize_news_sentiment_requirements(df: pd.DataFrame) -> Dict:
    return {
        "total_requirements": len(df),
        "topic_categories": df["topic_category"].tolist() if not df.empty else [],
        "allowed_values": "positive_placeholder, negative_placeholder, neutral_placeholder, mixed_placeholder, unknown"
    }
