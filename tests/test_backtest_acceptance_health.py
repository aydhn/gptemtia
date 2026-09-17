import pytest
import pandas as pd
from pathlib import Path
from advanced_backtest_acceptance.backtest_acceptance_health import (
    build_backtest_acceptance_health_check,
    HEALTH_COMPONENTS,
)

def test_backtest_acceptance_health():
    df, summary = build_backtest_acceptance_health_check(project_root=Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(HEALTH_COMPONENTS)
    assert summary["total_components"] == len(HEALTH_COMPONENTS)
    assert summary["healthy_components"] == len(HEALTH_COMPONENTS)
    assert summary["all_healthy"] is True
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Check invariants
    assert (df["healthy"] == True).all()
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()
