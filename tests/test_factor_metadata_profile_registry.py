import pytest
from advanced_factor_metadata.factor_metadata_profile_registry import build_factor_metadata_profile_registry


def test_build_factor_metadata_profile_registry():
    df, summary = build_factor_metadata_profile_registry()
    assert not df.empty
    assert summary["total_profiles"] >= 3
    assert summary["current_phase"] == 122
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 123
    assert summary["dry_run_default"] is True
    assert summary["non_signal"] is True
    assert "profile_name" in df.columns
    assert "current_phase" in df.columns
    assert (df["current_phase"] == 122).all()
