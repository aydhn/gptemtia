from pathlib import Path
import pandas as pd
from report_summarization.report_inventory import classify_source_report_module, classify_source_report_type, read_report_text

def test_classify_source_report_module():
    assert classify_source_report_module(Path("reports/output/research_reports/rep1.md")) == "research_reports"
    assert classify_source_report_module(Path("unknown/path/rep1.md")) == "unknown_module"

def test_classify_source_report_type():
    assert classify_source_report_type(Path("reports/output/test_status.md")) == "status_report"
    assert classify_source_report_type(Path("reports/output/test.csv")) == "data_report"

def test_read_report_text(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("Hello World!")

    text, meta = read_report_text(f, 100)
    assert text == "Hello World!"
    assert meta["status"] == "success"

    f = tmp_path / ".env"
    f.write_text("SECRET=123")
    text, meta = read_report_text(f, 100)
    assert text == ""
    assert meta["status"] == "skipped_secret"

    f = tmp_path / "large.txt"
    f.write_text("A" * 150)
    text, meta = read_report_text(f, 100)
    assert len(text) == 100
    assert meta["truncated"] is True
