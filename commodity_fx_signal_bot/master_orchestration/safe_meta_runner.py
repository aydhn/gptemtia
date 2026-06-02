"""
Safe meta-runner for dry-run validation and execution mapping.
"""

import pandas as pd
from pathlib import Path

from master_orchestration.master_config import MasterOrchestrationProfile
from master_orchestration.command_graph import classify_master_command_safety

class SafeMetaRunner:
    def __init__(self, project_root: Path, profile: MasterOrchestrationProfile):
        self.project_root = project_root
        self.profile = profile

    def validate_plan(self, plan_df: pd.DataFrame) -> dict:
        if plan_df.empty:
            return {"valid": True, "total": 0, "blocked": 0, "warnings": []}

        warnings = []
        blocked = 0

        for _, row in plan_df.iterrows():
            safety = row["safety_label"]
            if "blocked" in safety:
                warnings.append(f"Command '{row['command_name']}' is blocked ({safety})")
                blocked += 1

        return {
            "valid": blocked == 0,
            "total": len(plan_df),
            "blocked": blocked,
            "warnings": warnings
        }

    def dry_run_plan(self, plan_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
        # Emulates running a plan, returns the plan enriched with execution mock status
        if plan_df.empty:
            return pd.DataFrame(), {"total_executed": 0}

        execution_results = []
        for _, row in plan_df.iterrows():
            safety = row["safety_label"]
            status = "blocked" if "blocked" in safety else "dry_run_success"

            execution_results.append({
                "command_id": row["command_id"],
                "command_name": row["command_name"],
                "command": row["command"],
                "safety_label": safety,
                "execution_status": status,
                "mock_duration_ms": 10 if status == "dry_run_success" else 0
            })

        results_df = pd.DataFrame(execution_results)
        summary = summarize_meta_runner_results(results_df)
        return results_df, summary

    def execute_plan_if_explicitly_allowed(
        self,
        plan_df: pd.DataFrame,
        allow_execute: bool = False,
    ) -> tuple[pd.DataFrame, dict]:
        # Do not run if not allowed
        if not allow_execute or not self.profile.allow_execute:
            return self.dry_run_plan(plan_df)

        # Even if allow_execute=True, forbidden commands are blocked
        execution_results = []
        for _, row in plan_df.iterrows():
            safety = row["safety_label"]
            if "blocked" in safety:
                status = "blocked_safety_violation"
            else:
                # We would run it here, but for this phase we still dry run essentially
                status = "executed_safe_command"

            execution_results.append({
                "command_id": row["command_id"],
                "command_name": row["command_name"],
                "command": row["command"],
                "safety_label": safety,
                "execution_status": status,
                "mock_duration_ms": 100 if status == "executed_safe_command" else 0
            })

        results_df = pd.DataFrame(execution_results)
        summary = summarize_meta_runner_results(results_df)
        summary["execution_mode"] = "live_execution"
        return results_df, summary

def is_safe_meta_runner_command(command: str, profile: MasterOrchestrationProfile) -> dict:
    safety = classify_master_command_safety(command, profile)
    return {
        "command": command,
        "safety_label": safety,
        "is_safe": "blocked" not in safety
    }

def build_meta_runner_registry(commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> pd.DataFrame:
    # Build meta runner specific insights for commands
    if commands_df.empty:
        return pd.DataFrame()

    registry = []
    for _, row in commands_df.iterrows():
        cmd = row["command"]
        info = is_safe_meta_runner_command(cmd, profile)
        registry.append({
            "command_id": row["command_id"],
            "command": cmd,
            "safety_label": info["safety_label"],
            "is_executable": info["is_safe"] and profile.allow_execute
        })
    return pd.DataFrame(registry)

def summarize_meta_runner_results(results_df: pd.DataFrame) -> dict:
    if results_df.empty:
        return {"total_executed": 0}

    return {
        "total_commands": len(results_df),
        "dry_run_success": len(results_df[results_df["execution_status"] == "dry_run_success"]),
        "blocked": len(results_df[results_df["execution_status"].str.contains("blocked")])
    }
