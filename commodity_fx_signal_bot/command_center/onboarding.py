"""
Analyst onboarding materials.
"""

from typing import List
import pandas as pd
from command_center.command_models import SafeCommand, GuidedWorkflow, SafeRunbook
from command_center.command_config import CommandCenterProfile

def build_analyst_onboarding_sections(profile: CommandCenterProfile) -> List[dict]:
    return [
        {
            "title": "Project Purpose",
            "content": "This project is an offline research platform for commodity and FX signals."
        },
        {
            "title": "Safety Limits",
            "content": "This project DOES NOT execute live trades, send broker orders, or provide investment advice. All outputs are for offline research only."
        },
        {
            "title": "Directory Structure",
            "content": "Source code is in respective modules (e.g., data/, ml/, governance/). Outputs are saved in data/lake/ and reports/output/."
        },
        {
            "title": "Data Flow",
            "content": "Data is fetched, cached, and processed through various layers (features, ML, meta) before generating reports."
        },
        {
            "title": "Report Flow",
            "content": "Use the Command Center (Phase 50) to generate and view consolidated reports."
        },
        {
            "title": "Knowledge Base Usage",
            "content": "Use the knowledge base to query previous research findings."
        },
        {
            "title": "Status Commands",
            "content": "Run project_status_report to view the health of all modules."
        },
        {
            "title": "Troubleshooting",
            "content": "Consult the troubleshooting runbook for common issues."
        },
        {
            "title": "Forbidden Actions",
            "content": "Never attempt to connect to a live broker API or execute trades."
        }
    ]

def build_new_user_safe_start_guide(commands: List[SafeCommand], workflows: List[GuidedWorkflow], runbooks: List[SafeRunbook]) -> str:
    return "New User Safe Start Guide:\n1. Run `python -m scripts.run_command_center_status`\n2. Run `python -m scripts.run_project_status_report`\n3. Review the outputs in reports/output/command_center."

def build_codex_agent_onboarding_guide(commands: List[SafeCommand], workflows: List[GuidedWorkflow]) -> str:
    return "Codex Agent Guide:\n- Use the provided safe commands for offline analysis.\n- Do not attempt live deployments or real trading.\n- Use interactive query flows to understand the project state."

def build_onboarding_checklist(profile: CommandCenterProfile) -> pd.DataFrame:
    data = [
        {"step": "Read Onboarding Guide", "status": "Pending"},
        {"step": "Run Project Status Report", "status": "Pending"},
        {"step": "Review Safety Limits", "status": "Pending"}
    ]
    return pd.DataFrame(data)

def summarize_onboarding(checklist_df: pd.DataFrame) -> dict:
    return {
        "total_steps": len(checklist_df),
        "pending_steps": len(checklist_df[checklist_df["status"] == "Pending"])
    }
