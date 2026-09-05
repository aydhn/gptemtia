import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsTag, build_news_tag_id

def build_default_news_fx_tags(profile: NewsProviderProfile) -> List[NewsTag]:
    tags = [
        NewsTag(
            tag_id=build_news_tag_id("USD", "fx"),
            tag_label="USD",
            tag_domain="fx",
            mapped_entity="United States Dollar",
            description="Federal Reserve decisions, US Treasury actions, global reserve currency dynamics.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("EUR", "fx"),
            tag_label="EUR",
            tag_domain="fx",
            mapped_entity="Euro",
            description="European Central Bank monetary policy, Eurozone fragmentation risk, sovereign spreads.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("GBP", "fx"),
            tag_label="GBP",
            tag_domain="fx",
            mapped_entity="British Pound Sterling",
            description="Bank of England rate setting, UK fiscal policy, gilt market conditions.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("JPY", "fx"),
            tag_label="JPY",
            tag_domain="fx",
            mapped_entity="Japanese Yen",
            description="Bank of Japan yield curve control, intervention risks, global carry trade funding.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("CHF", "fx"),
            tag_label="CHF",
            tag_domain="fx",
            mapped_entity="Swiss Franc",
            description="Swiss National Bank policy, traditional safe-haven destination flows.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("TRY", "fx"),
            tag_label="TRY",
            tag_domain="fx",
            mapped_entity="Turkish Lira",
            description="CBRT monetary policy, domestic inflation path, reserve build-up, and regulatory changes.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("CNH", "fx"),
            tag_label="CNH",
            tag_domain="fx",
            mapped_entity="Offshore Chinese Yuan",
            description="PBOC fixing guidance, liquidity operations, China trade balances, economic stimulus.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("DXY", "fx"),
            tag_label="DXY",
            tag_domain="fx",
            mapped_entity="US Dollar Index Placeholder",
            description="Trade-weighted dollar valuation basket against major trading partners.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("MAJOR_FX", "fx"),
            tag_label="MAJOR_FX",
            tag_domain="fx",
            mapped_entity="G10 Major Currencies",
            description="Group of Ten developed market currency pairs and rate differentials.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("EM_FX", "fx"),
            tag_label="EM_FX",
            tag_domain="fx",
            mapped_entity="Emerging Market Currencies",
            description="Emerging market risk premia, external debt vulnerability, and portfolio capital flows.",
            manual_review_required=False
        )
    ]
    return tags

def build_news_fx_tag_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_fx_tags(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_fx_tags(df)
    return df, summary

def summarize_news_fx_tags(df: pd.DataFrame) -> Dict:
    return {
        "total_tags": len(df),
        "tags": df["tag_label"].tolist() if not df.empty else []
    }
