import pytest
import pandas as pd
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.maintenance_gaps import build_maintenance_gap_register

def test_maintenance_gap_register():
    profile = get_default_local_maintenance_profile()
    task_df = pd.DataFrame([{"domain_label": "other_maintenance", "task_id": "1"}])
    cadence = {"reports": pd.DataFrame()} # missing datalake etc

    df, summary = build_maintenance_gap_register(None, task_df, cadence, profile)

    assert not df.empty
    assert "missing_cadence" in df["gap_type"].values
    assert "missing_operator_review_items" in df["gap_type"].values
    assert "production incident" in summary["disclaimer"].lower()
