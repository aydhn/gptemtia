import pandas as pd
from decisions.decision_components import (
    calculate_signal_score_component,
    calculate_directional_consensus_component,
    calculate_regime_confirmation_component,
    calculate_strategy_readiness_score,
)


def test_signal_score_component():
    df = pd.DataFrame({"signal_score": [0.5, 0.8]})
    score = calculate_signal_score_component(df)
    assert score == 0.8


def test_regime_confirmation_component_empty():
    score = calculate_regime_confirmation_component(
        {}, pd.Timestamp("2023-01-01"), "bullish", "trend"
    )
    assert score == 0.5


def test_strategy_readiness_score():
    score = calculate_strategy_readiness_score({"a": 1.0, "b": 0.5})
    assert score == 0.75
