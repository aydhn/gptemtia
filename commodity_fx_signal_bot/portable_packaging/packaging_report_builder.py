import pandas as pd
from typing import Dict, Any, Optional

def build_packaging_disclaimer() -> str:
    return "> **UYARI:** Bu rapor offline/local packaging ve install verification çıktısıdır; gerçek emir, canlı sinyal, model deployment, broker talimatı, package publish, production scheduler veya yatırım tavsiyesi değildir."

def build_environment_snapshot_markdown_report(summary: Dict[str, Any], packages_df: Optional[pd.DataFrame] = None) -> str:
    md = f"# Environment Snapshot Report\n\n{build_packaging_disclaimer()}\n\n"
    md += f"- Python Version: {summary.get('python_version', 'Unknown')}\n"
    md += f"- Platform: {summary.get('platform', 'Unknown')}\n"
    md += f"- Packages Count: {summary.get('package_count', 0)}\n"
    return md

def build_dependency_inventory_markdown_report(summary: Dict[str, Any], dependency_df: Optional[pd.DataFrame] = None) -> str:
    md = f"# Dependency Inventory Report\n\n{build_packaging_disclaimer()}\n\n"
    md += f"- Total Packages: {summary.get('total_packages', 0)}\n"
    md += f"- Missing Requirements: {summary.get('missing_requirements', 0)}\n"
    return md

def build_requirements_export_markdown_report(summary: Dict[str, Any], export_df: Optional[pd.DataFrame] = None) -> str:
    md = f"# Requirements Export Report\n\n{build_packaging_disclaimer()}\n\n"
    md += f"- Files Created: {summary.get('files_created', 0)}\n"
    return md

def build_install_verification_markdown_report(summary: Dict[str, Any], install_df: Optional[pd.DataFrame] = None) -> str:
    md = f"# Install Verification Report\n\n{build_packaging_disclaimer()}\n\n"
    md += f"- Passed Checks: {summary.get('passed_checks', 0)} / {summary.get('total_checks', 0)}\n"
    return md

def build_portable_bundle_manifest_markdown_report(summary: Dict[str, Any], artifact_df: Optional[pd.DataFrame] = None) -> str:
    md = f"# Portable Bundle Manifest Report\n\n{build_packaging_disclaimer()}\n\n"
    md += f"- Included Artifacts: {summary.get('included_artifacts', 0)} / {summary.get('total_artifacts', 0)}\n"
    return md

def build_packaging_quality_markdown_report(summary: Dict[str, Any], quality: Dict[str, Any]) -> str:
    md = f"# Packaging Quality Report\n\n{build_packaging_disclaimer()}\n\n"
    md += f"- Passed: {quality.get('passed', False)}\n"
    return md

def build_packaging_status_markdown_report(summary: Dict[str, Any], status_df: Optional[pd.DataFrame] = None) -> str:
    md = f"# Packaging Status Report\n\n{build_packaging_disclaimer()}\n\n"
    md += f"Status overview.\n"
    return md
