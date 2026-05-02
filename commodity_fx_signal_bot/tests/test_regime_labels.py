import pytest
from regimes.regime_labels import (
    list_regime_labels,
    validate_regime_label,
    is_trend_regime,
    is_range_regime,
    is_volatility_regime,
    is_mtf_regime,
    BULLISH_TREND,
    RANGE_BOUND,
    HIGH_VOLATILITY,
    MTF_ALIGNED_TREND,
    UNKNOWN,
)
from core.exceptions import ConfigError


def test_list_regime_labels():
    labels = list_regime_labels()
    assert len(labels) > 0
    assert BULLISH_TREND in labels
    assert UNKNOWN in labels


def test_validate_regime_label():
    validate_regime_label(BULLISH_TREND)
    with pytest.raises(ConfigError):
        validate_regime_label("not_a_valid_label")


def test_is_trend_regime():
    assert is_trend_regime(BULLISH_TREND)
    assert not is_trend_regime(RANGE_BOUND)


def test_is_range_regime():
    assert is_range_regime(RANGE_BOUND)
    assert not is_range_regime(HIGH_VOLATILITY)


def test_is_volatility_regime():
    assert is_volatility_regime(HIGH_VOLATILITY)
    assert not is_volatility_regime(MTF_ALIGNED_TREND)


def test_is_mtf_regime():
    assert is_mtf_regime(MTF_ALIGNED_TREND)
    assert not is_mtf_regime(BULLISH_TREND)
