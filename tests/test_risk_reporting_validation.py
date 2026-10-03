import pandas as pd
import pytest
from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_reporting_validation import (
    validate_risk_reporting_profile_registry,
    validate_risk_report_contracts,
    validate_exposure_attribution_contracts,
    validate_limit_monitoring_contracts,
    validate_risk_reporting_guards,
    validate_risk_reporting_manifest,
    validate_no_forbidden_risk_reporting_claims,
    build_risk_reporting_validation_report,
)


@pytest.fixture
def profile():
    return get_default_risk_reporting_profile()


def test_validate_risk_reporting_profile_registry(profile):
    # Test valid case
    df_valid = pd.DataFrame({
        "non_production": [True, True],
        "allow_live_trading": [False, False]
    })
    result = validate_risk_reporting_profile_registry(df_valid, profile)
    assert result["is_valid"] is True
    assert len(result["errors"]) == 0

    # Test empty registry
    df_empty = pd.DataFrame()
    result = validate_risk_reporting_profile_registry(df_empty, profile)
    assert result["is_valid"] is False
    assert "Profile registry is empty" in result["errors"]

    # Test invalid non_production
    df_invalid_np = pd.DataFrame({
        "non_production": [True, False],
        "allow_live_trading": [False, False]
    })
    result = validate_risk_reporting_profile_registry(df_invalid_np, profile)
    assert result["is_valid"] is False
    assert "All profiles must be non_production=True" in result["errors"]

    # Test invalid allow_live_trading
    df_invalid_lt = pd.DataFrame({
        "non_production": [True, True],
        "allow_live_trading": [False, True]
    })
    result = validate_risk_reporting_profile_registry(df_invalid_lt, profile)
    assert result["is_valid"] is False
    assert "No profile may allow live trading" in result["errors"]


def test_validate_risk_report_contracts(profile):
    df_valid = pd.DataFrame({
        "risk_reporting_execution_allowed": [False, False],
        "live_trading_allowed": [False, False]
    })
    result = validate_risk_report_contracts(df_valid, profile)
    assert result["is_valid"] is True

    df_empty = pd.DataFrame()
    result = validate_risk_report_contracts(df_empty, profile)
    assert result["is_valid"] is False
    assert "Risk report contracts registry is empty" in result["errors"]

    df_invalid = pd.DataFrame({
        "risk_reporting_execution_allowed": [True, False],
        "live_trading_allowed": [False, True]
    })
    result = validate_risk_report_contracts(df_invalid, profile)
    assert result["is_valid"] is False
    assert "No contract may allow risk reporting execution" in result["errors"]
    assert "No contract may allow live trading" in result["errors"]


def test_validate_exposure_attribution_contracts(profile):
    df_valid = pd.DataFrame({
        "exposure_calculated": [False, False],
        "allows_execution": [False, False]
    })
    result = validate_exposure_attribution_contracts(df_valid, profile)
    assert result["is_valid"] is True

    df_empty = pd.DataFrame()
    result = validate_exposure_attribution_contracts(df_empty, profile)
    assert result["is_valid"] is False
    assert "Exposure attribution contracts registry is empty" in result["errors"]

    df_invalid = pd.DataFrame({
        "exposure_calculated": [True, False],
        "allows_execution": [False, True]
    })
    result = validate_exposure_attribution_contracts(df_invalid, profile)
    assert result["is_valid"] is False
    assert "No contract may have exposure_calculated=True" in result["errors"]
    assert "No contract may allow execution" in result["errors"]


def test_validate_limit_monitoring_contracts(profile):
    df_valid = pd.DataFrame({
        "is_enforced_live": [False, False],
        "allows_alerting": [False, False]
    })
    result = validate_limit_monitoring_contracts(df_valid, profile)
    assert result["is_valid"] is True

    df_empty = pd.DataFrame()
    result = validate_limit_monitoring_contracts(df_empty, profile)
    assert result["is_valid"] is False
    assert "Limit monitoring contracts registry is empty" in result["errors"]

    df_invalid = pd.DataFrame({
        "is_enforced_live": [True, False],
        "allows_alerting": [False, True]
    })
    result = validate_limit_monitoring_contracts(df_invalid, profile)
    assert result["is_valid"] is False
    assert "No contract may be enforced live" in result["errors"]
    assert "No contract may allow alerting" in result["errors"]


def test_validate_risk_reporting_guards(profile):
    df_map_valid = {
        "guard1": pd.DataFrame({"col": [1]}),
        "guard2": pd.DataFrame({"col": [1, 2]})
    }
    result = validate_risk_reporting_guards(df_map_valid, profile)
    assert result["is_valid"] is True

    df_map_empty_guard = {
        "guard1": pd.DataFrame({"col": [1]}),
        "guard2": pd.DataFrame()
    }
    result = validate_risk_reporting_guards(df_map_empty_guard, profile)
    assert result["is_valid"] is False
    assert "Guard registry 'guard2' is empty" in result["errors"]


def test_validate_risk_reporting_manifest(profile):
    df_valid = pd.DataFrame([{
        "current_phase": 155,
        "target_final_phase": 160,
        "next_phase": 156,
        "risk_report_generated": False,
        "exposure_attribution_generated": False,
        "limit_monitoring_executed": False,
        "metric_calculated": False,
        "var_calculated": False,
        "expected_shortfall_calculated": False,
        "exposure_calculated": False,
        "alert_generated": False,
        "dashboard_generated": False,
        "portfolio_adjustment_generated": False,
        "broker_order_sent": False,
        "live_order_sent": False,
    }])
    result = validate_risk_reporting_manifest(df_valid, profile)
    assert result["is_valid"] is True

    df_empty = pd.DataFrame()
    result = validate_risk_reporting_manifest(df_empty, profile)
    assert result["is_valid"] is False
    assert "Manifest is empty" in result["errors"]

    df_invalid = pd.DataFrame([{
        "current_phase": 100,
        "target_final_phase": 100,
        "next_phase": 100,
        "risk_report_generated": True,
        "exposure_attribution_generated": True,
        "limit_monitoring_executed": True,
        "metric_calculated": True,
        "var_calculated": True,
        "expected_shortfall_calculated": True,
        "exposure_calculated": True,
        "alert_generated": True,
        "dashboard_generated": True,
        "portfolio_adjustment_generated": True,
        "broker_order_sent": True,
        "live_order_sent": True,
    }])
    result = validate_risk_reporting_manifest(df_invalid, profile)
    assert result["is_valid"] is False
    assert "current_phase must be 155" in result["errors"]
    assert "target_final_phase must be 160" in result["errors"]
    assert "next_phase must be 156" in result["errors"]
    assert "risk_report_generated must be False" in result["errors"]
    assert "exposure_attribution_generated must be False" in result["errors"]
    assert "limit_monitoring_executed must be False" in result["errors"]
    assert "metric_calculated must be False" in result["errors"]
    assert "var_calculated must be False" in result["errors"]
    assert "expected_shortfall_calculated must be False" in result["errors"]
    assert "exposure_calculated must be False" in result["errors"]
    assert "alert_generated must be False" in result["errors"]
    assert "dashboard_generated must be False" in result["errors"]
    assert "portfolio_adjustment_generated must be False" in result["errors"]
    assert "broker_order_sent must be False" in result["errors"]
    assert "live_order_sent must be False" in result["errors"]


def test_validate_no_forbidden_risk_reporting_claims():
    # Test valid case
    result = validate_no_forbidden_risk_reporting_claims(
        text="This is a safe text.",
        df=pd.DataFrame({"safe_col1": [1], "safe_col2": [2]}),
        summary={"safe_key": "safe_value"}
    )
    assert result["is_safe"] is True
    assert result["action"] == "ALLOW"
    assert len(result["violations"]) == 0

    # Test invalid text (contains 'live_alert')
    result = validate_no_forbidden_risk_reporting_claims(text="We sent a live_alert today.")
    assert result["is_safe"] is False
    assert result["action"] == "BLOCK"
    assert "live_alert" in result["violations"]

    # Test invalid dataframe column (contains 'signal')
    result = validate_no_forbidden_risk_reporting_claims(df=pd.DataFrame({"signal": [1]}))
    assert result["is_safe"] is False
    assert result["action"] == "BLOCK"
    assert "signal" in result["violations"]

    # Test invalid summary (contains 'buy' as a key)
    result = validate_no_forbidden_risk_reporting_claims(summary={"buy": True})
    assert result["is_safe"] is False
    assert result["action"] == "BLOCK"
    assert "buy" in result["violations"]


def test_build_risk_reporting_validation_report(profile):
    tables = {
        "profiles": pd.DataFrame({"non_production": [True], "allow_live_trading": [False]}),
        "contracts": pd.DataFrame({"risk_reporting_execution_allowed": [False], "live_trading_allowed": [False]}),
        "exposure_contracts": pd.DataFrame({"exposure_calculated": [False], "allows_execution": [False]}),
        "limit_contracts": pd.DataFrame({"is_enforced_live": [False], "allows_alerting": [False]}),
        "manifest": pd.DataFrame([{
            "current_phase": 155,
            "target_final_phase": 160,
            "next_phase": 156,
            "risk_report_generated": False,
            "exposure_attribution_generated": False,
            "limit_monitoring_executed": False,
            "metric_calculated": False,
            "var_calculated": False,
            "expected_shortfall_calculated": False,
            "exposure_calculated": False,
            "alert_generated": False,
            "dashboard_generated": False,
            "portfolio_adjustment_generated": False,
            "broker_order_sent": False,
            "live_order_sent": False,
        }])
    }

    df, summary = build_risk_reporting_validation_report(tables, profile)

    assert not df.empty
    assert len(df) == 5
    assert df["is_valid"].all()
    assert summary["all_passed"] is True
    assert summary["status"] == "RISK_REPORT_CONTRACT_READY"
    assert summary["total_checks"] == 5

    # Test with an invalid table
    tables["profiles"] = pd.DataFrame({"non_production": [False], "allow_live_trading": [True]})
    df, summary = build_risk_reporting_validation_report(tables, profile)

    assert not df.empty
    assert len(df) == 5
    assert not df["is_valid"].all()
    assert summary["all_passed"] is False
    assert summary["status"] == "VALIDATION_FAILED"
