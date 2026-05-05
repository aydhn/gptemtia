import pandas as pd

from strategies.strategy_config import get_default_strategy_selection_profile
from strategies.strategy_rules import (
    calculate_strategy_family_fit,
    calculate_strategy_selection_score,
)


def test_calculate_strategy_family_fit():
    profile = get_default_strategy_selection_profile()
    decision_row = pd.Series(
        {
            "decision_score": 0.8,
            "confidence": 0.7,
            "quality_score": 0.6,
            "conflict_score": 0.1,
        }
    )
    context = {
        "regime": {"regime_label": "bullish_trend"},
        "mtf": {"mtf_trend_alignment_bullish": True},
    }

    fit = calculate_strategy_family_fit(
        "trend_following", decision_row, context, profile
    )

    assert isinstance(fit, dict)
    assert fit["family"] == "trend_following"
    assert fit["regime_fit"] == 0.9  # Preferred regime
    assert fit["mtf_fit"] == 0.9  # Aligned MTF
    assert fit["conflict_penalty"] == 0.1
    assert 0.0 <= fit["selection_score"] <= 1.0


def test_calculate_strategy_selection_score():
    profile = get_default_strategy_selection_profile()
    components = {
        "decision_score": 1.0,
        "decision_confidence": 1.0,
        "decision_quality": 1.0,
        "regime_fit": 1.0,
        "mtf_fit": 1.0,
        "asset_profile_fit": 1.0,
        "macro_fit": 1.0,
        "conflict_penalty": 0.0,
    }
    score = calculate_strategy_selection_score(components, profile)
    assert score >= 0.9


def test_missing_context_does_not_crash():
    profile = get_default_strategy_selection_profile()
    decision_row = pd.Series({"decision_score": 0.5})
    context = {}

    fit = calculate_strategy_family_fit(
        "trend_following", decision_row, context, profile
    )
    assert fit["regime_fit"] == 0.5
