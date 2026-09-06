"""Tests for Phase 134 Regime Accepted Reference Registries."""

from advanced_regime_featurestore_integration.regime_accepted_reference_registries import (
    build_regime_no_lookahead_accepted_reference_registry,
    build_regime_metadata_only_news_accepted_reference_registry,
    build_regime_source_preservation_accepted_reference_registry,
    build_regime_non_signal_accepted_reference_registry,
    summarize_regime_accepted_references,
)


def test_no_lookahead_references():
    df, summary = build_regime_no_lookahead_accepted_reference_registry()
    assert not df.empty
    assert (df["acceptance_status"] == "ACCEPTED").all()
    assert (df["non_signal"] == True).all()


def test_metadata_only_news_references():
    df, summary = build_regime_metadata_only_news_accepted_reference_registry()
    assert not df.empty
    assert (df["acceptance_status"] == "ACCEPTED").all()
    assert (df["source_preserved"] == True).all()


def test_source_preservation_references():
    df, summary = build_regime_source_preservation_accepted_reference_registry()
    assert not df.empty
    assert (df["acceptance_status"] == "ACCEPTED").all()


def test_non_signal_references():
    df, summary = build_regime_non_signal_accepted_reference_registry()
    assert not df.empty
    assert (df["acceptance_status"] == "ACCEPTED").all()
    assert (df["non_signal"] == True).all()

    s_res = summarize_regime_accepted_references(df)
    assert s_res["all_accepted"] is True
    assert s_res["all_non_signal"] is True
