import pytest
import pandas as pd
from portfolio_regime.tail_risk import (
    calculate_historical_var,
    calculate_historical_cvar,
    calculate_tail_loss_frequency,
    build_tail_risk_table
)
from portfolio_regime.regime_config import PortfolioRegimeProfile

def test_tail_risk():
    import numpy as np
    series = pd.Series(np.random.normal(0, 0.01, 100))

    var = calculate_historical_var(series, 0.05)
    assert var is not None
    assert var < 0

    cvar = calculate_historical_cvar(series, 0.05)
    assert cvar is not None
    assert cvar < var

    freq = calculate_tail_loss_frequency(series)
    assert freq is not None

    profile = PortfolioRegimeProfile(name="test", description="")
    table = build_tail_risk_table({"b1": series}, profile)
    assert not table.empty
