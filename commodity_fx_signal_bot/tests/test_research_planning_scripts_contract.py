import pytest
import sys
from unittest.mock import patch

def test_run_research_backlog_report_importable():
    import scripts.run_research_backlog_report
    assert hasattr(scripts.run_research_backlog_report, "main")

def test_run_priority_scoring_report_importable():
    import scripts.run_priority_scoring_report
    assert hasattr(scripts.run_priority_scoring_report, "main")

def test_run_next_best_experiment_report_importable():
    import scripts.run_next_best_experiment_report
    assert hasattr(scripts.run_next_best_experiment_report, "main")

def test_run_research_debt_report_importable():
    import scripts.run_research_debt_report
    assert hasattr(scripts.run_research_debt_report, "main")

def test_run_roadmap_health_report_importable():
    import scripts.run_roadmap_health_report
    assert hasattr(scripts.run_roadmap_health_report, "main")

def test_run_research_planning_status_importable():
    import scripts.run_research_planning_status
    assert hasattr(scripts.run_research_planning_status, "main")
