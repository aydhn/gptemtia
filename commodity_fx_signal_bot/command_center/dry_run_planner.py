"""
Dry run planner for the Command Center.
"""

from typing import List, Dict
import datetime
import pandas as pd
from command_center.command_models import CommandDryRunPlan, SafeCommand, build_dry_run_plan_id
from command_center.command_config import CommandCenterProfile
from command_center.command_safety import validate_safe_command

def build_command_dry_run_plan(title: str, command_ids: List[str], commands: List[SafeCommand], profile: CommandCenterProfile) -> CommandDryRunPlan:
    now_utc = datetime.datetime.utcnow().isoformat()
    plan_id = build_dry_run_plan_id(title, now_utc)

    plan_commands = []
    execution_order = []
    blocked_commands = []
    expected_outputs = []
    warnings = []

    command_dict = {c.command_id: c for c in commands}

    for cid in command_ids:
        if cid in command_dict:
            cmd = command_dict[cid]
            validation = validate_safe_command(cmd)
            if validation["valid"]:
                plan_commands.append(cmd)
                execution_order.append(cmd.command)
                expected_outputs.extend(cmd.output_paths)
            else:
                blocked_commands.append(cmd.command)
                warnings.append(f"Command {cmd.command_name} blocked: {validation['warning']}")
        else:
            warnings.append(f"Command ID {cid} not found in registry.")

    return CommandDryRunPlan(
        plan_id=plan_id,
        title=title,
        commands=plan_commands,
        execution_order=execution_order,
        blocked_commands=blocked_commands,
        expected_outputs=list(set(expected_outputs)),
        created_at_utc=now_utc,
        warnings=warnings
    )

def plan_full_status_check(commands: List[SafeCommand], profile: CommandCenterProfile) -> CommandDryRunPlan:
    status_ids = [c.command_id for c in commands if c.command_type == "status_command"]
    return build_command_dry_run_plan("Full Status Check", status_ids, commands, profile)

def plan_research_refresh(commands: List[SafeCommand], profile: CommandCenterProfile) -> CommandDryRunPlan:
    report_ids = [c.command_id for c in commands if c.command_type == "report_command"]
    return build_command_dry_run_plan("Research Refresh", report_ids, commands, profile)

def plan_knowledge_query(query_text: str, commands: List[SafeCommand], profile: CommandCenterProfile) -> CommandDryRunPlan:
    query_ids = [c.command_id for c in commands if c.command_type == "query_command"]
    plan = build_command_dry_run_plan(f"Knowledge Query: {query_text}", query_ids, commands, profile)
    # The actual query would be injected into the command, but for dry run we just plan it
    return plan

def plan_project_consolidation(commands: List[SafeCommand], profile: CommandCenterProfile) -> CommandDryRunPlan:
    consolidation_ids = [c.command_id for c in commands if c.command_name == "project_consolidation_report"]
    return build_command_dry_run_plan("Project Consolidation", consolidation_ids, commands, profile)

def dry_run_plan_to_dataframe(plan: CommandDryRunPlan) -> pd.DataFrame:
    data = []
    for idx, cmd in enumerate(plan.commands):
        data.append({
            "step": idx + 1,
            "command_name": cmd.command_name,
            "command": cmd.command,
            "safety_label": cmd.safety_label,
            "status": "planned"
        })
    for idx, cmd_str in enumerate(plan.blocked_commands):
        data.append({
            "step": len(plan.commands) + idx + 1,
            "command_name": "unknown",
            "command": cmd_str,
            "safety_label": "blocked",
            "status": "blocked"
        })
    return pd.DataFrame(data)

def summarize_dry_run_plan(plan: CommandDryRunPlan) -> dict:
    return {
        "plan_id": plan.plan_id,
        "title": plan.title,
        "num_planned_commands": len(plan.commands),
        "num_blocked_commands": len(plan.blocked_commands),
        "num_expected_outputs": len(plan.expected_outputs),
        "num_warnings": len(plan.warnings),
        "created_at_utc": plan.created_at_utc
    }
