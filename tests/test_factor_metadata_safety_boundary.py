import pytest
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_metadata_safety_boundary import (
    build_factor_metadata_no_go_conditions,
    build_factor_metadata_safe_go_conditions,
    build_factor_metadata_safety_boundary,
    summarize_factor_metadata_safety_boundary,
)


def test_build_factor_metadata_safety_boundary():
    profile = get_default_factor_metadata_profile()
    df, summary = build_factor_metadata_safety_boundary(profile)
    assert not df.empty
    assert summary["safety_status"] == "SECURE"
    assert summary["no_go_count"] >= 15
    assert summary["safe_go_count"] >= 10
    assert summary["destructive_action_allowed"] is False
    assert summary["non_signal"] is True

    no_go_df = build_factor_metadata_no_go_conditions(profile)
    assert (no_go_df["rule_type"] == "NO_GO").all()

    safe_go_df = build_factor_metadata_safe_go_conditions(profile)
    assert (safe_go_df["rule_type"] == "SAFE_GO").all()

    stats = summarize_factor_metadata_safety_boundary(df)
    assert stats["safety_status"] == "SECURE"
    assert stats["destructive_action_allowed"] is False
