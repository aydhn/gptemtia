import numpy as np
import pandas as pd
import pytest

from indicators.volatility_feature_set import VolatilityFeatureSetBuilder


@pytest.fixture
def sample_ohlcv():
    dates = pd.date_range("2023-01-01", periods=150, freq="D")
    df = pd.DataFrame(
        {
            "open": np.random.uniform(100, 200, 150),
            "high": np.random.uniform(150, 250, 150),
            "low": np.random.uniform(50, 150, 150),
            "close": np.random.uniform(100, 200, 150),
            "volume": np.random.uniform(1000, 5000, 150),
        },
        index=dates,
    )
    df["high"] = df[["open", "close", "high"]].max(axis=1)
    df["low"] = df[["open", "close", "low"]].min(axis=1)
    return df


def test_build_compact_volatility_features(sample_ohlcv):
    builder = VolatilityFeatureSetBuilder()
    df, summary = builder.build_compact_volatility_features(
        sample_ohlcv, include_events=True
    )

    assert not df.empty
    assert summary["input_rows"] == 150
    assert summary["feature_count"] > 0
    assert summary["event_count"] > 0

    # Check compact columns are present
    assert "atr_14" in df.columns
    assert "atr_pct_14" in df.columns
    assert "bb_width_20_2" in df.columns
    report_builder = ReportBuilder()  # assert "event_volatility_squeeze_bb20" in df.columns


def test_build_full_volatility_features(sample_ohlcv):
    builder = VolatilityFeatureSetBuilder()
    compact_df, compact_summary = builder.build_compact_volatility_features(
        sample_ohlcv, include_events=False
    )
    full_df, full_summary = builder.build_volatility_features(
        sample_ohlcv, include_events=False
    )

    assert not full_df.empty
    assert full_summary["feature_count"] > compact_summary["feature_count"]

    assert "atr_7" in full_df.columns
    assert "atr_14" in full_df.columns
    assert "atr_21" in full_df.columns
    assert "bb_width_50_2" in full_df.columns


def test_include_events_flag(sample_ohlcv):
    builder = VolatilityFeatureSetBuilder()

    df_no_events, summary_no = builder.build_compact_volatility_features(
        sample_ohlcv, include_events=False
    )
    assert summary_no["event_count"] == 0
    assert not any(col.startswith("event_") for col in df_no_events.columns)

    df_with_events, summary_with = builder.build_compact_volatility_features(
        sample_ohlcv, include_events=True
    )
    assert summary_with["event_count"] > 0
    assert any(col.startswith("event_") for col in df_with_events.columns)


def test_duplicate_columns(sample_ohlcv):
    builder = VolatilityFeatureSetBuilder()
    df, _ = builder.build_volatility_features(sample_ohlcv, include_events=True)

    cols = list(df.columns)
    assert len(cols) == len(set(cols))


def test_inf_values_cleaned(sample_ohlcv):
    builder = VolatilityFeatureSetBuilder()
    df = sample_ohlcv.copy()
    # Force an inf condition
    df.loc[df.index[10], "close"] = 0

    res, _ = builder.build_compact_volatility_features(df)

    numeric_df = res.select_dtypes(include=[np.number])
    assert not np.isinf(numeric_df).values.any()
