import pandas as pd
from research_planning.task_orchestration_plan import build_offline_task_orchestration_plan, group_tasks_into_research_batches
from research_planning.planning_config import get_default_research_planning_profile

def test_build_plan():
    profile = get_default_research_planning_profile()
    backlog_df = pd.DataFrame([{"task_id": "t1", "priority_score": 0.8}])
    dep_df = pd.DataFrame([{"task_id": "t1", "dependency_count": 0, "dependencies": []}])

    plan = build_offline_task_orchestration_plan(backlog_df, dep_df, profile)

    assert not plan.empty
    assert "sequence" in plan.columns
    assert "batch_id" in plan.columns
    assert "Do not use for live trading or deploy" in plan.iloc[0]["warnings"]
    assert "suggested_command" in plan.columns

def test_group_batches():
    df = pd.DataFrame([{"sequence": i} for i in range(1, 15)])
    batched = group_tasks_into_research_batches(df, max_batch_size=10)

    assert batched.iloc[0]["batch_id"] == 1
    assert batched.iloc[10]["batch_id"] == 2
