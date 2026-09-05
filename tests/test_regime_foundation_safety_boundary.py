from advanced_regime_foundation.regime_foundation_safety_boundary import (
    build_regime_foundation_safety_boundary,
    build_regime_foundation_no_go_conditions,
    build_regime_foundation_safe_go_conditions,
    summarize_regime_foundation_safety_boundary,
)


def test_regime_foundation_safety_boundary():
    df_no, s_no = build_regime_foundation_no_go_conditions()
    assert len(df_no) >= 15
    assert s_no["all_enforced"] is True

    df_safe, s_safe = build_regime_foundation_safe_go_conditions()
    assert len(df_safe) >= 8
    assert s_safe["all_active"] is True

    df, summary = build_regime_foundation_safety_boundary()
    assert not df.empty
    assert summary["safety_status"] == "SECURE"
    assert summary["no_go_count"] >= 15
    assert summary["safe_go_count"] >= 8
    assert summary["non_signal"] is True

    summ = summarize_regime_foundation_safety_boundary(df)
    assert summ["safety_status"] == "SECURE"
    assert summ["non_signal"] is True
