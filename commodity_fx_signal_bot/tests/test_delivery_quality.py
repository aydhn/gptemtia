from local_delivery.delivery_quality import build_delivery_quality_report

def test_build_quality():
    rep = build_delivery_quality_report({"test": "val"})
    assert rep["passed"] is True
