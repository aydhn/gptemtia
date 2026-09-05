"""Tests for Regime Transition Validation Report."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_profile_registry import (
    build_regime_transition_profile_registry,
)
from advanced_regime_transition.regime_state_sequence_contracts import (
    build_regime_state_sequence_contract_registry,
)
from advanced_regime_transition.regime_transition_metric_registry import (
    build_regime_transition_metric_registry,
)
from advanced_regime_transition.transition_diagnostics_manifest import (
    build_transition_diagnostics_manifest,
)
from advanced_regime_transition.regime_transition_validation import (
    build_regime_transition_validation_report,
    validate_no_forbidden_transition_claims,
)


def test_build_regime_transition_validation_report():
    profile = get_default_regime_transition_profile()
    df_prof, _ = build_regime_transition_profile_registry(profile)
    df_cont, _ = build_regime_state_sequence_contract_registry(profile)
    df_tmet, _ = build_regime_transition_metric_registry(profile)
    df_man, _ = build_transition_diagnostics_manifest(profile)

    tables = {
        "profiles": df_prof,
        "contracts": df_cont,
        "metrics": df_tmet,
        "manifest": df_man,
    }

    df_val, summary = build_regime_transition_validation_report(tables, profile)

    assert not df_val.empty
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["total_checks"] == 5
    assert summary["passed_checks"] == 5
    assert summary["failed_checks"] == 0
    assert summary["forbidden_claims_clean"] is True


def test_validate_no_forbidden_transition_claims():
    clean_text = "This is an offline research report on state persistence."
    res_clean = validate_no_forbidden_transition_claims(text=clean_text)
    assert res_clean["is_valid"] is True

    bad_text = "This generates a buy_signal for production broker."
    res_bad = validate_no_forbidden_transition_claims(text=bad_text)
    assert res_bad["is_valid"] is False
    assert res_bad["violations_count"] > 0
