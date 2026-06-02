"""
Master orchestration markdown report builders.
"""

import pandas as pd
from datetime import datetime

def build_master_disclaimer() -> str:
    return (
        "**UYARI**: Bu çıktı offline master orchestration/operational playbook raporudur. "
        "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        "otomatik trade onayı veya yatırım tavsiyesi değildir."
    )

def build_orchestration_map_markdown_report(summary: dict, layer_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Master Orchestration Layer Map Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        build_master_disclaimer(),
        "",
        "## Summary",
    ]
    for k, v in summary.items():
        lines.append(f"- **{k}**: {v}")

    if layer_df is not None and not layer_df.empty:
        lines.append("")
        lines.append("## Layer Map")
        lines.append(layer_df.to_markdown(index=False))

    return "\n".join(lines)

def build_master_command_plan_markdown_report(summary: dict, plan_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Offline Master Command Plan Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        build_master_disclaimer(),
        "",
        "## Summary",
    ]
    for k, v in summary.items():
        lines.append(f"- **{k}**: {v}")

    if plan_df is not None and not plan_df.empty:
        lines.append("")
        lines.append("## Command Plan")
        lines.append(plan_df.to_markdown(index=False))

    return "\n".join(lines)

def build_master_dry_run_markdown_report(summary: dict, dry_run_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Master Dry Run Execution Plan Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        build_master_disclaimer(),
        "",
        "## Summary",
    ]
    for k, v in summary.items():
        lines.append(f"- **{k}**: {v}")

    if dry_run_df is not None and not dry_run_df.empty:
        lines.append("")
        lines.append("## Dry Run Plan")
        lines.append(dry_run_df.to_markdown(index=False))

    return "\n".join(lines)

def build_operational_playbook_markdown_report(summary: dict, playbook_text: str | None = None) -> str:
    lines = [
        "# Operational Playbook Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        build_master_disclaimer(),
        "",
        "## Summary",
    ]
    for k, v in summary.items():
        lines.append(f"- **{k}**: {v}")

    if playbook_text:
        lines.append("")
        lines.append("## Playbook Content")
        lines.append("```text")
        lines.append(playbook_text)
        lines.append("```")

    return "\n".join(lines)

def build_phase_1_60_consolidation_markdown_report(summary: dict, matrix_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 1-60 Consolidation Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        build_master_disclaimer(),
        "",
        "## Summary",
    ]
    for k, v in summary.items():
        lines.append(f"- **{k}**: {v}")

    if matrix_df is not None and not matrix_df.empty:
        lines.append("")
        lines.append("## Consolidation Matrix")
        lines.append(matrix_df.to_markdown(index=False))

    return "\n".join(lines)

def build_master_safety_boundary_markdown_report(summary: dict, safety_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Master Safety Boundary Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        build_master_disclaimer(),
        "",
        "## Summary",
    ]
    for k, v in summary.items():
        lines.append(f"- **{k}**: {v}")

    if safety_df is not None and not safety_df.empty:
        lines.append("")
        lines.append("## Safety Boundaries")
        lines.append(safety_df.to_markdown(index=False))

    return "\n".join(lines)

def build_master_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Master Operational Status Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        build_master_disclaimer(),
        "",
        "## Summary",
    ]
    for k, v in summary.items():
        lines.append(f"- **{k}**: {v}")

    if status_df is not None and not status_df.empty:
        lines.append("")
        lines.append("## Operational Status")
        lines.append(status_df.to_markdown(index=False))

    return "\n".join(lines)
