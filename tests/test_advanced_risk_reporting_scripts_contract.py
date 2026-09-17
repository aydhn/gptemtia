# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 scripts contract."""

from pathlib import Path
import pytest

SCRIPT_NAMES = [
    "run_risk_reporting_profile_registry.py",
    "run_risk_report_contracts.py",
    "run_exposure_attribution_contracts.py",
    "run_limit_monitoring_contracts.py",
    "run_risk_monitor_placeholders.py",
    "run_risk_reporting_outputs_metrics.py",
    "run_risk_reporting_dependencies_guards.py",
    "run_risk_reporting_disabled_execution_reports.py",
    "run_risk_reporting_findings_manifest.py",
    "run_risk_reporting_health_check.py",
    "run_risk_reporting_validation_report.py",
    "run_risk_reporting_status.py",
]


def test_scripts_exist():
    scripts_dir = Path(__file__).resolve().parents[1] / "scripts"
    for name in SCRIPT_NAMES:
        path = scripts_dir / name
        assert path.exists(), f"Script {name} is missing in scripts directory"


def test_scripts_main_callable():
    scripts_dir = Path(__file__).resolve().parents[1] / "scripts"
    import importlib.util

    for name in SCRIPT_NAMES:
        path = scripts_dir / name
        module_name = name.replace(".py", "")
        spec = importlib.util.spec_from_file_location(module_name, str(path))
        assert spec is not None
        module = importlib.util.module_from_spec(spec)
        assert hasattr(module, "main") or hasattr(spec, "loader")
