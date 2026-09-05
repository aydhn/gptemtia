import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXCurrencyMetadata, build_fx_currency_id

def build_default_fx_currency_metadata(profile: FXProviderProfile) -> List[FXCurrencyMetadata]:
    currencies = [
        ("USD", "US Dollar", "North America", True),
        ("EUR", "Euro", "Europe", True),
        ("GBP", "British Pound", "Europe", True),
        ("JPY", "Japanese Yen", "Asia", True),
        ("CHF", "Swiss Franc", "Europe", True),
        ("CAD", "Canadian Dollar", "North America", True),
        ("AUD", "Australian Dollar", "Oceania", True),
        ("NZD", "New Zealand Dollar", "Oceania", True),
        ("TRY", "Turkish Lira", "Europe/Asia", False),
        ("MXN", "Mexican Peso", "North America", False),
        ("ZAR", "South African Rand", "Africa", False),
        ("BRL", "Brazilian Real", "South America", False),
        ("CNH", "Offshore Chinese Yuan", "Asia", False),
        ("SGD", "Singapore Dollar", "Asia", False)
    ]
    meta = [
        FXCurrencyMetadata(
            currency_id=build_fx_currency_id(c[0]), currency_code=c[0], currency_name=c[1],
            region=c[2], is_major_currency=c[3], notes="", warnings=[]
        ) for c in currencies
    ]
    meta.append(FXCurrencyMetadata(
        currency_id=build_fx_currency_id("XAU"), currency_code="XAU", currency_name="Gold",
        region="Global", is_major_currency=False, notes="Precious metals handled by commodities provider",
        warnings=["XAU is deferred to Phase 108 commodities provider"]
    ))
    return meta

def build_fx_currency_metadata_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_currency_metadata(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_currency_metadata(df)

def summarize_fx_currency_metadata(df: pd.DataFrame) -> Dict:
    return {
        "total_currencies": len(df),
        "major_count": int(df["is_major_currency"].sum()) if not df.empty else 0
    }
