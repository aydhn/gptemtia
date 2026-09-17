import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_domain_registry import (
    build_backtest_acceptance_domain_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import ALL_DOMAINS

def test_backtest_acceptance_domain_registry():
    df, summary = build_backtest_acceptance_domain_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(ALL_DOMAINS)
    assert summary["total_domains"] == len(ALL_DOMAINS)
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True
    assert summary["all_ready"] is True

    # Check that all domain names are included
    assert set(df["domain_name"]) == set(ALL_DOMAINS)
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()
