"""
Builds and manages pipeline execution plans.
"""

from dataclasses import dataclass, asdict
from typing import List, Optional, Dict
import pandas as pd
from orchestration.orchestration_config import OrchestrationProfile
from orchestration.orchestration_models import PipelineJob, build_orchestration_run_id
from orchestration.dependency_graph import DependencyGraph

@dataclass
class ExecutionPlan:
    plan_id: str
    workflow_name: str
    profile_name: str
    timeframe: str
    symbols: List[str]
    ordered_job_ids: List[str]
    job_count: int
    dry_run: bool
    dependency_summary: dict
    warnings: List[str]

def build_execution_plan(
    workflow_name: str,
    profile: OrchestrationProfile,
    jobs: List[PipelineJob],
    symbols: List[str],
    dependency_summary: Optional[Dict] = None
) -> ExecutionPlan:

    graph = DependencyGraph(jobs)
    ordered_job_ids, cycle_info = graph.topological_sort()

    warnings = []
    if cycle_info.get("has_cycles"):
        warnings.append("Cycle detected in dependency graph. Execution plan may be invalid.")
        ordered_job_ids = [] # Cannot execute safely

    plan_id = build_orchestration_run_id(workflow_name, profile.name, profile.timeframe, symbols)

    return ExecutionPlan(
        plan_id=plan_id,
        workflow_name=workflow_name,
        profile_name=profile.name,
        timeframe=profile.timeframe,
        symbols=symbols,
        ordered_job_ids=ordered_job_ids,
        job_count=len(ordered_job_ids),
        dry_run=profile.dry_run,
        dependency_summary=dependency_summary or {},
        warnings=warnings
    )

def execution_plan_to_dict(plan: ExecutionPlan) -> dict:
    return asdict(plan)

def execution_plan_to_dataframe(plan: ExecutionPlan, jobs: List[PipelineJob]) -> pd.DataFrame:
    job_map = {job.job_id: job for job in jobs}
    data = []

    for i, job_id in enumerate(plan.ordered_job_ids):
        job = job_map.get(job_id)
        if job:
            data.append({
                "execution_order": i + 1,
                "job_id": job.job_id,
                "job_name": job.job_name,
                "job_type": job.job_type,
                "requires_symbol": "symbol" in " ".join(job.dependencies) or not job.job_id.startswith("universe_") # Simplistic proxy
            })

    if not data:
         return pd.DataFrame(columns=["execution_order", "job_id", "job_name", "job_type", "requires_symbol"])
    return pd.DataFrame(data)

def validate_execution_plan(plan: ExecutionPlan, jobs: List[PipelineJob]) -> dict:
    enabled_jobs = {job.job_id for job in jobs if job.enabled}
    planned_jobs = set(plan.ordered_job_ids)

    missing_from_plan = list(enabled_jobs - planned_jobs)
    unknown_in_plan = list(planned_jobs - enabled_jobs)

    return {
        "is_valid": len(plan.warnings) == 0 and len(unknown_in_plan) == 0,
        "missing_from_plan": missing_from_plan,
        "unknown_in_plan": unknown_in_plan
    }
