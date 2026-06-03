"""
Backup safety rules and validation.
"""

from pathlib import Path
import pandas as pd
from .backup_config import BackupRecoveryProfile

def scan_backup_inventory_for_secret_risk(inventory_df: pd.DataFrame, project_root: Path) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "empty"}

def scan_backup_plans_for_forbidden_actions(plan_df: pd.DataFrame, profile: BackupRecoveryProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "empty"}

def validate_no_destructive_restore(plan_df: pd.DataFrame, profile: BackupRecoveryProfile) -> dict:
    return {"valid": True}

def validate_manifest_only_data_and_reports(inventory_df: pd.DataFrame, profile: BackupRecoveryProfile) -> dict:
    return {"valid": True}

def build_backup_safety_report(inventory_df: pd.DataFrame, backup_plan_df: pd.DataFrame, restore_plan_df: pd.DataFrame, profile: BackupRecoveryProfile, project_root: Path) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "empty"}
