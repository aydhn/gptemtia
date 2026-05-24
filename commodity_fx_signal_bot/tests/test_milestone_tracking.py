import pandas as pd
from research_planning.milestone_tracking import build_default_research_milestones, map_tasks_to_milestones, calculate_milestone_progress

def test_default_milestones():
    ms = build_default_research_milestones()
    assert not ms.empty
    assert "data_quality_maturity" in ms["milestone_id"].values

def test_map_tasks():
    ms = build_default_research_milestones()
    df = pd.DataFrame([{"task_id": "t1", "task_type": "data_quality_task", "status": "task_planned"}])

    mapped = map_tasks_to_milestones(df, ms)
    assert len(mapped) == 1
    assert mapped.iloc[0]["milestone_id"] == "data_quality_maturity"

def test_progress():
    df = pd.DataFrame([
        {"milestone_id": "ms1", "status": "task_completed"},
        {"milestone_id": "ms1", "status": "task_planned"}
    ])

    prog = calculate_milestone_progress(df)
    assert len(prog) == 1
    assert prog.iloc[0]["progress_percent"] == 50.0
    assert "Not a production milestone" in prog.iloc[0]["warnings"]
