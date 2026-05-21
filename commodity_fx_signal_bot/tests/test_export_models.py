from report_exports.export_models import (
    build_export_artifact_id,
    build_archive_id,
    build_comparison_id,
    sanitize_export_filename,
    ReportExportArtifact,
    report_export_artifact_to_dict
)

def test_build_export_artifact_id():
    assert build_export_artifact_id("rpt_1", "html_export") == "art_rpt_1_html_export"

def test_build_archive_id():
    res = build_archive_id("rpt_1", "2023-01-01T12:00:00Z")
    assert "-" not in res
    assert ":" not in res

def test_sanitize_export_filename():
    assert sanitize_export_filename("GC=F") == "GC_F"
    assert sanitize_export_filename(" EURUSD ") == "EURUSD"

def test_to_dict():
    art = ReportExportArtifact("a", "r", "t", "s", "p", "c", 10, [])
    d = report_export_artifact_to_dict(art)
    assert d["artifact_id"] == "a"
