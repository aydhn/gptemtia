import pandas as pd
from factor_research.value_proxy_factor import calculate_distance_from_long_ma

def test_value_proxy():
    df = pd.DataFrame({"A": [100]*252 + [110]})
    s = calculate_distance_from_long_ma(df, 252)
    assert s.loc["A"] > 0
