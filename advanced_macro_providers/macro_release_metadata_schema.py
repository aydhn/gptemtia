
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def build_macro_release_metadata_schema_contract(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "release_id", "type": "str", "required": True},
        {"field": "indicator", "type": "str", "required": True},
        {"field": "region", "type": "str", "required": True},
        {"field": "scheduled_release_time", "type": "datetime", "required": True},
        {"field": "actual_release_time", "type": "datetime", "required": False},
        {"field": "period_reference", "type": "str", "required": True},
        {"field": "actual", "type": "float", "required": False},
        {"field": "forecast", "type": "float", "required": False},
        {"field": "previous", "type": "float", "required": False},
        {"field": "revised_previous", "type": "float", "required": False},
        {"field": "importance", "type": "str", "required": False},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "retrieval_mode", "type": "str", "required": True},
        {"field": "manual_review_required", "type": "bool", "required": True},
    ]
    df = pd.DataFrame(schema)
    return df, summarize_macro_release_metadata_schema(df)

def summarize_macro_release_metadata_schema(df: pd.DataFrame) -> dict:
    return {"total_fields": len(df)}
