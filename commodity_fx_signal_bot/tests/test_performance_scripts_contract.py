import pytest
import importlib


def test_scripts_importable():
    scripts = [
        "scripts.run_performance_report_preview",
        "scripts.run_benchmark_comparison_preview",
        "scripts.run_inflation_adjusted_performance",
        "scripts.run_performance_batch",
        "scripts.run_performance_status",
    ]

    for script in scripts:
        module = importlib.import_module(script)
        assert hasattr(module, "main")
