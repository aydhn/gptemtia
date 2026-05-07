import pytest
import importlib

def test_script_imports():
    """Verify that all validation scripts can be imported without errors."""
    scripts = [
        "scripts.run_walk_forward_preview",
        "scripts.run_parameter_sensitivity_preview",
        "scripts.run_optimizer_candidate_preview",
        "scripts.run_validation_batch",
        "scripts.run_validation_status",
    ]

    for script in scripts:
        try:
            module = importlib.import_module(script)
            assert hasattr(module, "main"), f"Script {script} must have a main() function"
        except ImportError as e:
            pytest.fail(f"Could not import {script}: {e}")
