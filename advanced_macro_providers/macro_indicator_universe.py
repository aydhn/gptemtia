
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroIndicator, build_macro_indicator_id

def build_rates_and_yields_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return [
        MacroIndicator(
            indicator_id=build_macro_indicator_id("US_10Y_YIELD", "US"),
            canonical_indicator="US_10Y_YIELD",
            display_name="US 10 Year Yield",
            category_label="macro_rates_and_yields",
            region="US",
            currency="USD",
            default_frequency="daily",
            unit="percent",
            release_lag_note="End of day",
            revision_note="None",
            status_label="macro_provider_ready",
            warnings=[]
        ),
        MacroIndicator(
            indicator_id=build_macro_indicator_id("US_2Y_YIELD", "US"),
            canonical_indicator="US_2Y_YIELD",
            display_name="US 2 Year Yield",
            category_label="macro_rates_and_yields",
            region="US",
            currency="USD",
            default_frequency="daily",
            unit="percent",
            release_lag_note="End of day",
            revision_note="None",
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]

def build_inflation_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return [
        MacroIndicator(
            indicator_id=build_macro_indicator_id("US_CPI_YOY", "US"),
            canonical_indicator="US_CPI_YOY",
            display_name="US CPI YoY",
            category_label="macro_inflation",
            region="US",
            currency="USD",
            default_frequency="monthly",
            unit="percent",
            release_lag_note="Mid-month",
            revision_note="Frequent",
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]

def build_growth_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return []

def build_labor_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return []

def build_central_bank_policy_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return [
        MacroIndicator(
            indicator_id=build_macro_indicator_id("FED_POLICY_RATE", "US"),
            canonical_indicator="FED_POLICY_RATE",
            display_name="FED Policy Rate",
            category_label="macro_central_bank_policy",
            region="US",
            currency="USD",
            default_frequency="monthly",
            unit="percent",
            release_lag_note="FOMC dates",
            revision_note="None",
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]

def build_risk_sentiment_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return [
        MacroIndicator(
            indicator_id=build_macro_indicator_id("DXY_PLACEHOLDER", "US"),
            canonical_indicator="DXY_PLACEHOLDER",
            display_name="DXY Placeholder",
            category_label="macro_currency_index",
            region="US",
            currency="USD",
            default_frequency="daily",
            unit="index",
            release_lag_note="Realtime",
            revision_note="None",
            status_label="macro_provider_ready",
            warnings=[]
        ),
        MacroIndicator(
            indicator_id=build_macro_indicator_id("US_YIELD_CURVE_10Y2Y", "US"),
            canonical_indicator="US_YIELD_CURVE_10Y2Y",
            display_name="US Yield Curve 10Y-2Y",
            category_label="macro_yield_curve",
            region="US",
            currency="USD",
            default_frequency="daily",
            unit="percent",
            release_lag_note="EOD",
            revision_note="None",
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]

def build_default_macro_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return (build_rates_and_yields_indicators(profile) + build_inflation_indicators(profile) + 
            build_growth_indicators(profile) + build_labor_indicators(profile) + 
            build_central_bank_policy_indicators(profile) + build_risk_sentiment_indicators(profile))

def build_macro_indicator_universe_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_indicators(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_indicator_universe(df)

def summarize_macro_indicator_universe(df: pd.DataFrame) -> dict:
    return {"total_indicators": len(df)}
