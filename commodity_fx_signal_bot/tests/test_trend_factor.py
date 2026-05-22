import pandas as pd
from factor_research.trend_factor import calculate_price_trend_score

def test_trend():
    df = pd.DataFrame({"A": [100, 110, 121]})
    s = calculate_price_trend_score(df, 1)
    assert s.loc["A"] > 0
