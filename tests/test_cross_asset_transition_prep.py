"""Tests for Cross-Asset Transition Preparation."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.cross_asset_transition_prep import (
    build_cross_asset_transition_prep_report,
    summarize_cross_asset_transition_prep,
    CROSS_ASSET_PREP_DATA,
)


def test_build_cross_asset_transition_prep_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_cross_asset_transition_prep_report(profile)

    assert not df.empty
    assert len(df) == 3
    assert "cross_asset_pair" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_contexts"] == 3
    assert summary["all_aligned"] is True
    assert summary["all_non_signal"] is True


def test_summarize_cross_asset_transition_prep():
    profile = get_default_regime_transition_profile()
    df, _ = build_cross_asset_transition_prep_report(profile)
    summary = summarize_cross_asset_transition_prep(df)
    assert summary["total_contexts"] == 3
    assert summary["all_aligned"] is True
