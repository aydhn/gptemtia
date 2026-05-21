import pytest
import pandas as pd
from portfolio_regime.regime_conditioned_returns import (
    join_returns_with_regimes,
    calculate_regime_conditioned_symbol_returns,
    calculate_regime_conditioned_basket_returns,
    summarize_regime_conditioned_returns
)

def test_regime_conditioned_symbol_returns():
    ret_df = pd.DataFrame({"A": [0.01, -0.01, 0.02], "B": [-0.01, 0.01, -0.02]}, index=[1,2,3])
    reg_df = pd.DataFrame({"regime_label": ["risk_on_regime", "risk_off_regime", "risk_on_regime"]}, index=[1,2,3])

    res = calculate_regime_conditioned_symbol_returns(ret_df, reg_df)
    assert not res.empty
    assert "mean_return" in res.columns
    assert "hit_rate_positive" in res.columns

    summary = summarize_regime_conditioned_returns(res)
    assert summary["status"] == "success"
    assert summary["regimes_analyzed"] == 2
