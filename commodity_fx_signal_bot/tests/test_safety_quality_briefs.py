import pandas as pd
from report_summarization.safety_quality_briefs import (
    build_safety_brief, build_quality_brief, build_scenario_regression_brief,
    build_maintenance_performance_brief, build_final_review_brief
)
from report_summarization.summary_config import get_default_report_summary_profile

def test_safety_quality_briefs():
    profile = get_default_report_summary_profile()
    df = pd.DataFrame()

    t1, _ = build_safety_brief(df, df, profile)
    assert "Safety Brief" in t1

    t2, _ = build_quality_brief(df, df, profile)
    assert "Quality Brief" in t2

    t3, _ = build_scenario_regression_brief(df, df, profile)
    assert "Scenario Regression Brief" in t3

    t4, _ = build_maintenance_performance_brief(df, df, profile)
    assert "Maintenance & Performance Brief" in t4

    t5, _ = build_final_review_brief(df, df, df, profile)
    assert "Final Review Brief" in t5
