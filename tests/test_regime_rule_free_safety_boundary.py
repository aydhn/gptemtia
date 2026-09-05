from advanced_regime_rule_free.regime_rule_free_safety_boundary import (
    build_regime_rule_free_no_go_conditions,
    build_regime_rule_free_safe_go_conditions,
    build_regime_rule_free_safety_boundary,
    summarize_regime_rule_free_safety_boundary,
    NO_GO_CONDITIONS,
    SAFE_GO_CONDITIONS,
)


def test_build_regime_rule_free_safety_boundary():
    df, summary = build_regime_rule_free_safety_boundary()
    assert len(df) == 24
    assert summary["safety_status"] == "SECURE"
    assert summary["no_go_count"] == 16
    assert summary["safe_go_count"] == 8
    assert summary["all_active"] is True

    assert len(NO_GO_CONDITIONS) == 16
    assert len(SAFE_GO_CONDITIONS) == 8


def test_no_go_and_safe_go():
    df_no, s_no = build_regime_rule_free_no_go_conditions()
    assert len(df_no) == 16
    assert s_no["boundary_status"] == "SECURE"

    df_safe, s_safe = build_regime_rule_free_safe_go_conditions()
    assert len(df_safe) == 8
    assert s_safe["principles_status"] == "ACTIVE"
