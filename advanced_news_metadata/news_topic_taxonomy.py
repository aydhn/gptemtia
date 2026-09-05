import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def build_default_news_topic_taxonomy(profile: NewsProviderProfile) -> pd.DataFrame:
    records = [
        {"topic_id": "top_central_bank", "topic_name": "central_bank", "parent_topic": "macro", "description": "Monetary policy decisions, minutes, communications, policy rate adjustments.", "manual_review_required": False},
        {"topic_id": "top_inflation", "topic_name": "inflation", "parent_topic": "macro", "description": "CPI, PPI, core inflation measures, price indices, inflationary expectations.", "manual_review_required": False},
        {"topic_id": "top_growth", "topic_name": "growth", "parent_topic": "macro", "description": "GDP, industrial production, composite output, retail trade activity.", "manual_review_required": False},
        {"topic_id": "top_labor", "topic_name": "labor", "parent_topic": "macro", "description": "Employment, unemployment rate, nonfarm payrolls, job openings, wage growth.", "manual_review_required": False},
        {"topic_id": "top_geopolitics", "topic_name": "geopolitics", "parent_topic": "macro", "description": "Sovereign conflict, international sanctions, trade policy, diplomatic friction.", "manual_review_required": False},
        {"topic_id": "top_energy", "topic_name": "energy", "parent_topic": "commodity", "description": "Crude oil, petroleum products, natural gas storage, pipeline flows, OPEC.", "manual_review_required": False},
        {"topic_id": "top_metals", "topic_name": "metals", "parent_topic": "commodity", "description": "Precious metals (gold, silver) and base metals (copper, aluminum, zinc).", "manual_review_required": False},
        {"topic_id": "top_agriculture", "topic_name": "agriculture", "parent_topic": "commodity", "description": "Grains, oilseeds, soft commodities, agricultural weather shocks.", "manual_review_required": False},
        {"topic_id": "top_fx", "topic_name": "fx", "parent_topic": "fx", "description": "Currency pairs, central bank currency interventions, exchange rate volatility.", "manual_review_required": False},
        {"topic_id": "top_risk_sentiment", "topic_name": "risk_sentiment", "parent_topic": "cross_asset", "description": "Broad market risk appetite, VIX spikes, flight-to-safety, systemic liquidity.", "manual_review_required": False},
        {"topic_id": "top_liquidity", "topic_name": "liquidity", "parent_topic": "macro", "description": "Interbank liquidity, repo facilities, central bank balance sheet contraction/expansion.", "manual_review_required": False},
        {"topic_id": "top_calendar_event", "topic_name": "calendar_event", "parent_topic": "economic_calendar", "description": "Scheduled release announcements and economic calendar linkages.", "manual_review_required": False},
        {"topic_id": "top_official_statement", "topic_name": "official_statement", "parent_topic": "governance", "description": "Formal regulatory and sovereign statements.", "manual_review_required": False},
        {"topic_id": "top_licensed_news_placeholder", "topic_name": "licensed_news_placeholder", "parent_topic": "external_feed", "description": "Contract placeholder for licensed institutional news feeds.", "manual_review_required": True}
    ]
    return pd.DataFrame(records)

def build_news_topic_taxonomy_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_news_topic_taxonomy(profile)
    summary = summarize_news_topic_taxonomy(df)
    return df, summary

def summarize_news_topic_taxonomy(df: pd.DataFrame) -> Dict:
    return {
        "total_topics": len(df),
        "topics": df["topic_name"].tolist() if not df.empty else []
    }
