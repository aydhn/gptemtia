"""Tests for Macro Release Lag Policies."""

from advanced_feature_fusion.macro_release_lag_policies import (
    build_macro_release_lag_policy_registry,
    get_macro_release_lag_policies,
    get_macro_release_lag_policies_summary,
    validate_macro_release_available_at,
)


def test_macro_release_lag_policies():
    df, summary = build_macro_release_lag_policy_registry()
    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["zero_future_data_enforced"] is True


def test_validate_release_availability():
    # Valid: release <= base
    res_valid = validate_macro_release_available_at({
        "timestamp": "2025-01-01 12:00:00",
        "release_timestamp": "2025-01-01 10:00:00",
    })
    assert res_valid["available"] is True
    assert res_valid["manual_review_required"] is False

    # Invalid: release > base (future data)
    res_invalid = validate_macro_release_available_at({
        "timestamp": "2025-01-01 08:00:00",
        "release_timestamp": "2025-01-01 10:00:00",
    })
    assert res_invalid["available"] is False
    assert res_invalid["manual_review_required"] is True
