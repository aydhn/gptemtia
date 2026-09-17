import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_report_builder import (
    build_backtest_acceptance_disclaimer,
    build_backtest_acceptance_profile_markdown_report,
    build_backtest_acceptance_component_markdown_report,
    build_phase_acceptance_markdown_report,
    build_dependency_acceptance_markdown_report,
    build_validation_evidence_markdown_report,
    build_boundary_markdown_report,
    build_blocker_gap_warning_markdown_report,
    build_backtest_acceptance_findings_markdown_report,
    build_backtest_acceptance_readiness_score_markdown_report,
    build_backtest_acceptance_manifest_markdown_report,
    build_backtest_acceptance_validation_markdown_report,
    build_backtest_acceptance_safety_markdown_report,
    build_phase_153_handoff_markdown_report,
    build_backtest_acceptance_full_markdown_report,
)

def test_backtest_acceptance_disclaimer():
    disc = build_backtest_acceptance_disclaimer()
    assert "YASAL UYARI VE GÜVENLİK BİLDİRİMİ" in disc
    assert "Canlı emir" in disc
    assert "kesin AL/SAT" in disc
    assert "Phase 152" in disc

def test_report_builders():
    dummy_df = pd.DataFrame([{"col1": "val1", "col2": "val2"}])
    dummy_summary = {"status": "ACCEPTED", "active_profile": "test_profile", "readiness_score": 1.0}

    rep_profile = build_backtest_acceptance_profile_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Profile Registry" in rep_profile
    assert "val1" in rep_profile

    rep_comp = build_backtest_acceptance_component_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Component Registry" in rep_comp

    rep_phase = build_phase_acceptance_markdown_report({"phase_ref": "Phase 146", "phase_title": "Test Title"}, dummy_df)
    assert "Phase 146 Acceptance Report" in rep_phase

    rep_dep = build_dependency_acceptance_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Dependency Verification" in rep_dep

    rep_ev = build_validation_evidence_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Validation Evidence" in rep_ev

    rep_bound = build_boundary_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Boundaries" in rep_bound

    rep_block = build_blocker_gap_warning_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Findings" in rep_block

    rep_find = build_backtest_acceptance_findings_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Consolidated Findings" in rep_find

    rep_score = build_backtest_acceptance_readiness_score_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Readiness Score Report" in rep_score

    rep_man = build_backtest_acceptance_manifest_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Manifest" in rep_man

    rep_val = build_backtest_acceptance_validation_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Validation Report" in rep_val

    rep_safe = build_backtest_acceptance_safety_markdown_report(dummy_summary, dummy_df)
    assert "Backtest Acceptance Safety Boundary Report" in rep_safe

    rep_ho = build_phase_153_handoff_markdown_report(dummy_summary, dummy_df)
    assert "Phase 153 Portfolio Construction" in rep_ho

    full_rep = build_backtest_acceptance_full_markdown_report({"components": dummy_df}, dummy_summary)
    assert "Phase 152 Backtest Acceptance Consolidated Report" in full_rep
    assert "Table: Components" in full_rep
