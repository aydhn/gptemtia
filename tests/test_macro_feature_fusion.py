"""Tests for Macro Feature Fusion Features."""

import pandas as pd
from advanced_feature_fusion.macro_feature_fusion import (
    build_macro_feature_fusion_registry,
    summarize_macro_feature_fusion,
    add_macro_value_change_feature,
    add_macro_frequency_flag_placeholder,
)


def test_macro_features_registry():
    df, summary = build_macro_feature_fusion_registry()
    assert len(df) == 2
    assert summary["total_features"] == 2
    assert summary["non_signal_guaranteed"] is True


def test_add_macro_value_change():
    df = pd.DataFrame({"value": [10.0, 12.0, 15.0]})
    res = add_macro_value_change_feature(df, value_field="value", output_field="val_pct_change")
    assert "val_pct_change" in res.columns
    assert len(res) == 3
    # Check input was not mutated
    assert "val_pct_change" not in df.columns


def test_add_macro_frequency_flag():
    df = pd.DataFrame({"frequency": ["monthly", "quarterly"]})
    res = add_macro_frequency_flag_placeholder(df, frequency_field="frequency")
    assert "macro_frequency_flag_placeholder" in res.columns
    assert res["macro_frequency_flag_placeholder"].iloc[0] == "MONTHLY"
