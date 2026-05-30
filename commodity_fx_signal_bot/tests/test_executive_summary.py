import pandas as pd
from report_summarization.executive_summary import build_executive_summary
from report_summarization.summary_config import get_default_report_summary_profile

def test_build_executive_summary():
    profile = get_default_report_summary_profile()
    sums = pd.DataFrame([{"module_name": "mod1"}])
    finds = pd.DataFrame([{"text": "f1", "priority": "high_priority"}])
    warns = pd.DataFrame([{"text": "w1", "priority": "critical_priority"}])
    rg = pd.DataFrame([{"text": "r1"}])

    text, meta = build_executive_summary(sums, finds, warns, rg, profile)
    assert "EXECUTIVE SUMMARY" in text
    assert "f1" in text
    assert "w1" in text
    assert "r1" in text
    assert "yatırım tavsiyesi değildir" in text.lower()
