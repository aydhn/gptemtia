import pandas as pd
from typing import Tuple, Dict, Any, List
from pathlib import Path

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def build_maintenance_runbook_sections(
    task_df: pd.DataFrame,
    calendar_df: pd.DataFrame,
    command_df: pd.DataFrame,
    queue_df: pd.DataFrame
) -> List[Dict[str, str]]:

    sections = [
        {
            "title": "Purpose and Scope",
            "content": "This runbook provides manual steps for local maintenance of the offline research platform."
        },
        {
            "title": "Important Limitations",
            "content": "This runbook DOES NOT provide automatic scheduling instructions. Do not use for cloud, broker, or live deploy actions. No raw secrets are included."
        },
        {
            "title": "Monthly Review Workflow",
            "content": "1. Run status scripts.\n2. Review docs.\n3. Check secrets hygiene.\n4. Run consistency checks."
        },
        {
            "title": "Quarterly Review Workflow",
            "content": "1. Check dependency aging.\n2. Refresh documentation and architecture guides.\n3. Run manual test coverage review."
        },
        {
            "title": "Dependency Review",
            "content": "Manually inspect requirements files. Look for stale pins. DO NOT auto-upgrade."
        },
        {
            "title": "Report Refresh Cadence",
            "content": "Regenerate status and quality reports weekly or monthly depending on activity."
        },
        {
            "title": "Docs and Test Refresh Cadence",
            "content": "Update documentation before major phase handoffs. Update tests alongside code changes."
        },
        {
            "title": "Security, Backup, Packaging Refresh",
            "content": "Review sensitive files and test backup manifests periodically."
        },
        {
            "title": "Evidence, Metadata, Graph, Timeline, Consistency, Readiness Refresh",
            "content": "Run refresh commands to keep tracking artifacts up to date."
        },
        {
            "title": "Manual Review Queue Handling",
            "content": f"Currently {len(queue_df) if queue_df is not None else 0} items are queued for manual review."
        },
        {
            "title": "Safe Command Plan",
            "content": "Use commands listed in the refresh command plan (e.g. `python -m scripts.run_*`)."
        },
        {
            "title": "Do NOT Do",
            "content": "- Do not enable auto-upgrades.\n- Do not run broker commands.\n- Do not run live trading bots.\n- Do not deploy to external clouds."
        }
    ]
    return sections

def build_maintenance_runbook(
    task_df: pd.DataFrame,
    calendar_df: pd.DataFrame,
    command_df: pd.DataFrame,
    queue_df: pd.DataFrame,
    profile: LocalMaintenanceProfile
) -> Tuple[str, Dict[str, Any]]:

    sections = build_maintenance_runbook_sections(task_df, calendar_df, command_df, queue_df)

    lines = ["# Local Maintenance Runbook\n"]
    for sec in sections:
        lines.append(f"## {sec['title']}")
        lines.append(sec['content'])
        lines.append("")

    content = "\n".join(lines)
    summary = {
        "num_sections": len(sections),
        "disclaimer": "This runbook is a manual guide, not an automatic scheduler command set."
    }
    return content, summary

def save_maintenance_runbook(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
