"""Tests for Macro Revision Feature Placeholders."""

import pandas as pd
from advanced_feature_fusion.macro_revision_feature_placeholders import (
    build_macro_revision_feature_placeholder_registry,
    summarize_macro_revision_feature_placeholders,
    add_macro_revision_flag_placeholder,
)


def test_revision_features_registry():
    df, summary = build_macro_revision_feature_placeholder_registry()
    assert len(df) == 1
    assert summary["total_placeholders"] == 1
    assert summary["non_signal_guaranteed"] is True


def test_add_macro_revision_flag():
    df = pd.DataFrame({
        "revision_status": ["revised", "final"],
    })
    res = add_macro_revision_flag_placeholder(df, revision_status_field="revision_status", output_field="is_revised")
    assert "is_revised" in res.columns
    assert bool(res["is_revised"].iloc[0]) is True
    assert bool(res["is_revised"].iloc[1]) is False
