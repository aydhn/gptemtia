import pytest
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.dependency_review import build_dependency_review_checklist

def test_dependency_review_checklist():
    profile = get_default_local_maintenance_profile()
    df, summary = build_dependency_review_checklist(None, profile)

    assert not df.empty
    assert "upgrade command" not in summary["disclaimer"].lower() or "does not produce an upgrade command" in summary["disclaimer"].lower()
