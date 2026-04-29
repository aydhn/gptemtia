import pytest
import pandas as pd
import numpy as np

from data.cleaning.outlier_detector import (
    detect_return_outliers,
    detect_zscore_outliers,
    build_outlier_report,
)


def test_detect_return_outliers():
    df = pd.DataFrame(
        {"close": [100, 101, 150, 151]},  # 101 to 150 is nearly 50% return
        index=pd.date_range("2024-01-01", periods=4),
    )
    outliers = detect_return_outliers(df, threshold=0.20)
    assert len(outliers) == 1
    assert outliers.index[0] == pd.Timestamp("2024-01-03")


def test_build_outlier_report():
    df = pd.DataFrame(
        {"close": [100, 101, 150, 151]}, index=pd.date_range("2024-01-01", periods=4)
    )
    report = build_outlier_report(df)
    assert report["total_outliers"] > 0
    assert "return" in report["outliers_by_method"]
    assert len(report["details"]) > 0
