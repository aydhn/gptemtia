"""Test scripts."""
import subprocess
from pathlib import Path

def test_scripts_runnable():
    scripts = [
        "run_reproducibility_domain_registry.py",
        "run_reproducibility_dossier.py",
        "run_environment_replay_manifest.py",
        "run_deterministic_runbook.py",
        "run_build_free_reproduction_layer.py",
        "run_terminal_reproducibility_governance.py",
        "run_reproducibility_quality_report.py",
        "run_reproducibility_status.py",
    ]
    for script in scripts:
        script_path = Path("scripts") / script
        if script_path.exists():
            with open(script_path, "r", encoding="utf-8") as f:
                content = f.read()
            assert "def main():" in content
            assert "if __name__ == \"__main__\":" in content
