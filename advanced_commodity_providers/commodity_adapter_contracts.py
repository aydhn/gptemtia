
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile
from .commodity_provider_models import CommodityProviderContractItem, build_commodity_provider_contract_id

def build_default_commodity_adapter_contract_items(profile: CommodityProviderProfile) -> list[CommodityProviderContractItem]:
    forbidden = ["no scraping", "no browser automation", "no hidden API reverse engineering", "no paywall bypass", "no credential output", "no broker/live/order", "no futures broker execution", "no investment advice", "no futures advice", "no deployment", "no destructive file action"]
    areas = [
        "Commodity metadata contract", "Commodity capability contract", "Commodity symbol normalization contract", 
        "Commodity request validation contract", "Commodity fetch response contract", "Commodity error handling contract",
        "Commodity manual file contract", "Commodity local cache contract", "Commodity official API placeholder contract",
        "Commodity licensed placeholder contract", "Commodity dry-run fixture contract", "Commodity spot schema contract",
        "Commodity OHLCV schema contract", "Futures contract metadata contract", "Continuous contract requirement contract",
        "Roll adjustment requirement contract", "Commodity output validation contract", "Commodity safety contract"
    ]
    return [
        CommodityProviderContractItem(build_commodity_provider_contract_id(a.replace(' ', '_').lower()), a, "valid input", "valid output", forbidden, True)
        for a in areas
    ]

def build_commodity_adapter_contract(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_commodity_adapter_contract_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_commodity_adapter_contract(df)

def summarize_commodity_adapter_contract(df: pd.DataFrame) -> dict:
    return {"total_contracts": len(df)}
