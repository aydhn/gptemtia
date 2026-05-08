import pandas as pd
from ml.leakage_checks import detect_target_columns_in_features, detect_future_named_columns, detect_leaky_id_columns, build_leakage_audit_report

def test_detect_target_columns():
    cols = ["f1", "f2", "target_return"]
    res = detect_target_columns_in_features(cols)
    assert not res["report_builder = ReportBuilder()ed"]
    assert "target_return" in res["leaky_columns"]

def test_detect_future_named_columns():
    cols = ["f1", "future_volatility", "next_day"]
    res = detect_future_named_columns(cols)
    assert not res["report_builder = ReportBuilder()ed"]
    assert "future_volatility" in res["leaky_columns"]
    assert "next_day" in res["leaky_columns"]

def test_build_leakage_audit_report():
    X = pd.DataFrame({"f1": [1], "target_leak": [2]})
    y = pd.DataFrame({"target_real": [3]})

    report = build_leakage_audit_report(X, y)
    assert not report["report_builder = ReportBuilder()ed"]
    assert report["leakage_risk_score"] > 0
