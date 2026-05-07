import pytest
from levels.reward_risk import (
    calculate_reward_risk,
    build_reward_risk_table,
    select_best_reward_risk_candidate,
)


def test_calculate_rr():
    assert calculate_reward_risk(100.0, 98.0, 104.0, "long_bias_candidate") == 2.0
    assert calculate_reward_risk(100.0, 102.0, 96.0, "short_bias_candidate") == 2.0
    assert calculate_reward_risk(100.0, 102.0, 104.0, "long_bias_candidate") is None


def test_rr_table_and_select():
    table = build_reward_risk_table(
        100.0, [98.0, 95.0], [102.0, 106.0], "long_bias_candidate"
    )
    assert len(table) == 4
    best = select_best_reward_risk_candidate(table, 1.5)
    assert best["reward_risk"] is not None
