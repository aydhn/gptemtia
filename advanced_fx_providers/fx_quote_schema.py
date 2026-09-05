import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_fx_quote_schema_contract(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field": "pair", "type": "str", "required": True},
        {"field": "timestamp", "type": "datetime", "required": True},
        {"field": "bid", "type": "float", "required": True},
        {"field": "ask", "type": "float", "required": True},
        {"field": "mid", "type": "float", "required": False},
        {"field": "spread", "type": "float", "required": False},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "retrieval_mode", "type": "str", "required": True},
        {"field": "data_quality_status", "type": "str", "required": True},
        {"field": "manual_review_required", "type": "bool", "required": True},
    ]
    df = pd.DataFrame(schema)
    return df, summarize_fx_quote_schema(df)

def summarize_fx_quote_schema(df: pd.DataFrame) -> Dict:
    return {"total_fields": len(df), "warnings": ["Quote schema is abstract and does not represent live market data."]}
