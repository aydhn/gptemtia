import importlib
import pytest

SCRIPT_MODULES = [
    "scripts.run_backtest_acceptance_profile_registry",
    "scripts.run_backtest_acceptance_component_checkpoints",
    "scripts.run_backtest_phase_acceptance",
    "scripts.run_backtest_acceptance_dependencies_evidence",
    "scripts.run_backtest_acceptance_boundaries_findings",
    "scripts.run_backtest_acceptance_manifest",
    "scripts.run_backtest_acceptance_health_check",
    "scripts.run_backtest_acceptance_validation_report",
    "scripts.run_backtest_acceptance_status",
]

def test_scripts_contract():
    for mod_name in SCRIPT_MODULES:
        mod = importlib.import_module(mod_name)
        assert hasattr(mod, "main"), f"Module {mod_name} missing main() function."
        assert callable(getattr(mod, "main")), f"main in {mod_name} is not callable."
