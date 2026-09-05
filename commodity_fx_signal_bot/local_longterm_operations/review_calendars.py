"""Review calendars."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile
from .longterm_models import ReviewCalendarItem, build_review_calendar_item_id, review_calendar_item_to_dict

def build_default_review_calendar_items(profile: LocalLongTermOperationsProfile) -> list[ReviewCalendarItem]:
    items = []
    cads = ["yearly", "quarterly", "monthly", "weekly"]
    areas = ["architecture", "safety", "release dossier", "roadmap", "deprecation candidates", "DataLake", "reports", "generated docs", "quality reports", "incident/redteam/governance outputs", "status scripts", "quality scripts", "retention review", "open risks", "operator reading order", "no-go/safe-go", "latest generated outputs", "manual review items"]
    for c in cads:
        for a in areas:
            items.append(ReviewCalendarItem(
                calendar_id=build_review_calendar_item_id(f"{c}_review", a),
                calendar_name=f"{c}_review",
                cadence=c,
                review_area=a,
                calendar_status="calendar_rehearsal_manual_review",
                expected_manual_action="Review offline generated output.",
                warnings=["Gerçek scheduler veya calendar entegrasyonu değildir.", "Background daemon yoktur."]
            ))
    return items

def build_yearly_review_calendar_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    items = [i for i in build_default_review_calendar_items(profile) if i.cadence == "yearly"]
    df = pd.DataFrame([review_calendar_item_to_dict(i) for i in items])
    return df, summarize_review_calendar(df)

def build_quarterly_review_calendar_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    items = [i for i in build_default_review_calendar_items(profile) if i.cadence == "quarterly"]
    df = pd.DataFrame([review_calendar_item_to_dict(i) for i in items])
    return df, summarize_review_calendar(df)

def build_monthly_maintenance_calendar_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    items = [i for i in build_default_review_calendar_items(profile) if i.cadence == "monthly"]
    df = pd.DataFrame([review_calendar_item_to_dict(i) for i in items])
    return df, summarize_review_calendar(df)

def build_weekly_operator_review_calendar_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    items = [i for i in build_default_review_calendar_items(profile) if i.cadence == "weekly"]
    df = pd.DataFrame([review_calendar_item_to_dict(i) for i in items])
    return df, summarize_review_calendar(df)

def summarize_review_calendar(df: pd.DataFrame) -> dict:
    return {"total_items": len(df), "status_counts": df["calendar_status"].value_counts().to_dict() if not df.empty else {}}
