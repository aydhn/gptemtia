import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import EconomicEventCategory, build_economic_event_category_id
from advanced_economic_calendar.calendar_provider_labels import list_event_category_labels

def build_default_economic_event_categories(profile: CalendarProviderProfile) -> List[EconomicEventCategory]:
    categories = []
    for lbl in list_event_category_labels():
        categories.append(EconomicEventCategory(
            category_id=build_economic_event_category_id(lbl),
            category_label=lbl,
            category_name=lbl.replace("event_", "").replace("_", " ").title(),
            description=f"Category for {lbl}",
            example_events=[],
            warnings=[]
        ))
    return categories

def build_economic_event_category_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_economic_event_categories(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_economic_event_categories(df)
    return df, summary

def summarize_economic_event_categories(df: pd.DataFrame) -> Dict:
    return {
        "total_categories": len(df),
        "categories": df["category_label"].tolist() if not df.empty else []
    }
