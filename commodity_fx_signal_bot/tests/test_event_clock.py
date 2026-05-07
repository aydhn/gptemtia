import pytest
import pandas as pd
from backtesting.event_clock import EventClock


def test_event_clock():
    idx = pd.DatetimeIndex(["2020-01-01", "2020-01-02", "2020-01-03"])
    clock = EventClock(idx)

    assert clock.current() is None
    it = iter(clock)
    ts = next(it)
    assert ts == pd.Timestamp("2020-01-01")
    assert clock.current() == pd.Timestamp("2020-01-01")
    assert clock.next_timestamp() == pd.Timestamp("2020-01-02")
    assert clock.position() == 0
