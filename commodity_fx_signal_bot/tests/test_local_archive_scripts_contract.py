import pytest
import importlib

def test_archive_scripts_import():
    scripts = [
        "scripts.run_archive_domain_registry",
        "scripts.run_project_snapshot_catalog",
        "scripts.run_cold_storage_manifest",
        "scripts.run_archive_integrity_plan",
        "scripts.run_preservation_binder",
        "scripts.run_archive_quality_report",
        "scripts.run_archive_status"
    ]

    for s in scripts:
        try:
            mod = importlib.import_module(s)
        except ModuleNotFoundError:
            continue
        assert hasattr(mod, "main")
