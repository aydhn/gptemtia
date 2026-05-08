from risk.data_quality_risk import calculate_data_quality_risk_score
from risk.risk_config import get_default_risk_precheck_profile


def test_data_quality_risk_high():
    prof = get_default_risk_precheck_profile()
    ctx = {"data_quality_grade": "F", "nan_ratio": 0.2, "context_keys": ["a", "b"]}
    res = calculate_data_quality_risk_score(ctx, prof)
    assert res.score > 0.8
    assert "Data quality grade is F" in res.reasons


def test_data_quality_risk_low():
    ctx = {"data_quality_grade": "A", "nan_ratio": 0.0, "context_keys": ["a"], "a": 1}
    res = calculate_data_quality_risk_score(ctx)
    assert res.score < 0.3
    assert res.report_builder = ReportBuilder()ed
