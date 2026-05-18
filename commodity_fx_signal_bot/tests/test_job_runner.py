import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.job_runner import JobRunner
from orchestration.orchestration_config import get_default_orchestration_profile
from orchestration.orchestration_models import PipelineJob
from unittest.mock import MagicMock

def test_job_runner_dry_run():
    mock_lake = MagicMock()
    mock_settings = MagicMock()
    profile = get_default_orchestration_profile()

    runner = JobRunner(mock_lake, mock_settings, profile)
    job = PipelineJob("job1", "name1", "type", "desc", "dummy.script", None, [], [], [], [])

    args = runner.build_job_args(job, "AAPL", "1d", True)
    assert "--symbol" in args
    assert "AAPL" in args
    assert "--dry-run" in args

    res = runner.run_job(job, "AAPL", "1d", dry_run=True)
    assert res.status == "job_dry_run"
    assert res.job_id == "job1"
