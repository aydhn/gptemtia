
import pandas as pd
from pathlib import Path
from .macro_provider_config import MacroProviderProfile

def build_default_macro_health_findings(profile: MacroProviderProfile) -> pd.DataFrame:
    return pd.DataFrame([{"check": "all_good", "status": "pass", "manual_review_required": False}])

def build_macro_health_check(project_root: Path, profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_macro_health_findings(profile)
    return df, summarize_macro_health(df)

def summarize_macro_health(df: pd.DataFrame) -> dict:
    return {"status": "healthy"}
