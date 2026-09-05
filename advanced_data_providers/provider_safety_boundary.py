import pandas as pd
from .provider_config import DataProviderAbstractionProfile

def build_provider_no_go_conditions(profile: DataProviderAbstractionProfile) -> pd.DataFrame:
    conditions = [
        "live trading", "broker integration", "real order", "exact buy/sell instruction",
        "investment advice", "model deployment", "production deployment", "web server/dashboard",
        "external LLM/vector/embedding", "web scraping", "HTML scraping", "browser automation scraping",
        "hidden API reverse engineering", "paywall bypass", "rate limit abuse", "credential output",
        "required paid API lock-in", "cloud publish", "Docker push", "git tag", "archive creation",
        "destructive file action", "official approval wording"
    ]
    return pd.DataFrame([{"condition": c, "type": "no-go"} for c in conditions])

def build_provider_safe_go_conditions(profile: DataProviderAbstractionProfile) -> pd.DataFrame:
    conditions = [
        "local/offline provider abstraction", "dry-run fixture", "manual file placeholder",
        "local cache placeholder", "official API placeholder without network call",
        "licensed provider placeholder without credential", "provider metadata registry",
        "provider capability matching", "output schema contract", "manual review",
        "no broker/no live/no advice/no deploy/no scraping"
    ]
    return pd.DataFrame([{"condition": c, "type": "safe-go"} for c in conditions])

def build_provider_safety_boundary(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_provider_no_go_conditions(profile)
    safe_go = build_provider_safe_go_conditions(profile)
    df = pd.concat([no_go, safe_go], ignore_index=True)
    return df, summarize_provider_safety_boundary(df)

def summarize_provider_safety_boundary(df: pd.DataFrame) -> dict:
    return {"total_boundaries": len(df)}
