"""Test suite verifying all Phase 136 runner scripts conform to execution contracts."""

import importlib
import pytest

PHASE_136_SCRIPTS = [
    "scripts.run_gpu_ml_runtime_profile_registry",
    "scripts.run_local_hardware_discovery",
    "scripts.run_ml_dependency_capability_reports",
    "scripts.run_ml_runtime_safety_contracts",
    "scripts.run_ml_input_contracts",
    "scripts.run_gpu_ml_runtime_findings_manifest",
    "scripts.run_gpu_ml_runtime_health_check",
    "scripts.run_gpu_ml_runtime_validation_report",
    "scripts.run_gpu_ml_runtime_status",
]


@pytest.mark.parametrize("script_module", PHASE_136_SCRIPTS)
def test_script_import_and_main_contract(script_module):
    mod = importlib.import_module(script_module)
    assert hasattr(mod, "main"), f"Module {script_module} missing main() function"
    assert callable(mod.main)
