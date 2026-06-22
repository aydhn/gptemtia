import pytest
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.refresh_command_plan import build_refresh_command_plan, classify_refresh_command_safety

def test_refresh_command_plan():
    profile = get_default_local_maintenance_profile()
    df, summary = build_refresh_command_plan(profile)

    assert not df.empty
    assert "python -m scripts.run_system_healthcheck" in df["command"].values
    assert "scheduler" in summary["disclaimer"].lower()

def test_classify_refresh_command_safety():
    res1 = classify_refresh_command_safety("python -m scripts.run_live_trade")
    assert not res1["is_safe"]

    res2 = classify_refresh_command_safety("python -m scripts.run_system_healthcheck")
    assert res2["is_safe"]
