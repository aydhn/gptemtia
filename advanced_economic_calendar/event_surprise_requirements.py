import pandas as pd
from typing import Tuple, Dict
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile

def build_default_event_surprise_requirements(profile: CalendarProviderProfile) -> pd.DataFrame:
    reqs = [
        {"event_category": "event_inflation", "formula_placeholder": "surprise = actual - forecast", "direction_interpretation_note": "Positive surprise may lead to rate hike expectations", "normalization_need": "Normalize by historical standard deviation", "future_phase_owner": "Phase 113", "manual_review_required": True},
        {"event_category": "event_labor", "formula_placeholder": "surprise = actual - forecast", "direction_interpretation_note": "Positive surprise implies strong economy", "normalization_need": "Normalize by historical standard deviation", "future_phase_owner": "Phase 113", "manual_review_required": True},
        {"event_category": "event_growth", "formula_placeholder": "normalized_surprise = (actual - forecast) / historical_std_placeholder", "direction_interpretation_note": "Positive surprise implies strong economy", "normalization_need": "Normalize by historical standard deviation", "future_phase_owner": "Phase 113", "manual_review_required": True}
    ]
    return pd.DataFrame(reqs)

def build_event_surprise_calculation_requirement_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_event_surprise_requirements(profile)
    summary = summarize_event_surprise_requirements(df)
    return df, summary

def summarize_event_surprise_requirements(df: pd.DataFrame) -> Dict:
    return {
        "total_requirements": len(df)
    }
