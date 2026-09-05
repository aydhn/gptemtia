import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsTag, build_news_tag_id

def build_default_news_asset_tags(profile: NewsProviderProfile) -> List[NewsTag]:
    tags = [
        NewsTag(
            tag_id=build_news_tag_id("FX", "asset"),
            tag_label="FX",
            tag_domain="asset",
            mapped_entity="Foreign Exchange Market",
            description="News metadata related to currencies and foreign exchange markets.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("COMMODITIES", "asset"),
            tag_label="COMMODITIES",
            tag_domain="asset",
            mapped_entity="Broad Commodity Complex",
            description="News metadata related to raw materials, energy, metals, and agricultural products.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("PRECIOUS_METALS", "asset"),
            tag_label="PRECIOUS_METALS",
            tag_domain="asset",
            mapped_entity="Gold, Silver, Platinum Group",
            description="News metadata covering gold, silver, and precious metals.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("ENERGY", "asset"),
            tag_label="ENERGY",
            tag_domain="asset",
            mapped_entity="Crude Oil, Natural Gas, Refined Products",
            description="News metadata covering crude oil, natural gas, and energy supplies.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("INDUSTRIAL_METALS", "asset"),
            tag_label="INDUSTRIAL_METALS",
            tag_domain="asset",
            mapped_entity="Copper, Aluminum, Zinc, Nickel",
            description="News metadata covering base/industrial metals and infrastructure demand.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("AGRICULTURE", "asset"),
            tag_label="AGRICULTURE",
            tag_domain="asset",
            mapped_entity="Grains, Softs, Livestock",
            description="News metadata covering agricultural commodities, harvests, and supply shocks.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("MACRO", "asset"),
            tag_label="MACRO",
            tag_domain="asset",
            mapped_entity="Macroeconomic Aggregate Factors",
            description="News metadata covering sovereign macro indicators, GDP, inflation, and rate policy.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("RISK_SENTIMENT", "asset"),
            tag_label="RISK_SENTIMENT",
            tag_domain="asset",
            mapped_entity="Market-Wide Risk Appetite",
            description="News metadata reflecting broad risk-on / risk-off environment.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("CROSS_ASSET", "asset"),
            tag_label="CROSS_ASSET",
            tag_domain="asset",
            mapped_entity="Multi-Asset Intermarket Linkages",
            description="News metadata covering systemic cross-asset relationships and correlation shifts.",
            manual_review_required=False
        )
    ]
    return tags

def build_news_asset_tag_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_asset_tags(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_asset_tags(df)
    return df, summary

def summarize_news_asset_tags(df: pd.DataFrame) -> Dict:
    return {
        "total_tags": len(df),
        "tags": df["tag_label"].tolist() if not df.empty else []
    }
