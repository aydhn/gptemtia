import pandas as pd
from factor_research.factor_exposure import calculate_symbol_factor_exposure

def test_factor_exposure():
    df = pd.DataFrame({"symbol": ["A", "B"], "factor_id": ["f1", "f1"], "normalized_score": [0.8, 0.2]})
    res = calculate_symbol_factor_exposure(df)
    assert not res.empty
