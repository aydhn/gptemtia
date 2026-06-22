import pytest
import pandas as pd
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.manual_review_queue import build_manual_review_queue

def test_build_manual_review_queue():
    profile = get_default_local_maintenance_profile()

    dep_df = pd.DataFrame([{"status": "dependency_aging_warning", "dependency_name": "pandas", "review_reason": "stale"}])
    stale_report_df = pd.DataFrame([{"status": "stale_report", "file_path": "report.csv"}])

    df, summary = build_manual_review_queue(dep_df, stale_report_df, None, None, None, profile)

    assert not df.empty
    assert len(df) == 2
    assert "priority" in df.columns or "base_priority" in df.columns
    assert "not investment priority" in summary["disclaimer"].lower()
