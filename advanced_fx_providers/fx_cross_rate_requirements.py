import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_default_fx_cross_rate_requirements(profile: FXProviderProfile) -> pd.DataFrame:
    reqs = [
        {"target_pair": "EUR/JPY", "required_base_leg": "EUR/USD", "required_quote_leg": "USD/JPY", "cross_rate_formula_note": "EUR/USD * USD/JPY", "provider_dependency": "generic", "precision_note": "slippage not included", "manual_review_required": True},
        {"target_pair": "GBP/JPY", "required_base_leg": "GBP/USD", "required_quote_leg": "USD/JPY", "cross_rate_formula_note": "GBP/USD * USD/JPY", "provider_dependency": "generic", "precision_note": "slippage not included", "manual_review_required": True},
        {"target_pair": "EUR/GBP", "required_base_leg": "EUR/USD", "required_quote_leg": "GBP/USD", "cross_rate_formula_note": "EUR/USD / GBP/USD", "provider_dependency": "generic", "precision_note": "slippage not included", "manual_review_required": True},
        {"target_pair": "AUD/NZD", "required_base_leg": "AUD/USD", "required_quote_leg": "NZD/USD", "cross_rate_formula_note": "AUD/USD / NZD/USD", "provider_dependency": "generic", "precision_note": "slippage not included", "manual_review_required": True}
    ]
    return pd.DataFrame(reqs)

def build_fx_cross_rate_requirement_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_fx_cross_rate_requirements(profile)
    return df, summarize_fx_cross_rate_requirements(df)

def summarize_fx_cross_rate_requirements(df: pd.DataFrame) -> Dict:
    return {"total_requirements": len(df), "warnings": ["Cross-rate calculations are not investment advice or exact prices."]}
