import pandas as pd
from pathlib import Path
from research_planning.planning_pipeline import ResearchPlanningPipeline
from research_planning.planning_config import get_default_research_planning_profile

class MockSettings:
    pass

class MockDataLake:
    def load_governance_audit_report(self, *args, **kwargs):
        return pd.DataFrame([{"status": "failed", "check_name": "mock"}])

    def save_research_planning_signals(self, *args, **kwargs):
        self.saved_signals = True

    def save_research_backlog(self, *args, **kwargs):
        self.saved_backlog = True

    def save_research_priority_scores(self, *args, **kwargs):
        self.saved_priorities = True

    def save_next_best_experiments(self, *args, **kwargs):
        self.saved_next_best = True

    def save_research_debt_report(self, *args, **kwargs):
        self.saved_debt = True

    def save_roadmap_health_snapshot(self, *args, **kwargs):
        self.saved_roadmap = True

def test_pipeline_execution():
    lake = MockDataLake()
    settings = MockSettings()
    profile = get_default_research_planning_profile()

    pipeline = ResearchPlanningPipeline(lake, settings, Path("/tmp"), profile)

    # Run full report
    res, summary = pipeline.build_full_research_planning_report("1d", save=True)

    assert res["status"] == "success"
    assert summary["completed"]
    assert hasattr(lake, "saved_backlog")
    assert hasattr(lake, "saved_roadmap")
