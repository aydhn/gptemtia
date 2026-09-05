import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXPair, build_fx_pair_id

def build_major_fx_pairs(profile: FXProviderProfile) -> List[FXPair]:
    pairs = [("EUR/USD", "EUR", "USD"), ("GBP/USD", "GBP", "USD"), ("USD/JPY", "USD", "JPY"), 
             ("USD/CHF", "USD", "CHF"), ("USD/CAD", "USD", "CAD"), ("AUD/USD", "AUD", "USD"), 
             ("NZD/USD", "NZD", "USD")]
    return [
        FXPair(
            pair_id=build_fx_pair_id(p[0]), pair=p[0], base_currency=p[1], quote_currency=p[2],
            pair_group="fx_major_pair", default_symbol_variants=[p[0], p[0].replace("/", ""), p[0].replace("/", "_")],
            pip_convention_note="Standard pip mapping", status_label="fx_provider_ready", warnings=[]
        ) for p in pairs
    ]

def build_minor_fx_pairs(profile: FXProviderProfile) -> List[FXPair]:
    pairs = [("EUR/GBP", "EUR", "GBP"), ("EUR/JPY", "EUR", "JPY"), ("GBP/JPY", "GBP", "JPY"), 
             ("EUR/CHF", "EUR", "CHF"), ("AUD/JPY", "AUD", "JPY"), ("CAD/JPY", "CAD", "JPY"), 
             ("AUD/NZD", "AUD", "NZD")]
    return [
        FXPair(
            pair_id=build_fx_pair_id(p[0]), pair=p[0], base_currency=p[1], quote_currency=p[2],
            pair_group="fx_minor_pair", default_symbol_variants=[p[0], p[0].replace("/", ""), p[0].replace("/", "_")],
            pip_convention_note="Standard pip mapping", status_label="fx_provider_ready", warnings=[]
        ) for p in pairs
    ]

def build_exotic_fx_pairs(profile: FXProviderProfile) -> List[FXPair]:
    pairs = [("USD/TRY", "USD", "TRY"), ("EUR/TRY", "EUR", "TRY"), ("USD/MXN", "USD", "MXN"), 
             ("USD/ZAR", "USD", "ZAR"), ("USD/BRL", "USD", "BRL"), ("USD/CNH", "USD", "CNH"), 
             ("USD/SGD", "USD", "SGD")]
    return [
        FXPair(
            pair_id=build_fx_pair_id(p[0]), pair=p[0], base_currency=p[1], quote_currency=p[2],
            pair_group="fx_exotic_pair", default_symbol_variants=[p[0], p[0].replace("/", ""), p[0].replace("/", "_")],
            pip_convention_note="Non-standard pip mapping", status_label="fx_provider_ready", warnings=["Exotic pair - not investment advice"]
        ) for p in pairs
    ]

def build_default_fx_pairs(profile: FXProviderProfile) -> List[FXPair]:
    pairs = []
    if profile.enable_major_pairs: pairs.extend(build_major_fx_pairs(profile))
    if profile.enable_minor_pairs: pairs.extend(build_minor_fx_pairs(profile))
    if profile.enable_exotic_pairs: pairs.extend(build_exotic_fx_pairs(profile))
    return pairs

def build_fx_pair_universe_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_pairs(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_pair_universe(df)

def summarize_fx_pair_universe(df: pd.DataFrame) -> Dict:
    return {
        "total_pairs": len(df),
        "by_group": df["pair_group"].value_counts().to_dict() if not df.empty else {}
    }
