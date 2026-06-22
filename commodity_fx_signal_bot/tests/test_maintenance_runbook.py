import pytest
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.maintenance_runbook import build_maintenance_runbook

def test_build_maintenance_runbook():
    profile = get_default_local_maintenance_profile()
    text, summary = build_maintenance_runbook(None, None, None, None, profile)

    assert "Local Maintenance Runbook" in text
    assert "scheduler" in summary["disclaimer"].lower()
    assert "live deploy" in text.lower()
