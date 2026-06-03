"""
Backup dry-run plan generator.
"""

import pandas as pd
from .backup_config import BackupRecoveryProfile

def classify_backup_action(row: pd.Series, profile: BackupRecoveryProfile) -> str:
    policy = row.get("include_policy", "exclude")
    scope = row.get("backup_scope", "")

    if scope == "excluded_secret_scope":
        return "exclude_secret"
    if scope == "excluded_cache_scope":
        return "exclude_cache"
    if scope == "excluded_large_artifact_scope":
        return "exclude_large_artifact"

    if policy == "manifest_only":
        return "manifest_only_reference"

    if policy == "include":
        if profile.allow_backup_copy:
            return "include_file_if_explicit_backup_copy_allowed"
        return "include_in_manifest"

    return "blocked"


def build_backup_dry_run_plan(inventory_df: pd.DataFrame, manifest_json: dict, profile: BackupRecoveryProfile) -> tuple[pd.DataFrame, dict]:
    if inventory_df is None or inventory_df.empty:
        return pd.DataFrame(), {"status": "empty"}

    df = inventory_df.copy()
    df["backup_action"] = df.apply(lambda row: classify_backup_action(row, profile), axis=1)

    summary = summarize_backup_dry_run(df)
    return df, summary


def estimate_backup_size(plan_df: pd.DataFrame) -> dict:
    if plan_df is None or plan_df.empty:
        return {"bytes": 0}
    b = plan_df[plan_df["backup_action"].isin(["include_in_manifest", "include_file_if_explicit_backup_copy_allowed"])]["size_bytes"].sum()
    return {"bytes": b, "mb": b / (1024*1024)}

def validate_backup_dry_run_plan(plan_df: pd.DataFrame, profile: BackupRecoveryProfile) -> dict:
    if not profile.allow_backup_copy:
        if "include_file_if_explicit_backup_copy_allowed" in plan_df["backup_action"].values:
            return {"valid": False, "error": "Plan includes actual copy but profile forbids it."}
    return {"valid": True}

def summarize_backup_dry_run(plan_df: pd.DataFrame) -> dict:
    if plan_df is None or plan_df.empty:
        return {"status": "empty"}
    return {
        "total_actions": len(plan_df),
        "manifest_only": len(plan_df[plan_df["backup_action"] == "manifest_only_reference"]),
        "excluded": len(plan_df[plan_df["backup_action"].str.startswith("exclude")])
    }
