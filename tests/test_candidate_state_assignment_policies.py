from advanced_regime_rule_free.candidate_state_assignment_policies import (
    build_candidate_state_assignment_policy_registry,
    validate_candidate_state_assignment_policy,
)


def test_build_candidate_state_assignment_policy_registry():
    df, summary = build_candidate_state_assignment_policy_registry()
    assert len(df) == 8
    assert summary["all_non_signal"] is True
    assert summary["all_non_executable"] is True
    assert summary["all_non_trade_signal"] is True
    assert summary["policies_status"] == "VALID"

    policy_names = df["policy_name"].tolist()
    assert "threshold_free_context_assignment_placeholder" in policy_names
    assert "percentile_context_assignment_placeholder" in policy_names
    assert "rank_context_assignment_placeholder" in policy_names
    assert "distance_to_centroid_placeholder" in policy_names
    assert "cluster_membership_placeholder" in policy_names


def test_validate_candidate_state_assignment_policy():
    valid_p = {
        "policy_name": "threshold_free_context_assignment_placeholder",
        "execution_allowed": False,
        "generates_trade_signal": False,
        "non_signal": True,
    }
    assert validate_candidate_state_assignment_policy(valid_p)["is_valid"] is True

    invalid_p = {
        "policy_name": "buy_signal_rule",
        "execution_allowed": True,
        "generates_trade_signal": True,
        "non_signal": False,
    }
    res = validate_candidate_state_assignment_policy(invalid_p)
    assert res["is_valid"] is False
