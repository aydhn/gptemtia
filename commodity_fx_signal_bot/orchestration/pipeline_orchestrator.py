"""
Coordinates planning, execution, and reporting of pipeline workflows.
"""

from typing import List, Tuple, Optional, Dict
from data.storage.data_lake import DataLake
from config.settings import Settings
from orchestration.orchestration_config import OrchestrationProfile, get_default_orchestration_profile
from orchestration.orchestration_models import PipelineJob, JobExecutionResult, WorkflowRunManifest
from orchestration.dependency_checker import DependencyChecker
from orchestration.execution_plan import build_execution_plan, ExecutionPlan
from orchestration.job_runner import JobRunner
from orchestration.run_manifest import RunManifestBuilder
from orchestration.workflow_templates import get_workflow_template
from orchestration.job_registry import get_registered_job
import logging

logger = logging.getLogger(__name__)

class PipelineOrchestrator:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: Optional[OrchestrationProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_orchestration_profile()
        self.checker = DependencyChecker(data_lake)
        self.runner = JobRunner(data_lake, settings, self.profile)
        self.manifest_builder = RunManifestBuilder()

    def _resolve_workflow_jobs(self, workflow_name: str) -> List[PipelineJob]:
        template = get_workflow_template(workflow_name)
        jobs = []
        for job_name in template.job_names:
            try:
                jobs.append(get_registered_job(job_name))
            except ValueError as e:
                logger.warning(f"Failed to resolve job {job_name} for workflow {workflow_name}: {e}")
        return [j for j in jobs if j.enabled]

    def build_workflow_plan(
        self,
        workflow_name: str,
        symbols: List[str],
        timeframe: str = "1d",
    ) -> Tuple[ExecutionPlan, dict]:

        jobs = self._resolve_workflow_jobs(workflow_name)

        _, dep_summary = self.checker.check_workflow_dependencies(jobs, symbols, timeframe)

        plan = build_execution_plan(workflow_name, self.profile, jobs, symbols, dep_summary)
        return plan, dep_summary

    def run_job_sequence(
        self,
        jobs: List[PipelineJob],
        symbols: List[str],
        timeframe: str,
        dry_run: bool,
    ) -> List[JobExecutionResult]:

        results = []
        job_map = {j.job_id: j for j in jobs}

        for job in jobs:
            # Simple distinction: if it's a data_job or healthcheck without specific symbol needs, run once
            if job.job_type in ["healthcheck_job", "notification_job"] or job.job_id == "universe_build_job":
                res = self.runner.run_job(job, None, timeframe, dry_run=dry_run)
                results.append(res)
                if res.status == "job_failed" and not self.profile.continue_on_job_error:
                    logger.warning(f"Job {job.job_id} failed. Halting sequence.")
                    break
            else:
                 for symbol in symbols:
                      res = self.runner.run_job(job, symbol, timeframe, dry_run=dry_run)
                      results.append(res)
                      if res.status == "job_failed" and not self.profile.continue_on_symbol_error:
                          logger.warning(f"Job {job.job_id} failed for {symbol}. Halting symbol processing.")
                          break

        return results

    def run_workflow(
        self,
        workflow_name: str,
        symbols: List[str],
        timeframe: str = "1d",
        dry_run: Optional[bool] = None,
        save: bool = True,
    ) -> Tuple[WorkflowRunManifest, dict]:

        is_dry_run = dry_run if dry_run is not None else self.profile.dry_run

        plan, dep_summary = self.build_workflow_plan(workflow_name, symbols, timeframe)
        manifest = self.manifest_builder.start_run(workflow_name, self.profile.name, timeframe, symbols, is_dry_run)

        if not plan.ordered_job_ids:
             manifest.warnings.append("Execution plan is empty or invalid.")
             manifest = self.manifest_builder.finish_run(manifest)
             return manifest, {}

        jobs_to_run = self._resolve_workflow_jobs(workflow_name)
        # reorder based on plan
        ordered_jobs = []
        job_map = {j.job_id: j for j in jobs_to_run}
        for jid in plan.ordered_job_ids:
             if jid in job_map:
                  ordered_jobs.append(job_map[jid])

        results = self.run_job_sequence(ordered_jobs, symbols, timeframe, is_dry_run)

        for res in results:
             manifest = self.manifest_builder.add_job_result(manifest, res)

        manifest = self.manifest_builder.finish_run(manifest)

        # Save logic would go here, interacting with DataLake
        if save and hasattr(self.data_lake, "save_orchestration_run_manifest"):
            self.data_lake.save_orchestration_run_manifest(manifest.run_id, manifest)
            # Add other saves as implemented in datalake

        return manifest, self.manifest_builder.summarize_manifest(manifest)
