from report_exports.export_quality import (
    check_html_export_quality,
    check_for_forbidden_trade_terms_in_exports,
    build_report_export_quality_report
)

def test_check_html_export_quality():
    res = check_html_export_quality("<html>offline araştırma raporu</html>")
    assert res["passed"] is True

    res = check_html_export_quality("<html><script>alert(1)</script>offline araştırma raporu</html>")
    assert res["passed"] is False

def test_check_for_forbidden_trade_terms():
    res = check_for_forbidden_trade_terms_in_exports(text="This is a BUY signal")
    assert res["passed"] is False
    assert "BUY" in res["forbidden_terms"]

def test_build_report_export_quality_report():
    manifest = {
        "report_id": "rpt_1",
        "disclaimer_present": True,
        "no_trade_instruction_confirmed": True
    }
    res = build_report_export_quality_report([], manifest, {"report_id": "rpt_1"})
    assert res["html_available"] is False
    assert res["passed"] is False
