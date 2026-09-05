"""Tests for Regime State Sequence Contracts."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_state_sequence_contracts import (
    build_regime_state_sequence_contract_registry,
    summarize_state_sequence_contracts,
    validate_state_sequence_contract,
    EXPECTED_SEQUENCE_CONTRACTS,
)


def test_build_regime_state_sequence_contract_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_regime_state_sequence_contract_registry(profile)

    assert not df.empty
    assert len(df) == 9
    assert "contract_name" in df.columns
    assert "no_lookahead_required" in df.columns
    assert "non_signal_required" in df.columns

    assert (df["no_lookahead_required"] == True).all()
    assert (df["non_signal_required"] == True).all()
    assert (df["model_training_allowed"] == False).all()
    assert (df["clustering_allowed"] == False).all()

    assert summary["total_contracts"] == 9
    assert summary["all_non_signal_required"] is True
    assert summary["all_no_lookahead_required"] is True


def test_summarize_state_sequence_contracts():
    profile = get_default_regime_transition_profile()
    df, _ = build_regime_state_sequence_contract_registry(profile)
    summary = summarize_state_sequence_contracts(df)
    assert summary["total_contracts"] == 9
    assert summary["all_no_lookahead_required"] is True


def test_validate_state_sequence_contract():
    valid = EXPECTED_SEQUENCE_CONTRACTS[0]
    res = validate_state_sequence_contract(valid)
    assert res["is_valid"] is True
