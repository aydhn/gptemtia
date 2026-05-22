import pandas as pd
from factor_research.factor_ic import calculate_factor_ic_proxy

def test_factor_ic():
    df = pd.DataFrame({"f1": [0.1, 0.2, 0.3]}, index=["A", "B", "C"])
    ret = pd.DataFrame({"A": [0.1], "B": [0.2], "C": [0.3]}, index=["2020-01-01"])
    res = calculate_factor_ic_proxy(df, ret)
    assert not res.empty
