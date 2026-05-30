import pandas as pd
from report_summarization.analyst_brief import build_analyst_brief
from report_summarization.summary_config import get_default_report_summary_profile

def test_build_analyst_brief():
    profile = get_default_report_summary_profile()
    sums = pd.DataFrame([{"module_name": "mod1"}])
    finds = pd.DataFrame([{"text": "f1", "priority": "high_priority"}])
    warns = pd.DataFrame([{"text": "w1", "priority": "critical_priority"}])
    rg = pd.DataFrame([{"text": "r1"}])

    text, meta = build_analyst_brief(sums, finds, warns, rg, profile)
    assert "ANALYST BRIEF" in text
    assert "yatırım tavsiyesi değildir" in text.lower()
