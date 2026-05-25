"""
Registry for guided offline workflows.
"""

from typing import List
import pandas as pd
from command_center.command_models import GuidedWorkflow, SafeCommand, build_workflow_id
from command_center.command_config import CommandCenterProfile

def _find_command_id(commands: List[SafeCommand], module: str, name: str) -> str:
    for cmd in commands:
        if cmd.module_name == module and cmd.command_name == name:
            return cmd.command_id
    return ""

def build_research_refresh_workflow(commands: List[SafeCommand]) -> GuidedWorkflow:
    return GuidedWorkflow(
        workflow_id=build_workflow_id("research_refresh", "research_refresh_workflow"),
        workflow_name="Research Refresh",
        workflow_type="research_refresh_workflow",
        description="A guided workflow to refresh offline research artifacts.",
        steps=[
            {
                "step_number": 1,
                "title": "Check Project Status",
                "purpose": "Verify current outputs availability.",
                "command_id": _find_command_id(commands, "command_center", "project_status_report"),
                "command": "python -m scripts.run_project_status_report",
                "expected_output": "project_status_report.md",
                "safety_note": "Offline status check only."
            }
        ],
        required_commands=["python -m scripts.run_project_status_report"],
        optional_commands=[],
        expected_outputs=["Project Status Report"],
        warnings=[]
    )

def build_report_generation_workflow(commands: List[SafeCommand]) -> GuidedWorkflow:
    return GuidedWorkflow(
        workflow_id=build_workflow_id("report_generation", "report_generation_workflow"),
        workflow_name="Report Generation",
        workflow_type="report_generation_workflow",
        description="A guided workflow to generate research reports.",
        steps=[
            {
                "step_number": 1,
                "title": "Generate Symbol Report",
                "purpose": "Generate report for a specific symbol.",
                "command_id": _find_command_id(commands, "research_reports", "symbol_research_report"),
                "command": "python -m scripts.run_symbol_research_report --symbol GC=F",
                "expected_output": "symbol_research_report.md",
                "safety_note": "Offline report generation only."
            }
        ],
        required_commands=[],
        optional_commands=["python -m scripts.run_symbol_research_report --symbol GC=F"],
        expected_outputs=["Symbol Research Report"],
        warnings=[]
    )

def build_knowledge_query_workflow(commands: List[SafeCommand]) -> GuidedWorkflow:
    return GuidedWorkflow(
        workflow_id=build_workflow_id("knowledge_query", "knowledge_query_workflow"),
        workflow_name="Knowledge Query",
        workflow_type="knowledge_query_workflow",
        description="A guided workflow to query the knowledge base.",
        steps=[
            {
                "step_number": 1,
                "title": "Run Research Query",
                "purpose": "Query the knowledge base for specific findings.",
                "command_id": _find_command_id(commands, "knowledge_base", "research_query"),
                "command": "python -m scripts.run_research_query --query '...' ",
                "expected_output": "query_result.md",
                "safety_note": "Offline knowledge base query."
            }
        ],
        required_commands=["python -m scripts.run_research_query"],
        optional_commands=[],
        expected_outputs=["Query Result Report"],
        warnings=[]
    )

def build_governance_review_workflow(commands: List[SafeCommand]) -> GuidedWorkflow:
    return GuidedWorkflow(
        workflow_id=build_workflow_id("governance_review", "governance_review_workflow"),
        workflow_name="Governance Review",
        workflow_type="governance_review_workflow",
        description="A guided workflow to review research governance.",
        steps=[
            {
                "step_number": 1,
                "title": "Check Governance Status",
                "purpose": "Check governance status and dependencies.",
                "command_id": _find_command_id(commands, "governance", "governance_status"),
                "command": "python -m scripts.run_governance_status",
                "expected_output": "governance_status.md",
                "safety_note": "Offline governance check."
            }
        ],
        required_commands=["python -m scripts.run_governance_status"],
        optional_commands=[],
        expected_outputs=["Governance Status Report"],
        warnings=[]
    )

def build_experiment_review_workflow(commands: List[SafeCommand]) -> GuidedWorkflow:
    return GuidedWorkflow(
        workflow_id=build_workflow_id("experiment_review", "experiment_review_workflow"),
        workflow_name="Experiment Review",
        workflow_type="experiment_review_workflow",
        description="A guided workflow to review experiments.",
        steps=[
            {
                "step_number": 1,
                "title": "Check Experiment Status",
                "purpose": "Check experiment status and leaderboard.",
                "command_id": _find_command_id(commands, "experiments", "experiment_status"),
                "command": "python -m scripts.run_experiment_status",
                "expected_output": "experiment_status.md",
                "safety_note": "Offline experiment check."
            }
        ],
        required_commands=["python -m scripts.run_experiment_status"],
        optional_commands=[],
        expected_outputs=["Experiment Status Report"],
        warnings=[]
    )

def build_planning_review_workflow(commands: List[SafeCommand]) -> GuidedWorkflow:
    return GuidedWorkflow(
        workflow_id=build_workflow_id("planning_review", "planning_review_workflow"),
        workflow_name="Planning Review",
        workflow_type="planning_review_workflow",
        description="A guided workflow to review research planning.",
        steps=[
            {
                "step_number": 1,
                "title": "Check Planning Status",
                "purpose": "Check research planning status and backlog.",
                "command_id": _find_command_id(commands, "research_planning", "research_planning_status"),
                "command": "python -m scripts.run_research_planning_status",
                "expected_output": "research_planning_status.md",
                "safety_note": "Offline planning check."
            }
        ],
        required_commands=["python -m scripts.run_research_planning_status"],
        optional_commands=[],
        expected_outputs=["Planning Status Report"],
        warnings=[]
    )

def build_troubleshooting_workflow(commands: List[SafeCommand]) -> GuidedWorkflow:
    return GuidedWorkflow(
        workflow_id=build_workflow_id("troubleshooting", "troubleshooting_workflow"),
        workflow_name="Troubleshooting",
        workflow_type="troubleshooting_workflow",
        description="A guided workflow to troubleshoot issues.",
        steps=[],
        required_commands=[],
        optional_commands=[],
        expected_outputs=[],
        warnings=["Not implemented yet"]
    )

def build_onboarding_workflow(commands: List[SafeCommand]) -> GuidedWorkflow:
    return GuidedWorkflow(
        workflow_id=build_workflow_id("onboarding", "onboarding_workflow"),
        workflow_name="Onboarding",
        workflow_type="onboarding_workflow",
        description="A guided workflow for onboarding.",
        steps=[],
        required_commands=[],
        optional_commands=[],
        expected_outputs=[],
        warnings=["Not implemented yet"]
    )

def build_default_workflows(commands: List[SafeCommand], profile: CommandCenterProfile) -> List[GuidedWorkflow]:
    return [
        build_research_refresh_workflow(commands),
        build_report_generation_workflow(commands),
        build_knowledge_query_workflow(commands),
        build_governance_review_workflow(commands),
        build_experiment_review_workflow(commands),
        build_planning_review_workflow(commands),
        build_troubleshooting_workflow(commands),
        build_onboarding_workflow(commands)
    ]

def workflows_to_dataframe(workflows: List[GuidedWorkflow]) -> pd.DataFrame:
    data = [
        {
            "workflow_id": w.workflow_id,
            "workflow_name": w.workflow_name,
            "workflow_type": w.workflow_type,
            "description": w.description,
            "num_steps": len(w.steps)
        } for w in workflows
    ]
    return pd.DataFrame(data)
