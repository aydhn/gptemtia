import pandas as pd
from report_exports.report_tracking import (
    calculate_tracking_deltas,
    summarize_tracking_table
)

def test_calculate_tracking_deltas():
    df = pd.DataFrame([
        {"created_at_utc": "2023-01-01", "research_score": 0.5, "warning_count": 1, "missing_sources_count": 0},
        {"created_at_utc": "2023-01-02", "research_score": 0.6, "warning_count": 0, "missing_sources_count": 0}
    ])
    res = calculate_tracking_deltas(df)
    assert len(res) == 2
    assert res.iloc[1]["comparison_label"] == "improved"

def test_summarize_tracking_table():
    df = pd.DataFrame([
        {"symbol": "GC=F", "comparison_label": "improved"}
    ])
    summary = summarize_tracking_table(df)
    assert summary["symbols_tracked"] == 1
    assert summary["improved_count"] == 1
