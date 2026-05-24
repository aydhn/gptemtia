import pandas as pd
from research_planning.next_best_experiment import build_next_best_experiment_from_task, build_next_best_experiment_table, filter_executable_research_candidates
from research_planning.planning_models import ResearchTask
from research_planning.planning_config import get_default_research_planning_profile

def test_build_experiment():
    profile = get_default_research_planning_profile()
    task = ResearchTask("t1", "meta_research_task", "title", "desc", "planned", 0.8, "high", "", [], [], ["meta"], "high", "medium", [], "", [])

    exp = build_next_best_experiment_from_task(task, profile)
    assert exp.experiment_name == "meta_conflict_resolution_experiment"
    assert "Not an auto-run command" in exp.warnings

def test_build_table():
    profile = get_default_research_planning_profile()
    df = pd.DataFrame([{"task_id": "t1", "task_type": "meta_research_task", "priority_score": 0.8}])

    table, summary = build_next_best_experiment_table(df, profile)

    assert not table.empty
    assert "experiment_name" in table.columns
    assert not summary["is_auto_run"]

def test_filter_executable():
    df = pd.DataFrame([{"confidence_score": 0.8}, {"confidence_score": 0.2}])
    filtered = filter_executable_research_candidates(df)
    assert len(filtered) == 1
