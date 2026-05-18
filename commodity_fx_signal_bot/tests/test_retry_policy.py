import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.retry_policy import build_retry_policy, should_retry_job, summarize_retry_plan
from orchestration.orchestration_config import get_default_orchestration_profile
from orchestration.orchestration_models import JobExecutionResult

def test_retry_policy():
    profile = get_default_orchestration_profile()
    policy = build_retry_policy(profile)
    assert not policy.enabled

    res = JobExecutionResult("job1", "n", "AAPL", "1d", "job_failed", None, None, None, 1, [], [], [])
    assert should_retry_job(res, policy) is False

    summary = summarize_retry_plan([res], policy)
    assert summary["candidate_count"] == 0
