# -*- coding: utf-8 -*-
"""Contract tests verifying all 10 Phase 140 scripts execute cleanly with exit code 0."""

import os
import subprocess
import sys
from pathlib import Path
import pytest

SCRIPTS = [
    "run_ensemble_model_profile_registry.py",
    "run_candidate_model_contracts.py",
    "run_candidate_model_eligibility_compatibility.py",
    "run_ensemble_strategy_contracts.py",
    "run_ensemble_disabled_execution_reports.py",
    "run_ensemble_dependencies_inputs.py",
    "run_ensemble_findings_manifest.py",
    "run_ensemble_model_health_check.py",
    "run_ensemble_model_validation_report.py",
    "run_ensemble_model_status.py",
]


@pytest.mark.parametrize("script_name", SCRIPTS)
def test_phase_140_script_execution(script_name):
    project_root = Path(__file__).resolve().parent.parent
    script_path = project_root / "scripts" / script_name

    assert script_path.exists(), f"Script not found: {script_path}"

    env = os.environ.copy()
    env["PYTHONPATH"] = str(project_root)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(project_root),
        env=env,
        capture_output=True,
        text=True,
        timeout=60,
    )

    assert result.returncode == 0, (
        f"Script {script_name} failed with return code {result.returncode}.\n"
        f"STDOUT:\n{result.stdout}\n"
        f"STDERR:\n{result.stderr}"
    )
