import importlib
import pytest

@pytest.mark.parametrize("script", [
    "scripts.run_simplification_domain_registry",
    "scripts.run_final_modular_complexity_map",
    "scripts.run_optional_slimming_plan",
    "scripts.run_repo_ergonomics_rehearsal",
    "scripts.run_maintainability_seed",
    "scripts.run_simplification_quality_report",
    "scripts.run_simplification_status"
])
def test_script_contract(script):
    mod = importlib.import_module(script)
    assert hasattr(mod, "main")
