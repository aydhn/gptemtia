from advanced_regime_foundation.regime_non_signal_policies import (
    build_regime_non_signal_policy_registry,
    validate_regime_non_signal_text,
    summarize_regime_non_signal_policies,
)


def test_regime_non_signal_policies():
    df, summary = build_regime_non_signal_policy_registry()
    assert not df.empty
    assert summary["all_mandatory"] is True
    assert summary["all_non_signal"] is True

    clean_text = "Market is in an elevated volatility compression environment."
    assert validate_regime_non_signal_text(clean_text)["is_valid"] is True

    violating_text = "Rejim bullish olduğu için hemen long aç."
    res_viol = validate_regime_non_signal_text(violating_text)
    assert res_viol["is_valid"] is False
    assert res_viol["forbidden_matches_count"] >= 1

    summ = summarize_regime_non_signal_policies(df)
    assert summ["total_policies"] == len(df)
    assert summ["all_mandatory"] is True
