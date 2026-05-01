import pytest
import pandas as pd
from mtf.mtf_events import detect_mtf_trend_alignment_events, build_mtf_event_frame


def test_detect_mtf_trend_alignment_events():
    df = pd.DataFrame({"mtf_trend_alignment_score": [0.1, 0.8, -0.9]})

    res = detect_mtf_trend_alignment_events(df)
    # Threshold default 0.60
    assert list(res["event_mtf_trend_alignment_candidate"]) == [0, 1, 1]


def test_build_mtf_event_frame():
    df = pd.DataFrame({"mtf_trend_alignment_score": [0.8], "mtf_conflict_score": [0.9]})

    res, summ = build_mtf_event_frame(df)
    assert "event_mtf_trend_alignment_candidate" in res.columns
    assert "event_mtf_high_conflict" in res.columns
    assert summ["total_event_count"] > 0
