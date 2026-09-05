import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import EconomicEvent, build_economic_event_id

def build_central_bank_events(profile: CalendarProviderProfile) -> List[EconomicEvent]:
    events = [
        ("FOMC_RATE_DECISION", "US", "USD", "FED_POLICY_RATE"),
        ("ECB_RATE_DECISION", "EU", "EUR", "ECB_POLICY_RATE"),
        ("BOE_RATE_DECISION", "UK", "GBP", "BOE_POLICY_RATE"),
        ("BOJ_RATE_DECISION", "JP", "JPY", "BOJ_POLICY_RATE"),
        ("CBRT_RATE_DECISION", "TR", "TRY", "CBRT_POLICY_RATE"),
        ("FED_CHAIR_SPEECH_PLACEHOLDER", "US", "USD", "NONE"),
        ("ECB_PRESIDENT_SPEECH_PLACEHOLDER", "EU", "EUR", "NONE")
    ]
    return [EconomicEvent(build_economic_event_id(e[0], e[1]), e[0], e[0], "event_central_bank_policy", e[1], e[2], e[3], "event_importance_high", "monthly/periodic", "no revision", "calendar_provider_ready", []) for e in events]

def build_inflation_events(profile: CalendarProviderProfile) -> List[EconomicEvent]:
    events = [
        ("US_CPI_RELEASE", "US", "USD", "US_CPI_YOY"),
        ("US_CORE_CPI_RELEASE", "US", "USD", "US_CORE_CPI_YOY"),
        ("EU_CPI_RELEASE", "EU", "EUR", "EU_CPI_YOY"),
        ("UK_CPI_RELEASE", "UK", "GBP", "UK_CPI_YOY"),
        ("TR_CPI_RELEASE", "TR", "TRY", "TR_CPI_YOY"),
        ("JP_CPI_RELEASE", "JP", "JPY", "JP_CPI_YOY")
    ]
    return [EconomicEvent(build_economic_event_id(e[0], e[1]), e[0], e[0], "event_inflation", e[1], e[2], e[3], "event_importance_high", "monthly", "can be revised", "calendar_provider_ready", []) for e in events]

def build_labor_events(profile: CalendarProviderProfile) -> List[EconomicEvent]:
    events = [
        ("US_NONFARM_PAYROLLS_RELEASE", "US", "USD", "US_NONFARM_PAYROLLS"),
        ("US_UNEMPLOYMENT_RELEASE", "US", "USD", "US_UNEMPLOYMENT_RATE"),
        ("EU_UNEMPLOYMENT_RELEASE", "EU", "EUR", "EU_UNEMPLOYMENT_RATE"),
        ("UK_UNEMPLOYMENT_RELEASE", "UK", "GBP", "UK_UNEMPLOYMENT_RATE"),
        ("TR_UNEMPLOYMENT_RELEASE", "TR", "TRY", "TR_UNEMPLOYMENT_RATE")
    ]
    return [EconomicEvent(build_economic_event_id(e[0], e[1]), e[0], e[0], "event_labor", e[1], e[2], e[3], "event_importance_high", "monthly", "often revised", "calendar_provider_ready", []) for e in events]

def build_growth_events(profile: CalendarProviderProfile) -> List[EconomicEvent]:
    events = [
        ("US_GDP_RELEASE", "US", "USD", "US_GDP_QOQ"),
        ("EU_GDP_RELEASE", "EU", "EUR", "EU_GDP_QOQ"),
        ("UK_GDP_RELEASE", "UK", "GBP", "UK_GDP_QOQ"),
        ("TR_GDP_RELEASE", "TR", "TRY", "TR_GDP_YOY"),
        ("CHINA_GDP_RELEASE", "CN", "CNY", "CN_GDP_YOY")
    ]
    return [EconomicEvent(build_economic_event_id(e[0], e[1]), e[0], e[0], "event_growth", e[1], e[2], e[3], "event_importance_high", "quarterly", "revised multiple times", "calendar_provider_ready", []) for e in events]

def build_pmi_sentiment_events(profile: CalendarProviderProfile) -> List[EconomicEvent]:
    events = [
        ("US_ISM_PMI_RELEASE", "US", "USD", "US_ISM_PMI"),
        ("EU_PMI_RELEASE", "EU", "EUR", "EU_PMI"),
        ("UK_PMI_RELEASE", "UK", "GBP", "UK_PMI"),
        ("CHINA_PMI_RELEASE", "CN", "CNY", "CN_PMI"),
        ("GLOBAL_PMI_PLACEHOLDER", "GLOBAL", "NONE", "GLOBAL_PMI")
    ]
    return [EconomicEvent(build_economic_event_id(e[0], e[1]), e[0], e[0], "event_pmi_sentiment", e[1], e[2], e[3], "event_importance_medium", "monthly", "sometimes revised", "calendar_provider_ready", []) for e in events]

def build_energy_inventory_events(profile: CalendarProviderProfile) -> List[EconomicEvent]:
    events = [
        ("US_EIA_CRUDE_INVENTORY_PLACEHOLDER", "US", "USD", "US_CRUDE_INV"),
        ("US_EIA_NATURAL_GAS_STORAGE_PLACEHOLDER", "US", "USD", "US_NATGAS_INV")
    ]
    return [EconomicEvent(build_economic_event_id(e[0], e[1]), e[0], e[0], "event_energy_inventory", e[1], e[2], e[3], "event_importance_medium", "weekly", "rarely revised", "calendar_provider_ready", []) for e in events]

def build_default_economic_events(profile: CalendarProviderProfile) -> List[EconomicEvent]:
    events = []
    events.extend(build_central_bank_events(profile))
    events.extend(build_inflation_events(profile))
    events.extend(build_labor_events(profile))
    events.extend(build_growth_events(profile))
    events.extend(build_pmi_sentiment_events(profile))
    events.extend(build_energy_inventory_events(profile))
    return events

def build_economic_event_universe_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_economic_events(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_economic_event_universe(df)
    return df, summary

def summarize_economic_event_universe(df: pd.DataFrame) -> Dict:
    return {
        "total_events": len(df),
        "categories": df["category_label"].nunique() if not df.empty else 0
    }
