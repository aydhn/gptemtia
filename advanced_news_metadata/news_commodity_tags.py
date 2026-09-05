import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsTag, build_news_tag_id

def build_default_news_commodity_tags(profile: NewsProviderProfile) -> List[NewsTag]:
    tags = [
        NewsTag(
            tag_id=build_news_tag_id("GOLD", "commodity"),
            tag_label="GOLD",
            tag_domain="commodity",
            mapped_entity="Gold (XAU)",
            description="Gold spot, futures, central bank bullion purchases, and safe-haven flows.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("SILVER", "commodity"),
            tag_label="SILVER",
            tag_domain="commodity",
            mapped_entity="Silver (XAG)",
            description="Silver spot, industrial demand, solar/green technology use, and dual-nature dynamics.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("CRUDE_OIL", "commodity"),
            tag_label="CRUDE_OIL",
            tag_domain="commodity",
            mapped_entity="Crude Petroleum Complex",
            description="Global petroleum market headlines, refinery utilization, and global supply/demand.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("BRENT", "commodity"),
            tag_label="BRENT",
            tag_domain="commodity",
            mapped_entity="Brent Crude Oil Benchmark",
            description="North Sea Brent crude pricing, OPEC+ production policies, seaborne oil freight.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("WTI", "commodity"),
            tag_label="WTI",
            tag_domain="commodity",
            mapped_entity="West Texas Intermediate Crude Oil",
            description="US domestic crude production, Cushing hub storage levels, and pipeline infrastructure.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("NATURAL_GAS", "commodity"),
            tag_label="NATURAL_GAS",
            tag_domain="commodity",
            mapped_entity="Natural Gas (Henry Hub / TTF)",
            description="Natural gas storage, LNG trade flows, weather forecast impact on heating/cooling demand.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("COPPER", "commodity"),
            tag_label="COPPER",
            tag_domain="commodity",
            mapped_entity="Copper (High Grade / LME)",
            description="Doctor Copper macroeconomic indicator, mining supply disruptions, industrial electrification.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("AGRICULTURE", "commodity"),
            tag_label="AGRICULTURE",
            tag_domain="commodity",
            mapped_entity="Grains & Oilseeds (Corn, Wheat, Soybeans)",
            description="Crop condition reports, WASDE data, weather extremes, export restrictions.",
            manual_review_required=False
        ),
        NewsTag(
            tag_id=build_news_tag_id("ENERGY_INVENTORY", "commodity"),
            tag_label="ENERGY_INVENTORY",
            tag_domain="commodity",
            mapped_entity="Crude & Petroleum Product Inventories",
            description="EIA weekly petroleum status, API estimates, strategic petroleum reserve releases.",
            manual_review_required=False
        )
    ]
    return tags

def build_news_commodity_tag_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_commodity_tags(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_commodity_tags(df)
    return df, summary

def summarize_news_commodity_tags(df: pd.DataFrame) -> Dict:
    return {
        "total_tags": len(df),
        "tags": df["tag_label"].tolist() if not df.empty else []
    }
