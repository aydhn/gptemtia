"""Tests for Event Importance Feature Placeholders."""

import pandas as pd
from advanced_feature_fusion.event_importance_feature_placeholders import (
    build_event_importance_feature_placeholder_registry,
    summarize_event_importance_feature_placeholders,
    add_event_importance_weight_placeholder,
)


def test_importance_registry():
    df, summary = build_event_importance_feature_placeholder_registry()
    assert len(df) == 1
    assert summary["total_placeholders"] == 1
    assert summary["non_signal_guaranteed"] is True


def test_add_event_importance_weight():
    df = pd.DataFrame({
        "importance": ["high", "medium", "low", "unknown"],
    })
    res = add_event_importance_weight_placeholder(df)
    assert "event_importance_weight_placeholder" in res.columns
    assert res["event_importance_weight_placeholder"].iloc[0] == 1.0
    assert res["event_importance_weight_placeholder"].iloc[1] == 0.5
    assert res["event_importance_weight_placeholder"].iloc[2] == 0.2
    assert res["event_importance_weight_placeholder"].iloc[3] == 0.1
