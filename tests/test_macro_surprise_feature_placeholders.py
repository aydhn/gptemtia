"""Tests for Macro Surprise Feature Placeholders."""

import pandas as pd
from advanced_feature_fusion.macro_surprise_feature_placeholders import (
    build_macro_surprise_feature_placeholder_registry,
    summarize_macro_surprise_feature_placeholders,
    add_macro_surprise_placeholder,
)


def test_surprise_features_registry():
    df, summary = build_macro_surprise_feature_placeholder_registry()
    assert len(df) == 1
    assert summary["total_placeholders"] == 1
    assert summary["non_signal_guaranteed"] is True


def test_add_macro_surprise_placeholder():
    df = pd.DataFrame({
        "actual": [3.2, 5.0],
        "forecast": [3.0, 5.0],
    })
    res = add_macro_surprise_placeholder(df, actual_field="actual", forecast_field="forecast", output_field="surprise")
    assert "surprise" in res.columns
    assert round(res["surprise"].iloc[0], 2) == 0.2
    assert res["surprise"].iloc[1] == 0.0
    # Input immutability
    assert "surprise" not in df.columns
