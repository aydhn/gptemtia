from advanced_regime_rule_free.regime_rule_free_source_preservation_policies import (
    validate_regime_rule_free_source_preservation_action,
    build_regime_rule_free_source_preservation_policy_registry,
    summarize_regime_rule_free_source_preservation_policies,
    FORBIDDEN_SOURCE_ACTIONS,
)


def test_validate_regime_rule_free_source_preservation_action():
    assert validate_regime_rule_free_source_preservation_action("read_source_file")["is_permitted"] is True

    assert validate_regime_rule_free_source_preservation_action("overwrite_source")["is_permitted"] is False
    assert validate_regime_rule_free_source_preservation_action("delete_source")["is_permitted"] is False
    assert validate_regime_rule_free_source_preservation_action("auto_drop_feature")["is_permitted"] is False


def test_build_regime_rule_free_source_preservation_policy_registry():
    df, summary = build_regime_rule_free_source_preservation_policy_registry()
    assert len(df) == 5
    assert summary["all_rules_enforced"] is True
    assert summary["forbidden_actions_count"] == len(FORBIDDEN_SOURCE_ACTIONS)
    assert summary["preservation_status"] == "SECURE"
