"""
Builds Markdown reports for the Command Center.
"""

import pandas as pd

def build_command_center_disclaimer() -> str:
    return "> **DISCLAIMER:** Bu rapor offline command center/project consolidation çıktısıdır; gerçek emir, canlı sinyal, model deployment, broker talimatı veya yatırım tavsiyesi değildir.\n\n"

def build_command_catalog_markdown_report(summary: dict, commands_df: pd.DataFrame) -> str:
    md = "# Command Catalog Report\n\n"
    md += build_command_center_disclaimer()
    md += "## Summary\n"
    for k, v in summary.items():
        md += f"- **{k}:** {v}\n"
    md += "\n## Commands\n"
    if commands_df is not None and not commands_df.empty:
        md += commands_df.to_markdown(index=False)
    else:
        md += "No commands found.\n"
    return md

def build_guided_workflow_markdown_report(summary: dict, workflows_df: pd.DataFrame) -> str:
    md = "# Guided Workflow Report\n\n"
    md += build_command_center_disclaimer()
    md += "## Summary\n"
    for k, v in summary.items():
        md += f"- **{k}:** {v}\n"
    md += "\n## Workflows\n"
    if workflows_df is not None and not workflows_df.empty:
        md += workflows_df.to_markdown(index=False)
    else:
        md += "No workflows found.\n"
    return md

def build_safe_runbook_markdown_report(summary: dict, runbooks_df: pd.DataFrame) -> str:
    md = "# Safe Runbook Report\n\n"
    md += build_command_center_disclaimer()
    md += "## Summary\n"
    for k, v in summary.items():
        md += f"- **{k}:** {v}\n"
    md += "\n## Runbooks\n"
    if runbooks_df is not None and not runbooks_df.empty:
        md += runbooks_df.to_markdown(index=False)
    else:
        md += "No runbooks found.\n"
    return md

def build_project_status_markdown_report(summary: dict, status_df: pd.DataFrame) -> str:
    md = "# Project Status Report\n\n"
    md += build_command_center_disclaimer()
    md += "## Summary\n"
    for k, v in summary.items():
        md += f"- **{k}:** {v}\n"
    md += "\n## Module Status\n"
    if status_df is not None and not status_df.empty:
        md += status_df.to_markdown(index=False)
    else:
        md += "No status data found.\n"
    return md

def build_project_consolidation_markdown_report(summary: dict, consolidation_df: pd.DataFrame | None = None) -> str:
    md = "# Project Consolidation Report\n\n"
    md += build_command_center_disclaimer()
    md += "## Summary\n"
    for k, v in summary.items():
        if isinstance(v, dict):
            md += f"- **{k}:**\n"
            for sub_k, sub_v in v.items():
                md += f"  - {sub_k}: {sub_v}\n"
        else:
            md += f"- **{k}:** {v}\n"
    if consolidation_df is not None and not consolidation_df.empty:
        md += "\n## Consolidation Details\n"
        md += consolidation_df.to_markdown(index=False)
    return md

def build_analyst_command_query_markdown_report(summary: dict, result_df: pd.DataFrame | None = None) -> str:
    md = "# Analyst Command Query Report\n\n"
    md += build_command_center_disclaimer()
    md += "## Query Summary\n"
    for k, v in summary.items():
        md += f"- **{k}:** {v}\n"
    md += "\n## Suggested Commands\n"
    if result_df is not None and not result_df.empty:
        md += result_df.to_markdown(index=False)
    else:
        md += "No suggested commands found for this query.\n"
    return md
