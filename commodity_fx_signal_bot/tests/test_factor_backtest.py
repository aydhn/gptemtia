import pandas as pd
from factor_research.factor_backtest import calculate_forward_returns

def test_factor_backtest():
    df = pd.DataFrame({"A": [0.01, 0.02, 0.03]})
    s = calculate_forward_returns(df, 1)
    # rolling sum shift -1
    # 0 -> 1 = 0.02
    assert s.iloc[0]["A"] == 0.02
