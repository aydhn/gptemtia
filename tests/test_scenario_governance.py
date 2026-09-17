# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Scenario Governance."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.scenario_governance import (
    build_scenario_governance_registry,
    SCENARIO_GOVERNANCE_ITEMS,
)


def test_build_scenario_governance():
    profile = get_default_backtest_governance_profile()
    df, summary = build_scenario_governance_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "scenario_id" in df.columns
    assert "name" in df.columns
    assert (df["execution_allowed"] == False).all()
    assert (df["status"] == "GOVERNANCE_CONTRACT_READY").all()
    assert summary["total_scenarios"] == 3
    assert summary["execution_disabled"] is True
    assert len(SCENARIO_GOVERNANCE_ITEMS) == 3
