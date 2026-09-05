
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def build_macro_timeseries_schema_contract(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "indicator", "type": "str", "required": True},
        {"field": "timestamp", "type": "datetime", "required": True},
        {"field": "value", "type": "float", "required": True},
        {"field": "unit", "type": "str", "required": True},
        {"field": "region", "type": "str", "required": True},
        {"field": "currency", "type": "str", "required": False},
        {"field": "frequency", "type": "str", "required": True},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "retrieval_mode", "type": "str", "required": True},
        {"field": "release_reference", "type": "str", "required": False},
        {"field": "revision_status", "type": "str", "required": False},
        {"field": "data_quality_status", "type": "str", "required": False},
        {"field": "manual_review_required", "type": "bool", "required": True},
    ]
    df = pd.DataFrame(schema)
    return df, summarize_macro_timeseries_schema(df)

def summarize_macro_timeseries_schema(df: pd.DataFrame) -> dict:
    return {"total_fields": len(df)}
