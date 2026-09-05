
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def match_macro_provider_capabilities(
    requested_data_type: str,
    requested_category: str,
    requested_region: str,
    frequency: str,
    capability_df: pd.DataFrame,
) -> pd.DataFrame:
    return capability_df

def build_macro_provider_capability_matcher_report(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"match": "all"}]), summarize_macro_provider_capability_matcher(pd.DataFrame([{"match": "all"}]))

def summarize_macro_provider_capability_matcher(df: pd.DataFrame) -> dict:
    return {"total_matches": len(df)}
