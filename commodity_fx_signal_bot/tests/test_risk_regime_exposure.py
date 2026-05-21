import pytest
import pandas as pd
from portfolio_regime.risk_regime_exposure import (
    calculate_basket_regime_exposure,
    calculate_asset_class_regime_exposure
)

def test_risk_regime_exposure():
    ret_df = pd.DataFrame({"A": [0.01, -0.01], "B": [0.02, -0.02]}, index=[1,2])
    reg_df = pd.DataFrame({"regime_label": ["r1", "r2"]}, index=[1,2])

    basket_returns = {"b1": ret_df["A"]}

    res = calculate_basket_regime_exposure(basket_returns, reg_df)
    assert not res.empty
    assert "exposure_score" in res.columns
