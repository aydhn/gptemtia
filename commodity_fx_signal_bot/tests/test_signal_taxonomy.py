import pytest
from signals.signal_taxonomy import (
    infer_event_group,
    infer_directional_bias,
    infer_candidate_type,
    is_warning_event,
)


def test_infer_event_group():
    assert infer_event_group("rsi_oversold") == "momentum"
    assert infer_event_group("ema_cross") == "trend"
    assert infer_event_group("bb_squeeze") == "volatility"
    assert infer_event_group("random_xyz") == "unknown"


def test_infer_directional_bias():
    assert infer_directional_bias("bullish_pinbar") == "bullish"
    assert infer_directional_bias("bearish_engulfing") == "bearish"
    assert infer_directional_bias("squeeze_neutral") == "neutral"
    assert infer_directional_bias("risk_warning") == "warning"
    assert infer_directional_bias("something") == "unknown"


def test_infer_candidate_type():
    assert infer_candidate_type("trend_following_setup") == "trend_following"
    assert infer_candidate_type("oversold_reversion") == "mean_reversion"
    assert infer_candidate_type("bb_expansion") == "volatility_expansion"


def test_is_warning_event():
    assert is_warning_event("risk_too_high") is True
    assert is_warning_event("bullish_signal") is False
