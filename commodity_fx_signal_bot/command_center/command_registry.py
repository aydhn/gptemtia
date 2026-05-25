"""
Registry for safe offline commands.
"""

import pandas as pd
from typing import List
from command_center.command_models import SafeCommand, build_safe_command_id
from command_center.command_config import CommandCenterProfile
from command_center.command_safety import classify_command_safety, detect_forbidden_command_terms

def _create_command(name: str, module: str, c_type: str, command_str: str, desc: str, requires_args: bool = False, example_args: dict = None, outputs: List[str] = None) -> SafeCommand:
    return SafeCommand(
        command_id=build_safe_command_id(name, module),
        command_name=name,
        command_type=c_type,
        safety_label="safe_offline_command",  # Will be validated later
        command=command_str,
        description=desc,
        module_name=module,
        dry_run_supported=True,
        requires_arguments=requires_args,
        example_arguments=example_args or {},
        output_paths=outputs or [],
        warnings=[]
    )

def build_core_status_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="analyst_workspace_status",
            module="knowledge_base",
            c_type="status_command",
            command_str="python -m scripts.run_analyst_workspace_status",
            desc="Generates the status of the analyst workspace.",
            outputs=["reports/output/knowledge_base/analyst_workspace_status.txt"]
        ),
        _create_command(
            name="project_status_report",
            module="command_center",
            c_type="status_command",
            command_str="python -m scripts.run_project_status_report",
            desc="Generates the overall project status report.",
            outputs=["reports/output/command_center/markdown/project_status_report.md"]
        ),
        _create_command(
            name="project_consolidation_report",
            module="command_center",
            c_type="status_command",
            command_str="python -m scripts.run_project_consolidation_report",
            desc="Generates the project consolidation report.",
            outputs=["reports/output/command_center/markdown/project_consolidation_report.md"]
        )
    ]

def build_research_report_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="research_report_status",
            module="research_reports",
            c_type="status_command",
            command_str="python -m scripts.run_research_report_status",
            desc="Generates status for research reports."
        ),
        _create_command(
            name="symbol_research_report",
            module="research_reports",
            c_type="report_command",
            command_str="python -m scripts.run_symbol_research_report",
            desc="Generates a research report for a specific symbol.",
            requires_args=True,
            example_args={"--symbol": "GC=F", "--timeframe": "1d"}
        )
    ]

def build_portfolio_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="portfolio_research_status",
            module="portfolio_research",
            c_type="status_command",
            command_str="python -m scripts.run_portfolio_research_status",
            desc="Generates status for portfolio research."
        )
    ]

def build_regime_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="portfolio_regime_status",
            module="portfolio_regime",
            c_type="status_command",
            command_str="python -m scripts.run_portfolio_regime_status",
            desc="Generates status for portfolio regime."
        )
    ]

def build_synthetic_index_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="synthetic_index_status",
            module="synthetic_indices",
            c_type="status_command",
            command_str="python -m scripts.run_synthetic_index_status",
            desc="Generates status for synthetic indices."
        )
    ]

def build_factor_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="factor_research_status",
            module="factor_research",
            c_type="status_command",
            command_str="python -m scripts.run_factor_research_status",
            desc="Generates status for factor research."
        )
    ]

def build_meta_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="meta_research_status",
            module="meta_research",
            c_type="status_command",
            command_str="python -m scripts.run_meta_research_status",
            desc="Generates status for meta research."
        )
    ]

def build_experiment_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="experiment_status",
            module="experiments",
            c_type="status_command",
            command_str="python -m scripts.run_experiment_status",
            desc="Generates status for experiments."
        )
    ]

def build_governance_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="governance_status",
            module="governance",
            c_type="status_command",
            command_str="python -m scripts.run_governance_status",
            desc="Generates status for governance."
        )
    ]

def build_planning_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="research_planning_status",
            module="research_planning",
            c_type="status_command",
            command_str="python -m scripts.run_research_planning_status",
            desc="Generates status for research planning."
        )
    ]

def build_knowledge_base_commands() -> List[SafeCommand]:
    return [
        _create_command(
            name="knowledge_index_report",
            module="knowledge_base",
            c_type="report_command",
            command_str="python -m scripts.run_knowledge_index_report",
            desc="Generates the knowledge index report."
        ),
        _create_command(
            name="research_query",
            module="knowledge_base",
            c_type="query_command",
            command_str="python -m scripts.run_research_query",
            desc="Runs an interactive research query.",
            requires_args=True,
            example_args={"--query": "GC=F hakkında ne biliyoruz?"}
        )
    ]

def build_default_command_registry(profile: CommandCenterProfile) -> List[SafeCommand]:
    commands = []
    commands.extend(build_core_status_commands())

    if profile.include_research_reports:
        commands.extend(build_research_report_commands())
    if profile.include_portfolio_reports:
        commands.extend(build_portfolio_commands())
    if profile.include_regime_reports:
        commands.extend(build_regime_commands())
    if profile.include_synthetic_indices:
        commands.extend(build_synthetic_index_commands())
    if profile.include_factor_research:
        commands.extend(build_factor_commands())
    if profile.include_meta_research:
        commands.extend(build_meta_commands())
    if profile.include_experiments:
        commands.extend(build_experiment_commands())
    if profile.include_governance:
        commands.extend(build_governance_commands())
    if profile.include_planning:
        commands.extend(build_planning_commands())
    if profile.include_knowledge_base:
        commands.extend(build_knowledge_base_commands())

    # Re-validate safety
    for cmd in commands:
        safety = classify_command_safety(cmd.command)
        cmd.safety_label = safety
        terms = detect_forbidden_command_terms(cmd.command)
        if terms["forbidden_terms_found"]:
            cmd.warnings.append(f"Forbidden terms found: {terms['found_terms']}")

    return commands

def command_registry_to_dataframe(commands: List[SafeCommand]) -> pd.DataFrame:
    data = [
        {
            "command_id": c.command_id,
            "command_name": c.command_name,
            "module_name": c.module_name,
            "command_type": c.command_type,
            "safety_label": c.safety_label,
            "command": c.command,
            "description": c.description,
            "requires_arguments": c.requires_arguments
        } for c in commands
    ]
    return pd.DataFrame(data)
