import pandas as pd

from data.cleaning.ohlcv_cleaner import OHLCVCleaner


def test_drop_duplicate_index():
    cleaner = OHLCVCleaner()
    df = pd.DataFrame(
        {"close": [100, 101, 102]},
        index=pd.DatetimeIndex(["2024-01-01", "2024-01-01", "2024-01-02"]),
    )
    cleaned, dup_count = cleaner.drop_duplicate_timestamps(df)
    assert len(cleaned) == 2
    assert dup_count == 1
    # keep last behavior
    assert cleaned.loc["2024-01-01", "close"] == 101


def test_standardize_columns():
    cleaner = OHLCVCleaner()
    df = pd.DataFrame({"Open": [1], "High": [2], "LOW": [3], "Close": [4]})
    cleaned = cleaner.standardize_columns(df)
    assert list(cleaned.columns) == ["open", "high", "low", "close"]


def test_sort_datetime_index():
    cleaner = OHLCVCleaner()
    df = pd.DataFrame(
        {"close": [102, 100, 101]},
        index=pd.DatetimeIndex(["2024-01-03", "2024-01-01", "2024-01-02"]),
    )
    cleaned = cleaner.sort_datetime_index(df)
    assert list(cleaned.index) == [
        pd.Timestamp("2024-01-01"),
        pd.Timestamp("2024-01-02"),
        pd.Timestamp("2024-01-03"),
    ]


def test_clean_does_not_mutate():
    cleaner = OHLCVCleaner()
    df = pd.DataFrame(
        {"close": [100, 101, 102]},
        index=pd.DatetimeIndex(["2024-01-01", "2024-01-01", "2024-01-02"]),
    )
    original_len = len(df)
    cleaned, summary = cleaner.clean(df)
    assert len(df) == original_len  # Original should still have 3 rows
    assert len(cleaned) == 2  # Cleaned should have 2
    assert summary["duplicate_rows_removed"] == 1


def test_repair_high_low_inconsistencies():
    cleaner = OHLCVCleaner()
    df = pd.DataFrame(
        {
            "open": [100.0, 100.0, 100.0],
            "high": [105.0, 95.0, 105.0],  # Middle row high is wrong
            "low": [90.0, 105.0, 115.0],  # Middle and last row low are wrong
            "close": [95.0, 110.0, 110.0],
        },
        index=pd.DatetimeIndex(["2024-01-01", "2024-01-02", "2024-01-03"]),
    )

    cleaned, repaired_count = cleaner.repair_high_low_inconsistencies(df)

    assert repaired_count == 2
    assert list(cleaned["high"]) == [105.0, 110.0, 115.0]
    assert list(cleaned["low"]) == [90.0, 95.0, 100.0]
