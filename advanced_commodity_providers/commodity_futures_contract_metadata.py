
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def build_commodity_futures_contract_metadata_schema(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "root_symbol", "type": "str"},
        {"field": "contract_month", "type": "str"},
        {"field": "expiry_date", "type": "datetime"},
        {"field": "exchange_ref", "type": "str"},
        {"field": "contract_size", "type": "float"},
        {"field": "tick_size", "type": "float"},
        {"field": "quote_currency", "type": "str"},
        {"field": "unit", "type": "str"},
        {"field": "provider_name", "type": "str"},
        {"field": "manual_review_required", "type": "bool"}
    ]
    df = pd.DataFrame(schema)
    return df, summarize_commodity_futures_contract_metadata(df)

def summarize_commodity_futures_contract_metadata(df: pd.DataFrame) -> dict:
    return {"total_fields": len(df)}
