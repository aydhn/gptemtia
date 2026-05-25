"""
Data models for the Command Center.
"""

from dataclasses import dataclass, asdict
from typing import List, Dict

@dataclass
class SafeCommand:
    command_id: str
    command_name: str
    command_type: str
    safety_label: str
    command: str
    description: str
    module_name: str
    dry_run_supported: bool
    requires_arguments: bool
    example_arguments: dict
    output_paths: List[str]
    warnings: List[str]

@dataclass
class GuidedWorkflow:
    workflow_id: str
    workflow_name: str
    workflow_type: str
    description: str
    steps: List[dict]
    required_commands: List[str]
    optional_commands: List[str]
    expected_outputs: List[str]
    warnings: List[str]

@dataclass
class SafeRunbook:
    runbook_id: str
    runbook_name: str
    runbook_type: str
    description: str
    sections: List[dict]
    command_ids: List[str]
    safety_notes: List[str]
    warnings: List[str]

@dataclass
class CommandDryRunPlan:
    plan_id: str
    title: str
    commands: List[SafeCommand]
    execution_order: List[str]
    blocked_commands: List[str]
    expected_outputs: List[str]
    created_at_utc: str
    warnings: List[str]


def build_safe_command_id(command_name: str, module_name: str) -> str:
    return f"cmd_{module_name}_{command_name}".lower().replace(" ", "_").replace("-", "_")

def build_workflow_id(workflow_name: str, workflow_type: str) -> str:
    return f"wf_{workflow_type}_{workflow_name}".lower().replace(" ", "_").replace("-", "_")

def build_runbook_id(runbook_name: str, runbook_type: str) -> str:
    return f"rb_{runbook_type}_{runbook_name}".lower().replace(" ", "_").replace("-", "_")

def build_dry_run_plan_id(title: str, created_at_utc: str) -> str:
    return f"drp_{created_at_utc}_{title}".lower().replace(" ", "_").replace("-", "_").replace(":", "")

def safe_command_to_dict(command: SafeCommand) -> dict:
    return asdict(command)

def guided_workflow_to_dict(workflow: GuidedWorkflow) -> dict:
    return asdict(workflow)

def safe_runbook_to_dict(runbook: SafeRunbook) -> dict:
    return asdict(runbook)

def command_dry_run_plan_to_dict(plan: CommandDryRunPlan) -> dict:
    return asdict(plan)

def sanitize_command_text(command: str) -> str:
    return command.strip().replace("\n", " ").replace("\t", " ")
