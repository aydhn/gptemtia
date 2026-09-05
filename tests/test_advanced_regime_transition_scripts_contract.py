"""Tests for Advanced Regime Transition Scripts Contract."""

from pathlib import Path
import importlib

EXPECTED_SCRIPTS = [
    "run_regime_transition_profile_registry",
    "run_regime_state_sequence_contracts",
    "run_regime_transition_metrics",
    "run_state_transition_diagnostics",
    "run_transition_context_reports",
    "run_transition_quality_findings",
    "run_transition_diagnostics_manifest",
    "run_regime_transition_health_check",
    "run_regime_transition_validation_report",
    "run_regime_transition_status",
]


def test_scripts_exist():
    scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
    for script_name in EXPECTED_SCRIPTS:
        script_file = scripts_dir / f"{script_name}.py"
        assert script_file.exists(), f"Script {script_name}.py is missing"


def test_scripts_have_main_and_disclaimer():
    scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
    for script_name in EXPECTED_SCRIPTS:
        script_file = scripts_dir / f"{script_name}.py"
        content = script_file.read_text(encoding="utf-8")
        assert "def main():" in content
        assert "PHASE 130" in content
        assert "Non-Signal" in content or "non_signal" in content
