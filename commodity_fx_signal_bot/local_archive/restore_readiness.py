import pandas as pd
from typing import Tuple, Dict, Optional
from .archive_config import LocalArchiveProfile

def build_archive_restore_readiness_checklist(item_df: pd.DataFrame, manifest: Optional[Dict], profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    steps = [
        {"step_id": "CHK_MAN", "description": "Is Cold Storage Manifest present?"},
        {"step_id": "CHK_HASH", "description": "Is Hash Manifest present?"},
        {"step_id": "CHK_EXC", "description": "Are exclusions properly documented?"}
    ]
    results = []
    for row in steps:
        status = "pass" if row["step_id"] == "CHK_MAN" and manifest else "pending"
        results.append({"step_id": row["step_id"], "description": row["description"], "status": status})
    df = pd.DataFrame(results)
    return df, summarize_restore_readiness(df)

def summarize_restore_readiness(checklist_df: pd.DataFrame) -> Dict:
    if checklist_df.empty: return {"total_checks": 0}
    passed = int((checklist_df['status'] == 'pass').sum())
    return {"total_checks": len(checklist_df), "passed": passed, "notice": "Restore readiness checklist is a manual guide."}
