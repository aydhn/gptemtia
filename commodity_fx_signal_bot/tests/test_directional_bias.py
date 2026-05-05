import pandas as pd
from decisions.directional_bias import (
    calculate_directional_bias_counts,
    infer_dominant_direction,
    calculate_directional_consensus_score,
    detect_directional_conflict,
)


def test_directional_bias_counts():
    df = pd.DataFrame({"signal_direction": ["bullish", "bullish", "bearish"]})
    counts = calculate_directional_bias_counts(df)
    assert counts["bullish"] == 2
    assert counts["bearish"] == 1


def test_infer_dominant_direction():
    df = pd.DataFrame({"signal_direction": ["bullish", "bullish", "bearish"]})
    dom = infer_dominant_direction(df)
    assert dom == "bullish"


def test_directional_consensus_score():
    df = pd.DataFrame({"signal_direction": ["bullish", "bullish", "bearish"]})
    score = calculate_directional_consensus_score(df)
    assert 0.0 <= score <= 1.0


def test_detect_directional_conflict():
    df = pd.DataFrame(
        {"signal_direction": ["bullish", "bearish", "bullish", "bearish"]}
    )
    res = detect_directional_conflict(df, conflict_threshold=0.4)
    assert res["is_directional_conflict"] == True
