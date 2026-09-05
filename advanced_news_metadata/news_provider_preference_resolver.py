import pandas as pd
from typing import Tuple, Dict
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def resolve_news_provider_preferences_from_config_profiles(profile: NewsProviderProfile) -> pd.DataFrame:
    preferences = [
        {"research_profile": "no_scraping_public_api_preferred", "preferred_provider": "news_dry_run_fixture_provider", "rationale": "Prioritize zero scraping with local offline fixture."},
        {"research_profile": "local_cache_preferred", "preferred_provider": "news_local_cache_provider_placeholder", "rationale": "Fast replay using cached local metadata."},
        {"research_profile": "manual_file_import_preferred", "preferred_provider": "news_manual_file_provider_placeholder", "rationale": "User offline curated research file ingestion."},
        {"research_profile": "official_provider_preferred", "preferred_provider": "news_official_api_provider_placeholder", "rationale": "Regulatory communiques from official channels."},
        {"research_profile": "news_metadata_provider_placeholder", "preferred_provider": "news_licensed_provider_placeholder", "rationale": "Institutional feed contract testing."},
        {"research_profile": "macro_sensitive_research", "preferred_provider": "news_dry_run_fixture_provider", "rationale": "Macro news metadata fixture evaluation."},
        {"research_profile": "gold_macro_research", "preferred_provider": "news_dry_run_fixture_provider", "rationale": "Gold safe-haven and inflation metadata analysis."},
        {"research_profile": "oil_macro_research", "preferred_provider": "news_dry_run_fixture_provider", "rationale": "Energy inventory and supply news linkage."},
        {"research_profile": "cross_asset_macro_research", "preferred_provider": "news_dry_run_fixture_provider", "rationale": "Multi-asset intermarket metadata coverage."},
        {"research_profile": "volatility_regime_research", "preferred_provider": "news_dry_run_fixture_provider", "rationale": "Market uncertainty and shock headline metadata."},
        {"research_profile": "risk_sentiment_research_placeholder", "preferred_provider": "news_dry_run_fixture_provider", "rationale": "Systemic risk appetite classification testing."}
    ]
    return pd.DataFrame(preferences)

def build_news_provider_preference_resolver_report(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = resolve_news_provider_preferences_from_config_profiles(profile)
    summary = summarize_news_provider_preference_resolver(df)
    return df, summary

def summarize_news_provider_preference_resolver(df: pd.DataFrame) -> Dict:
    return {
        "total_preferences": len(df),
        "profiles": df["research_profile"].tolist() if not df.empty else []
    }
