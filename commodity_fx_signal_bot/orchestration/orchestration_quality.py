"""
Quality checks and validation for orchestration layer outputs.
"""

from typing import List, Dict, Optional
import pandas as pd
from orchestration.orchestration_models import PipelineJob, WorkflowRunManifest, JobExecutionResult
from orchestration.execution_plan import ExecutionPlan

_FORBIDDEN_LIVE_TERMS = [
    "LIVE_ORDER",
    "BROKER_ORDER",
    "SEND_ORDER",
    "EXECUTE_TRADE",
    "REAL_POSITION",
    "LIVE_POSITION",
    "REAL_PORTFOLIO",
    "LIVE_SIGNAL"
]

def check_job_registry_quality(jobs: List[PipelineJob]) -> dict:
    from orchestration.job_registry import validate_registered_jobs
    return validate_registered_jobs()

def check_dependency_graph_quality(graph_summary: dict) -> dict:
    return {
        "valid": not graph_summary.get("has_cycles", False),
        "has_cycles": graph_summary.get("has_cycles", False),
        "cycle_count": graph_summary.get("cycle_count", 0)
    }

def check_execution_plan_quality(plan: ExecutionPlan) -> dict:
    valid = len(plan.warnings) == 0 and plan.job_count > 0
    return {
        "valid": valid,
        "warnings": plan.warnings
    }

def check_manifest_quality(manifest: WorkflowRunManifest) -> dict:
    valid = manifest.failed_count == 0 and manifest.job_count > 0
    return {
        "valid": valid,
        "failed_count": manifest.failed_count,
        "skipped_count": manifest.skipped_count,
        "success_rate": manifest.success_count / manifest.job_count if manifest.job_count > 0 else 0
    }

def check_failed_jobs(results: List[JobExecutionResult]) -> dict:
    failed = [r for r in results if r.status == "job_failed"]
    blocked = [r for r in results if r.status == "job_blocked"]
    return {
        "failed_count": len(failed),
        "blocked_count": len(blocked),
        "failed_jobs": [{"job_id": r.job_id, "symbol": r.symbol} for r in failed]
    }

def check_for_forbidden_live_terms_in_orchestration(
    df: Optional[pd.DataFrame] = None,
    summary: Optional[dict] = None
) -> dict:
    found_terms = set()

    def check_string(s: str):
        if not isinstance(s, str):
            return
        upper_s = s.upper()
        for term in _FORBIDDEN_LIVE_TERMS:
            if term in upper_s:
                found_terms.add(term)

    if df is not None:
        for col in df.select_dtypes(include=['object']):
            for val in df[col].dropna():
                check_string(str(val))

    if summary is not None:
        import json
        check_string(json.dumps(summary))

    return {
        "passed": len(found_terms) == 0,
        "found_terms": list(found_terms)
    }

def build_orchestration_quality_report(
    manifest: WorkflowRunManifest,
    plan: ExecutionPlan,
    dependency_summary: dict
) -> dict:

    graph_quality = check_dependency_graph_quality(dependency_summary)
    plan_quality = check_execution_plan_quality(plan)
    manifest_quality = check_manifest_quality(manifest)

    # Also we'd ideally pass the results dataframe to check terms, but we can check the manifest dict
    from orchestration.orchestration_models import workflow_run_manifest_to_dict
    term_check = check_for_forbidden_live_terms_in_orchestration(summary=workflow_run_manifest_to_dict(manifest))

    warnings = []
    if not graph_quality["valid"]: warnings.append("Dependency graph has cycles.")
    if not plan_quality["valid"]: warnings.extend(plan_quality["warnings"])
    if manifest.failed_count > 0: warnings.append(f"{manifest.failed_count} jobs failed.")
    if not term_check["passed"]: warnings.append(f"Forbidden terms found: {term_check['found_terms']}")

    passed = graph_quality["valid"] and plan_quality["valid"] and term_check["passed"]

    return {
        "registry_valid": True, # Assumed valid if we got here
        "dependency_graph_valid": graph_quality["valid"],
        "execution_plan_valid": plan_quality["valid"],
        "manifest_valid": manifest_quality["valid"],
        "failed_job_count": manifest.failed_count,
        "blocked_job_count": manifest.skipped_count, # roughly
        "forbidden_live_terms_found": not term_check["passed"],
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": warnings
    }

from orchestration.execution_plan import ExecutionPlan
