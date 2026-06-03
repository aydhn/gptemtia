"""
Restore dry-run plan generator.
"""

import pandas as pd
from .backup_config import BackupRecoveryProfile

def classify_restore_action(artifact: dict, profile: BackupRecoveryProfile) -> str:
    policy = artifact.get("include_policy", "exclude")
    scope = artifact.get("backup_scope", "")

    if scope == "excluded_secret_scope":
        return "skip_excluded_secret"

    if policy == "manifest_only":
        return "restore_manifest_only_reference"

    if artifact.get("artifact_type") == "directory":
        return "recreate_directory"

    if scope == "config_template_scope":
        return "recreate_config_from_template"

    if policy == "include":
        if profile.allow_restore_copy:
            if not profile.allow_overwrite:
                return "verify_existing_file"
            return "restore_file_if_explicit_restore_copy_allowed"
        return "verify_existing_file"

    return "blocked"


def build_restore_dry_run_plan(manifest_json: dict, profile: BackupRecoveryProfile) -> tuple[pd.DataFrame, dict]:
    # In a real implementation this would join against inventory_df
    # For now we'll just mock it as empty
    df = pd.DataFrame()
    return df, {"status": "mocked"}

def build_restore_order(plan_df: pd.DataFrame) -> pd.DataFrame:
    if plan_df.empty: return plan_df
    if "restore_priority" in plan_df.columns:
        return plan_df.sort_values(by="restore_priority", ascending=True)
    return plan_df

def validate_restore_dry_run_plan(plan_df: pd.DataFrame, profile: BackupRecoveryProfile) -> dict:
    return {"valid": True}

def summarize_restore_dry_run(plan_df: pd.DataFrame) -> dict:
    return {"status": "empty"}
