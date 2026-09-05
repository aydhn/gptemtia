from advanced_market_behavior_diagnostics.market_behavior_diagnostics_domain_registry import (
    build_market_behavior_diagnostics_domain_registry,
    summarize_market_behavior_diagnostics_domains,
    CORE_BEHAVIOR_DOMAINS,
)


def test_market_behavior_diagnostics_domain_registry():
    df, summary = build_market_behavior_diagnostics_domain_registry()

    assert not df.empty
    assert len(df) == len(CORE_BEHAVIOR_DOMAINS)
    assert "domain_name" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True
    assert "volatility_behavior_domain" in summary["domain_names"]
    assert "trend_behavior_domain" in summary["domain_names"]

