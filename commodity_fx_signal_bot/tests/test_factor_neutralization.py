import pandas as pd
from factor_research.factor_neutralization import demean_scores_by_group

def test_factor_neutralization():
    df = pd.DataFrame({"asset_class": ["C", "C"], "factor_id": ["f1", "f1"], "normalized_score": [0.8, 0.2]})
    res = demean_scores_by_group(df)
    assert round(res.iloc[0]["normalized_score"], 2) == 0.30
