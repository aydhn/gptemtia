# -*- coding: utf-8 -*-
"""Unit tests verifying all Phase 160 scripts execute cleanly in dry-run mode."""

import subprocess
import sys


def run_script(module_name: str):
    res = subprocess.run(
        [sys.executable, "-m", module_name, "--dry-run", "--no-save"],
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0, f"Script {module_name} failed: {res.stderr}"


def test_run_final_delivery_profile_registry():
    run_script("scripts.run_final_delivery_profile_registry")


def test_run_final_delivery_package_contracts():
    run_script("scripts.run_final_delivery_package_contracts")


def test_run_final_delivery_inventory():
    run_script("scripts.run_final_delivery_inventory")


def test_run_final_delivery_evidence():
    run_script("scripts.run_final_delivery_evidence")


def test_run_final_delivery_phase_summaries():
    run_script("scripts.run_final_delivery_phase_summaries")


def test_run_final_delivery_boundaries():
    run_script("scripts.run_final_delivery_boundaries")


def test_run_final_delivery_disabled_execution_reports():
    run_script("scripts.run_final_delivery_disabled_execution_reports")


def test_run_final_delivery_findings_manifest():
    run_script("scripts.run_final_delivery_findings_manifest")


def test_run_final_delivery_health_check():
    run_script("scripts.run_final_delivery_health_check")


def test_run_final_delivery_validation_report():
    run_script("scripts.run_final_delivery_validation_report")


def test_run_final_delivery_status():
    run_script("scripts.run_final_delivery_status")


def test_run_final_160_phase_completion_report():
    run_script("scripts.run_final_160_phase_completion_report")
