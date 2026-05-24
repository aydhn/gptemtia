import pandas as pd
from research_planning.planning_report_builder import (
    build_research_planning_disclaimer,
    build_research_backlog_markdown_report,
    build_priority_scoring_markdown_report,
    build_next_best_experiment_markdown_report,
    build_research_debt_markdown_report,
    build_roadmap_health_markdown_report
)

def test_disclaimer():
    disc = build_research_planning_disclaimer()
    assert "offline research planning" in disc
    assert "gerçek emir" in disc

def test_markdown_reports():
    df = pd.DataFrame([{"a": 1}])
    sum1 = {"total_tasks": 5}
    md1 = build_research_backlog_markdown_report(sum1, df)
    assert "Total Tasks: 5" in md1
    assert "offline research planning" in md1

    md2 = build_roadmap_health_markdown_report({"roadmap_status": "healthy_research_roadmap"}, df)
    assert "healthy_research_roadmap" in md2
