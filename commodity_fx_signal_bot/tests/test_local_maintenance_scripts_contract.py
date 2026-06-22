import pytest
import importlib

def test_scripts_importable():
    scripts = [
        "scripts.run_maintenance_domain_registry",
        "scripts.run_periodic_review_calendar",
        "scripts.run_refresh_cadence_report",
        "scripts.run_dependency_aging_watch",
        "scripts.run_maintenance_sustainability_report",
        "scripts.run_maintenance_quality_report",
        "scripts.run_maintenance_status"
    ]

    for script in scripts:
        try:
            mod = importlib.import_module(script)
            assert hasattr(mod, "main")
        except ImportError as e:
            pytest.fail(f"Could not import {script}: {e}")
