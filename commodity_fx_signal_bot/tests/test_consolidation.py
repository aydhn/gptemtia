import pytest
import pandas as pd
from pathlib import Path
from command_center.consolidation import (
    build_project_consolidation_summary,
    build_consolidation_score,
    infer_project_maturity_label,
    build_consolidation_table,
    build_phase_1_to_50_digest
)

def test_consolidation_summary():
    status_df = pd.DataFrame([{"status_label": "active", "warnings": []}])
    health_df = pd.DataFrame([{"health_label": "healthy_offline_module", "health_score": 1.0}])
    phase_df = pd.DataFrame([{"status": "covered"}])
    script_df = pd.DataFrame([{"script_class": "status_script", "warnings": [], "inferred_module": "command_center"}])

    summary = build_project_consolidation_summary(status_df, health_df, phase_df, script_df)
    assert "status_summary" in summary

    assert "script_summary" in summary
    assert "coverage_summary" in summary

def test_consolidation_score_and_label():
    summary = {
        "health_summary": {"healthy_modules": 15},
        "coverage_summary": {"phases_covered": 10}
    }
    score = build_consolidation_score(summary)
    assert score == 1.0

    label = infer_project_maturity_label(score)
    assert label == "consolidated_offline_research_platform"
    assert "production readiness" not in label

def test_build_consolidation_table():
    summary = {
        "health_summary": {"healthy_modules": 15},
        "coverage_summary": {"phases_covered": 10}
    }
    df = build_consolidation_table(summary)
    assert not df.empty

def test_build_phase_1_to_50_digest():
    digest = build_phase_1_to_50_digest(Path("."))
    assert isinstance(digest, str)
    assert "offline" in digest.lower()
    assert "live trade" in digest.lower() # It should mention it does not generate live trades
