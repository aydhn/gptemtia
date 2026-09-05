
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderContractItem, build_macro_provider_contract_id

def build_default_macro_adapter_contract_items(profile: MacroProviderProfile) -> list[MacroProviderContractItem]:
    return [
        MacroProviderContractItem(
            contract_id=build_macro_provider_contract_id("macro_fetch"),
            contract_area="Macro fetch response contract",
            input_expectation="Valid MacroProviderRequest",
            output_expectation="Valid MacroProviderResponse",
            forbidden_behavior=["no scraping", "no browser automation", "no hidden API reverse engineering", "no paywall bypass", "no credential output", "no broker/live/order", "no investment advice", "no directional macro claim", "no deployment", "no destructive file action"],
            manual_review_required=True
        )
    ]

def build_macro_adapter_contract(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_adapter_contract_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_adapter_contract(df)

def summarize_macro_adapter_contract(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
