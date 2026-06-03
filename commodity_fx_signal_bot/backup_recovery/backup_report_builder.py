"""
Backup report building utilities.
"""

import pandas as pd

def build_backup_disclaimer() -> str:
    return (
        "*** WARNING / UYARI ***\n"
        "Bu rapor offline/local backup-restore dry-run ve disaster recovery planning çıktısıdır; "
        "gerçek emir, canlı sinyal, model deployment, broker talimatı, production scheduler, "
        "cloud backup, otomatik restore veya yatırım tavsiyesi değildir. "
        "Varsayılan davranış dry-run ve manifest üretimidir.\n"
        "***********************\n"
    )

def build_project_state_inventory_markdown_report(summary: dict, inventory_df: pd.DataFrame | None = None) -> str:
    return build_backup_disclaimer() + "# Project State Inventory\n\n" + str(summary)

def build_backup_manifest_markdown_report(summary: dict, manifest_json: dict | None = None) -> str:
    return build_backup_disclaimer() + "# Backup Manifest\n\n" + str(summary)

def build_backup_dry_run_markdown_report(summary: dict, backup_plan_df: pd.DataFrame | None = None) -> str:
    return build_backup_disclaimer() + "# Backup Dry-Run Plan\n\n" + str(summary)

def build_restore_dry_run_markdown_report(summary: dict, restore_plan_df: pd.DataFrame | None = None) -> str:
    return build_backup_disclaimer() + "# Restore Dry-Run Plan\n\n" + str(summary)

def build_disaster_recovery_markdown_report(summary: dict, dr_manifest: dict | None = None) -> str:
    return build_backup_disclaimer() + "# Disaster Recovery Manifest\n\n" + str(summary)

def build_restore_verification_markdown_report(summary: dict, verification_df: pd.DataFrame | None = None) -> str:
    return build_backup_disclaimer() + "# Restore Verification\n\n" + str(summary)

def build_backup_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return build_backup_disclaimer() + "# Backup Quality\n\n" + str(summary)

def build_backup_recovery_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return build_backup_disclaimer() + "# Backup Recovery Status\n\n" + str(summary)
