import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile, list_news_provider_profiles
from advanced_news_metadata.news_provider_models import NewsProviderProfileItem, build_news_provider_profile_id

def build_default_news_provider_profile_items(profile: NewsProviderProfile) -> List[NewsProviderProfileItem]:
    items = []
    for p in list_news_provider_profiles(enabled_only=True):
        items.append(NewsProviderProfileItem(
            profile_id=build_news_provider_profile_id(p.name),
            profile_name=p.name,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            no_scraping=not p.allow_web_scraping,
            metadata_only=not p.allow_full_article_download,
            status_label="news_provider_ready",
            warnings=[]
        ))
    return items

def build_news_metadata_provider_profile_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_provider_profile_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_provider_profile_registry(df)
    return df, summary

def summarize_news_provider_profile_registry(df: pd.DataFrame) -> Dict:
    return {
        "total_profiles": len(df),
        "profiles": df["profile_name"].tolist() if not df.empty else []
    }
