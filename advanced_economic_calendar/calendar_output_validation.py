import pandas as pd
from typing import Tuple, Dict
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile

def build_default_calendar_output_validation_rules(profile: CalendarProviderProfile) -> pd.DataFrame:
    rules = [
        {"rule_id": "val_1", "target_schema": "calendar_event", "field_name": "event_status", "rule_description": "Validate status format", "severity": "medium", "future_phase_owner": "Phase 112", "manual_review_required": True},
        {"rule_id": "val_2", "target_schema": "release_event", "field_name": "scheduled_time", "rule_description": "Check for missing/stale events", "severity": "high", "future_phase_owner": "Phase 112", "manual_review_required": True},
        {"rule_id": "val_3", "target_schema": "release_event", "field_name": "actual_release_time", "rule_description": "Timezone alignment check", "severity": "medium", "future_phase_owner": "Phase 113", "manual_review_required": True},
        {"rule_id": "val_4", "target_schema": "release_event", "field_name": "surprise_value", "rule_description": "Surprise calculation handling", "severity": "low", "future_phase_owner": "Phase 113", "manual_review_required": True},
        {"rule_id": "val_5", "target_schema": "release_event", "field_name": "revision_status", "rule_description": "Revision checks", "severity": "medium", "future_phase_owner": "Phase 115", "manual_review_required": True}
    ]
    return pd.DataFrame(rules)

def build_calendar_output_validation_contract(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_calendar_output_validation_rules(profile)
    summary = summarize_calendar_output_validation(df)
    return df, summary

def summarize_calendar_output_validation(df: pd.DataFrame) -> Dict:
    return {
        "total_rules": len(df)
    }
