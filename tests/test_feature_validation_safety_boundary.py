import pytest
from advanced_feature_validation.feature_validation_safety_boundary import (
    validate_feature_validation_safety_boundary,
    get_safety_boundary_rules,
)


def test_feature_validation_safety_boundary():
    rules = get_safety_boundary_rules()
    assert len(rules["no_go_rules"]) >= 10
    assert len(rules["safe_go_principles"]) >= 5

    res = validate_feature_validation_safety_boundary()
    assert res["status"] == "SECURE"
    assert res["current_phase"] == 121
    assert res["non_signal_mandate"] is True
    assert res["dry_run_mandate"] is True
    assert res["destructive_action_allowed"] is False
