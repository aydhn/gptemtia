import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.orchestration_quality import (
    check_job_registry_quality,
    check_dependency_graph_quality,
    check_manifest_quality,
    check_for_forbidden_live_terms_in_orchestration
)
from orchestration.orchestration_models import WorkflowRunManifest

def test_orchestration_quality():
    registry_check = check_job_registry_quality([])
    assert registry_check["valid"]

    graph_check = check_dependency_graph_quality({"has_cycles": False})
    assert graph_check["valid"]

    manifest = WorkflowRunManifest("rid", "wf", "prof", "1d", [], "dt", None, "status", 1, 1, 0, 0, True, [], [])
    man_check = check_manifest_quality(manifest)
    assert man_check["valid"]

    terms_check = check_for_forbidden_live_terms_in_orchestration(summary={"test": "LIVE_ORDER"})
    assert not terms_check["passed"]
    assert "LIVE_ORDER" in terms_check["found_terms"]
