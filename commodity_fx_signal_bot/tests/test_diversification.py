import pandas as pd
import numpy as np
from portfolio_research.diversification import (
    calculate_diversification_score,
    calculate_effective_number_of_assets,
    infer_diversification_label,
    build_diversification_table
)

def test_diversification():
    corr = pd.DataFrame({
        "A": [1.0, 0.2],
        "B": [0.2, 1.0]
    }, index=["A", "B"])

    score = calculate_diversification_score(corr)
    assert 0.0 <= score <= 1.0

    w = {"A": 0.5, "B": 0.5}
    eff = calculate_effective_number_of_assets(w)
    assert eff == 2.0

    label = infer_diversification_label(score, eff, 2)
    assert label in ["well_diversified", "moderately_diversified", "concentrated", "highly_concentrated"]
