import pandas as pd
from report_summarization.finding_extractor import extract_findings_from_text, classify_finding_type, infer_finding_priority, extract_related_symbols, findings_to_dataframe
from report_summarization.summary_config import get_default_report_summary_profile

def test_extract_findings_from_text():
    profile = get_default_report_summary_profile()
    text = "There is a critical missing data point. The quality is bad for GC=F."
    findings = extract_findings_from_text("r1", "p1", "m1", text, profile)
    assert len(findings) == 2

def test_classify_finding_type():
    assert classify_finding_type("This is a warning") == "warning_finding"
    assert classify_finding_type("This is a gap") == "gap_finding"

def test_infer_finding_priority():
    assert infer_finding_priority("This is critical and failed") == "critical_priority"
    assert infer_finding_priority("Just a small gap") == "medium_priority"

def test_extract_related_symbols():
    symbols = extract_related_symbols("Data for GC=F and SI=F")
    assert "GC=F" in symbols
    assert "SI=F" in symbols

def test_findings_to_dataframe():
    profile = get_default_report_summary_profile()
    findings = extract_findings_from_text("r1", "p1", "m1", "There is a gap.", profile)
    df = findings_to_dataframe(findings)
    assert not df.empty
    assert "finding_type" in df.columns
