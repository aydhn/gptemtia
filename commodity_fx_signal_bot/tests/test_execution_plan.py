import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.execution_plan import build_execution_plan, validate_execution_plan, execution_plan_to_dataframe
from orchestration.orchestration_models import PipelineJob
from orchestration.orchestration_config import get_default_orchestration_profile

def test_execution_plan():
    job1 = PipelineJob("job1", "name1", "type", "desc", None, None, [], [], [], [])
    profile = get_default_orchestration_profile()

    plan = build_execution_plan("wf", profile, [job1], ["AAPL"])
    assert plan.job_count == 1
    assert "job1" in plan.ordered_job_ids

    df = execution_plan_to_dataframe(plan, [job1])
    assert not df.empty

    val = validate_execution_plan(plan, [job1])
    assert val["is_valid"]
