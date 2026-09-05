import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def build_default_news_impact_requirements(profile: NewsProviderProfile) -> pd.DataFrame:
    records = [
        {
            "requirement_id": "imp_req_central_bank",
            "topic_category": "central_bank",
            "impact_placeholder_method": "qualitative_impact_scale_placeholder",
            "asset_relevance_note": "Relevance to interest rates, sovereign yields, and currency valuation.",
            "macro_relevance_note": "Direct transmission to monetary policy stance.",
            "limitation_note": "Placeholder only; strictly NOT a price impact forecast or trading instruction.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        },
        {
            "requirement_id": "imp_req_inflation",
            "topic_category": "inflation",
            "impact_placeholder_method": "qualitative_impact_scale_placeholder",
            "asset_relevance_note": "Relevance to real yields, gold, and purchasing power.",
            "macro_relevance_note": "Guides central bank policy reaction function.",
            "limitation_note": "Placeholder only; no price directional projection.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        },
        {
            "requirement_id": "imp_req_energy",
            "topic_category": "energy",
            "impact_placeholder_method": "qualitative_impact_scale_placeholder",
            "asset_relevance_note": "Relevance to WTI, Brent, and natural gas benchmark contracts.",
            "macro_relevance_note": "Headline inflation component and terms of trade impact.",
            "limitation_note": "Placeholder only; does not predict commodity price moves.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        },
        {
            "requirement_id": "imp_req_fx",
            "topic_category": "fx",
            "impact_placeholder_method": "qualitative_impact_scale_placeholder",
            "asset_relevance_note": "Relevance to bilateral exchange rates and crosses.",
            "macro_relevance_note": "Imported inflation and cross-border capital flows.",
            "limitation_note": "Placeholder only; no currency directional claim.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        },
        {
            "requirement_id": "imp_req_risk_sentiment",
            "topic_category": "risk_sentiment",
            "impact_placeholder_method": "qualitative_impact_scale_placeholder",
            "asset_relevance_note": "Systemic cross-asset volatility and risk premium shifts.",
            "macro_relevance_note": "Broad financial conditions index impact.",
            "limitation_note": "Informational classification placeholder.",
            "future_phase_owner": "Phase 112 Data Quality Engine / Phase 113 Normalization",
            "manual_review_required": True
        }
    ]
    return pd.DataFrame(records)

def build_news_impact_placeholder_requirement_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_news_impact_requirements(profile)
    summary = summarize_news_impact_requirements(df)
    return df, summary

def summarize_news_impact_requirements(df: pd.DataFrame) -> Dict:
    return {
        "total_requirements": len(df),
        "topic_categories": df["topic_category"].tolist() if not df.empty else []
    }
