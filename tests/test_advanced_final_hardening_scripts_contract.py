# -*- coding: utf-8 -*-
"""Unit tests verifying all Phase 159 scripts execute cleanly in dry-run mode."""

import subprocess
import sys


def run_script(module_name: str):
    res = subprocess.run(
        [sys.executable, "-m", module_name, "--dry-run", "--no-save"],
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0, f"Script {module_name} failed: {res.stderr}"


def test_run_final_hardening_profile_registry():
    run_script("scripts.run_final_hardening_profile_registry")


def test_run_final_hardening_contracts():
    run_script("scripts.run_final_hardening_contracts")


def test_run_operator_runbook_contracts():
    run_script("scripts.run_operator_runbook_contracts")


def test_run_release_candidate_checklists():
    run_script("scripts.run_release_candidate_checklists")


def test_run_final_freeze_audits():
    run_script("scripts.run_final_freeze_audits")


def test_run_final_inventory_reports():
    run_script("scripts.run_final_inventory_reports")


def test_run_release_candidate_boundaries():
    run_script("scripts.run_release_candidate_boundaries")


def test_run_release_candidate_findings_manifest():
    run_script("scripts.run_release_candidate_findings_manifest")


def test_run_final_hardening_health_check():
    run_script("scripts.run_final_hardening_health_check")


def test_run_final_hardening_validation_report():
    run_script("scripts.run_final_hardening_validation_report")


def test_run_release_candidate_status():
    run_script("scripts.run_release_candidate_status")
