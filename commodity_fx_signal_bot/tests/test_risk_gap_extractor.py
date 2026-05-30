import pandas as pd
from report_summarization.risk_gap_extractor import extract_risks_and_gaps, classify_risk_gap_priority
from report_summarization.summary_config import get_default_report_summary_profile

def test_extract_risks_and_gaps():
    profile = get_default_report_summary_profile()
    text = "We have a risk of drift. There is a missing test."
    rg = extract_risks_and_gaps("r1", "p1", "m1", text, profile)
    assert len(rg) == 2
    assert "risk_finding" in [r.finding_type for r in rg]
    assert "gap_finding" in [r.finding_type for r in rg]

def test_classify_risk_gap_priority():
    assert classify_risk_gap_priority("This is a failure") == "critical_priority"
    assert classify_risk_gap_priority("There is a gap") == "medium_priority"
