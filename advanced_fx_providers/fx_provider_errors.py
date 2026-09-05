import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderError, build_fx_provider_error_id

def build_fx_provider_error_schema(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field": "error_id", "type": "str", "required": True},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "error_type", "type": "str", "required": True},
        {"field": "message", "type": "str", "required": True},
        {"field": "retryable", "type": "bool", "required": True},
        {"field": "blocked_by_safety", "type": "bool", "required": True},
        {"field": "recommendation", "type": "str", "required": True}
    ]
    df = pd.DataFrame(schema)
    return df, summarize_fx_provider_errors(df)

def create_fx_provider_error(provider_name: str, error_type: str, message: str, retryable: bool = False, blocked_by_safety: bool = False, recommendation: str = "") -> FXProviderError:
    return FXProviderError(
        error_id=build_fx_provider_error_id(provider_name, error_type),
        provider_name=provider_name, error_type=error_type, message=message,
        retryable=retryable, blocked_by_safety=blocked_by_safety, recommendation=recommendation
    )

def fx_provider_error_to_dict(error: FXProviderError) -> Dict:
    return error.to_dict()

def summarize_fx_provider_errors(df: pd.DataFrame) -> Dict:
    return {"total_fields": len(df)}
