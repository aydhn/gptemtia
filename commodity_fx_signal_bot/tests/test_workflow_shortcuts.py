import pytest
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.workflow_shortcuts import build_default_workflow_shortcuts

def test_workflow_shortcuts():
    profile = get_default_analyst_ux_profile()
    df, summary = build_default_workflow_shortcuts(profile)

    assert not df.empty
    assert summary["count"] > 0
    assert "Daily Offline Review" in df["name"].values
    assert "Scenario Demo" in df["name"].values

    # check no auto execution
    for warnings in df["warnings"]:
        assert "Otomatik execution yapmaz" in warnings[0]
