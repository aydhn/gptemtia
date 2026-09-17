# -*- coding: utf-8 -*-
"""Contract tests verifying all 10 Phase 139 scripts execute cleanly with exit code 0."""

import os
import subprocess
import sys
from pathlib import Path
import pytest

SCRIPTS = [
    "run_gpu_training_governance_profile_registry.py",
    "run_gpu_training_resource_policies.py",
    "run_gpu_training_harness_contracts.py",
    "run_gpu_training_dry_run_guards.py",
    "run_gpu_training_disabled_execution_reports.py",
    "run_gpu_training_dependencies_inputs.py",
    "run_gpu_training_findings_manifest.py",
    "run_gpu_training_governance_health_check.py",
    "run_gpu_training_governance_validation_report.py",
    "run_gpu_training_governance_status.py",
]


@pytest.mark.parametrize("script_name", SCRIPTS)
def test_phase_139_script_execution(script_name):
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
