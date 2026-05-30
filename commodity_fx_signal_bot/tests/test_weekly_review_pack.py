import pandas as pd
from report_summarization.weekly_review_pack import build_weekly_offline_review_pack
from report_summarization.summary_config import get_default_report_summary_profile

def test_build_weekly_review_pack():
    profile = get_default_report_summary_profile()
    sums = pd.DataFrame([{"module_name": "mod1"}])
    finds = pd.DataFrame()
    warns = pd.DataFrame()
    rg = pd.DataFrame()

    text, meta = build_weekly_offline_review_pack(sums, finds, warns, rg, profile)
    assert "WEEKLY OFFLINE REVIEW PACK" in text
    assert "yatırım tavsiyesi değildir" in text.lower()
