import pytest
import pandas as pd
from levels.level_filters import (
    should_block_level_candidate,
    infer_level_candidate_label,
)
from levels.level_config import get_default_level_profile


def test_should_block():
    prof = get_default_level_profile()
    row = pd.Series({"sizing_label": "sizing_rejected_candidate"})
    eval_d = {"reward_risk": 1.0}
    blocked, reasons = should_block_level_candidate(row, eval_d, prof)
    assert blocked is True
    assert "sizing_rejection" in reasons
    assert "insufficient_reward_risk" in reasons


def test_infer_label():
    prof = get_default_level_profile()
    row = pd.Series(
        {
            "sizing_label": "sizing_approved_candidate",
            "directional_bias": "long_bias_candidate",
        }
    )
    eval_d = {"reward_risk": 2.0, "stop_distance_pct": 0.05}
    label = infer_level_candidate_label(row, eval_d, prof)
    assert label == "level_watchlist_candidate"
