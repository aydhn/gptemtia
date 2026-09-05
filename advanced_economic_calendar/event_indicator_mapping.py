import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import EventIndicatorMapping, build_event_indicator_mapping_id

def build_default_event_indicator_mappings(profile: CalendarProviderProfile) -> List[EventIndicatorMapping]:
    return [
        EventIndicatorMapping(build_event_indicator_mapping_id("US_CPI_RELEASE", "US_CPI_YOY"), "US_CPI_RELEASE", "US_CPI_YOY", "US", "USD", "Direct map", True),
        EventIndicatorMapping(build_event_indicator_mapping_id("US_CORE_CPI_RELEASE", "US_CORE_CPI_YOY"), "US_CORE_CPI_RELEASE", "US_CORE_CPI_YOY", "US", "USD", "Direct map", True),
        EventIndicatorMapping(build_event_indicator_mapping_id("US_NONFARM_PAYROLLS_RELEASE", "US_NONFARM_PAYROLLS"), "US_NONFARM_PAYROLLS_RELEASE", "US_NONFARM_PAYROLLS", "US", "USD", "Direct map", True),
        EventIndicatorMapping(build_event_indicator_mapping_id("FOMC_RATE_DECISION", "FED_POLICY_RATE"), "FOMC_RATE_DECISION", "FED_POLICY_RATE", "US", "USD", "Direct map", True),
        EventIndicatorMapping(build_event_indicator_mapping_id("ECB_RATE_DECISION", "ECB_POLICY_RATE"), "ECB_RATE_DECISION", "ECB_POLICY_RATE", "EU", "EUR", "Direct map", True),
        EventIndicatorMapping(build_event_indicator_mapping_id("CBRT_RATE_DECISION", "CBRT_POLICY_RATE"), "CBRT_RATE_DECISION", "CBRT_POLICY_RATE", "TR", "TRY", "Direct map", True),
        EventIndicatorMapping(build_event_indicator_mapping_id("US_GDP_RELEASE", "US_GDP_QOQ"), "US_GDP_RELEASE", "US_GDP_QOQ", "US", "USD", "Direct map", True),
        EventIndicatorMapping(build_event_indicator_mapping_id("EU_GDP_RELEASE", "EU_GDP_QOQ"), "EU_GDP_RELEASE", "EU_GDP_QOQ", "EU", "EUR", "Direct map", True),
        EventIndicatorMapping(build_event_indicator_mapping_id("US_EIA_CRUDE_INVENTORY_PLACEHOLDER", "commodity/macro energy inventory placeholder"), "US_EIA_CRUDE_INVENTORY_PLACEHOLDER", "commodity/macro energy inventory placeholder", "US", "USD", "Placeholder", True)
    ]

def build_event_region_currency_indicator_mapping_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_event_indicator_mappings(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_event_indicator_mapping(df)
    return df, summary

def summarize_event_indicator_mapping(df: pd.DataFrame) -> Dict:
    return {
        "total_mappings": len(df)
    }
