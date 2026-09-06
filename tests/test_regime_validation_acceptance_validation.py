"""Tests for Regime Validation Acceptance Subsystem Validation."""

import pandas as pd
from advanced_regime_validation_acceptance.regime_validation_acceptance_validation import (
    validate_regime_validation_acceptance_profile_registry,
    validate_regime_validation_gate_registry,
    validate_regime_validation_acceptance_manifest,
    validate_no_forbidden_regime_acceptance_claims,
    build_regime_validation_acceptance_validation_report,
)


def test_subsystem_validation():
    # Profile validation
    valid_profiles = pd.DataFrame([{
        "profile_name": "test_profile",
        "current_phase": 133,
        "target_final_phase": 160,
        "next_phase": 134,
        "non_signal": True,
    }])
    assert validate_regime_validation_acceptance_profile_registry(valid_profiles)["passed"] is True

    invalid_profiles = pd.DataFrame([{
        "profile_name": "test_profile",
        "current_phase": 999,
        "target_final_phase": 160,
        "next_phase": 134,
        "non_signal": True,
    }])
    assert validate_regime_validation_acceptance_profile_registry(invalid_profiles)["passed"] is False

    # Gates validation
    valid_gates = pd.DataFrame([{"non_signal": True}] * 19)
    assert validate_regime_validation_gate_registry(valid_gates)["passed"] is True

    invalid_gates = pd.DataFrame([{"non_signal": True}] * 5)
    assert validate_regime_validation_gate_registry(invalid_gates)["passed"] is False

    # Report builder
    df_rep, summary = build_regime_validation_acceptance_validation_report()
    assert not df_rep.empty
    assert summary["status"] == "VALIDATION_PASS"
    assert summary["forbidden_claims_clean"] is True
