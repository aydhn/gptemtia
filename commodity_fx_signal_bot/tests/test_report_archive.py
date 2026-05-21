import pytest
from pathlib import Path
from report_exports.report_archive import ReportArchive
from report_exports.export_models import ReportArchiveRecord

def test_report_archive(tmp_path):
    archive = ReportArchive(tmp_path)

    record = ReportArchiveRecord(
        archive_id="arc_1",
        report_id="rpt_1",
        report_type="symbol",
        symbol="GC=F",
        timeframe="1d",
        profile_name="balanced",
        created_at_utc="2023-01-01T12:00:00Z",
        research_score=0.8,
        warning_count=0,
        missing_sources_count=0,
        markdown_path=None,
        html_path=None,
        pdf_path=None,
        csv_paths=[],
        quality_passed=True,
        metadata={}
    )

    archive.add_record(record)
    df = archive.load_records()
    assert len(df) == 1
    assert df.iloc[0]["archive_id"] == "arc_1"

    summary = archive.summarize()
    assert summary["total_records"] == 1

    prev = archive.find_previous_report("symbol", "GC=F", "1d", "balanced")
    assert prev["report_id"] == "rpt_1"
