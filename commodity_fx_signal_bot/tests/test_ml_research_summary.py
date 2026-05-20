import pytest
from research_reports.ml_summary import (
    summarize_ml_dataset,
    summarize_ml_training,
    summarize_ml_prediction,
    summarize_ml_integration,
    build_ml_research_summary
)
from research_reports.research_config import ResearchReportProfile

def test_ml_summaries():
    m1 = summarize_ml_dataset({})
    assert m1["dataset_available"] is False

    m2 = summarize_ml_training({})
    assert m2["model_count"] == 0

    m3 = summarize_ml_prediction({})
    assert m3["prediction_candidate_count"] == 0

    m4 = summarize_ml_integration({})
    assert m4["ml_context_available"] is False

def test_build_ml_research_summary():
    prof = ResearchReportProfile("test", "test")
    res = build_ml_research_summary({}, prof)
    assert "warnings" in res
