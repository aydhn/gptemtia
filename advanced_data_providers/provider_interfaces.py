from typing import Protocol, runtime_checkable
import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderMetadata, ProviderCapability, ProviderRequest, ProviderResponse

@runtime_checkable
class BaseDataProvider(Protocol):
    provider_name: str
    provider_type: str

    def metadata(self) -> ProviderMetadata:
        ...

    def capabilities(self) -> list[ProviderCapability]:
        ...

    def validate_request(self, request: ProviderRequest) -> dict:
        ...

    def fetch(self, request: ProviderRequest) -> ProviderResponse:
        ...

    def health_check(self) -> dict:
        ...

def build_provider_interface_contract(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    contract = {
        "method": ["metadata", "capabilities", "validate_request", "fetch", "health_check"],
        "return_type": ["ProviderMetadata", "list[ProviderCapability]", "dict", "ProviderResponse", "dict"]
    }
    df = pd.DataFrame(contract)
    return df, summarize_provider_interface_contract(df)

def summarize_provider_interface_contract(df: pd.DataFrame) -> dict:
    return {"total_methods": len(df)}
