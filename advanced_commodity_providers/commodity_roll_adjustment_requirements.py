
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def build_default_roll_adjustment_requirements(profile: CommodityProviderProfile) -> pd.DataFrame:
    data = [
        {"adjustment_method": "no_adjustment_placeholder", "use_case": "raw_analysis", "risks": "price_gap", "future_phase_owner": "Phase 113", "manual_review_required": True},
        {"adjustment_method": "backward_adjustment_placeholder", "use_case": "backtesting", "risks": "negative_prices", "future_phase_owner": "Phase 113", "manual_review_required": True},
        {"adjustment_method": "ratio_adjustment_placeholder", "use_case": "returns_analysis", "risks": "level_distortion", "future_phase_owner": "Phase 113", "manual_review_required": True},
        {"adjustment_method": "calendar_roll_placeholder", "use_case": "standard_roll", "risks": "liquidity_drop", "future_phase_owner": "Phase 113", "manual_review_required": True},
        {"adjustment_method": "volume_open_interest_roll_placeholder", "use_case": "liquidity_roll", "risks": "complex_logic", "future_phase_owner": "Phase 113", "manual_review_required": True}
    ]
    return pd.DataFrame(data)

def build_commodity_roll_adjustment_requirement_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_roll_adjustment_requirements(profile)
    return df, summarize_roll_adjustment_requirements(df)

def summarize_roll_adjustment_requirements(df: pd.DataFrame) -> dict:
    return {"total_requirements": len(df)}
