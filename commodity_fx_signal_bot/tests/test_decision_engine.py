import pandas as pd
from decisions.decision_engine import DecisionEngine
from decisions.decision_config import get_default_decision_profile


def test_build_decision_for_timestamp():
    engine = DecisionEngine(get_default_decision_profile())
    df = pd.DataFrame(
        {
            "signal_direction": ["bullish", "bullish"],
            "candidate_type": ["trend", "trend"],
            "signal_score": [0.8, 0.9],
        }
    )

    cand = engine.build_decision_for_timestamp(
        "GC=F", "1d", pd.Timestamp("2023-01-01"), df, {}
    )

    assert cand.symbol == "GC=F"
    assert cand.directional_bias == "bullish"
    assert 0.0 <= cand.decision_score <= 1.0
    assert "BUY" not in cand.decision_label
    assert cand.decision_label in [
        "long_bias_candidate",
        "short_bias_candidate",
        "neutral_candidate",
        "no_trade_candidate",
        "watchlist_candidate",
        "conflict_candidate",
    ]
