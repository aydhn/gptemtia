"""Tests for Phase 131 Cross-Asset Regime Scripts Contract."""

from pathlib import Path

EXPECTED_SCRIPTS = [
    "run_cross_asset_regime_profile_registry",
    "run_cross_asset_regime_entities",
    "run_cross_asset_regime_contexts",
    "run_cross_asset_regime_linkage_reports",
    "run_cross_asset_regime_alignment_guards",
    "run_cross_asset_regime_findings_manifest",
    "run_cross_asset_regime_health_check",
    "run_cross_asset_regime_validation_report",
    "run_cross_asset_regime_status",
]


def test_cross_asset_regime_scripts_exist():
    scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
    for script_name in EXPECTED_SCRIPTS:
        script_file = scripts_dir / f"{script_name}.py"
        assert script_file.exists(), f"Script {script_name}.py is missing"


def test_cross_asset_regime_scripts_have_main_and_phase_reference():
    scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
    for script_name in EXPECTED_SCRIPTS:
        script_file = scripts_dir / f"{script_name}.py"
        content = script_file.read_text(encoding="utf-8")
        assert "def main():" in content
        assert "Phase 131" in content or "PHASE 131" in content
