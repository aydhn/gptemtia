import pandas as pd
from typing import Dict, Optional

def build_archive_disclaimer() -> str:
    return "Bu çıktı offline/local archival strategy ve preservation planning raporudur. Cloud backup, yatırım tavsiyesi değildir."

def _df_to_md(df: pd.DataFrame) -> str:
    if df is None or df.empty: return "No data available."
    return df.to_markdown(index=False)

def build_archive_domain_registry_markdown_report(summary: Dict, domain_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Archive Domain Registry Report\n{build_archive_disclaimer()}\n\n{_df_to_md(domain_df)}"

def build_project_snapshot_catalog_markdown_report(summary: Dict, snapshot_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Project Snapshot Catalog Report\n{build_archive_disclaimer()}\n\n{_df_to_md(snapshot_df)}"

def build_cold_storage_manifest_markdown_report(summary: Dict, manifest: Optional[Dict] = None) -> str:
    return f"# Cold Storage Manifest Report\n{build_archive_disclaimer()}\n"

def build_archive_integrity_plan_markdown_report(summary: Dict, plan_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Archive Integrity Verification Plan\n{build_archive_disclaimer()}\n\n{_df_to_md(plan_df)}"

def build_preservation_binder_markdown_report(summary: Dict, binder_text: Optional[str] = None) -> str:
    return f"{binder_text if binder_text else '# Long-Horizon Preservation Binder'}\n{build_archive_disclaimer()}\n"

def build_archive_quality_markdown_report(summary: Dict, quality: Optional[Dict] = None) -> str:
    return f"# Archive Quality Report\n{build_archive_disclaimer()}\n"

def build_archive_status_markdown_report(summary: Dict, status_df: Optional[pd.DataFrame] = None) -> str:
    return f"# Local Archive Status Report\n{build_archive_disclaimer()}\n\n{_df_to_md(status_df)}"
