import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderContractItem, build_fx_provider_contract_id

def build_default_fx_adapter_contract_items(profile: FXProviderProfile) -> List[FXProviderContractItem]:
    areas = [
        "FX metadata contract", "FX capability contract", "FX pair normalization contract",
        "FX request validation contract", "FX fetch response contract", "FX error handling contract",
        "FX manual file contract", "FX local cache contract", "FX official API placeholder contract",
        "FX licensed placeholder contract", "FX dry-run fixture contract", "FX quote schema contract",
        "FX OHLCV schema contract", "FX cross-rate requirement contract", "FX output validation contract",
        "FX safety contract"
    ]
    forbidden = [
        "no scraping", "no browser automation", "no hidden API reverse engineering",
        "no paywall bypass", "no credential output", "no broker/live/order",
        "no investment advice", "no deployment", "no destructive file action"
    ]
    return [
        FXProviderContractItem(
            contract_id=build_fx_provider_contract_id(area), contract_area=area,
            input_expectation="Provider agnostic input", output_expectation="Standardized output schema",
            forbidden_behavior=forbidden, manual_review_required=True
        ) for area in areas
    ]

def build_fx_adapter_contract(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_adapter_contract_items(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_adapter_contract(df)

def summarize_fx_adapter_contract(df: pd.DataFrame) -> Dict:
    return {"total_contracts": len(df)}
