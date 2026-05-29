from scenario_regression.regression_report_builder import build_regression_disclaimer

def test_disclaimer():
    d = build_regression_disclaimer()
    assert "offline" in d
    assert "yatırım tavsiyesi değildir" in d
