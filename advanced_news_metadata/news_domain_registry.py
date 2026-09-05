import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsDomain, build_news_domain_id
from advanced_news_metadata.news_provider_labels import list_news_domain_labels

def build_default_news_domains(profile: NewsProviderProfile) -> List[NewsDomain]:
    domains = []
    for lbl in list_news_domain_labels():
        domains.append(NewsDomain(
            domain_id=build_news_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Domain for {lbl}",
            required_outputs=["schema", "registry"],
            warnings=[]
        ))
    return domains

def build_news_metadata_domain_registry(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_domains(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_domains(df)
    return df, summary

def summarize_news_domains(df: pd.DataFrame) -> Dict:
    return {
        "total_domains": len(df),
        "domains": df["domain_label"].tolist() if not df.empty else []
    }
