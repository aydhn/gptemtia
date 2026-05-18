"""
Job runner with dry-run support and script subprocess execution capabilities.
"""

import subprocess
import time
from datetime import datetime, timezone
from typing import Optional, List, Tuple
from config.settings import Settings
from data.storage.data_lake import DataLake
from orchestration.orchestration_config import OrchestrationProfile
from orchestration.orchestration_models import PipelineJob, JobExecutionResult

class JobRunner:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: OrchestrationProfile,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile

    def build_job_args(
        self,
        job: PipelineJob,
        symbol: Optional[str],
        timeframe: str,
        dry_run: bool,
    ) -> List[str]:
        args = []
        if symbol:
            args.extend(["--symbol", symbol])
        if timeframe:
            args.extend(["--timeframe", timeframe])
        if dry_run and job.dry_run_supported:
            args.append("--dry-run")
        return args

    def run_script_module(
        self,
        script_module: str,
        args: List[str],
        dry_run: bool = True,
    ) -> Tuple[int, str, str]:
        cmd = ["python", "-m", script_module] + args
        if dry_run:
             # In dry run, we don't actually run the script
             # We assume it would succeed if dependencies were met
             return 0, f"DRY RUN: {cmd}", ""

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300 # 5 minute timeout for safety
            )
            # Truncate output to prevent massive logs
            out = result.stdout[:5000] if result.stdout else ""
            err = result.stderr[:5000] if result.stderr else ""
            return result.returncode, out, err
        except subprocess.TimeoutExpired as e:
            return 124, "", f"Timeout expired: {e}"
        except Exception as e:
            return 1, "", f"Execution error: {str(e)}"

    def run_job(
        self,
        job: PipelineJob,
        symbol: Optional[str],
        timeframe: str,
        dry_run: Optional[bool] = None,
    ) -> JobExecutionResult:

        is_dry_run = dry_run if dry_run is not None else self.profile.dry_run

        start_time = time.time()
        start_dt = datetime.now(timezone.utc).isoformat()

        args = self.build_job_args(job, symbol, timeframe, is_dry_run)

        status = "job_unknown"
        warnings = []
        error_message = None
        produced_outputs = []

        if not job.script_module:
             status = "job_failed"
             error_message = "No script module defined"
        else:
             retcode, stdout, stderr = self.run_script_module(job.script_module, args, is_dry_run)

             if is_dry_run:
                  status = "job_dry_run"
                  produced_outputs = job.expected_outputs # Assume produced in dry run
             elif retcode == 0:
                  status = "job_success"
                  produced_outputs = job.expected_outputs # In reality, we'd check datalake
             else:
                  status = "job_failed"
                  error_message = f"Return code {retcode}. Stderr: {stderr}"

        end_time = time.time()
        end_dt = datetime.now(timezone.utc).isoformat()

        return JobExecutionResult(
            job_id=job.job_id,
            job_name=job.job_name,
            symbol=symbol,
            timeframe=timeframe,
            status=status,
            started_at_utc=start_dt,
            finished_at_utc=end_dt,
            duration_seconds=end_time - start_time,
            attempts=1,
            produced_outputs=produced_outputs,
            missing_dependencies=[], # This is populated by pre-checks in orchestrator
            warnings=warnings,
            error_message=error_message
        )
