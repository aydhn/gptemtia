import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_default_lightweight_mode_recommendations(profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"recommendation": "generate quality reports selectively", "warning": "Config degistirmez."}])

def build_lightweight_mode_recommendation_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_lightweight_mode_recommendations(profile)
    return df, summarize_lightweight_mode_recommendations(df)

def summarize_lightweight_mode_recommendations(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
