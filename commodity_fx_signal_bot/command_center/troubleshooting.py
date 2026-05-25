"""
Troubleshooting registry and plans.
"""

from typing import List, Tuple
import pandas as pd
from command_center.command_models import SafeCommand
from command_center.command_config import CommandCenterProfile

def build_common_issue_registry() -> pd.DataFrame:
    data = [
        {"issue": "pytest failure", "description": "A unit test is failing."},
        {"issue": "missing report", "description": "Expected report file is not found."},
        {"issue": "missing data lake output", "description": "Expected data lake file is not found."},
        {"issue": "stale artifacts", "description": "Files haven't been updated recently."},
        {"issue": "knowledge index empty", "description": "Knowledge base index has no documents."},
        {"issue": "governance lineage missing", "description": "Governance graph is incomplete."},
        {"issue": "experiment manifest missing", "description": "Experiment tracking files are missing."},
        {"issue": "meta consensus missing", "description": "Meta research results are missing."},
        {"issue": "factor scores missing", "description": "Factor research scores are missing."},
        {"issue": "command blocked", "description": "A command was blocked by safety rules."},
        {"issue": "config validation error", "description": "Configuration settings are invalid."}
    ]
    return pd.DataFrame(data)

def map_issue_to_safe_commands(issue_keyword: str, commands: List[SafeCommand]) -> pd.DataFrame:
    matched = []
    issue_lower = issue_keyword.lower()

    for cmd in commands:
        if issue_lower in cmd.description.lower() or issue_lower in cmd.command_name.lower():
            matched.append(cmd)

    # Always include basic status if no specific match
    if not matched:
        for cmd in commands:
            if cmd.command_name == "project_status_report":
                matched.append(cmd)
                break

    data = [{"command_name": c.command_name, "command": c.command} for c in matched]
    return pd.DataFrame(data)

def build_troubleshooting_plan(issue_keyword: str, commands: List[SafeCommand], profile: CommandCenterProfile) -> Tuple[pd.DataFrame, dict]:
    plan_df = map_issue_to_safe_commands(issue_keyword, commands)
    summary = {
        "issue_keyword": issue_keyword,
        "suggested_commands": len(plan_df)
    }
    return plan_df, summary

def summarize_troubleshooting_plan(plan_df: pd.DataFrame) -> dict:
    return {
        "num_commands": len(plan_df)
    }
