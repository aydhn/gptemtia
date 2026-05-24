import pandas as pd
from research_planning.roadmap_health import calculate_roadmap_health_score, infer_roadmap_status, build_roadmap_health_snapshot

def test_calculate_health():
    df = pd.DataFrame([{"t": 1}, {"t": 2}])
    score = calculate_roadmap_health_score(df, {"total_debt_items": 1}, {})
    assert 0 <= score <= 1.0

def test_infer_status():
    assert infer_roadmap_status(0.5, 5, 10) == "blocked_research_roadmap"
    assert infer_roadmap_status(0.5, 25, 0) == "overloaded_research_roadmap"
    assert infer_roadmap_status(0.8, 5, 0) == "healthy_research_roadmap"
    assert infer_roadmap_status(0.5, 5, 0) == "manageable_research_roadmap"

def test_snapshot():
    df = pd.DataFrame([{"priority_label": "high_research_priority", "status": "task_planned"}])
    snapshot = build_roadmap_health_snapshot(df, {"total_debt_items": 0}, {"total_opportunities": 0})

    assert snapshot.backlog_count == 1
    assert snapshot.high_priority_count == 1
    assert snapshot.blocked_count == 0
    assert "Not a production readiness indicator" in snapshot.warnings
