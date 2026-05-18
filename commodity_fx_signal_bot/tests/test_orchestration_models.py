import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.orchestration_models import (
    PipelineJob,
    JobExecutionResult,
    WorkflowRunManifest,
    build_orchestration_run_id,
    build_job_id,
    pipeline_job_to_dict,
    workflow_run_manifest_to_dict
)

def test_build_run_id_deterministic():
    id1 = build_orchestration_run_id("wf", "prof", "1d", ["AAPL"])
    id2 = build_orchestration_run_id("wf", "prof", "1d", ["AAPL"])
    assert id1 == id2
    assert "run_" in id1

def test_build_job_id():
    id1 = build_job_id("name", "type")
    assert id1 == "name_type"

def test_to_dict_methods():
    job = PipelineJob("id", "name", "type", "desc", None, None, [], [], [], [])
    d = pipeline_job_to_dict(job)
    assert "job_id" in d

    manifest = WorkflowRunManifest("rid", "wf", "prof", "1d", [], "dt", None, "status", 0, 0, 0, 0, True, [], [])
    md = workflow_run_manifest_to_dict(manifest)
    assert "run_id" in md
