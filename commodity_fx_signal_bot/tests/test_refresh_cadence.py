import pytest
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.refresh_cadence import (
    build_report_refresh_cadence_registry,
    build_datalake_refresh_cadence_registry,
    build_documentation_refresh_cadence_registry,
    build_test_refresh_cadence_registry,
    build_safety_security_refresh_cadence_registry,
    build_backup_packaging_refresh_cadence_registry,
    build_cross_layer_refresh_cadence_registry
)

def test_refresh_cadence_registries():
    profile = get_default_local_maintenance_profile()

    r1, s1 = build_report_refresh_cadence_registry(profile)
    assert not r1.empty

    r2, s2 = build_datalake_refresh_cadence_registry(profile)
    assert not r2.empty

    r3, s3 = build_documentation_refresh_cadence_registry(profile)
    assert not r3.empty

    r4, s4 = build_test_refresh_cadence_registry(profile)
    assert not r4.empty

    r5, s5 = build_safety_security_refresh_cadence_registry(profile)
    assert not r5.empty

    r6, s6 = build_backup_packaging_refresh_cadence_registry(profile)
    assert not r6.empty

    r7, s7 = build_cross_layer_refresh_cadence_registry(profile)
    assert not r7.empty

    assert "dry-run" in s1["disclaimer"].lower() or "auto-run is strictly disabled" in s1["disclaimer"].lower()
