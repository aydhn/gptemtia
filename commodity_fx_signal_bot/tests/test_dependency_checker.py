import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from unittest.mock import MagicMock
from orchestration.dependency_checker import DependencyChecker
from orchestration.orchestration_models import PipelineJob

def test_dependency_checker():
    mock_lake = MagicMock()
    checker = DependencyChecker(mock_lake)
    checker._check_dependency_exists = MagicMock(return_value=True)

    job = PipelineJob("job1", "name1", "type", "desc", None, None, [], [], ["dep1"], ["opt1"])

    res = checker.check_job_dependencies(job, "AAPL", "1d")
    assert res["status"] == "dependency_available"

    checker._check_dependency_exists = MagicMock(return_value=False)
    res_missing = checker.check_job_dependencies(job, "AAPL", "1d")
    assert res_missing["status"] == "dependency_missing"
    assert "dep1" in res_missing["missing_required"]

    df, summary = checker.check_workflow_dependencies([job], ["AAPL"], "1d")
    assert not df.empty
    assert summary["total_checks"] == 1
