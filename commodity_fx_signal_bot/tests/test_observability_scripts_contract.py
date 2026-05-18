import pytest
import importlib

def test_script_imports():
    scripts = [
        "scripts.run_system_healthcheck",
        "scripts.run_component_healthcheck",
        "scripts.run_data_freshness_check",
        "scripts.run_artifact_integrity_check",
        "scripts.run_runtime_metrics_report",
        "scripts.run_error_taxonomy_report",
        "scripts.run_self_diagnostics",
        "scripts.run_observability_status"
    ]

    for script in scripts:
        # Just ensure they can be imported without crashing (validates syntax & imports)
        mod = importlib.import_module(script)
        assert hasattr(mod, "main")
