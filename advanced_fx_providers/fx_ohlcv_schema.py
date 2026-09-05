import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_fx_ohlcv_schema_contract(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field": "pair", "type": "str", "required": True},
        {"field": "timestamp", "type": "datetime", "required": True},
        {"field": "open", "type": "float", "required": True},
        {"field": "high", "type": "float", "required": True},
        {"field": "low", "type": "float", "required": True},
        {"field": "close", "type": "float", "required": True},
        {"field": "volume", "type": "float", "required": False},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "retrieval_mode", "type": "str", "required": True},
        {"field": "adjusted_flag", "type": "bool", "required": True},
        {"field": "data_quality_status", "type": "str", "required": True},
        {"field": "manual_review_required", "type": "bool", "required": True},
    ]
    df = pd.DataFrame(schema)
    return df, summarize_fx_ohlcv_schema(df)

def summarize_fx_ohlcv_schema(df: pd.DataFrame) -> Dict:
    return {"total_fields": len(df), "warnings": ["FX spot volume represents tick count or dealer volume; use with caution."]}
