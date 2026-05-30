import pandas as pd
from report_summarization.summary_quality import check_summary_quality, check_for_forbidden_terms_in_summaries, build_summary_quality_report
from report_summarization.summary_config import get_default_report_summary_profile

def test_check_for_forbidden_terms():
    res = check_for_forbidden_terms_in_summaries(text="This is a live order command.")
    assert res["valid"] is False
    assert "live order" in res["forbidden_terms_found"]

def test_check_summary_quality():
    profile = get_default_report_summary_profile()
    df = pd.DataFrame([{"text": "safe text"}])
    res = check_summary_quality(df, profile)
    assert res["valid"] is True

    df_unsafe = pd.DataFrame([{"text": "this is a buy now instruction"}])
    res_unsafe = check_summary_quality(df_unsafe, profile)
    assert res_unsafe["valid"] is False

def test_build_summary_quality_report():
    df = pd.DataFrame([{"text": "safe text"}])
    report = build_summary_quality_report({"status": "ok"}, summaries_df=df)
    assert report["passed"] is True
