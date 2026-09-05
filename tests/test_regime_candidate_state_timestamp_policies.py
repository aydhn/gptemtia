import pandas as pd
from advanced_regime_rule_free.regime_candidate_state_timestamp_policies import (
    validate_candidate_state_timestamp_policy,
    build_regime_candidate_state_timestamp_policy_registry,
    summarize_candidate_state_timestamp_policies,
)


def test_validate_candidate_state_timestamp_policy():
    monotonic_df = pd.DataFrame({
        "timestamp_utc": ["2025-01-01T10:00:00Z", "2025-01-01T11:00:00Z"],
        "context_ts": ["2025-01-01T09:00:00Z", "2025-01-01T10:30:00Z"],
    })
    res_valid = validate_candidate_state_timestamp_policy(monotonic_df, base_ts="timestamp_utc", context_ts="context_ts")
    assert res_valid["is_valid"] is True

    non_monotonic_df = pd.DataFrame({
        "timestamp_utc": ["2025-01-01T12:00:00Z", "2025-01-01T11:00:00Z"],
    })
    res_invalid = validate_candidate_state_timestamp_policy(non_monotonic_df, base_ts="timestamp_utc")
    assert res_invalid["is_valid"] is False


def test_build_regime_candidate_state_timestamp_policy_registry():
    df, summary = build_regime_candidate_state_timestamp_policy_registry()
    assert len(df) == 4
    assert summary["all_enforced"] is True
    assert summary["status"] == "VALID"
