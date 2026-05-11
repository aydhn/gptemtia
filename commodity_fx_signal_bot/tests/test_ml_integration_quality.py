import pytest
import pandas as pd
from ml_integration.integration_quality import (
    check_ml_context_coverage,
    check_for_forbidden_live_terms_in_ml_integration,
    build_ml_integration_quality_report
)

def test_coverage():
    dates = pd.date_range("2023-01-01", periods=10)
    df1 = pd.DataFrame({"dummy": range(10)}, index=dates)
    df2 = pd.DataFrame({"dummy": range(5)}, index=dates[:5])

    res = check_ml_context_coverage(df1, df2)
    assert res["coverage_ratio"] == 1.0

def test_forbidden_terms():
    df = pd.DataFrame({"col1": ["LIVE_ORDER_123", "normal"]})
    res = check_for_forbidden_live_terms_in_ml_integration(df)
    assert not res["passed_forbidden_check"]
    assert "LIVE_ORDER" in res["forbidden_live_terms_found"]

    df2 = pd.DataFrame({"col1": ["normal", "data"]})
    res2 = check_for_forbidden_live_terms_in_ml_integration(df2)
    assert res2["passed_forbidden_check"]
