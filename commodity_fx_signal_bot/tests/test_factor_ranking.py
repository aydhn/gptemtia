import pandas as pd
from factor_research.factor_ranking import calculate_composite_factor_score

def test_factor_ranking():
    df = pd.DataFrame({"symbol": ["A", "A", "B"], "factor_id": ["f1", "f2", "f1"], "normalized_score": [0.8, 0.6, 0.2]})
    s = calculate_composite_factor_score(df)
    assert s.loc["A"] == 0.7
