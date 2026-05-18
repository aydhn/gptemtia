import pytest
import pandas as pd

from observability.observability_quality import (
    check_health_report_quality,
    check_runtime_metrics_quality,
    check_log_records_quality,
    check_diagnostics_summary_quality,
    check_for_sensitive_data_in_observability,
    check_for_forbidden_trade_terms_in_observability,
    build_observability_quality_report
)

def test_check_health_report_quality():
    assert check_health_report_quality(None)["valid"] == False

    df_valid = pd.DataFrame({"component": ["x"], "status": ["healthy"], "health_score": [0.5]})
    assert check_health_report_quality(df_valid)["valid"] == True

    df_invalid = pd.DataFrame({"component": ["x"], "status": ["healthy"], "health_score": [1.5]})
    assert check_health_report_quality(df_invalid)["valid"] == False

def test_check_runtime_metrics_quality():
    assert check_runtime_metrics_quality(None)["valid"] == False

    df_valid = pd.DataFrame({"duration_seconds": [1.0, 5.5]})
    assert check_runtime_metrics_quality(df_valid)["valid"] == True

    df_invalid = pd.DataFrame({"duration_seconds": [-1.0, 5.5]})
    assert check_runtime_metrics_quality(df_invalid)["valid"] == False

def test_check_sensitive_data():
    df = pd.DataFrame({"msg": ["some text", "bot_token=ABC1234"]})
    res = check_for_sensitive_data_in_observability(df=df)
    assert res["safe"] == False
    assert "bot_token" in res["found_sensitive"]

    summary = {"info": "normal", "nested": {"password": "pwd"}}
    res2 = check_for_sensitive_data_in_observability(summary=summary)
    assert res2["safe"] == False
    assert "password" in res2["found_sensitive"]

def test_check_forbidden_trade_terms():
    df = pd.DataFrame({"msg": ["SEND_ORDER now!", "normal"]})
    res = check_for_forbidden_trade_terms_in_observability(df=df)
    assert res["safe"] == False
    assert "SEND_ORDER" in res["found_terms"]

    summary = {"action": "EXECUTE_TRADE on signal"}
    res2 = check_for_forbidden_trade_terms_in_observability(summary=summary)
    assert res2["safe"] == False
    assert "EXECUTE_TRADE" in res2["found_terms"]

def test_build_observability_quality_report():
    summary = {"overall_health_score": 0.5, "actions": ["Check system"]}
    health_df = pd.DataFrame({"component": ["x"], "status": ["healthy"], "health_score": [0.5]})

    report = build_observability_quality_report(summary, health_df)
    assert report["passed"] == True
    assert report["sensitive_data_found"] == False
    assert report["forbidden_trade_terms_found"] == False
    assert report["warning_count"] == 0
