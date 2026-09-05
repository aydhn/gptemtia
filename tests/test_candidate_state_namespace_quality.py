from advanced_market_behavior_diagnostics.candidate_state_namespace_quality import (
    build_candidate_state_namespace_quality_report,
    summarize_candidate_state_namespace_quality,
)


def test_candidate_state_namespace_quality():
    df, summary = build_candidate_state_namespace_quality_report()

    assert not df.empty
    assert "candidate_state_name" in df.columns
    assert "namespace_valid" in df.columns
    assert summary["all_namespaces_valid"] is True
    assert summary["forbidden_keywords_found"] is False
    assert summary["non_signal"] is True
