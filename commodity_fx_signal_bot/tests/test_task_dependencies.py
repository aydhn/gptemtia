import pandas as pd
from research_planning.task_dependencies import infer_task_dependencies, build_task_dependency_table, detect_task_dependency_cycles, build_task_execution_order
from research_planning.planning_models import ResearchTask

def test_infer_dependencies():
    df = pd.DataFrame([{"task_id": "dq1", "task_type": "data_quality_task"}])
    task = ResearchTask("ml1", "ml_research_task", "title", "desc", "planned", 0.0, "", "", [], [], [], "", "", [], "", [])

    deps = infer_task_dependencies(task, df)
    assert len(deps) == 1
    assert deps[0] == "dq1"

def test_build_dependency_table():
    df = pd.DataFrame([
        {"task_id": "dq1", "task_type": "data_quality_task"},
        {"task_id": "ml1", "task_type": "ml_research_task"}
    ])

    dep_df = build_task_dependency_table(df)
    assert len(dep_df) == 2
    ml_row = dep_df[dep_df["task_id"] == "ml1"]
    assert ml_row.iloc[0]["dependency_count"] == 1

def test_execution_order():
    dep_df = pd.DataFrame([{"task_id": "ml1", "dependency_count": 1, "dependencies": []}, {"task_id": "dq1", "dependency_count": 0, "dependencies": []}])
    backlog_df = pd.DataFrame([{"task_id": "ml1", "priority_score": 0.8}, {"task_id": "dq1", "priority_score": 0.9}])

    order = build_task_execution_order(dep_df, backlog_df)
    assert len(order) == 2
    assert order.iloc[0]["task_id"] == "dq1" # Lower dep count, higher priority
