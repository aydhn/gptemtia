import pandas as pd

from macro.macro_quality import (
    build_macro_quality_report,
    check_macro_missing_values,
    check_macro_series_staleness,
)


def test_check_macro_series_staleness():
    now = pd.Timestamp.now()
    d = pd.date_range(now - pd.Timedelta(days=50), periods=2, freq="D")
    df = pd.DataFrame({"col": [1, 2]}, index=d)
    res = check_macro_series_staleness(df, max_staleness_days=45)
    assert len(res["stale_series"]) == 1


def test_check_macro_missing_values():
    df = pd.DataFrame({"col": [1, None, 3]})
    res = check_macro_missing_values(df)
    assert res["missing_ratio_by_column"]["col"] == 1 / 3


def test_build_macro_quality_report():
    df = pd.DataFrame(
        {"col": [1, 2, 3]}, index=pd.date_range("2020-01-01", periods=3, freq="D")
    )
    res = build_macro_quality_report(df, {"test": "ok"})
    assert not res["passed"]
    assert "warnings" in res
