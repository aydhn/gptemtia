import subprocess
import time
from datetime import datetime, timezone
import pandas as pd
from pathlib import Path
from typing import Optional, Tuple, Dict

from .performance_config import PerformanceProfile
from .performance_models import RuntimeProfileRecord, build_runtime_profile_id, sanitize_command_for_profile

_FORBIDDEN_COMMAND_TERMS = [
    "live", "broker", "deploy", "daemon", "order", "execute", "background"
]

def is_safe_performance_command(command: str) -> dict:
    sanitized = sanitize_command_for_profile(command.lower())
    for term in _FORBIDDEN_COMMAND_TERMS:
        if term in sanitized:
            return {"safe": False, "reason": f"Contains forbidden term: {term}"}
    return {"safe": True, "reason": ""}

def build_default_profile_commands() -> pd.DataFrame:
    commands = [
        {"command_name": "command_center_status", "module_name": "command_center", "command": "python -m scripts.run_command_center_status"},
        {"command_name": "analyst_workspace_status", "module_name": "knowledge_base", "command": "python -m scripts.run_analyst_workspace_status"},
        {"command_name": "governance_status", "module_name": "governance", "command": "python -m scripts.run_governance_status"},
        {"command_name": "experiment_status", "module_name": "experiments", "command": "python -m scripts.run_experiment_status"},
        {"command_name": "research_planning_status", "module_name": "research_planning", "command": "python -m scripts.run_research_planning_status"},
        {"command_name": "release_quality_gate_status", "module_name": "quality_gates", "command": "python -m scripts.run_release_quality_gate_status"},
        {"command_name": "performance_status", "module_name": "performance", "command": "python -m scripts.run_performance_status"},
    ]
    return pd.DataFrame(commands)

def summarize_runtime_profiles(runtime_df: pd.DataFrame) -> dict:
    if runtime_df.empty:
        return {"total_commands": 0, "avg_runtime": 0.0, "timeouts": 0}
    return {
        "total_commands": len(runtime_df),
        "avg_runtime": runtime_df["duration_seconds"].mean() if "duration_seconds" in runtime_df.columns else 0.0,
        "timeouts": int(runtime_df["timed_out"].sum()) if "timed_out" in runtime_df.columns else 0
    }

class RuntimeProfiler:
    def __init__(self, project_root: Path, profile: PerformanceProfile):
        self.project_root = project_root
        self.profile = profile

    def profile_safe_command(
        self,
        command_name: str,
        command: str,
        module_name: str,
        timeout_seconds: Optional[int] = None,
    ) -> RuntimeProfileRecord:

        started_at = datetime.now(timezone.utc)
        started_at_str = started_at.isoformat()
        profile_id = build_runtime_profile_id(command_name, started_at_str)

        safety_check = is_safe_performance_command(command)
        if not safety_check["safe"]:
            return RuntimeProfileRecord(
                profile_id=profile_id,
                command_name=command_name,
                module_name=module_name,
                command=command,
                started_at_utc=started_at_str,
                finished_at_utc=started_at_str,
                duration_seconds=0.0,
                exit_code=1,
                timed_out=False,
                stdout_tail=None,
                stderr_tail=safety_check["reason"],
                warnings=[f"BLOCKED: {safety_check['reason']}"]
            )

        timeout = timeout_seconds or self.profile.max_runtime_seconds_per_script

        start_time = time.time()

        try:
            # We mock the actual execution if it takes too long or just to test the harness.
            # In a real scenario, this would be:
            process = subprocess.run(
                command,
                shell=True,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            end_time = time.time()
            finished_at = datetime.now(timezone.utc).isoformat()

            return RuntimeProfileRecord(
                profile_id=profile_id,
                command_name=command_name,
                module_name=module_name,
                command=command,
                started_at_utc=started_at_str,
                finished_at_utc=finished_at,
                duration_seconds=end_time - start_time,
                exit_code=process.returncode,
                timed_out=False,
                stdout_tail=process.stdout[-500:] if process.stdout else None,
                stderr_tail=process.stderr[-500:] if process.stderr else None,
                warnings=[]
            )

        except subprocess.TimeoutExpired as e:
            end_time = time.time()
            finished_at = datetime.now(timezone.utc).isoformat()
            return RuntimeProfileRecord(
                profile_id=profile_id,
                command_name=command_name,
                module_name=module_name,
                command=command,
                started_at_utc=started_at_str,
                finished_at_utc=finished_at,
                duration_seconds=end_time - start_time,
                exit_code=None,
                timed_out=True,
                stdout_tail=e.stdout.decode()[-500:] if e.stdout else None,
                stderr_tail=e.stderr.decode()[-500:] if e.stderr else None,
                warnings=[f"Command timed out after {timeout} seconds"]
            )
        except Exception as e:
            end_time = time.time()
            finished_at = datetime.now(timezone.utc).isoformat()
            return RuntimeProfileRecord(
                profile_id=profile_id,
                command_name=command_name,
                module_name=module_name,
                command=command,
                started_at_utc=started_at_str,
                finished_at_utc=finished_at,
                duration_seconds=end_time - start_time,
                exit_code=1,
                timed_out=False,
                stdout_tail=None,
                stderr_tail=str(e),
                warnings=[f"Execution failed: {str(e)}"]
            )

    def profile_command_registry(
        self,
        commands_df: pd.DataFrame,
        limit: Optional[int] = None,
    ) -> Tuple[pd.DataFrame, Dict]:

        records = []
        count = 0

        for _, row in commands_df.iterrows():
            if limit and count >= limit:
                break

            cmd_name = row.get("command_name", f"cmd_{count}")
            cmd = row.get("command", "")
            mod_name = row.get("module_name", "unknown")

            # Since these are dummy scripts that don't exist yet, we'll mock the execution
            # by overriding the actual subprocess call with a safe dummy call if we can't find them,
            # or just let it fail gracefully which is also fine.
            # Here we just run it, it will likely return exit_code=1 or 2 (file not found), which is fine for tests.

            record = self.profile_safe_command(cmd_name, cmd, mod_name)
            records.append(record)
            count += 1

        import dataclasses
        df = pd.DataFrame([dataclasses.asdict(r) for r in records])
        summary = summarize_runtime_profiles(df)

        return df, summary
