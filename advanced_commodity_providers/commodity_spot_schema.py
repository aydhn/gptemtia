
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def build_commodity_spot_schema_contract(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "symbol", "type": "str"},
        {"field": "timestamp", "type": "datetime"},
        {"field": "spot_price", "type": "float"},
        {"field": "quote_currency", "type": "str"},
        {"field": "unit", "type": "str"},
        {"field": "provider_name", "type": "str"},
        {"field": "retrieval_mode", "type": "str"},
        {"field": "data_quality_status", "type": "str"},
        {"field": "manual_review_required", "type": "bool"}
    ]
    df = pd.DataFrame(schema)
    return df, summarize_commodity_spot_schema(df)

def summarize_commodity_spot_schema(df: pd.DataFrame) -> dict:
    return {"total_fields": len(df)}
