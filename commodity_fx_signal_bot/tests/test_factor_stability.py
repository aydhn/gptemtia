import pandas as pd
from factor_research.factor_stability import calculate_rank_stability

def test_factor_stability():
    curr = pd.DataFrame({"symbol": ["A"], "factor_id": ["f1"], "rank": [1]})
    prev = pd.DataFrame({"symbol": ["A"], "factor_id": ["f1"], "rank": [2]})
    res = calculate_rank_stability(curr, prev)
    assert not res.empty
