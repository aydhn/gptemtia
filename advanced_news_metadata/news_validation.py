import pandas as pd
from typing import Tuple, Dict, Optional
from advanced_news_metadata.news_provider_config import NewsProviderProfile

def _default_val() -> Dict:
    return {"valid": True, "errors": []}

def validate_news_provider_profile_registry(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Profile registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_domain_registry(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Domain registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_source_registry(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Source registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_source_categories(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Source categories registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_metadata_schema(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Metadata schema contract is empty")
    elif "metadata_only" not in df["field_name"].values:
        errors.append("Metadata schema contract must contain metadata_only field")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_item_reference_schema(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Item reference schema is empty")
    elif "no_full_text_policy" not in df["field_name"].values:
        errors.append("Item reference schema must contain no_full_text_policy field")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_asset_tags(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Asset tags registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_macro_tags(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Macro tags registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_commodity_tags(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Commodity tags registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_fx_tags(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("FX tags registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_event_linkage(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Event linkage registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_region_currency_mapping(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Region currency mapping is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_topic_taxonomy(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Topic taxonomy is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_sentiment_requirements(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Sentiment requirements registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_impact_requirements(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Impact requirements registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_freshness_requirements(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Freshness requirements registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_deduplication_requirements(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Deduplication requirements registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_provider_capability_registry(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Capability registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_provider_metadata_registry(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Provider metadata registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_provider_request_schema(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Request schema is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_provider_response_schema(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Response schema is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_adapter_contract(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Adapter contract is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_provider_registry(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Provider registry is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_output_validation_contract(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Output validation contract is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_news_safety_boundary(df: pd.DataFrame, profile: NewsProviderProfile) -> Dict:
    errors = []
    if df.empty:
        errors.append("Safety boundary is empty")
    return {"valid": len(errors) == 0, "errors": errors}

def validate_no_forbidden_news_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict] = None
) -> Dict:
    forbidden_terms = [
        "live trading approved", "broker order", "real order sent", "investment advice",
        "yatırım tavsiyesidir", "kesin al", "kesin sat", "news direction guaranteed",
        "guaranteed news signal", "sentiment signal", "guaranteed profit",
        "full article downloaded", "copyrighted article copied", "production deployed",
        "model deployed", "NLP model deployed", "web server started", "dashboard created",
        "scraping enabled", "news page scraping enabled", "HTML scraping enabled",
        "browser automation scraping", "hidden API reverse engineering", "paywall bypass",
        "rate limit abuse", "external LLM called", "vector database created",
        "embeddings generated", "ZIP generated", "archive created", "Docker image pushed",
        "git tag created", "official approval granted", "production approved",
        "news provider credential printed", "API key printed", "secret printed",
        "paid API required", "network call required"
    ]
    disclaimer_phrases = [
        "yatırım tavsiyesi değildir", "canlı emir yoktur", "broker entegrasyonu değildir",
        "scraping yapılmaz", "news page scraping yapılmaz", "HTML scraping yapılmaz",
        "deployment değildir", "official approval değildir", "kesin AL/SAT değildir",
        "credential output yoktur", "paid API zorunlu değildir", "network call zorunlu değildir",
        "news direction guaranteed değildir", "sentiment signal değildir",
        "full article downloaded değildir"
    ]

    target_text = (text or "") + " "
    if df is not None and not df.empty:
        target_text += " " + df.to_string()
    if summary:
        target_text += " " + str(summary)
    
    target_lower = target_text.lower()
    for disc in disclaimer_phrases:
        target_lower = target_lower.replace(disc.lower(), " ")

    found = []
    for term in forbidden_terms:
        if term.lower() in target_lower:
            found.append(term)

    return {"valid": len(found) == 0, "forbidden_found": found}

def build_news_validation_report(tables: Dict[str, pd.DataFrame], profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    records = []
    for name, table in tables.items():
        val = {"valid": not table.empty, "errors": [] if not table.empty else ["Table empty"]}
        records.append({"table_name": name, "status": "pass" if val["valid"] else "fail", "errors": val["errors"]})
    df = pd.DataFrame(records)
    summary = {
        "total_tables_validated": len(df),
        "passed": len(df[df["status"] == "pass"]) if not df.empty else 0
    }
    return df, summary
