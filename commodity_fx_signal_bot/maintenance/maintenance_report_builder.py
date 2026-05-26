"""Maintenance Report Builder for offline maintenance."""
import pandas as pd
from typing import Dict, Optional

def build_maintenance_disclaimer() -> str:
    return (
        "*** DISCLAIMER ***\n"
        "Bu rapor offline data retention/storage lifecycle maintenance çıktısıdır; "
        "gerçek emir, canlı sinyal, model deployment, broker talimatı, production scheduler "
        "veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        "dosyalar otomatik silinmez veya taşınmaz.\n"
        "******************\n\n"
    )

def build_storage_inventory_markdown_report(summary: Dict, inventory_df: Optional[pd.DataFrame] = None) -> str:
    md = build_maintenance_disclaimer()
    md += "# Storage Inventory Report\n\n"
    md += f"- **Total Files:** {summary.get('total_files', 0)}\n"
    md += f"- **Total Size (Bytes):** {summary.get('total_size_bytes', 0)}\n"
    md += f"- **Protected Files:** {summary.get('protected_files', 0)}\n"
    return md

def build_retention_policy_markdown_report(summary: Dict, policies_df: Optional[pd.DataFrame] = None) -> str:
    md = build_maintenance_disclaimer()
    md += "# Retention Policies Report\n\n"
    md += f"- **Total Policies:** {summary.get('total_policies', 0)}\n"
    return md

def build_cleanup_dry_run_markdown_report(summary: Dict, cleanup_df: Optional[pd.DataFrame] = None) -> str:
    md = build_maintenance_disclaimer()
    md += "# Cleanup Dry-Run Report\n\n"
    md += f"- **Cleanup Candidates:** {summary.get('candidate_count', 0)}\n"
    md += f"- **Reclaimable Storage (Bytes):** {summary.get('reclaimable_bytes', 0)}\n"
    return md

def build_archive_dry_run_markdown_report(summary: Dict, archive_df: Optional[pd.DataFrame] = None) -> str:
    md = build_maintenance_disclaimer()
    md += "# Archive Dry-Run Report\n\n"
    md += f"- **Archive Candidates:** {summary.get('candidate_count', 0)}\n"
    md += f"- **Total Archive Size (Bytes):** {summary.get('total_size_bytes', 0)}\n"
    return md

def build_storage_lifecycle_markdown_report(summary: Dict, health_df: Optional[pd.DataFrame] = None) -> str:
    md = build_maintenance_disclaimer()
    md += "# Storage Lifecycle Health Report\n\n"
    md += f"- **Storage Pressure Score:** {summary.get('score', 0.0)}\n"
    md += f"- **Health Label:** {summary.get('label', 'unknown')}\n"
    return md

def build_maintenance_status_markdown_report(summary: Dict, status_df: Optional[pd.DataFrame] = None) -> str:
    md = build_maintenance_disclaimer()
    md += "# Maintenance Status Report\n\n"
    md += f"- **Status:** {summary.get('status', 'OK')}\n"
    return md
