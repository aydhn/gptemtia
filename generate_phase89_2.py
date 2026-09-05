import os
from pathlib import Path

def create_files():
    base_dir = Path("commodity_fx_signal_bot/local_longterm_operations")
    
    with open(base_dir / "review_calendars.py", "w", encoding="utf-8") as f:
        f.write('''"""Review calendars."""
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
''')

    with open(base_dir / "lifecycle_workbook.py", "w", encoding="utf-8") as f:
        f.write('''"""Lifecycle maintenance workbook."""
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
''')

    with open(base_dir / "maintenance_cadence.py", "w", encoding="utf-8") as f:
        f.write('''"""Maintenance cadence."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_maintenance_cadence_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"cadence": "yearly", "action": "full_review", "warnings": ["scheduler oluşturmaz"]},
        {"cadence": "monthly", "action": "quick_check", "warnings": ["scheduler oluşturmaz"]}
    ])

def build_maintenance_cadence_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_maintenance_cadence_items(profile)
    return df, summarize_maintenance_cadence(df)

def summarize_maintenance_cadence(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
''')

    with open(base_dir / "maintenance_ownership.py", "w", encoding="utf-8") as f:
        f.write('''"""Maintenance ownership."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_maintenance_ownership_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"area": "all", "owner": "local_analyst", "warnings": ["gerçek organizasyon yetkisi değildir"]}
    ])

def build_maintenance_ownership_rehearsal_matrix(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_maintenance_ownership_items(profile)
    return df, summarize_maintenance_ownership(df)

def summarize_maintenance_ownership(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
''')

    with open(base_dir / "maintenance_evidence.py", "w", encoding="utf-8") as f:
        f.write('''"""Maintenance evidence."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile

def build_default_maintenance_evidence_items(profile: LocalLongTermOperationsProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"evidence_id": "ev_01", "type": "report", "warnings": ["audit proof değildir", "manual_review_required bağlamında kalmalı"]}
    ])

def build_maintenance_evidence_checklist(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_maintenance_evidence_items(profile)
    return df, summarize_maintenance_evidence(df)

def summarize_maintenance_evidence(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
''')

if __name__ == "__main__":
    create_files()
