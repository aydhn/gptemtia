import pytest
import pandas as pd
from portfolio_regime.regime_config import PortfolioRegimeProfile
from portfolio_regime.stress_windows import (
    identify_historical_stress_windows,
    classify_stress_severity,
    build_stress_window_summary
)

def test_stress_windows():
    profile = PortfolioRegimeProfile(name="test", description="")
    series = pd.Series([1.0]*30, index=pd.date_range("2023-01-01", periods=30))

    windows = identify_historical_stress_windows(series, profile)
    assert not windows.empty

    assert classify_stress_severity(-0.15) == "severe_stress"

    summary = build_stress_window_summary(windows)
    assert summary["status"] == "success"
