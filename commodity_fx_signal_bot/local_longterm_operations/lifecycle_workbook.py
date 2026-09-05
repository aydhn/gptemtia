"""Lifecycle maintenance workbook."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile
from .longterm_models import LifecycleWorkbookItem, build_lifecycle_workbook_item_id, lifecycle_workbook_item_to_dict

def build_default_lifecycle_workbook_items(profile: LocalLongTermOperationsProfile) -> list[LifecycleWorkbookItem]:
    areas = ["data", "models", "reports", "docs"]
    items = []
    for a in areas:
        items.append(LifecycleWorkbookItem(
            workbook_id=build_lifecycle_workbook_item_id(a, "Is it clean?"),
            workbook_area=a,
            lifecycle_status="lifecycle_rehearsal_needs_manual_review",
            review_question="Is it clean?",
            evidence_refs=["local_reports"],
            manual_review_required=True,
            warnings=["Official lifecycle policy değildir."]
        ))
    return items

def build_lifecycle_maintenance_workbook(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_lifecycle_workbook_items(profile)
    df = pd.DataFrame([lifecycle_workbook_item_to_dict(i) for i in items])
    return df, summarize_lifecycle_maintenance_workbook(df)

def summarize_lifecycle_maintenance_workbook(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
