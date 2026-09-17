import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_profile_registry import (
    build_backtest_acceptance_profile_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_config import (
    get_backtest_acceptance_profile,
)

def test_backtest_acceptance_profile_registry():
    df, summary = build_backtest_acceptance_profile_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) > 0
    assert summary["total_profiles"] == len(df)
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True
    assert summary["all_dry_run"] is True
    assert summary["all_local_only"] is True
    assert summary["all_non_production"] is True

    # Check columns and safety flags
    assert "production_ready" in df.columns
    assert "broker_ready" in df.columns
    assert (df["production_ready"] == False).all()
    assert (df["broker_ready"] == False).all()
    assert (df["non_signal"] == True).all()

    # Active profile check
    active = get_backtest_acceptance_profile("strict_non_production_backtest_acceptance_safety")
    df_custom, summary_custom = build_backtest_acceptance_profile_registry(active)
    assert summary_custom["active_profile"] == "strict_non_production_backtest_acceptance_safety"
    assert (df_custom.loc[df_custom["profile_name"] == "strict_non_production_backtest_acceptance_safety", "is_active"]).iloc[0] == True
