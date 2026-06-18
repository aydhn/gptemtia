import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile
from .readiness_models import OperatorChecklistItem, build_operator_checklist_item_id

def build_pre_handoff_stabilization_checklist(profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    items = [
        OperatorChecklistItem(
            item_id=build_operator_checklist_item_id("stabilization", "Verify no gaps"),
            checklist_name="stabilization",
            domain="gaps",
            instruction="Check gaps register",
            expected_output="No critical gaps",
            status="pending",
            safe_command="python -m scripts.run_readiness_reports",
            warnings=[]
        )
    ]
    from .readiness_models import operator_checklist_item_to_dict
    df = pd.DataFrame([operator_checklist_item_to_dict(i) for i in items])
    return df, summarize_stabilization_checklist(df)

def build_stabilization_domains() -> pd.DataFrame:
    domains = [
        "docs", "tests", "reports", "DataLake", "secrets hygiene", "backup/restore dry-run",
        "portable packaging", "evidence governance", "artifact metadata", "local graph",
        "local timeline", "local consistency", "operator checklist", "known gaps", "known limitations"
    ]
    return pd.DataFrame({"domain": domains})

def map_stabilization_items_to_known_gaps(gap_df: pd.DataFrame | None, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    if gap_df is None or gap_df.empty:
        df = pd.DataFrame(columns=["gap", "stabilization_plan"])
    else:
        df = gap_df.copy()
        df["stabilization_plan"] = "manual_review"
    return df, {"mapped": len(df)}

def summarize_stabilization_checklist(stabilization_df: pd.DataFrame) -> dict:
    return {
        "total_items": len(stabilization_df)
    }
