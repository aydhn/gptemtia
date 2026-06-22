import pytest
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.operator_review_checklist import build_operator_periodic_review_checklist

def test_operator_periodic_review_checklist():
    profile = get_default_local_maintenance_profile()
    df, summary = build_operator_periodic_review_checklist(profile)

    assert not df.empty
    assert "status reports refresh" in df["task"].values
    assert "dependency review" in df["task"].values
    assert "scheduler" in summary["disclaimer"].lower()
