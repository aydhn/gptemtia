"""Tests for Phase 132 Macro/Event/News Regime Scripts Contract."""

from pathlib import Path

EXPECTED_SCRIPTS = [
    "run_macro_event_news_regime_profile_registry",
    "run_macro_event_news_regime_entities",
    "run_macro_regime_contexts",
    "run_event_regime_contexts",
    "run_news_metadata_regime_contexts",
    "run_macro_event_news_alignment_guards",
    "run_macro_event_news_findings_manifest",
    "run_macro_event_news_regime_health_check",
    "run_macro_event_news_regime_validation_report",
    "run_macro_event_news_regime_status",
]


def test_macro_event_news_regime_scripts_exist():
    scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
    for script_name in EXPECTED_SCRIPTS:
        script_file = scripts_dir / f"{script_name}.py"
        assert script_file.exists(), f"Script {script_name}.py is missing"


def test_macro_event_news_regime_scripts_have_main_and_phase_reference():
    scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
    for script_name in EXPECTED_SCRIPTS:
        script_file = scripts_dir / f"{script_name}.py"
        content = script_file.read_text(encoding="utf-8")
        assert "def main():" in content
        assert "Phase 132" in content or "PHASE 132" in content
