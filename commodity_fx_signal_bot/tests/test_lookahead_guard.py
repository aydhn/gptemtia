import pytest
import pandas as pd
from backtesting.lookahead_guard import LookaheadGuard


def test_lookahead_violation():
    guard = LookaheadGuard()
    res = guard.validate_candidate_timestamp(
        pd.Timestamp("2020-01-02"), pd.Timestamp("2020-01-01")
    )
    assert not res["passed"]

    res2 = guard.validate_candidate_timestamp(
        pd.Timestamp("2020-01-01"), pd.Timestamp("2020-01-01")
    )
    assert res2["passed"]
