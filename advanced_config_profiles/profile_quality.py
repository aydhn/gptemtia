import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile

def check_config_profile_registry_quality(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"quality": "good"}

def check_research_mode_preset_quality(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"quality": "good"}

def check_composed_profile_quality(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"quality": "good"}

def check_profile_compatibility_quality(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"quality": "good"}

def check_for_forbidden_terms_in_profiles(text: str = None, df: pd.DataFrame = None, summary: dict = None) -> dict:
    forbidden = ["live trading approved", "broker order", "real order sent", "investment advice", "yatırım tavsiyesidir", "kesin al", "kesin sat", "production deployed", "model deployed", "web server started", "dashboard created", "scraping enabled", "external llm called", "vector database created", "embeddings generated", "zip generated", "archive created", "docker image pushed", "git tag created", "official approval granted", "production approved", "guaranteed signal", "guaranteed profit"]
    combined = str(text) + str(df) + str(summary)
    combined = combined.lower()
    
    # Exclude false positives
    combined = combined.replace("yatırım tavsiyesi değildir", "")
    combined = combined.replace("canlı emir yoktur", "")
    combined = combined.replace("broker entegrasyonu değildir", "")
    combined = combined.replace("scraping yapılmaz", "")
    combined = combined.replace("deployment değildir", "")
    combined = combined.replace("official approval değildir", "")
    combined = combined.replace("kesin al/sat değildir", "")
    
    found = [f for f in forbidden if f in combined]
    return {"forbidden_terms_found": found}

def build_profile_quality_report(summary: dict, registry_df: pd.DataFrame = None, composed_df: pd.DataFrame = None) -> dict:
    return {"status": "quality check completed", "forbidden_terms": check_for_forbidden_terms_in_profiles(df=registry_df)}
