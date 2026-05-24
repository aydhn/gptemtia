import pandas as pd
from research_planning.backlog_builder import map_signal_to_task, build_backlog_from_signals, merge_existing_backlog, filter_backlog_by_priority
from research_planning.planning_models import ResearchSignal
from research_planning.planning_config import get_default_research_planning_profile

def test_map_signal_to_task():
    sig = ResearchSignal("sig1", "governance", "audit", None, None, 0.5, 0.5, 0.5, 0.5, "Title", "Desc", {}, [])
    profile = get_default_research_planning_profile()
    task = map_signal_to_task(sig, profile)

    assert task.task_type == "governance_task"
    assert "sig1" in task.source_signal_ids

def test_build_backlog():
    sig = ResearchSignal("sig1", "governance", "audit", None, None, 0.5, 0.5, 0.5, 0.5, "Title", "Desc", {}, [])
    profile = get_default_research_planning_profile()
    df, summary = build_backlog_from_signals([sig], profile)

    assert not df.empty
    assert "is_execution_list" in summary
    assert not summary["is_execution_list"]

def test_filter_backlog():
    df = pd.DataFrame([{"task_id": "1", "priority_score": 0.8}, {"task_id": "2", "priority_score": 0.2}])
    filtered = filter_backlog_by_priority(df, 0.5)
    assert len(filtered) == 1
    assert filtered.iloc[0]["task_id"] == "1"

def test_merge_backlog():
    df1 = pd.DataFrame([{"task_id": "1", "title": "Old"}])
    df2 = pd.DataFrame([{"task_id": "1", "title": "New"}, {"task_id": "2", "title": "Other"}])

    merged, summary = merge_existing_backlog(df1, df2)
    assert len(merged) == 2

    t1 = merged[merged["task_id"] == "1"]
    assert t1.iloc[0]["title"] == "New"
