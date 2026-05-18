"""
Builds and manages orchestration workflow run manifests.
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import List
from orchestration.orchestration_models import WorkflowRunManifest, JobExecutionResult, build_orchestration_run_id

class RunManifestBuilder:
    def __init__(self):
        pass

    def start_run(
        self,
        workflow_name: str,
        profile_name: str,
        timeframe: str,
        symbols: List[str],
        dry_run: bool,
    ) -> WorkflowRunManifest:
        run_id = build_orchestration_run_id(workflow_name, profile_name, timeframe, symbols)
        return WorkflowRunManifest(
            run_id=run_id,
            workflow_name=workflow_name,
            profile_name=profile_name,
            timeframe=timeframe,
            symbols=symbols,
            started_at_utc=datetime.now(timezone.utc).isoformat(),
            finished_at_utc=None,
            workflow_status="workflow_running",
            job_count=0,
            success_count=0,
            failed_count=0,
            skipped_count=0,
            dry_run=dry_run,
            results=[],
            warnings=[]
        )

    def add_job_result(
        self,
        manifest: WorkflowRunManifest,
        result: JobExecutionResult,
    ) -> WorkflowRunManifest:
        from orchestration.orchestration_models import job_execution_result_to_dict
        manifest.results.append(job_execution_result_to_dict(result))
        manifest.job_count += 1

        if result.status == "job_success" or result.status == "job_dry_run":
            manifest.success_count += 1
        elif result.status == "job_failed":
            manifest.failed_count += 1
        elif result.status in ["job_skipped", "job_blocked"]:
            manifest.skipped_count += 1

        return manifest

    def finish_run(
        self,
        manifest: WorkflowRunManifest,
    ) -> WorkflowRunManifest:
        manifest.finished_at_utc = datetime.now(timezone.utc).isoformat()

        if manifest.failed_count > 0:
             manifest.workflow_status = "workflow_partial_success" if manifest.success_count > 0 else "workflow_failed"
        elif manifest.dry_run:
             manifest.workflow_status = "workflow_dry_run"
        elif manifest.skipped_count == manifest.job_count and manifest.job_count > 0:
             manifest.workflow_status = "workflow_blocked"
        else:
             manifest.workflow_status = "workflow_success"

        return manifest

    def summarize_manifest(
        self,
        manifest: WorkflowRunManifest,
    ) -> dict:
        return {
            "run_id": manifest.run_id,
            "status": manifest.workflow_status,
            "total_jobs": manifest.job_count,
            "success": manifest.success_count,
            "failed": manifest.failed_count,
            "skipped": manifest.skipped_count,
            "dry_run": manifest.dry_run
        }

def save_manifest_to_json(manifest: WorkflowRunManifest, path: Path) -> Path:
    from orchestration.orchestration_models import workflow_run_manifest_to_dict
    data = workflow_run_manifest_to_dict(manifest)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path

def load_manifest_from_json(path: Path) -> WorkflowRunManifest:
    with open(path, "r") as f:
        data = json.load(f)
    return WorkflowRunManifest(**data)
