import pandas as pd
from research_planning.priority_scoring import calculate_task_priority_score, infer_priority_label, score_backlog_priorities
from research_planning.planning_models import ResearchTask, ResearchSignal
from research_planning.planning_config import get_default_research_planning_profile

def test_calculate_score():
    sig = ResearchSignal("s1", "gov", "audit", None, None, 0.5, 0.5, 0.5, 0.5, "Title", "Desc", {}, [])
    task = ResearchTask("t1", "type", "title", "desc", "planned", 0.0, "", "", ["s1"], [], [], "", "", [], "", [])

    score = calculate_task_priority_score(task, {"s1": sig})
    assert 0 <= score <= 1.0

def test_infer_label():
    profile = get_default_research_planning_profile()
    assert infer_priority_label(0.9, profile) == "critical_research_priority"
    assert infer_priority_label(0.75, profile) == "high_research_priority"
    assert infer_priority_label(0.5, profile) == "medium_research_priority"
    assert infer_priority_label(0.2, profile) == "low_research_priority"
    assert infer_priority_label(0.05, profile) == "deferred_research_priority"

def test_score_backlog():
    profile = get_default_research_planning_profile()
    df = pd.DataFrame([{"task_id": "t1", "source_signal_ids": ["s1"]}])
    sig = ResearchSignal("s1", "gov", "audit", None, None, 0.8, 0.8, 0.8, 0.8, "Title", "Desc", {}, [])

    scored, summary = score_backlog_priorities(df, [sig], profile)

    assert "priority_score" in scored.columns
    assert "priority_label" in scored.columns
    assert not summary["is_live_priority"]
