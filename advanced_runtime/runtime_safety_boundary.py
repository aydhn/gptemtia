import pandas as pd
from .runtime_config import AdvancedRuntimeProfile

def build_runtime_no_go_conditions(profile: AdvancedRuntimeProfile) -> pd.DataFrame:
    conditions = [
        "live trading", "broker integration", "real order", "investment advice",
        "model deployment", "production deployment", "web server/dashboard",
        "external LLM/vector/embedding", "scraping", "cloud publish",
        "Docker push", "git tag", "archive creation", "destructive file action",
        "official approval wording"
    ]
    return pd.DataFrame([{"condition": c, "type": "no-go"} for c in conditions])

def build_runtime_safe_go_conditions(profile: AdvancedRuntimeProfile) -> pd.DataFrame:
    conditions = [
        "local/offline runtime contract", "dry-run report commands",
        "DataLake/FeatureStore contract", "docs/report generation",
        "manual review", "no broker/no live/no advice/no deploy/no scraping"
    ]
    return pd.DataFrame([{"condition": c, "type": "safe-go"} for c in conditions])

def build_runtime_safety_boundary(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    df1 = build_runtime_no_go_conditions(profile)
    df2 = build_runtime_safe_go_conditions(profile)
    df = pd.concat([df1, df2], ignore_index=True)
    return df, summarize_runtime_safety_boundary(df)

def summarize_runtime_safety_boundary(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total": len(df), "no_go": len(df[df["type"] == "no-go"])}
