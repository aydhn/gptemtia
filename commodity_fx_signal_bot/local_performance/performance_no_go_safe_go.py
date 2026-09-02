import pandas as pd
from .performance_config import LocalPerformanceProfile

def build_performance_no_go_conditions(profile: LocalPerformanceProfile) -> pd.DataFrame:
    data = [
        "real benchmark claim", "load/stress test claim", "production profiling claim",
        "cloud cost approval claim", "production capacity approval claim", "live/broker/deploy claim",
        "investment performance claim", "investment advice wording", "raw secret output",
        "file deletion/move/overwrite claim", "package publish/cloud upload claim"
    ]
    return pd.DataFrame([{"condition": c, "status": "no-go"} for c in data])

def build_performance_safe_go_conditions(profile: LocalPerformanceProfile) -> pd.DataFrame:
    data = [
        "read-only estimate reports available", "lightweight runtime profile documented",
        "heavy-output warnings documented", "retention rehearsal documented", "no benchmark executed",
        "no background monitoring", "no cloud dependency", "manual review required"
    ]
    return pd.DataFrame([{"condition": c, "status": "safe-go", "warning": "production capacity approval degildir"} for c in data])

def build_performance_no_go_safe_go_summary(profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df1 = build_performance_no_go_conditions(profile)
    df2 = build_performance_safe_go_conditions(profile)
    df = pd.concat([df1, df2], ignore_index=True)
    return df, summarize_performance_no_go_safe_go(df)

def summarize_performance_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    if summary_df is None or summary_df.empty: return {"total": 0}
    return {"total": len(summary_df), "no_go": len(summary_df[summary_df["status"]=="no-go"]), "safe_go": len(summary_df[summary_df["status"]=="safe-go"])}
