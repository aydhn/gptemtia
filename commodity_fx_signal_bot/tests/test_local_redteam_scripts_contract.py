import pytest
import importlib

def test_scripts_contract():
    scripts = [
        "scripts.run_redteam_domain_registry",
        "scripts.run_final_local_redteam_rehearsal",
        "scripts.run_misuse_scenario_library",
        "scripts.run_adversarial_prompt_safety_checklist",
        "scripts.run_safety_assurance_summary",
        "scripts.run_redteam_quality_report",
        "scripts.run_redteam_status"
    ]
    for script in scripts:
        module = importlib.import_module(script)
        assert hasattr(module, "main")
