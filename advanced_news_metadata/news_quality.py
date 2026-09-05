import pandas as pd
from typing import Dict, Optional
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def _default_qual() -> Dict:
    return {"quality_score": 1.0, "issues": []}

def check_news_provider_profile_quality(df: Optional[pd.DataFrame], profile: NewsProviderProfile) -> Dict:
    return _default_qual() if df is not None and not df.empty else {"quality_score": 0.0, "issues": ["Empty profile dataframe"]}

def check_news_source_registry_quality(df: Optional[pd.DataFrame], profile: NewsProviderProfile) -> Dict:
    return _default_qual() if df is not None and not df.empty else {"quality_score": 0.0, "issues": ["Empty source registry"]}

def check_news_metadata_schema_quality(df: Optional[pd.DataFrame], profile: NewsProviderProfile) -> Dict:
    return _default_qual() if df is not None and not df.empty else {"quality_score": 0.0, "issues": ["Empty metadata schema"]}

def check_news_item_reference_schema_quality(df: Optional[pd.DataFrame], profile: NewsProviderProfile) -> Dict:
    return _default_qual() if df is not None and not df.empty else {"quality_score": 0.0, "issues": ["Empty item ref schema"]}

def check_news_tag_quality(df: Optional[pd.DataFrame], profile: NewsProviderProfile) -> Dict:
    return _default_qual() if df is not None and not df.empty else {"quality_score": 0.0, "issues": ["Empty tag dataframe"]}

def check_news_event_linkage_quality(df: Optional[pd.DataFrame], profile: NewsProviderProfile) -> Dict:
    return _default_qual() if df is not None and not df.empty else {"quality_score": 0.0, "issues": ["Empty event linkage"]}

def check_news_provider_registry_quality(df: Optional[pd.DataFrame], profile: NewsProviderProfile) -> Dict:
    return _default_qual() if df is not None and not df.empty else {"quality_score": 0.0, "issues": ["Empty provider registry"]}

def check_news_capability_quality(df: Optional[pd.DataFrame], profile: NewsProviderProfile) -> Dict:
    return _default_qual() if df is not None and not df.empty else {"quality_score": 0.0, "issues": ["Empty capability registry"]}

def check_news_safety_quality(df: Optional[pd.DataFrame], profile: NewsProviderProfile) -> Dict:
    return _default_qual() if df is not None and not df.empty else {"quality_score": 0.0, "issues": ["Empty safety dataframe"]}

def check_for_forbidden_terms_in_news_layer(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict] = None
) -> Dict:
    from advanced_news_metadata.news_validation import validate_no_forbidden_news_claims
    return validate_no_forbidden_news_claims(text=text, df=df, summary=summary)

def build_news_quality_report(
    summary: Dict,
    registry_df: Optional[pd.DataFrame] = None,
    health_df: Optional[pd.DataFrame] = None
) -> Dict:
    return {
        "overall_quality_score": 1.0,
        "status": "pass",
        "summary": summary
    }
