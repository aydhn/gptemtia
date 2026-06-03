"""
Recovery runbook generator.
"""

from pathlib import Path
import pandas as pd
from .backup_config import BackupRecoveryProfile

def build_project_state_recovery_runbook(manifest: dict, restore_plan_df: pd.DataFrame, verification_df: pd.DataFrame, profile: BackupRecoveryProfile) -> tuple[str, dict]:
    text = "# Project State Recovery Runbook\n\n"
    text += "Bu dokuman offline/local backup-restore dry-run ve disaster recovery planning ciktisidir.\n"
    return text, {"length": len(text)}

def build_recovery_runbook_sections(manifest: dict, restore_plan_df: pd.DataFrame, verification_df: pd.DataFrame) -> list[dict]:
    return []

def build_recovery_troubleshooting_section(verification_df: pd.DataFrame) -> str:
    return "Troubleshooting:\n"

def save_recovery_runbook(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
