"""
Master command plan logic.
"""

import pandas as pd
from master_orchestration.master_config import MasterOrchestrationProfile
from master_orchestration.master_models import MasterCommand

def build_master_commands_from_registry(commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> list[MasterCommand]:
    cmds = []
    if commands_df.empty:
        return cmds

    for _, row in commands_df.iterrows():
        cmds.append(MasterCommand(
            command_id=row["command_id"],
            command_name=row["command_name"],
            command=row["command"],
            module_name=row["module_name"],
            operating_modes=["all"],
            safety_label=row["safety_label"],
            dry_run=True,
            expected_outputs=[],
            depends_on_commands=[],
            warnings=[]
        ))
    return cmds

def master_commands_to_dataframe(commands: list[MasterCommand]) -> pd.DataFrame:
    if not commands:
        return pd.DataFrame()
    return pd.DataFrame([vars(c) for c in commands])

def build_offline_master_command_plan(commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> tuple[pd.DataFrame, dict]:
    cmds = build_master_commands_from_registry(commands_df, profile)
    plan_df = master_commands_to_dataframe(cmds)

    # ensure default dry_run
    if not plan_df.empty:
        plan_df["dry_run"] = True

    summary = summarize_master_command_plan(plan_df)
    return plan_df, summary

def build_master_dry_run_execution_plan(commands_df: pd.DataFrame, operating_mode: str, profile: MasterOrchestrationProfile) -> tuple[pd.DataFrame, dict]:
    # Filter by operating_mode if we had them, for now just use all
    cmds = build_master_commands_from_registry(commands_df, profile)
    plan_df = master_commands_to_dataframe(cmds)

    if not plan_df.empty:
        plan_df["dry_run"] = True

    summary = summarize_master_command_plan(plan_df)
    summary["operating_mode"] = operating_mode
    return plan_df, summary

def summarize_master_command_plan(plan_df: pd.DataFrame) -> dict:
    if plan_df.empty:
        return {"total_plan_commands": 0}

    return {
        "total_plan_commands": len(plan_df),
        "safe_commands": len(plan_df[~plan_df["safety_label"].str.contains("blocked")]),
        "blocked_commands": len(plan_df[plan_df["safety_label"].str.contains("blocked")]),
        "is_dry_run_default": plan_df["dry_run"].all()
    }
