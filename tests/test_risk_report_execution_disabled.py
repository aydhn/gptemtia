"""Unit tests for Risk Report Execution Disabled Report."""

import pandas as pd

from advanced_risk_reporting.risk_report_execution_disabled import (
    build_risk_report_execution_disabled_report,
    validate_no_risk_report_execution_request,
)
from advanced_risk_reporting.risk_reporting_config import (
    get_default_risk_reporting_profile,
)


def test_build_risk_report_execution_disabled_report_default():
    df, summary = build_risk_report_execution_disabled_report()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert summary["is_disabled"] is True
    assert summary["status"] == "execution_blocked_no_risk_report"
    assert "component_name" in df.columns
    assert df.iloc[0]["component_name"] == "risk_report_engine"
    assert bool(df.iloc[0]["is_disabled"]) is True
    assert df.iloc[0]["enforcement_mechanism"] == "STRICT_SAFETY_GATE_EXECUTION_BLOCKED"


def test_build_risk_report_execution_disabled_report_with_profile():
    profile = get_default_risk_reporting_profile()
    df, _summary = build_risk_report_execution_disabled_report(profile)
    assert isinstance(df, pd.DataFrame)
    assert df["current_phase"].iloc[0] == profile.current_phase
    assert df["target_final_phase"].iloc[0] == profile.target_final_phase


def test_validate_no_risk_report_execution_request_allowed_string():
    result = validate_no_risk_report_execution_request("get risk report summary")
    assert result["is_blocked"] is False
    assert result["is_safe"] is True
    assert result["action"] == "ALLOW"
    assert result["reason"] == "No violation"


def test_validate_no_risk_report_execution_request_blocked_string():
    result = validate_no_risk_report_execution_request("please run_risk_report now")
    assert result["is_blocked"] is True
    assert result["is_safe"] is False
    assert result["action"] == "BLOCK"
    assert (
        result["reason"] == "Risk report execution strictly disabled in contract phase"
    )


def test_validate_no_risk_report_execution_request_allowed_dict():
    result = validate_no_risk_report_execution_request({"command": "view_report"})
    assert result["is_blocked"] is False
    assert result["is_safe"] is True
    assert result["action"] == "ALLOW"


def test_validate_no_risk_report_execution_request_blocked_dict():
    result = validate_no_risk_report_execution_request(
        {"command": "execute_risk_report", "params": {}}
    )
    assert result["is_blocked"] is True
    assert result["is_safe"] is False
    assert result["action"] == "BLOCK"


def test_validate_no_risk_report_execution_request_case_insensitive():
    result = validate_no_risk_report_execution_request("GENERATE_RISK_REPORT")
    assert result["is_blocked"] is True
    assert result["is_safe"] is False
    assert result["action"] == "BLOCK"
