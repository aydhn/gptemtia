# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Forbidden Columns."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.evaluation_forbidden_column_policies import (
    build_evaluation_forbidden_column_policy_registry,
    validate_evaluation_forbidden_columns,
)


def test_evaluation_forbidden_columns():
    profile = get_default_benchmark_evaluation_profile()
    df, s = build_evaluation_forbidden_column_policy_registry(profile)

    assert not df.empty
    assert len(df) >= 10
    assert "forbidden_column" in df.columns
    assert s["total_forbidden_columns"] >= 10

    # Test validation function
    res_clean = validate_evaluation_forbidden_columns(["open", "high", "low", "close", "volume"])
    assert res_clean["is_clean"] is True

    res_dirty = validate_evaluation_forbidden_columns(["open", "future_price", "prediction"])
    assert res_dirty["is_clean"] is False
    assert len(res_dirty["detected_columns"]) >= 1
