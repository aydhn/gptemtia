"""Test suite for Phase 137 ML Dataset No Lookahead Guards."""

import pytest
import pandas as pd
from advanced_ml_dataset_registry.ml_dataset_no_lookahead_guards import (
    build_ml_dataset_no_lookahead_guard_registry,
    validate_no_future_ml_dataset_join,
    validate_no_forbidden_no_lookahead_columns,
    summarize_ml_dataset_no_lookahead_guards,
)


def test_build_no_lookahead_guards():
    df, summary = build_ml_dataset_no_lookahead_guard_registry()
    assert not df.empty
    assert summary["total_no_lookahead_guards"] >= 5


def test_validate_forbidden_columns():
    good_df = pd.DataFrame({"timestamp_utc": [1], "feature": [2]})
    v_good = validate_no_forbidden_no_lookahead_columns(good_df)
    assert v_good["valid"] is True

    bad_df = pd.DataFrame({"future_return": [0.01], "timestamp_utc": [1]})
    v_bad = validate_no_forbidden_no_lookahead_columns(bad_df)
    assert v_bad["valid"] is False
