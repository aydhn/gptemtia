import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.run_manifest import RunManifestBuilder, save_manifest_to_json, load_manifest_from_json
from orchestration.orchestration_models import JobExecutionResult
import json
from pathlib import Path

def test_run_manifest_builder(tmp_path):
    builder = RunManifestBuilder()
    manifest = builder.start_run("wf", "prof", "1d", ["AAPL"], True)
    assert manifest.job_count == 0
    assert manifest.workflow_status == "workflow_running"

    res = JobExecutionResult("job1", "n1", "AAPL", "1d", "job_success", "t", "t", 1.0, 1, [], [], [])
    manifest = builder.add_job_result(manifest, res)
    assert manifest.job_count == 1
    assert manifest.success_count == 1

    manifest = builder.finish_run(manifest)
    assert manifest.workflow_status == "workflow_dry_run"

    p = tmp_path / "manifest.json"
    save_manifest_to_json(manifest, p)
    loaded = load_manifest_from_json(p)
    assert loaded.run_id == manifest.run_id
