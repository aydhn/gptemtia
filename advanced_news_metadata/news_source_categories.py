import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsSourceCategory, build_news_source_category_id

def build_default_news_source_categories(profile: NewsProviderProfile) -> List[NewsSourceCategory]:
    categories = [
        NewsSourceCategory(
            category_id=build_news_source_category_id("news_source_official_statement"),
            category_label="news_source_official_statement",
            category_name="Official Statement",
            description="Official announcements and communiques by sovereign or regulatory authorities.",
            example_sources=["CENTRAL_BANK_STATEMENTS_PLACEHOLDER", "GOVERNMENT_AGENCY_RELEASES_PLACEHOLDER"],
            warnings=[]
        ),
        NewsSourceCategory(
            category_id=build_news_source_category_id("news_source_central_bank"),
            category_label="news_source_central_bank",
            category_name="Central Bank",
            description="Policy decisions, interest rate announcements, and monetary policy statement metadata.",
            example_sources=["FED_RELEASES_PLACEHOLDER", "ECB_COMMUNIQUES_PLACEHOLDER", "TCMB_POLICY_PLACEHOLDER"],
            warnings=[]
        ),
        NewsSourceCategory(
            category_id=build_news_source_category_id("news_source_government_agency"),
            category_label="news_source_government_agency",
            category_name="Government Agency",
            description="Government departments (Treasury, Commerce, Labor) official statistical releases.",
            example_sources=["BLS_RELEASES_PLACEHOLDER", "CENSUS_RELEASES_PLACEHOLDER"],
            warnings=[]
        ),
        NewsSourceCategory(
            category_id=build_news_source_category_id("news_source_exchange_notice"),
            category_label="news_source_exchange_notice",
            category_name="Exchange Notice",
            description="Market operation notices, trading hour amendments, margin requirement changes.",
            example_sources=["CME_NOTICES_PLACEHOLDER", "ICE_NOTICES_PLACEHOLDER"],
            warnings=[]
        ),
        NewsSourceCategory(
            category_id=build_news_source_category_id("news_source_energy_agency"),
            category_label="news_source_energy_agency",
            category_name="Energy Agency",
            description="Energy information administration, IEA, and OPEC official report metadata.",
            example_sources=["EIA_NOTICES_PLACEHOLDER", "IEA_RELEASES_PLACEHOLDER"],
            warnings=[]
        ),
        NewsSourceCategory(
            category_id=build_news_source_category_id("news_source_general_financial_news_placeholder"),
            category_label="news_source_general_financial_news_placeholder",
            category_name="General Financial News Placeholder",
            description="General public financial market news metadata contract placeholder.",
            example_sources=["FINANCIAL_PORTAL_METADATA_PLACEHOLDER"],
            warnings=["No web scraping; metadata contracts only."]
        ),
        NewsSourceCategory(
            category_id=build_news_source_category_id("news_source_licensed_newswire_placeholder"),
            category_label="news_source_licensed_newswire_placeholder",
            category_name="Licensed Newswire Placeholder",
            description="Enterprise financial newswires requiring subscription licenses.",
            example_sources=["LICENSED_NEWSWIRE_FEED_PLACEHOLDER"],
            warnings=["No credential printing or automatic connection."]
        ),
        NewsSourceCategory(
            category_id=build_news_source_category_id("news_source_public_dataset_placeholder"),
            category_label="news_source_public_dataset_placeholder",
            category_name="Public Dataset Placeholder",
            description="Open-access research datasets containing historical news headlines and tags.",
            example_sources=["RESEARCH_NEWS_ARCHIVE_PLACEHOLDER"],
            warnings=["Manual review required for licensing boundaries."]
        ),
        NewsSourceCategory(
            category_id=build_news_source_category_id("news_source_manual_research_note"),
            category_label="news_source_manual_research_note",
            category_name="Manual Research Note",
            description="User-curated offline research documents and news metadata logs.",
            example_sources=["OFFLINE_RESEARCH_LEDGER"],
            warnings=[]
        ),
        NewsSourceCategory(
            category_id=build_news_source_category_id("news_source_local_analyst_note"),
            category_label="news_source_manual_research_note",
            category_name="Local Analyst Note",
            description="Internal analyst event logs and macro commentary metadata.",
            example_sources=["LOCAL_ANALYST_DIARY"],
            warnings=[]
        )
    ]
    return categories

def build_news_source_category_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_source_categories(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_source_categories(df)
    return df, summary

def summarize_news_source_categories(df: pd.DataFrame) -> Dict:
    return {
        "total_categories": len(df),
        "categories": df["category_name"].tolist() if not df.empty else []
    }
