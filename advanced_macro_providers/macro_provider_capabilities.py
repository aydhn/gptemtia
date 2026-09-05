
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderCapability, build_macro_provider_capability_id

def build_default_macro_provider_capabilities(profile: MacroProviderProfile) -> list[MacroProviderCapability]:
    caps = [
        MacroProviderCapability(
            capability_id=build_macro_provider_capability_id("macro_dry_run_fixture_provider", "timeseries"),
            provider_name="macro_dry_run_fixture_provider",
            provider_type="provider_dry_run_fixture",
            macro_categories=["macro_rates_and_yields", "macro_inflation"],
            data_types=["macro_data_timeseries", "macro_data_release_metadata"],
            frequency_support=["daily", "monthly"],
            region_support=["US", "EU"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            no_scraping_compliant=True,
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]
    return caps

def build_macro_provider_capability_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_provider_capabilities(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_provider_capabilities(df)

def summarize_macro_provider_capabilities(df: pd.DataFrame) -> dict:
    return {"total_capabilities": len(df)}
