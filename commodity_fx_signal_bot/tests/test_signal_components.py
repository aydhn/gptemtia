import pytest
import pandas as pd
from signals.signal_components import (
    calculate_event_strength_score,
    calculate_category_confluence_score,
    calculate_directional_confluence_score,
    calculate_conflict_score,
)


def test_calculate_event_strength_score():
    df = pd.DataFrame(
        {
            "is_warning": [False, False],
            "is_context": [False, False],
            "normalized_strength": [0.8, 0.6],
        }
    )
    score = calculate_event_strength_score(df, pd.Timestamp("2023-01-01"))
    assert score > 0.0


def test_calculate_category_confluence_score():
    df = pd.DataFrame(
        {
            "is_warning": [False, False, False],
            "is_context": [False, False, False],
            "event_group": ["trend", "momentum", "volatility"],
        }
    )
    score = calculate_category_confluence_score(df, pd.Timestamp("2023-01-01"))
    assert score == 0.6  # 3 / 5.0


def test_calculate_directional_confluence_score():
    df = pd.DataFrame(
        {
            "is_warning": [False, False],
            "is_context": [False, False],
            "directional_bias": ["bullish", "bullish"],
        }
    )
    score = calculate_directional_confluence_score(
        df, pd.Timestamp("2023-01-01"), "bullish"
    )
    assert score == 1.0


def test_calculate_conflict_score():
    df = pd.DataFrame({"directional_bias": ["bullish", "bearish"]})
    score = calculate_conflict_score(df, {}, pd.Timestamp("2023-01-01"), "bullish")
    assert score == 0.5
