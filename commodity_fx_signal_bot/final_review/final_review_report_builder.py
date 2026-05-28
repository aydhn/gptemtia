import pandas as pd
from typing import Dict, Optional

def build_final_review_disclaimer() -> str:
    return "DISCLAIMER: Bu rapor offline final system review/release readiness dry-run çıktısıdır; gerçek emir, canlı sinyal, model deployment, broker talimatı, production release, otomatik trade onayı veya yatırım tavsiyesi değildir."

def build_final_system_review_markdown_report(summary: dict, audit_tables: Optional[Dict[str, pd.DataFrame]] = None) -> str:
    lines = ["# Final System Review Report", "", build_final_review_disclaimer(), ""]

    lines.append(f"- Passed: {summary.get('passed', False)}")

    if audit_tables:
        for name, df in audit_tables.items():
            lines.append(f"## {name}")
            lines.append(df.to_markdown(index=False))
            lines.append("")

    return "\n".join(lines)

def build_architecture_audit_markdown_report(summary: dict, audit_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Architecture Audit Report", "", build_final_review_disclaimer(), ""]
    if audit_df is not None and not audit_df.empty:
        lines.append(audit_df.to_markdown(index=False))
    return "\n".join(lines)

def build_safety_audit_markdown_report(summary: dict, safety_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Safety Audit Report", "", build_final_review_disclaimer(), ""]
    lines.append(f"- Passed: {summary.get('passed', False)}")
    lines.append(f"- Critical Issues: {summary.get('critical_issues', 0)}")
    lines.append("")
    if safety_df is not None and not safety_df.empty:
        lines.append(safety_df.to_markdown(index=False))
    return "\n".join(lines)

def build_offline_acceptance_markdown_report(summary: dict, acceptance_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Offline Acceptance Audit Report", "", build_final_review_disclaimer(), ""]
    if acceptance_df is not None and not acceptance_df.empty:
        lines.append(acceptance_df.to_markdown(index=False))
    return "\n".join(lines)

def build_release_readiness_dry_run_markdown_report(summary: dict, dry_run_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Release Readiness Dry-Run Report", "", build_final_review_disclaimer(), ""]
    lines.append(f"- Ready: {summary.get('is_ready', False)}")
    lines.append("")
    if dry_run_df is not None and not dry_run_df.empty:
        lines.append(dry_run_df.to_markdown(index=False))
    return "\n".join(lines)

def build_final_consolidation_markdown_report(summary: dict, phase_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Final Consolidation Audit Report", "", build_final_review_disclaimer(), ""]
    if phase_df is not None and not phase_df.empty:
        lines.append(phase_df.to_markdown(index=False))
    return "\n".join(lines)
