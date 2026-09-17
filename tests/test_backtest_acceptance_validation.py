import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_validation import (
    validate_no_forbidden_backtest_acceptance_claims,
    validate_backtest_acceptance_profile_registry,
    validate_backtest_acceptance_component_checkpoints,
    validate_phase_acceptance_registries,
    validate_backtest_acceptance_manifest,
    build_backtest_acceptance_validation_report,
    FORBIDDEN_TERMS,
)
from advanced_backtest_acceptance.backtest_acceptance_profile_registry import build_backtest_acceptance_profile_registry
from advanced_backtest_acceptance.backtest_acceptance_component_checkpoints import build_backtest_acceptance_component_checkpoint_registry
from advanced_backtest_acceptance.backtest_acceptance_manifest import build_backtest_acceptance_manifest

def test_validate_no_forbidden_claims():
    assert validate_no_forbidden_backtest_acceptance_claims("Clean research documentation.") is True

    for term in FORBIDDEN_TERMS:
        with pytest.raises(ValueError, match="Forbidden claim or term detected"):
            validate_no_forbidden_backtest_acceptance_claims(f"Here is a {term} generated.")

def test_validate_profile_registry():
    df_prof, _ = build_backtest_acceptance_profile_registry()
    assert validate_backtest_acceptance_profile_registry(df_prof) is True

    df_bad = df_prof.copy()
    df_bad["current_phase"] = 999
    with pytest.raises(ValueError, match="Invalid current_phase"):
        validate_backtest_acceptance_profile_registry(df_bad)

def test_validate_component_checkpoints():
    df_chk, _ = build_backtest_acceptance_component_checkpoint_registry()
    assert validate_backtest_acceptance_component_checkpoints(df_chk) is True

    df_bad = df_chk.copy()
    df_bad["production_ready"] = True
    with pytest.raises(ValueError, match="production_ready must be False"):
        validate_backtest_acceptance_component_checkpoints(df_bad)

def test_validate_phase_acceptance():
    valid_map = {"phase_146": pd.DataFrame([{"passed": True}])}
    assert validate_phase_acceptance_registries(valid_map) is True

    invalid_map = {"phase_146": pd.DataFrame([{"passed": False}])}
    with pytest.raises(ValueError, match="Checks failed in phase acceptance registry"):
        validate_phase_acceptance_registries(invalid_map)

def test_validate_manifest():
    df_mnf, _ = build_backtest_acceptance_manifest()
    assert validate_backtest_acceptance_manifest(df_mnf) is True

    df_bad = df_mnf.copy()
    df_bad["live_trading_ready"] = True
    # If production_ready is changed to True
    df_bad2 = df_mnf.copy()
    df_bad2["production_ready"] = True
    with pytest.raises(ValueError, match="Manifest production_ready must be False"):
        validate_backtest_acceptance_manifest(df_bad2)

def test_build_validation_report():
    df, summary = build_backtest_acceptance_validation_report({})
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert summary["all_passed"] is True
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True
    assert (df["passed"] == True).all()
