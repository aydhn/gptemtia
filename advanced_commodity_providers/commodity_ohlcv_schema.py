
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def build_commodity_ohlcv_schema_contract(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "symbol", "type": "str"},
        {"field": "timestamp", "type": "datetime"},
        {"field": "open", "type": "float"},
        {"field": "high", "type": "float"},
        {"field": "low", "type": "float"},
        {"field": "close", "type": "float"},
        {"field": "volume", "type": "float"},
        {"field": "open_interest", "type": "float"},
        {"field": "provider_name", "type": "str"},
        {"field": "retrieval_mode", "type": "str"},
        {"field": "contract_type", "type": "str"},
        {"field": "adjusted_flag", "type": "bool"},
        {"field": "data_quality_status", "type": "str"},
        {"field": "manual_review_required", "type": "bool"}
    ]
    df = pd.DataFrame(schema)
    return df, summarize_commodity_ohlcv_schema(df)

def summarize_commodity_ohlcv_schema(df: pd.DataFrame) -> dict:
    return {"total_fields": len(df)}
