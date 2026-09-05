import pandas as pd
from advanced_regime_rule_free.regime_rule_free_report_builder import (
    build_regime_rule_free_disclaimer,
    _df_to_markdown_simple,
    build_regime_rule_free_profile_markdown_report,
    build_rule_free_labeling_contract_markdown_report,
    build_candidate_state_schema_markdown_report,
    build_unsupervised_prep_contract_markdown_report,
    build_algorithm_placeholder_markdown_report,
    build_candidate_state_metadata_markdown_report,
    build_candidate_state_integrity_markdown_report,
    build_regime_rule_free_validation_markdown_report,
    build_regime_rule_free_safety_markdown_report,
    build_phase_129_handoff_markdown_report,
)


def test_build_regime_rule_free_disclaimer():
    disc = build_regime_rule_free_disclaimer()
    assert "YASAL UYARI" in disc
    assert "Phase 128" in disc
    assert "non-signal" in disc.lower()


def test_df_to_markdown_simple():
    empty_res = _df_to_markdown_simple(pd.DataFrame())
    assert "Tabloda veri bulunmuyor" in empty_res

    df = pd.DataFrame({"colA": [1, 2], "colB": ["x", "y"]})
    res = _df_to_markdown_simple(df)
    assert "| colA | colB |" in res
    assert "| 1 | x |" in res


def test_markdown_reports():
    test_df = pd.DataFrame({"item": ["a", "b"], "status": ["OK", "OK"]})
    summary = {"active_profile": "test", "status": "READY", "is_valid": True}

    rep1 = build_regime_rule_free_profile_markdown_report(summary, test_df)
    assert "Phase 128: Regime Rule-Free Profile Registry Report" in rep1

    rep2 = build_rule_free_labeling_contract_markdown_report(summary, test_df)
    assert "Rule-Free Labeling Contracts Report" in rep2

    rep3 = build_candidate_state_schema_markdown_report(summary, test_df)
    assert "Candidate State Schema Report" in rep3

    rep4 = build_unsupervised_prep_contract_markdown_report(summary, test_df)
    assert "Unsupervised Preparation Contracts Report" in rep4

    rep5 = build_algorithm_placeholder_markdown_report(summary, test_df)
    assert "Algorithm & Metric Placeholders Report" in rep5

    rep6 = build_candidate_state_metadata_markdown_report(summary, test_df)
    assert "Candidate State Metadata Report" in rep6

    rep7 = build_candidate_state_integrity_markdown_report(summary, test_df)
    assert "Candidate State Integrity Manifest Report" in rep7

    rep8 = build_regime_rule_free_validation_markdown_report(summary, test_df)
    assert "Regime Rule-Free Validation Report" in rep8

    rep9 = build_regime_rule_free_safety_markdown_report(summary, test_df)
    assert "Regime Rule-Free Safety Boundary Report" in rep9

    rep10 = build_phase_129_handoff_markdown_report(summary, test_df)
    assert "Phase 128 to Phase 129 Handoff Report" in rep10
