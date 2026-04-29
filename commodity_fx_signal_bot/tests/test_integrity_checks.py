import pandas as pd

from data.cleaning.integrity_checks import (
    check_high_low_relationship,
    check_open_close_within_high_low,
    run_integrity_checks,
)


def test_check_high_low_relationship():
    df = pd.DataFrame(
        {"high": [100, 105, 90], "low": [95, 100, 95]}  # Row 2: high (90) < low (95)
    )
    errors = check_high_low_relationship(df)
    assert len(errors) == 1
    assert "high < low" in errors[0]


def test_check_open_close_within_high_low():
    df = pd.DataFrame(
        {
            "open": [102, 110],  # Row 1: open (110) > high (105)
            "high": [105, 105],
            "low": [95, 95],
            "close": [100, 100],
        }
    )
    warnings = check_open_close_within_high_low(df)
    assert len(warnings) == 1
    assert "open > high" in warnings[0]


def test_run_integrity_checks():
    df = pd.DataFrame(
        {
            "open": [100],
            "high": [105],
            "low": [95],
            "close": [102],
            "adj_close": [102],
            "volume": [100],
        },
        index=pd.DatetimeIndex(["2024-01-01"]),
    )

    report = run_integrity_checks(df, min_rows=10)
    assert not report["passed"]  # fails because rows < 10
    assert "minimum required is 10" in report["errors"][0]
