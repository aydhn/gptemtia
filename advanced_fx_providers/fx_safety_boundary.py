import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_fx_no_go_conditions(profile: FXProviderProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": c, "status": "no-go"} for c in [
        "live trading", "broker integration", "real order", "exact buy/sell instruction",
        "investment advice", "model deployment", "production deployment", "web server/dashboard",
        "external LLM/vector/embedding", "web scraping", "HTML scraping", "browser automation scraping",
        "hidden API reverse engineering", "paywall bypass", "rate limit abuse", "credential output",
        "required paid API lock-in", "cloud publish", "Docker push", "git tag", "archive creation",
        "destructive file action", "official approval wording"
    ]])

def build_fx_safe_go_conditions(profile: FXProviderProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": c, "status": "safe-go"} for c in [
        "local/offline FX provider abstraction", "FX dry-run fixture", "FX manual file placeholder",
        "FX local cache placeholder", "FX official API placeholder without network call",
        "FX licensed provider placeholder without credential", "FX pair universe registry",
        "FX symbol normalization map", "FX capability matching", "FX output schema contract",
        "manual review", "no broker/no live/no advice/no deploy/no scraping"
    ]])

def build_fx_safety_boundary(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    nogo = build_fx_no_go_conditions(profile)
    safego = build_fx_safe_go_conditions(profile)
    df = pd.concat([nogo, safego], ignore_index=True)
    return df, summarize_fx_safety_boundary(df)

def summarize_fx_safety_boundary(df: pd.DataFrame) -> Dict:
    return {"nogo_count": len(df[df["status"]=="no-go"]), "safego_count": len(df[df["status"]=="safe-go"])}
