import pandas as pd
import pytest

from indicators.divergence_feature_set import DivergenceFeatureSetBuilder


@pytest.fixture
def synthetic_df():
    return pd.DataFrame(
        {
            "open": [10.0, 9.0, 8.0, 9.0, 10.0],
            "high": [11.0, 10.0, 9.0, 10.0, 11.0],
            "low": [9.0, 8.0, 7.0, 8.0, 9.0],
            "close": [10.0, 9.0, 8.0, 9.0, 10.0],
            "volume": [100, 200, 300, 200, 100],
            "rsi_14": [50.0, 40.0, 30.0, 40.0, 50.0],
        }
    )


def test_build_compact_divergence_features(synthetic_df):
    builder = DivergenceFeatureSetBuilder()

    # We pass include_events=True by default
    df_out, summary = builder.build_compact_divergence_features(
        synthetic_df, include_events=True
    )

    # Check that events are included
    assert any(c.startswith("event_") for c in df_out.columns)

    # Check that regular divergence is included
    assert any(c.startswith("div_regular_") for c in df_out.columns)

    # Check that pivot columns are EXCLUDED in compact
    assert not any(c.startswith("pivot_") for c in df_out.columns)


def test_build_divergence_features_full(synthetic_df):
    builder = DivergenceFeatureSetBuilder()

    df_out, summary = builder.build_divergence_features(
        synthetic_df, include_events=False
    )

    # Pivot columns should be present in full
    assert any(c.startswith("pivot_") for c in df_out.columns)

    # Events should be absent since include_events=False
    assert not any(c.startswith("event_") for c in df_out.columns)


def test_validate_divergence_features(synthetic_df):
    builder = DivergenceFeatureSetBuilder()

    df_out, summary = builder.build_divergence_features(
        synthetic_df, include_events=True
    )

    val_res = builder.validate_divergence_features(df_out)

    # The dataframe might contain 100% NaN columns for events that didn't trigger
    # So valid should be true, but warnings might exist
    assert val_res["valid"] == True

    # Duplicate columns shouldn't exist
    assert len(df_out.columns) == len(set(df_out.columns))
