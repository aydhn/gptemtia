import pandas as pd
from typing import Optional, Dict, Any

def build_maintenance_disclaimer() -> str:
    return (
        "> **DISCLAIMER:** Bu rapor offline/local long-term maintenance ve sustainability planning çıktısıdır; "
        "production scheduler, otomatik bakım daemon'u, canlı sinyal, broker talimatı, model deployment, "
        "resmi SLA veya yatırım tavsiyesi değildir. Bulgular manuel periyodik review ve sürdürülebilirlik "
        "planlaması amaçlıdır."
    )

def build_maintenance_domain_registry_markdown_report(summary: Dict[str, Any], domain_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Maintenance Domain Registry\n"]
    lines.append(build_maintenance_disclaimer() + "\n")

    if domain_df is not None and not domain_df.empty:
        lines.append("## Domains\n")
        lines.append(domain_df.to_markdown(index=False))

    return "\n".join(lines)

def build_periodic_review_calendar_markdown_report(summary: Dict[str, Any], calendar_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Periodic Review Calendar\n"]
    lines.append(build_maintenance_disclaimer() + "\n")

    if calendar_df is not None and not calendar_df.empty:
        lines.append("## Scheduled Tasks\n")
        lines.append(calendar_df.to_markdown(index=False))

    return "\n".join(lines)

def build_refresh_cadence_markdown_report(summary: Dict[str, Any], cadence_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Refresh Cadence Registry\n"]
    lines.append(build_maintenance_disclaimer() + "\n")

    if cadence_df is not None and not cadence_df.empty:
        lines.append("## Cadence\n")
        lines.append(cadence_df.to_markdown(index=False))

    return "\n".join(lines)

def build_dependency_aging_markdown_report(summary: Dict[str, Any], dep_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Dependency Aging Watch\n"]
    lines.append(build_maintenance_disclaimer() + "\n")

    if dep_df is not None and not dep_df.empty:
        lines.append("## Dependencies\n")
        lines.append(dep_df.to_markdown(index=False))

    return "\n".join(lines)

def build_sustainability_markdown_report(summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None, risk_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Project Sustainability Report\n"]
    lines.append(build_maintenance_disclaimer() + "\n")

    if score_df is not None and not score_df.empty:
        lines.append("## Score\n")
        lines.append(score_df.to_markdown(index=False) + "\n")

    if risk_df is not None and not risk_df.empty:
        lines.append("## Risks\n")
        lines.append(risk_df.to_markdown(index=False))

    return "\n".join(lines)

def build_maintenance_quality_markdown_report(summary: Dict[str, Any], quality: Optional[Dict[str, Any]] = None) -> str:
    lines = ["# Maintenance Quality Report\n"]
    lines.append(build_maintenance_disclaimer() + "\n")

    if quality:
        lines.append(f"**Passed:** {quality.get('passed', False)}\n")
        lines.append("## Checks\n")
        for k, v in quality.get("checks", {}).items():
            lines.append(f"- {k}: {v}")

    return "\n".join(lines)

def build_maintenance_status_markdown_report(summary: Dict[str, Any], status_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Maintenance Status Report\n"]
    lines.append(build_maintenance_disclaimer() + "\n")

    if status_df is not None and not status_df.empty:
        lines.append("## File Status\n")
        lines.append(status_df.to_markdown(index=False))

    return "\n".join(lines)
