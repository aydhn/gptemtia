import pandas as pd
import numpy as np
from synthetic_indices.weighting_schemes import (
    calculate_equal_weights,
    calculate_inverse_volatility_weights,
    calculate_research_score_weights,
    cap_and_redistribute_weights,
    validate_weights
)

def test_equal_weights():
    weights = calculate_equal_weights(["A", "B", "C", "D"])
    assert len(weights) == 4
    assert sum(weights.values()) == 1.0
    assert weights["A"] == 0.25

def test_inverse_volatility_weights():
    # Construct a dummy DataFrame
    df = pd.DataFrame({
        "A": [0.01, -0.01, 0.02, -0.02], # Std = ~0.018
        "B": [0.05, -0.05, 0.10, -0.10]  # Std = ~0.091 -> Lower weight
    })
    weights, _ = calculate_inverse_volatility_weights(df, max_single_weight=1.0)
    assert sum(weights.values()) == 1.0
    assert weights["A"] > weights["B"]

def test_research_score_weights():
    ranking_df = pd.DataFrame({
        "symbol": ["A", "B", "C"],
        "research_score": [10, 20, 30]
    })
    weights, _ = calculate_research_score_weights(ranking_df, ["A", "B", "C"], max_single_weight=1.0)
    assert sum(weights.values()) == 1.0
    assert weights["C"] > weights["B"] > weights["A"]

def test_cap_and_redistribute():
    weights = {"A": 0.6, "B": 0.3, "C": 0.1}
    capped = cap_and_redistribute_weights(weights, max_single_weight=0.4)
    assert np.isclose(capped["A"], 0.4)
    assert np.isclose(sum(capped.values()), 1.0)

def test_validate_weights():
    weights = {"A": 0.5, "B": 0.5}
    assert len(validate_weights(weights)) == 0

    bad_weights = {"A": 0.5, "B": 0.4} # Sum != 1.0
    assert len(validate_weights(bad_weights)) > 0
