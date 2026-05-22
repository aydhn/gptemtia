import pandas as pd
from factor_research.momentum_factor import calculate_return_momentum_score

def test_momentum():
    df = pd.DataFrame({"A": [0.01, -0.02, 0.05]})
    s = calculate_return_momentum_score(df, 2)
    assert round(s.loc["A"], 2) == 0.03
