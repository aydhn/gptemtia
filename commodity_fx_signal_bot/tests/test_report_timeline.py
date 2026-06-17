import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.report_timeline import classify_report_family, infer_report_generation_module, summarize_report_generation_timeline

def test_classify_report_family():
    assert classify_report_family(Path("reports/output/quality_gates/a.md"), Path(".")) == "quality_gates"
    assert classify_report_family(Path("reports/output/unknown/a.md"), Path(".")) == "unknown_report_family"

def test_infer_report_generation_module():
    assert infer_report_generation_module(Path("reports/output/quality_gates/a.md"), Path(".")) == "quality_gates"

def test_summarize_report_generation_timeline():
    df = pd.DataFrame([{"relative_path": "a.txt"}, {"relative_path": "a.txt"}])
    summary = summarize_report_generation_timeline(df)
    assert summary["total_report_events"] == 2
    assert summary["unique_reports"] == 1
