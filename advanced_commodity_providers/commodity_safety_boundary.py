
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def build_commodity_no_go_conditions(profile: CommodityProviderProfile) -> pd.DataFrame:
    data = [{"condition": c} for c in [
        "live trading", "broker integration", "futures broker integration", "real order",
        "exact buy/sell instruction", "investment advice", "futures advice", "model deployment",
        "production deployment", "web server/dashboard", "external LLM/vector/embedding",
        "web scraping", "HTML scraping", "browser automation scraping", "hidden API reverse engineering",
        "paywall bypass", "rate limit abuse", "credential output", "required paid API lock-in",
        "cloud publish", "Docker push", "git tag", "archive creation", "destructive file action",
        "official approval wording"
    ]]
    return pd.DataFrame(data)

def build_commodity_safe_go_conditions(profile: CommodityProviderProfile) -> pd.DataFrame:
    data = [{"condition": c} for c in [
        "local/offline commodity provider abstraction", "commodity dry-run fixture",
        "commodity manual file placeholder", "commodity local cache placeholder",
        "commodity official API placeholder without network call",
        "commodity licensed provider placeholder without credential",
        "commodity universe registry", "commodity symbol normalization map",
        "commodity capability matching", "commodity output schema contract",
        "futures metadata placeholder", "continuous contract requirement documentation",
        "roll adjustment requirement documentation", "manual review",
        "no broker/no live/no advice/no deploy/no scraping"
    ]]
    return pd.DataFrame(data)

def build_commodity_safety_boundary(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_commodity_no_go_conditions(profile)
    safe_go = build_commodity_safe_go_conditions(profile)
    df = pd.concat([no_go, safe_go], keys=["no_go", "safe_go"]).reset_index()
    return df, summarize_commodity_safety_boundary(df)

def summarize_commodity_safety_boundary(df: pd.DataFrame) -> dict:
    return {"total_conditions": len(df)}
