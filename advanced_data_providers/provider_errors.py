import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderError, build_provider_error_id
from dataclasses import asdict

def create_provider_error(
    provider_name: str, 
    error_type: str, 
    message: str, 
    retryable: bool = False, 
    blocked_by_safety: bool = False, 
    recommendation: str = ""
) -> ProviderError:
    return ProviderError(
        error_id=build_provider_error_id(provider_name, error_type),
        provider_name=provider_name,
        error_type=error_type,
        message=message,
        retryable=retryable,
        blocked_by_safety=blocked_by_safety,
        recommendation=recommendation
    )

def build_provider_error_schema(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    schema = {
        "field": ["error_id", "provider_name", "error_type", "message", "retryable", "blocked_by_safety", "recommendation"],
        "type": ["str", "str", "str", "str", "bool", "bool", "str"]
    }
    df = pd.DataFrame(schema)
    return df, {"total_fields": len(df)}

def provider_error_to_dict(error: ProviderError) -> dict:
    return asdict(error)

def summarize_provider_errors(df: pd.DataFrame) -> dict:
    return {"total_error_types": len(df)}
