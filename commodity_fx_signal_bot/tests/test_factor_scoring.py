import pandas as pd
from factor_research.factor_scoring import minmax_normalize_series

def test_scoring():
    s = pd.Series([1, 2, 3])
    norm = minmax_normalize_series(s)
    assert norm.iloc[0] == 0.0
    assert norm.iloc[2] == 1.0
