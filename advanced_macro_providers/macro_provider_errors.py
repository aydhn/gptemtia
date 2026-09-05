
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderError, build_macro_provider_error_id

def build_macro_provider_error_schema(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [{"field": "error_id", "type": "str"}]
    df = pd.DataFrame(schema)
    return df, {"total_fields": 1}

def create_macro_provider_error(provider_name: str, error_type: str, message: str, retryable: bool = False, blocked_by_safety: bool = False, recommendation: str = "") -> MacroProviderError:
    return MacroProviderError(
        error_id=build_macro_provider_error_id(provider_name, error_type),
        provider_name=provider_name,
        error_type=error_type,
        message=message,
        retryable=retryable,
        blocked_by_safety=blocked_by_safety,
        recommendation=recommendation
    )

def macro_provider_error_to_dict(error: MacroProviderError) -> dict:
    return vars(error)

def summarize_macro_provider_errors(df: pd.DataFrame) -> dict:
    return {"total_errors": len(df)}
