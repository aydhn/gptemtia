import pandas as pd

from strategies.strategy_config import get_default_strategy_selection_profile
from strategies.strategy_selector import StrategySelector


def test_select_for_decision():
    profile = get_default_strategy_selection_profile()
    selector = StrategySelector(profile)

    row = pd.Series(
        {
            "decision_label": "long_bias_candidate",
            "candidate_type": "trend_following",
            "decision_score": 0.9,
            "quality_score": 0.9,
        },
        name=pd.Timestamp("2023-01-01"),
    )

    context = {
        "regime": {"regime_label": "bullish_trend"},
        "mtf": {"mtf_trend_alignment_bullish": True},
    }

    candidates = selector.select_for_decision("TEST", "1d", row, context)
    assert isinstance(candidates, list)

    assert len(candidates) > 0
    for c in candidates:
        assert c.directional_bias not in ["BUY", "SELL", "OPEN_LONG", "OPEN_SHORT"]
