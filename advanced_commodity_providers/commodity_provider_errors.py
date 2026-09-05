
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityProviderError, build_commodity_provider_error_id, commodity_provider_error_to_dict

def create_commodity_provider_error(provider_name: str, error_type: str, message: str, retryable: bool = False, blocked_by_safety: bool = False, recommendation: str = "") -> CommodityProviderError:
    return CommodityProviderError(
        error_id=build_commodity_provider_error_id(provider_name, error_type),
        provider_name=provider_name,
        error_type=error_type,
        message=message,
        retryable=retryable,
        blocked_by_safety=blocked_by_safety,
        recommendation=recommendation
    )

def build_commodity_provider_error_schema(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "error_id", "type": "str"},
        {"field": "provider_name", "type": "str"},
        {"field": "error_type", "type": "str"},
        {"field": "message", "type": "str"},
        {"field": "retryable", "type": "bool"},
        {"field": "blocked_by_safety", "type": "bool"},
        {"field": "recommendation", "type": "str"}
    ]
    df = pd.DataFrame(schema)
    return df, summarize_commodity_provider_errors(df)

def summarize_commodity_provider_errors(df: pd.DataFrame) -> dict:
    return {"total_fields": len(df)}
