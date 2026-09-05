
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def build_macro_no_go_conditions(profile: MacroProviderProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "no live trading"}])

def build_macro_safe_go_conditions(profile: MacroProviderProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "local offline"}])

def build_macro_safety_boundary(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"boundary": "safe"}])
    return df, summarize_macro_safety_boundary(df)

def summarize_macro_safety_boundary(df: pd.DataFrame) -> dict:
    return {"total_boundaries": len(df)}
