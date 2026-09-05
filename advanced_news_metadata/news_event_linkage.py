import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsEventLinkage, build_news_event_linkage_id

def build_default_news_event_linkages(profile: NewsProviderProfile) -> List[NewsEventLinkage]:
    linkages = [
        NewsEventLinkage(
            linkage_id=build_news_event_linkage_id("CENTRAL_BANK", "FOMC_RATE_DECISION"),
            news_topic="central_bank",
            linked_calendar_event="FOMC_RATE_DECISION",
            linked_macro_indicator="FED_POLICY_RATE",
            linked_asset_or_commodity="USD",
            linkage_note="Monetary policy statement metadata mapped to FOMC policy rate decision calendar release.",
            manual_review_required=True
        ),
        NewsEventLinkage(
            linkage_id=build_news_event_linkage_id("INFLATION", "US_CPI_RELEASE"),
            news_topic="inflation",
            linked_calendar_event="US_CPI_RELEASE",
            linked_macro_indicator="US_CPI_YOY",
            linked_asset_or_commodity="USD",
            linkage_note="Consumer inflation headline metadata mapped to US CPI release event and macro time series.",
            manual_review_required=True
        ),
        NewsEventLinkage(
            linkage_id=build_news_event_linkage_id("LABOR", "US_NONFARM_PAYROLLS_RELEASE"),
            news_topic="labor",
            linked_calendar_event="US_NONFARM_PAYROLLS_RELEASE",
            linked_macro_indicator="US_NONFARM_PAYROLLS",
            linked_asset_or_commodity="USD",
            linkage_note="Labor market employment release metadata mapped to US nonfarm payrolls calendar event.",
            manual_review_required=True
        ),
        NewsEventLinkage(
            linkage_id=build_news_event_linkage_id("ENERGY_INVENTORY", "US_EIA_CRUDE_INVENTORY_PLACEHOLDER"),
            news_topic="energy",
            linked_calendar_event="US_EIA_CRUDE_INVENTORY_PLACEHOLDER",
            linked_macro_indicator="WTI_CRUDE",
            linked_asset_or_commodity="CRUDE_OIL",
            linkage_note="Energy inventory change metadata mapped to EIA release and WTI benchmark.",
            manual_review_required=True
        ),
        NewsEventLinkage(
            linkage_id=build_news_event_linkage_id("GOLD", "FOMC_RATE_DECISION"),
            news_topic="metals",
            linked_calendar_event="FOMC_RATE_DECISION",
            linked_macro_indicator="gold_macro_research",
            linked_asset_or_commodity="XAU/USD",
            linkage_note="Bullion safe-haven and real yield metadata mapped to gold macro research profile.",
            manual_review_required=True
        ),
        NewsEventLinkage(
            linkage_id=build_news_event_linkage_id("OIL", "OPEC_MEETING_PLACEHOLDER"),
            news_topic="energy",
            linked_calendar_event="OPEC_MEETING_PLACEHOLDER",
            linked_macro_indicator="oil_macro_research",
            linked_asset_or_commodity="WTI_CRUDE",
            linkage_note="OPEC ministerial meeting metadata mapped to oil macro research profile.",
            manual_review_required=True
        )
    ]
    return linkages

def build_news_event_linkage_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_event_linkages(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_event_linkage(df)
    return df, summary

def summarize_news_event_linkage(df: pd.DataFrame) -> Dict:
    return {
        "total_linkages": len(df),
        "topics": df["news_topic"].unique().tolist() if not df.empty else [],
        "events": df["linked_calendar_event"].unique().tolist() if not df.empty else []
    }
