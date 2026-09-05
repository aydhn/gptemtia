
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def build_default_continuous_contract_requirements(profile: CommodityProviderProfile) -> pd.DataFrame:
    data = [
        {"commodity_symbol": "WTI_CRUDE", "continuous_method_placeholder": "front_month", "roll_rule_placeholder": "volume_switch", "adjustment_required": True, "data_quality_dependency": "phase112", "manual_review_required": True}
    ]
    return pd.DataFrame(data)

def build_commodity_continuous_contract_requirement_registry(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_continuous_contract_requirements(profile)
    return df, summarize_continuous_contract_requirements(df)

def summarize_continuous_contract_requirements(df: pd.DataFrame) -> dict:
    return {"total_requirements": len(df)}
