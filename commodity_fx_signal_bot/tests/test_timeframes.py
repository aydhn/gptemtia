import pytest

from config.timeframes import (
    get_timeframe,
    is_derived_timeframe,
    list_timeframes,
    timeframe_to_minutes,
    validate_timeframe,
)
from core.exceptions import ConfigError


def test_list_timeframes():
    tfs = list_timeframes(enabled_only=True)
    assert len(tfs) > 0
    names = [tf.name for tf in tfs]
    assert "1d" in names

    all_tfs = list_timeframes(enabled_only=False)
    assert len(all_tfs) >= len(tfs)


def test_get_timeframe():
    tf = get_timeframe("1d")
    assert tf.name == "1d"
    assert tf.minutes == 1440
    assert tf.category == "daily"

    with pytest.raises(ConfigError):
        get_timeframe("unknown_tf")


def test_validate_timeframe():
    validate_timeframe("1d")

    with pytest.raises(ConfigError):
        validate_timeframe("unknown")


def test_timeframe_to_minutes():
    assert timeframe_to_minutes("1h") == 60
    assert timeframe_to_minutes("1d") == 1440


def test_is_derived_timeframe():
    assert is_derived_timeframe("4h") is True
    assert is_derived_timeframe("1d") is False
