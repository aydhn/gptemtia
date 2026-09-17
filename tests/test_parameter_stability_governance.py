# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Parameter Stability Governance."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.parameter_stability_governance import (
    build_parameter_stability_governance_registry,
    PARAMETER_STABILITY_ITEMS,
)


def test_build_parameter_stability_governance():
    profile = get_default_backtest_governance_profile()
    df, summary = build_parameter_stability_governance_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "stability_id" in df.columns
    assert "name" in df.columns
    assert (df["execution_allowed"] == False).all()
    assert (df["status"] == "GOVERNANCE_CONTRACT_READY").all()
    assert summary["total_rules"] == 3
    assert summary["execution_disabled"] is True
    assert len(PARAMETER_STABILITY_ITEMS) == 3
