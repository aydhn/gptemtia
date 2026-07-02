import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def identify_items_due_for_retention_review(item_df: pd.DataFrame, policy_df: pd.DataFrame, profile: LocalArchiveProfile) -> pd.DataFrame:
    if item_df.empty or policy_df.empty or 'item_status' not in item_df.columns:
        return pd.DataFrame()
    due = item_df[item_df['item_status'] == 'archive_candidate'].copy()
    if 'domain_label' in due.columns and 'domain_label' in policy_df.columns:
        due = due.merge(policy_df[['domain_label', 'review_interval_days', 'retention_label']], on='domain_label', how='left')
    due['review_reason'] = "Periodic manual review"
    return due

def build_retention_review_checklist(policy_df: pd.DataFrame, item_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame([
        {"task": "Are long-term artifacts still relevant?", "status": "pending"},
        {"task": "Are excluded paths still excluded properly?", "status": "pending"},
        {"task": "Do generated outputs need a refresh?", "status": "pending"},
        {"task": "Do stale docs need an updated archive snapshot?", "status": "pending"},
        {"task": "Does the hash manifest need a refresh?", "status": "pending"},
        {"task": "Has the cold storage manifest been reviewed manually?", "status": "pending"}
    ])
    return df, summarize_retention_review(df)

def summarize_retention_review(review_df: pd.DataFrame) -> Dict:
    if review_df.empty: return {"tasks": 0}
    return {
        "total_checklist_items": len(review_df),
        "notice": "This is a manual checklist. Deletion must be done manually by the operator."
    }
