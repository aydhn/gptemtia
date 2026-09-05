
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def build_default_macro_output_validation_rules(profile: MacroProviderProfile) -> pd.DataFrame:
    rules = [
        {"rule_id": "val_1", "target_schema": "macro_timeseries", "field_name": "value", "rule_description": "Value should not be null", "severity": "high", "future_phase_owner": "Phase 112", "manual_review_required": True}
    ]
    return pd.DataFrame(rules)

def build_macro_output_validation_contract(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_macro_output_validation_rules(profile)
    return df, summarize_macro_output_validation(df)

def summarize_macro_output_validation(df: pd.DataFrame) -> dict:
    return {"total_rules": len(df)}
