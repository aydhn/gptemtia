import pytest
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.domain_registry import build_maintenance_domain_registry

def test_maintenance_domain_registry():
    profile = get_default_local_maintenance_profile()
    df, summary = build_maintenance_domain_registry(profile)
    assert not df.empty
    assert "domain_id" in df.columns
    assert summary["total_domains"] > 0
    # Check that generic roles are used
    assert all(role in ["operator", "maintainer", "analyst"] for role in df["owner_role"])
    assert "contract" not in df.to_string().lower() or "not a maintenance contract" in summary["disclaimer"].lower()
