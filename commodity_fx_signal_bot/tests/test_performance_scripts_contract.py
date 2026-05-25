import pytest
import sys
from pathlib import Path

def test_performance_scripts_importable():
    scripts_dir = Path("scripts")

    scripts = [
        "run_performance_profile_report",
        "run_resource_budget_report",
        "run_cache_strategy_report",
        "run_large_run_stability_report",
        "run_runtime_optimization_report",
        "run_performance_status"
    ]

    for script_name in scripts:
        try:
            mod = __import__(f"scripts.{script_name}", fromlist=['main'])
            assert hasattr(mod, 'main'), f"Script {script_name} must have a main() function"
        except ImportError as e:
            pytest.fail(f"Could not import {script_name}: {e}")

