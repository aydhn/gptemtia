
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroIndicatorCategory, build_macro_category_id

def build_default_macro_indicator_categories(profile: MacroProviderProfile) -> list[MacroIndicatorCategory]:
    cats = ["rates_and_yields", "inflation", "growth", "labor", "trade_balance", "central_bank_policy", "liquidity", "risk_sentiment", "yield_curve", "currency_index"]
    return [MacroIndicatorCategory(
        category_id=build_macro_category_id(c),
        category_label=f"macro_{c}",
        category_name=c.replace("_", " ").title(),
        description=f"{c} category",
        example_indicators=[],
        warnings=[]
    ) for c in cats]

def build_macro_indicator_category_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_indicator_categories(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_indicator_categories(df)

def summarize_macro_indicator_categories(df: pd.DataFrame) -> dict:
    return {"total_categories": len(df)}
