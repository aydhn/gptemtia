import pytest
import importlib

def test_local_consistency_scripts_contract():
    scripts = [
        "scripts.run_consistency_check_registry",
        "scripts.run_cross_layer_consistency_matrix",
        "scripts.run_contradiction_detection_report",
        "scripts.run_stale_reconciliation_plan",
        "scripts.run_system_coherence_report",
        "scripts.run_consistency_quality_report",
        "scripts.run_consistency_status"
    ]
    for script in scripts:
        module = importlib.import_module(script)
        assert hasattr(module, "main"), f"{script} must have a main function"
