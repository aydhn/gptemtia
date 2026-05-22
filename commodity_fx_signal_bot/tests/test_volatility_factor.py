import pandas as pd
from factor_research.volatility_factor import calculate_realized_volatility

def test_volatility():
    df = pd.DataFrame({"A": [0.01, -0.02, 0.05, 0.0, 0.01]})
    s = calculate_realized_volatility(df, 3)
    assert s.loc["A"] > 0
