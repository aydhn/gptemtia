
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroRegionMetadata, build_macro_region_id

def build_default_macro_region_metadata(profile: MacroProviderProfile) -> list[MacroRegionMetadata]:
    regions = [
        ("US", "USD", "FED", "United States"),
        ("EU", "EUR", "ECB", "Eurozone"),
        ("UK", "GBP", "BOE", "United Kingdom"),
        ("JP", "JPY", "BOJ", "Japan"),
        ("TR", "TRY", "CBRT", "Turkey"),
        ("CN", "CNY", "PBOC", "China")
    ]
    return [MacroRegionMetadata(
        region_id=build_macro_region_id(r[0]),
        region_code=r[0],
        region_name=r[3],
        currency_code=r[1],
        central_bank_ref=r[2],
        notes="",
        warnings=[]
    ) for r in regions]

def build_macro_region_country_currency_metadata_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_region_metadata(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_region_metadata(df)

def summarize_macro_region_metadata(df: pd.DataFrame) -> dict:
    return {"total_regions": len(df)}
