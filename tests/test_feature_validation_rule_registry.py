import pytest
from advanced_feature_validation.feature_validation_rule_registry import (
    get_feature_validation_rule_registry,
    get_feature_validation_rules_summary,
)


def test_feature_validation_rule_registry():
    rules = get_feature_validation_rule_registry()
    assert len(rules) >= 10
    rule_ids = [r.rule_id for r in rules]
    assert "RULE-VAL-001" in rule_ids
    assert "RULE-VAL-002" in rule_ids

    summary = get_feature_validation_rules_summary()
    assert summary["total_rules"] == len(rules)
    assert summary["enabled_rules"] == len(rules)
    assert summary["current_phase"] == 121
