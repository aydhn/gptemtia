import pandas as pd
from typing import Tuple, Dict
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile

def build_default_event_time_normalization_requirements(profile: CalendarProviderProfile) -> pd.DataFrame:
    reqs = [
        {"time_field": "scheduled_time", "timezone_policy": "UTC", "session_alignment_note": "Align with market hours", "release_delay_handling": "Log delays", "future_phase_owner": "Phase 113", "manual_review_required": True},
        {"time_field": "actual_release_time", "timezone_policy": "UTC", "session_alignment_note": "Align with market hours", "release_delay_handling": "Calculate delay", "future_phase_owner": "Phase 113", "manual_review_required": True}
    ]
    return pd.DataFrame(reqs)

def build_event_time_normalization_requirement_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_event_time_normalization_requirements(profile)
    summary = summarize_event_time_normalization_requirements(df)
    return df, summary

def summarize_event_time_normalization_requirements(df: pd.DataFrame) -> Dict:
    return {
        "total_requirements": len(df)
    }
