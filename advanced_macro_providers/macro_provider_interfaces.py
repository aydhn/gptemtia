
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderMetadata, MacroProviderCapability, MacroProviderRequest, MacroProviderResponse

class BaseMacroProvider:
    provider_name: str = "base"
    provider_type: str = "base"
    
    def metadata(self) -> MacroProviderMetadata:
        raise NotImplementedError
    
    def capabilities(self) -> list[MacroProviderCapability]:
        raise NotImplementedError
        
    def validate_request(self, request: MacroProviderRequest) -> dict:
        raise NotImplementedError
        
    def fetch_macro(self, request: MacroProviderRequest) -> MacroProviderResponse:
        raise NotImplementedError
        
    def health_check(self) -> dict:
        raise NotImplementedError

def build_macro_provider_interface_contract(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"method": "fetch_macro"}]), {"total": 1}

def summarize_macro_provider_interface_contract(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
