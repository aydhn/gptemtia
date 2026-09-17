# -*- coding: utf-8 -*-
"""Contract tests verifying all 9 Phase 138 scripts execute cleanly with exit code 0."""

import os
import subprocess
import sys
from pathlib import Path
import pytest

SCRIPTS = [
    "run_baseline_ml_model_profile_registry.py",
    "run_baseline_model_contracts.py",
    "run_dry_run_training_harness_contracts.py",
    "run_baseline_model_safety_reports.py",
    "run_baseline_model_dependencies_inputs.py",
    "run_baseline_model_findings_manifest.py",
    "run_baseline_ml_model_health_check.py",
    "run_baseline_ml_model_validation_report.py",
    "run_baseline_ml_model_status.py",
]


@pytest.mark.parametrize("script_name", SCRIPTS)
def test_phase_138_script_execution(script_name):
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
