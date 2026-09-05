"""Tests for State Transition Matrix Placeholders."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.state_transition_matrix_placeholders import (
    build_state_transition_matrix_placeholder_registry,
    summarize_state_transition_matrix_placeholders,
    TRANSITION_MATRIX_PLACEHOLDERS,
)


def test_build_state_transition_matrix_placeholder_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_state_transition_matrix_placeholder_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "matrix_id" in df.columns
    assert "is_placeholder" in df.columns
    assert (df["is_placeholder"] == True).all()
    assert (df["markov_chain_fitted"] == False).all()
    assert (df["forward_probability_generated"] == False).all()

    assert summary["total_matrix_entries"] == 3
    assert summary["all_placeholders"] is True
    assert summary["zero_markov_fitted"] is True


def test_summarize_state_transition_matrix_placeholders():
    profile = get_default_regime_transition_profile()
    df, _ = build_state_transition_matrix_placeholder_registry(profile)
    summary = summarize_state_transition_matrix_placeholders(df)
    assert summary["total_matrix_entries"] == 3
    assert summary["zero_markov_fitted"] is True
