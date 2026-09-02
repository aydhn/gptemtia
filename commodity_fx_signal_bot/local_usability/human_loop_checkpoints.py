import pandas as pd
from .usability_config import LocalUsabilityProfile

def build_default_human_loop_checkpoints(profile: LocalUsabilityProfile) -> pd.DataFrame:
    return pd.DataFrame([{"checkpoint": "output generated ama okunmadı"}])

def build_human_in_the_loop_checkpoint_registry(profile: LocalUsabilityProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_human_loop_checkpoints(profile)
    return df, {"total": len(df)}

def summarize_human_loop_checkpoints(checkpoint_df: pd.DataFrame) -> dict:
    return {"total": len(checkpoint_df)}
