"""Atlas no-go / safe-go module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile

def build_meta_index_no_go_conditions(profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "enterprise search claim", "type": "no-go"},
        {"condition": "cloud index claim", "type": "no-go"},
        {"condition": "vector DB claim", "type": "no-go"},
        {"condition": "investment advice wording", "type": "no-go"}
    ])

def build_meta_index_safe_go_conditions(profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "local meta-index documented", "type": "safe-go"},
        {"condition": "manual review required", "type": "safe-go"}
    ])

def build_meta_index_no_go_safe_go_summary(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df_no = build_meta_index_no_go_conditions(profile)
    df_safe = build_meta_index_safe_go_conditions(profile)
    df = pd.concat([df_no, df_safe], ignore_index=True)
    return df, summarize_meta_index_no_go_safe_go(df)

def summarize_meta_index_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {
        "no_go_count": len(summary_df[summary_df["type"] == "no-go"]),
        "safe_go_count": len(summary_df[summary_df["type"] == "safe-go"])
    }
