import pytest
import pandas as pd
from signals.signal_scoring import SignalScorer
from signals.signal_config import get_default_signal_scoring_profile


def test_signal_scorer():
    prof = get_default_signal_scoring_profile()
    scorer = SignalScorer(prof)

    events_df = pd.DataFrame(
        {
            "timestamp": ["2023-01-01"],
            "candidate_type": ["trend_following"],
            "directional_bias": ["bullish"],
            "is_warning": [False],
            "is_context": [False],
            "event_name": ["ema_cross"],
            "event_group": ["trend"],
            "normalized_strength": [1.0],
        }
    )

    context_frames = {}

    cands, summary = scorer.score_timestamps("GC=F", "1d", events_df, context_frames)

    assert summary["processed_timestamps"] == 1
    assert len(cands) == 1
    assert cands[0].candidate_score >= 0.0
    assert cands[0].candidate_score <= 1.0
