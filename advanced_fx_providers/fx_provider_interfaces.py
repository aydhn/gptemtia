import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderMetadata, FXProviderCapability, FXProviderRequest, FXProviderResponse

class BaseFXProvider:
    provider_name: str = "base"
    provider_type: str = "base"

    def metadata(self) -> FXProviderMetadata:
        raise NotImplementedError

    def capabilities(self) -> List[FXProviderCapability]:
        raise NotImplementedError

    def validate_request(self, request: FXProviderRequest) -> Dict:
        raise NotImplementedError

    def fetch_fx(self, request: FXProviderRequest) -> FXProviderResponse:
        raise NotImplementedError

    def health_check(self) -> Dict:
        raise NotImplementedError

def build_fx_provider_interface_contract(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    methods = [
        {"method": "metadata", "return_type": "FXProviderMetadata"},
        {"method": "capabilities", "return_type": "List[FXProviderCapability]"},
        {"method": "validate_request", "return_type": "Dict"},
        {"method": "fetch_fx", "return_type": "FXProviderResponse"},
        {"method": "health_check", "return_type": "Dict"}
    ]
    df = pd.DataFrame(methods)
    return df, summarize_fx_provider_interface_contract(df)

def summarize_fx_provider_interface_contract(df: pd.DataFrame) -> Dict:
    return {"total_methods": len(df)}
