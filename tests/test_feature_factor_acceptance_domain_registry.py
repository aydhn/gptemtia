from advanced_feature_factor_acceptance.feature_factor_acceptance_domain_registry import (
    build_feature_factor_acceptance_domain_registry,
    summarize_feature_factor_acceptance_domain_registry,
)

def test_acceptance_domain_registry():
    df, summary = build_feature_factor_acceptance_domain_registry()
    assert not df.empty
    assert summary["total_domains"] >= 10
    assert summary["block_domains"] == 10
    assert summary["handoff_domains"] == 1
    assert summary["non_signal"] is True

    s = summarize_feature_factor_acceptance_domain_registry(df)
    assert s["total_domains"] >= 10
    assert s["all_non_signal"] is True
