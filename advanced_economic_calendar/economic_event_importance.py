import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import EventImportanceRule, build_event_importance_rule_id

def build_default_event_importance_rules(profile: CalendarProviderProfile) -> List[EventImportanceRule]:
    return [
        EventImportanceRule(build_event_importance_rule_id("event_central_bank_policy", "GLOBAL"), "event_central_bank_policy", "GLOBAL", "event_importance_high", "Central bank decisions move markets", True),
        EventImportanceRule(build_event_importance_rule_id("event_inflation", "GLOBAL"), "event_inflation", "GLOBAL", "event_importance_high", "Inflation affects interest rates", True),
        EventImportanceRule(build_event_importance_rule_id("event_labor", "US"), "event_labor", "US", "event_importance_high", "US labor data is critical", True)
    ]

def build_economic_event_importance_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_event_importance_rules(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_event_importance(df)
    return df, summary

def summarize_event_importance(df: pd.DataFrame) -> Dict:
    return {
        "total_rules": len(df)
    }
