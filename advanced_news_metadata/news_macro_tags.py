import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsTag, build_news_tag_id

def build_default_news_macro_tags(profile: NewsProviderProfile) -> List[NewsTag]:
    tags = [
        NewsTag(
            tag_id=build_news_tag_id("CENTRAL_BANK", "macro"),
            tag_label="CENTRAL_BANK",
            tag_domain="macro",
            mapped_entity="Monetary Policy & Rates",
            description="Central bank rate decisions, statements, minutes, and forward guidance.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("INFLATION", "macro"),
            tag_label="INFLATION",
            tag_domain="macro",
            mapped_entity="CPI, PPI, PCE Price Indices",
            description="Consumer and producer inflation prints, wage growth, and price dynamics.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("GROWTH", "macro"),
            tag_label="GROWTH",
            tag_domain="macro",
            mapped_entity="GDP & Economic Activity",
            description="Gross domestic product, industrial production, and composite economic activity.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("LABOR", "macro"),
            tag_label="LABOR",
            tag_domain="macro",
            mapped_entity="Employment & Labor Market",
            description="Payroll employment, unemployment rate, claims, and labor tightness.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("YIELD_CURVE", "macro"),
            tag_label="YIELD_CURVE",
            tag_domain="macro",
            mapped_entity="Sovereign Bond Yields & Term Structure",
            description="Sovereign curve steepening/inversion, benchmark 2Y/10Y yield developments.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("LIQUIDITY", "macro"),
            tag_label="LIQUIDITY",
            tag_domain="macro",
            mapped_entity="Financial Conditions & Balance Sheet Policy",
            description="Central bank asset purchases/QT, bank reserves, money supply, interbank funding.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("RISK_SENTIMENT", "macro"),
            tag_label="RISK_SENTIMENT",
            tag_domain="macro",
            mapped_entity="Systemic Risk Appetite",
            description="Macro risk aversion, volatility spikes, flight-to-safety episodes.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("GEOPOLITICS", "macro"),
            tag_label="GEOPOLITICS",
            tag_domain="macro",
            mapped_entity="Geopolitical Conflicts & Trade Friction",
            description="International trade sanctions, diplomatic tensions, supply disruptions.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("TRADE_BALANCE", "macro"),
            tag_label="TRADE_BALANCE",
            tag_domain="macro",
            mapped_entity="Current Account & Trade Data",
            description="Export/import balances, current account deficits/surpluses, terms of trade.",
            manual_review_required=False
        )
    ]
    return tags

def build_news_macro_tag_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_macro_tags(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_macro_tags(df)
    return df, summary

def summarize_news_macro_tags(df: pd.DataFrame) -> Dict:
    return {
        "total_tags": len(df),
        "tags": df["tag_label"].tolist() if not df.empty else []
    }
