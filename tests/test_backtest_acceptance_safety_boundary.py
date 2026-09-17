import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_safety_boundary import (
    build_backtest_acceptance_no_go_conditions,
    build_backtest_acceptance_safe_go_conditions,
    build_backtest_acceptance_safety_boundary,
    NO_GO_RULES,
    SAFE_GO_RULES,
)

def test_backtest_acceptance_safety_boundary():
    no_go = build_backtest_acceptance_no_go_conditions()
    assert len(no_go) == len(NO_GO_RULES)
    assert all(item["prohibited"] is True for item in no_go)

    safe_go = build_backtest_acceptance_safe_go_conditions()
    assert len(safe_go) == len(SAFE_GO_RULES)
    assert all(item["permitted"] is True for item in safe_go)

    df, summary = build_backtest_acceptance_safety_boundary()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(NO_GO_RULES) + len(SAFE_GO_RULES)
    assert summary["no_go_count"] == len(NO_GO_RULES)
    assert summary["safe_go_count"] == len(SAFE_GO_RULES)
    assert summary["safety_status"] == "SECURE"
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Invariants
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()
