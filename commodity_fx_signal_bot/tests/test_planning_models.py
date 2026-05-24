from research_planning.planning_models import (
    build_research_signal_id,
    build_research_task_id,
    build_next_best_experiment_id,
    clamp_planning_score,
    ResearchSignal,
    research_signal_to_dict
)

def test_id_builders_deterministic():
    id1 = build_research_signal_id("moduleA", "title", "EURUSD")
    id2 = build_research_signal_id("moduleA", "title", "EURUSD")
    assert id1 == id2

    t_id1 = build_research_task_id("type", "title", ["EURUSD"])
    t_id2 = build_research_task_id("type", "title", ["EURUSD"])
    assert t_id1 == t_id2

def test_clamp_planning_score():
    assert clamp_planning_score(-0.5) == 0.0
    assert clamp_planning_score(1.5) == 1.0
    assert clamp_planning_score(0.5) == 0.5
    assert clamp_planning_score(None) == 0.0

def test_dataclass_to_dict():
    sig = ResearchSignal("id", "src", "type", "EURUSD", "1d", 0.5, 0.5, 0.5, 0.5, "title", "desc", {}, [])
    d = research_signal_to_dict(sig)
    assert "signal_id" in d
    assert d["signal_id"] == "id"
