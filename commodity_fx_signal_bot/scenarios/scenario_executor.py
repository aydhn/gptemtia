"""
Dry-run executor for offline scenarios.
"""

import pandas as pd
from pathlib import Path
from typing import List, Tuple
from datetime import datetime
import subprocess

from scenarios.scenario_config import ScenarioProfile
from scenarios.scenario_models import ScenarioDefinition, ScenarioDryRunResult, build_dry_run_id
from scenarios.demo_command_sequences import _is_safe


class ScenarioDryRunExecutor:
    def __init__(self, project_root: Path, profile: ScenarioProfile):
        self.project_root = project_root
        self.profile = profile

    def dry_run_scenario(
        self,
        scenario: ScenarioDefinition,
        command_sequence_df: pd.DataFrame,
        execute_safe_commands: bool = False,
    ) -> ScenarioDryRunResult:
        """Plans or executes a scenario dry-run."""

        started_at = datetime.utcnow().isoformat()
        dry_run_id = build_dry_run_id(scenario.scenario_id, started_at)

        executed = []
        blocked = []
        warnings = ["Dry-run execution.", "No live trading or broker connectivity."]

        # Get commands for this scenario
        if not command_sequence_df.empty:
            scenario_cmds = command_sequence_df[command_sequence_df["scenario_id"] == scenario.scenario_id]
        else:
            scenario_cmds = pd.DataFrame()

        for _, row in scenario_cmds.iterrows():
            cmd = row["command"]
            if not row["is_safe"] or not _is_safe(cmd):
                blocked.append(cmd)
                warnings.append(f"Blocked command: {cmd}")
            else:
                if execute_safe_commands and self.profile.run_dry_run_validation:
                    # In a real environment we might execute subprocess.run
                    # but here we just simulate execution to be completely safe
                    executed.append(f"[SIMULATED] {cmd}")
                else:
                    executed.append(f"[PLANNED] {cmd}")

        result = ScenarioDryRunResult(
            dry_run_id=dry_run_id,
            scenario_id=scenario.scenario_id,
            scenario_name=scenario.scenario_name,
            started_at_utc=started_at,
            finished_at_utc=datetime.utcnow().isoformat(),
            status="completed" if not blocked else "completed_with_blocks",
            executed_commands=executed,
            blocked_commands=blocked,
            produced_outputs=[], # Filled during validation
            validation_passed=True if not blocked else False,
            warnings=warnings
        )

        return result

    def dry_run_all_scenarios(
        self,
        scenarios: List[ScenarioDefinition],
        command_sequences_df: pd.DataFrame,
        execute_safe_commands: bool = False,
    ) -> Tuple[pd.DataFrame, dict]:
        """Runs dry-run planning/execution for all scenarios."""
        results = []

        for scenario in scenarios:
            res = self.dry_run_scenario(scenario, command_sequences_df, execute_safe_commands)
            results.append(res.__dict__)

        if results:
            df = pd.DataFrame(results)
        else:
            df = pd.DataFrame(columns=[
                "dry_run_id", "scenario_id", "scenario_name", "started_at_utc",
                "finished_at_utc", "status", "executed_commands", "blocked_commands",
                "produced_outputs", "validation_passed", "warnings"
            ])

        summary = {
            "total_runs": len(results),
            "passed": int(df["validation_passed"].sum()) if not df.empty else 0,
            "blocked": int((~df["validation_passed"]).sum()) if not df.empty else 0,
            "warnings": ["These are simulated or safe offline executions only."]
        }

        return df, summary


def is_safe_scenario_command(command: str) -> dict:
    """Wrapper to check if a command is safe."""
    safe = _is_safe(command)
    return {
        "is_safe": safe,
        "blocked_reason": "Contains forbidden pattern (live, broker, deploy, daemon, etc.)" if not safe else None
    }


def build_dry_run_execution_plan(scenario: ScenarioDefinition, command_sequence_df: pd.DataFrame) -> pd.DataFrame:
    """Extracts the planned execution steps for a scenario."""
    if command_sequence_df.empty:
        return pd.DataFrame()
    return command_sequence_df[command_sequence_df["scenario_id"] == scenario.scenario_id].copy()


def summarize_scenario_dry_runs(dry_run_df: pd.DataFrame) -> dict:
    """Summarizes dry run results."""
    if dry_run_df.empty:
        return {"total_runs": 0}

    return {
        "total_runs": len(dry_run_df),
        "passed_runs": int(dry_run_df["validation_passed"].sum()),
        "failed_runs": int((~dry_run_df["validation_passed"]).sum()),
        "total_blocked_commands": sum(len(x) for x in dry_run_df["blocked_commands"] if isinstance(x, list)),
        "warnings": ["Dry run results. Not live execution."]
    }
