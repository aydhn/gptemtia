import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_default_fx_output_validation_rules(profile: FXProviderProfile) -> pd.DataFrame:
    rules = [
        {"rule_id": "rule_ohlc_consistency", "target_schema": "fx_ohlcv_schema", "field_name": "open,high,low,close", "rule_description": "low <= open,close <= high", "severity": "high", "future_phase_owner": "Phase 112", "manual_review_required": False},
        {"rule_id": "rule_symbol_normalization", "target_schema": "all", "field_name": "pair", "rule_description": "Pair must be canonical", "severity": "medium", "future_phase_owner": "Phase 113", "manual_review_required": False}
    ]
    return pd.DataFrame(rules)

def build_fx_output_validation_contract(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_fx_output_validation_rules(profile)
    return df, summarize_fx_output_validation(df)

def summarize_fx_output_validation(df: pd.DataFrame) -> Dict:
    return {"total_rules": len(df)}
