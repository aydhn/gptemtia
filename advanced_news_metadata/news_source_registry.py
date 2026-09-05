import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsSource, build_news_source_id

def build_default_news_sources(profile: NewsProviderProfile) -> List[NewsSource]:
    sources = [
        NewsSource(
            source_id=build_news_source_id("CENTRAL_BANK_STATEMENTS_PLACEHOLDER"),
            source_name="CENTRAL_BANK_STATEMENTS_PLACEHOLDER",
            source_category="news_source_central_bank",
            region="GLOBAL",
            coverage_note="Monetary policy releases, rate decisions, press conference statement metadata.",
            license_note="Public official statements; metadata-only access.",
            metadata_only_policy="metadata_only_strict",
            no_scraping_policy="no_scraping_strict",
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsSource(
            source_id=build_news_source_id("GOVERNMENT_AGENCY_RELEASES_PLACEHOLDER"),
            source_name="GOVERNMENT_AGENCY_RELEASES_PLACEHOLDER",
            source_category="news_source_government_agency",
            region="GLOBAL",
            coverage_note="Labor, trade, finance ministry official announcement metadata.",
            license_note="Public government releases; metadata-only access.",
            metadata_only_policy="metadata_only_strict",
            no_scraping_policy="no_scraping_strict",
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsSource(
            source_id=build_news_source_id("ENERGY_AGENCY_NOTICES_PLACEHOLDER"),
            source_name="ENERGY_AGENCY_NOTICES_PLACEHOLDER",
            source_category="news_source_energy_agency",
            region="GLOBAL",
            coverage_note="Energy market updates, inventory report announcement metadata.",
            license_note="Agency official reports; metadata-only access.",
            metadata_only_policy="metadata_only_strict",
            no_scraping_policy="no_scraping_strict",
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsSource(
            source_id=build_news_source_id("EXCHANGE_NOTICE_PLACEHOLDER"),
            source_name="EXCHANGE_NOTICE_PLACEHOLDER",
            source_category="news_source_exchange_notice",
            region="GLOBAL",
            coverage_note="Exchange circuit breakers, margin adjustments, contract specification notices.",
            license_note="Exchange disclosures; metadata-only access.",
            metadata_only_policy="metadata_only_strict",
            no_scraping_policy="no_scraping_strict",
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsSource(
            source_id=build_news_source_id("LICENSED_NEWSWIRE_PLACEHOLDER"),
            source_name="LICENSED_NEWSWIRE_PLACEHOLDER",
            source_category="news_source_licensed_newswire_placeholder",
            region="GLOBAL",
            coverage_note="Licensed professional newswire feed metadata placeholder.",
            license_note="Requires commercial license; no credential requested or outputted.",
            metadata_only_policy="metadata_only_strict",
            no_scraping_policy="no_scraping_strict",
            status_label="news_provider_placeholder_only",
            warnings=["Requires manual licensing review and offline configuration."]
        ),
        NewsSource(
            source_id=build_news_source_id("PUBLIC_DATASET_PLACEHOLDER"),
            source_name="PUBLIC_DATASET_PLACEHOLDER",
            source_category="news_source_public_dataset_placeholder",
            region="GLOBAL",
            coverage_note="Research benchmark news metadata public dataset placeholder.",
            license_note="Public research datasets; compliance and license manual review required.",
            metadata_only_policy="metadata_only_strict",
            no_scraping_policy="no_scraping_strict",
            status_label="news_provider_placeholder_only",
            warnings=["Public terms of use require manual verification."]
        ),
        NewsSource(
            source_id=build_news_source_id("MANUAL_RESEARCH_NOTE_PLACEHOLDER"),
            source_name="MANUAL_RESEARCH_NOTE_PLACEHOLDER",
            source_category="news_source_manual_research_note",
            region="LOCAL",
            coverage_note="User-supplied offline research metadata files.",
            license_note="Local user-provided data; strictly local-only.",
            metadata_only_policy="metadata_only_strict",
            no_scraping_policy="no_scraping_strict",
            status_label="news_provider_ready",
            warnings=[]
        ),
        NewsSource(
            source_id=build_news_source_id("LOCAL_ANALYST_NOTE_PLACEHOLDER"),
            source_name="LOCAL_ANALYST_NOTE_PLACEHOLDER",
            source_category="news_source_manual_research_note",
            region="LOCAL",
            coverage_note="Local analyst research tag mapping and metadata notes.",
            license_note="Proprietary local offline research notes.",
            metadata_only_policy="metadata_only_strict",
            no_scraping_policy="no_scraping_strict",
            status_label="news_provider_ready",
            warnings=[]
        )
    ]
    return sources

def build_news_source_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_sources(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_source_registry(df)
    return df, summary

def summarize_news_source_registry(df: pd.DataFrame) -> Dict:
    return {
        "total_sources": len(df),
        "sources": df["source_name"].tolist() if not df.empty else [],
        "categories": df["source_category"].unique().tolist() if not df.empty else []
    }
