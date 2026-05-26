"""Duplicate Artifact Detection for offline maintenance."""
import pandas as pd
from typing import Dict
from pathlib import Path

def detect_duplicate_files_by_name_size(inventory_df: pd.DataFrame) -> pd.DataFrame:
    if inventory_df.empty:
        return pd.DataFrame()

    df = inventory_df.copy()
    df["file_name"] = df["path"].apply(lambda p: Path(p).name)

    # Exclude tiny files from duplicate detection to avoid false positives
    df = df[df["size_bytes"] > 1024].copy()

    dupes = df[df.duplicated(subset=["file_name", "size_bytes"], keep=False)].copy()

    if dupes.empty:
        return pd.DataFrame()

    records = []
    group_id = 1
    for name_size, group in dupes.groupby(["file_name", "size_bytes"]):
        for _, row in group.iterrows():
            records.append({
                "duplicate_group_id": f"dup_grp_{group_id}",
                "artifact_id": row["artifact_id"],
                "relative_path": row["relative_path"],
                "file_name": row["file_name"],
                "size_bytes": row["size_bytes"],
                "modified_at_utc": row["modified_at_utc"],
                "duplicate_reason": "Same name and exact size",
                "recommended_action": "review_required_action",
                "warnings": []
            })
        group_id += 1

    return pd.DataFrame(records)

def detect_duplicate_reports_by_family(inventory_df: pd.DataFrame) -> pd.DataFrame:
    # Simplified placeholder
    return pd.DataFrame()

def detect_potential_duplicate_artifacts(inventory_df: pd.DataFrame) -> pd.DataFrame:
    return detect_duplicate_files_by_name_size(inventory_df)

def summarize_duplicate_artifacts(duplicate_df: pd.DataFrame) -> Dict:
    if duplicate_df.empty:
        return {"duplicate_count": 0}
    return {
        "duplicate_count": len(duplicate_df),
        "groups": duplicate_df["duplicate_group_id"].nunique() if "duplicate_group_id" in duplicate_df else 0
    }
