from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_capability_groups(profile: LocalBriefingProfile) -> pd.DataFrame:
    groups = [
        "research reporting", "DataLake storage", "backtest/paper outputs",
        "evidence governance", "artifact metadata", "local graph", "timeline",
        "consistency", "readiness", "maintenance", "archive", "disaster recovery rehearsal",
        "training/onboarding", "briefing/communication"
    ]
    return pd.DataFrame({"capability_group": groups, "status": ["offline_ready"] * len(groups)})

def map_capabilities_to_outputs(project_root: Path, profile: LocalBriefingProfile) -> pd.DataFrame:
    df = build_capability_groups(profile)
    df["outputs"] = df["capability_group"].apply(lambda x: f"reports/output/{x.split('/')[0]}")
    return df

def build_capability_map_nontechnical(project_root: Path, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    df = map_capabilities_to_outputs(project_root, profile)
    return df, summarize_capability_map(df)

def summarize_capability_map(capability_df: pd.DataFrame) -> dict:
    if capability_df is None or capability_df.empty:
        return {"total_capabilities": 0}
    return {"total_capabilities": len(capability_df)}
