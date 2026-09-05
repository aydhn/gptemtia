
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def build_default_commodity_output_validation_rules(profile: CommodityProviderProfile) -> pd.DataFrame:
    data = [
        {"rule_id": "val_1", "target_schema": "commodity_spot_schema", "field_name": "spot_price", "rule_description": "Greater than zero", "severity": "error", "future_phase_owner": "Phase 112", "manual_review_required": True},
        {"rule_id": "val_2", "target_schema": "commodity_ohlcv_schema", "field_name": "high", "rule_description": "High >= Low", "severity": "error", "future_phase_owner": "Phase 112", "manual_review_required": True}
    ]
    return pd.DataFrame(data)

def build_commodity_output_validation_contract(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_commodity_output_validation_rules(profile)
    return df, summarize_commodity_output_validation(df)

def summarize_commodity_output_validation(df: pd.DataFrame) -> dict:
    return {"total_rules": len(df)}
