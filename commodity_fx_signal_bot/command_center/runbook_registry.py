"""
Registry for safe offline runbooks.
"""

from typing import List
import pandas as pd
from command_center.command_models import SafeRunbook, SafeCommand, GuidedWorkflow, build_runbook_id
from command_center.command_config import CommandCenterProfile

def build_safe_start_runbook(commands: List[SafeCommand], workflows: List[GuidedWorkflow]) -> SafeRunbook:
    return SafeRunbook(
        runbook_id=build_runbook_id("safe_start", "safe_start_runbook"),
        runbook_name="Safe Start Runbook",
        runbook_type="safe_start_runbook",
        description="A runbook for safely starting and checking the offline system.",
        sections=[
            {"title": "Purpose", "content": "To safely check the status of all modules."},
            {"title": "When to use", "content": "After initial setup or daily start."},
            {"title": "Safety Limits", "content": "No live trading, no execution."}
        ],
        command_ids=[c.command_id for c in commands if c.command_type == "status_command"],
        safety_notes=["These commands only read offline data and generate reports."],
        warnings=[]
    )

def build_daily_research_runbook(commands: List[SafeCommand], workflows: List[GuidedWorkflow]) -> SafeRunbook:
    return SafeRunbook(
        runbook_id=build_runbook_id("daily_research", "daily_research_runbook"),
        runbook_name="Daily Research Runbook",
        runbook_type="daily_research_runbook",
        description="A runbook for daily offline research generation.",
        sections=[
            {"title": "Purpose", "content": "To generate daily research digests and rankings."},
            {"title": "When to use", "content": "Daily, after data ingestion."},
            {"title": "Safety Limits", "content": "No live trading, no execution."}
        ],
        command_ids=[],
        safety_notes=["These commands generate offline reports."],
        warnings=[]
    )

def build_weekly_review_runbook(commands: List[SafeCommand], workflows: List[GuidedWorkflow]) -> SafeRunbook:
    return SafeRunbook(
        runbook_id=build_runbook_id("weekly_review", "weekly_review_runbook"),
        runbook_name="Weekly Review Runbook",
        runbook_type="weekly_review_runbook",
        description="A runbook for weekly offline research review.",
        sections=[
            {"title": "Purpose", "content": "To review governance, planning, and experiments."},
            {"title": "When to use", "content": "Weekly."},
            {"title": "Safety Limits", "content": "No live trading, no execution."}
        ],
        command_ids=[],
        safety_notes=["These commands generate offline review reports."],
        warnings=[]
    )

def build_troubleshooting_runbook(commands: List[SafeCommand], workflows: List[GuidedWorkflow]) -> SafeRunbook:
    return SafeRunbook(
        runbook_id=build_runbook_id("troubleshooting", "troubleshooting_runbook"),
        runbook_name="Troubleshooting Runbook",
        runbook_type="troubleshooting_runbook",
        description="A runbook for safely troubleshooting offline issues.",
        sections=[
            {"title": "Purpose", "content": "To safely diagnose module health and project status."},
            {"title": "When to use", "content": "When there are issues or missing reports."},
            {"title": "Safety Limits", "content": "No live trading, no execution."}
        ],
        command_ids=[],
        safety_notes=["These commands check system status and generate diagnostic reports."],
        warnings=[]
    )

def build_governance_review_runbook(commands: List[SafeCommand], workflows: List[GuidedWorkflow]) -> SafeRunbook:
    return SafeRunbook(
        runbook_id=build_runbook_id("governance_review", "governance_review_runbook"),
        runbook_name="Governance Review Runbook",
        runbook_type="governance_review_runbook",
        description="A runbook for reviewing research governance.",
        sections=[],
        command_ids=[],
        safety_notes=[],
        warnings=[]
    )

def build_knowledge_query_runbook(commands: List[SafeCommand], workflows: List[GuidedWorkflow]) -> SafeRunbook:
    return SafeRunbook(
        runbook_id=build_runbook_id("knowledge_query", "knowledge_query_runbook"),
        runbook_name="Knowledge Query Runbook",
        runbook_type="knowledge_query_runbook",
        description="A runbook for querying the knowledge base.",
        sections=[],
        command_ids=[],
        safety_notes=[],
        warnings=[]
    )

def build_report_export_runbook(commands: List[SafeCommand], workflows: List[GuidedWorkflow]) -> SafeRunbook:
    return SafeRunbook(
        runbook_id=build_runbook_id("report_export", "report_export_runbook"),
        runbook_name="Report Export Runbook",
        runbook_type="report_export_runbook",
        description="A runbook for exporting reports.",
        sections=[],
        command_ids=[],
        safety_notes=[],
        warnings=[]
    )

def build_project_consolidation_runbook(commands: List[SafeCommand], workflows: List[GuidedWorkflow]) -> SafeRunbook:
    return SafeRunbook(
        runbook_id=build_runbook_id("project_consolidation", "project_consolidation_runbook"),
        runbook_name="Project Consolidation Runbook",
        runbook_type="project_consolidation_runbook",
        description="A runbook for generating the project consolidation report.",
        sections=[],
        command_ids=[],
        safety_notes=[],
        warnings=[]
    )

def build_default_runbooks(commands: List[SafeCommand], workflows: List[GuidedWorkflow], profile: CommandCenterProfile) -> List[SafeRunbook]:
    return [
        build_safe_start_runbook(commands, workflows),
        build_daily_research_runbook(commands, workflows),
        build_weekly_review_runbook(commands, workflows),
        build_troubleshooting_runbook(commands, workflows),
        build_governance_review_runbook(commands, workflows),
        build_knowledge_query_runbook(commands, workflows),
        build_report_export_runbook(commands, workflows),
        build_project_consolidation_runbook(commands, workflows)
    ]

def runbooks_to_dataframe(runbooks: List[SafeRunbook]) -> pd.DataFrame:
    data = [
        {
            "runbook_id": r.runbook_id,
            "runbook_name": r.runbook_name,
            "runbook_type": r.runbook_type,
            "description": r.description,
            "num_commands": len(r.command_ids)
        } for r in runbooks
    ]
    return pd.DataFrame(data)
