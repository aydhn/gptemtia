import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def classify_integrity_verification_method(item_row: pd.Series, profile: LocalArchiveProfile) -> str:
    status = item_row.get("integrity_status", "integrity_unknown")
    if status == "integrity_hash_available": return "sha256_manifest_check"
    elif status == "integrity_hash_skipped_large_file": return "skipped_large_file_manual_check"
    elif status == "integrity_missing_hash": return "file_presence_check"
    return "manual_open_check"

def build_archive_integrity_verification_plan(item_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    plan = []
    if not item_df.empty and 'item_status' in item_df.columns:
        cand_df = item_df[item_df['item_status'] == 'archive_candidate'].copy()
        for _, row in cand_df.iterrows():
            plan.append({
                "item_id": row.get('item_id', ''),
                "relative_path": row.get('relative_path', ''),
                "integrity_status": row.get('integrity_status', 'unknown'),
                "verification_method": classify_integrity_verification_method(row, profile)
            })
    df = pd.DataFrame(plan)
    return df, summarize_integrity_verification_plan(df)

def summarize_integrity_verification_plan(plan_df: pd.DataFrame) -> Dict:
    if plan_df.empty: return {"total_items": 0}
    return {
        "total_items_in_plan": len(plan_df),
        "notice": "Verification plan is read-only. Offline hash calculation is required during actual restore."
    }
