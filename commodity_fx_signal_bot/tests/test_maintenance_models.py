import pytest
from local_maintenance.maintenance_models import (
    build_maintenance_domain_id,
    build_maintenance_task_id,
    build_dependency_watch_id,
    build_maintenance_binder_id,
    MaintenanceDomain,
    maintenance_domain_to_dict
)

def test_build_ids_deterministic():
    id1 = build_maintenance_domain_id("test")
    id2 = build_maintenance_domain_id("test")
    assert id1 == id2
    assert id1.startswith("domain_")

    tid1 = build_maintenance_task_id("domain", "task")
    tid2 = build_maintenance_task_id("domain", "task")
    assert tid1 == tid2
    assert tid1.startswith("task_")

def test_dataclass_to_dict():
    domain = MaintenanceDomain(
        domain_id="1", domain_name="n", domain_label="l",
        description="d", owner_role="o", default_cadence="c",
        required_artifacts=[], warnings=[]
    )
    d = maintenance_domain_to_dict(domain)
    assert d["domain_id"] == "1"
    assert "domain_name" in d
