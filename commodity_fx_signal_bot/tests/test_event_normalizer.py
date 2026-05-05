import pytest
import pandas as pd
from signals.event_normalizer import normalize_event_frame


def test_normalize_event_frame_boolean():
    df = pd.DataFrame(
        {"rsi_oversold": [True, False, True]},
        index=pd.date_range("2023-01-01", periods=3),
    )
    norm, sum = normalize_event_frame("GC=F", "1d", "momentum", df)

    assert sum["event_count"] == 2
    assert len(norm) == 2
    assert norm["normalized_strength"].iloc[0] == 1.0


def test_normalize_event_frame_numeric():
    df = pd.DataFrame(
        {"zscore": [0.5, -0.3, 0.0]}, index=pd.date_range("2023-01-01", periods=3)
    )
    norm, sum = normalize_event_frame("GC=F", "1d", "mean_reversion", df)

    assert sum["event_count"] == 2
    assert len(norm) == 2
    assert norm["normalized_strength"].iloc[0] == 0.5
    assert norm["normalized_strength"].iloc[1] == 0.3  # abs val normalized
