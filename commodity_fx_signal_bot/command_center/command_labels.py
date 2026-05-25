"""
Controlled label sets for the offline command center.
"""

from typing import List
from core.exceptions import ConfigError

COMMAND_TYPE_LABELS = [
    "status_command",
    "report_command",
    "query_command",
    "workflow_command",
    "runbook_command",
    "diagnostic_command",
    "consolidation_command",
    "maintenance_command",
    "unknown_command"
]

COMMAND_SAFETY_LABELS = [
    "safe_offline_command",
    "dry_run_only_command",
    "review_required_command",
    "blocked_live_command",
    "blocked_broker_command",
    "blocked_deploy_command",
    "blocked_daemon_command",
    "unsafe_unknown_command"
]

WORKFLOW_TYPE_LABELS = [
    "research_refresh_workflow",
    "report_generation_workflow",
    "knowledge_query_workflow",
    "governance_review_workflow",
    "experiment_review_workflow",
    "planning_review_workflow",
    "troubleshooting_workflow",
    "onboarding_workflow",
    "unknown_workflow"
]

RUNBOOK_TYPE_LABELS = [
    "safe_start_runbook",
    "daily_research_runbook",
    "weekly_review_runbook",
    "troubleshooting_runbook",
    "governance_review_runbook",
    "knowledge_query_runbook",
    "report_export_runbook",
    "project_consolidation_runbook",
    "unknown_runbook"
]

def list_command_type_labels() -> List[str]:
    return list(COMMAND_TYPE_LABELS)

def list_command_safety_labels() -> List[str]:
    return list(COMMAND_SAFETY_LABELS)

def list_workflow_type_labels() -> List[str]:
    return list(WORKFLOW_TYPE_LABELS)

def list_runbook_type_labels() -> List[str]:
    return list(RUNBOOK_TYPE_LABELS)

def validate_command_type(label: str) -> None:
    if label not in COMMAND_TYPE_LABELS:
        raise ConfigError(f"Invalid command type label: {label}")

def validate_command_safety(label: str) -> None:
    if label not in COMMAND_SAFETY_LABELS:
        raise ConfigError(f"Invalid command safety label: {label}")

def validate_workflow_type(label: str) -> None:
    if label not in WORKFLOW_TYPE_LABELS:
        raise ConfigError(f"Invalid workflow type label: {label}")

def validate_runbook_type(label: str) -> None:
    if label not in RUNBOOK_TYPE_LABELS:
        raise ConfigError(f"Invalid runbook type label: {label}")
