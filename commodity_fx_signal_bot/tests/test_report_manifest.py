from report_exports.report_manifest import (
    build_report_export_manifest,
    validate_report_export_manifest
)

def test_build_report_export_manifest():
    manifest = build_report_export_manifest(
        "rpt_1", "symbol", "GC=F", "1d", "balanced", []
    )
    assert manifest["report_id"] == "rpt_1"
    assert manifest["disclaimer_present"] is True
    assert manifest["no_trade_instruction_confirmed"] is True

def test_validate_report_export_manifest():
    manifest = {
        "report_id": "rpt_1",
        "disclaimer_present": True,
        "no_trade_instruction_confirmed": True
    }
    res = validate_report_export_manifest(manifest)
    assert res["valid"] is True
