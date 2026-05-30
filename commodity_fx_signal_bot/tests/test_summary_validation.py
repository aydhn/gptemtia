import pandas as pd
from report_summarization.summary_validation import validate_summary_records, build_summary_validation_report
from report_summarization.summary_config import get_default_report_summary_profile

def test_validate_summary_records():
    profile = get_default_report_summary_profile()
    df = pd.DataFrame([{"id": 1}])
    res = validate_summary_records(df, profile)
    assert res["valid"] is True
    assert res["count"] == 1

def test_build_summary_validation_report():
    profile = get_default_report_summary_profile()
    df = pd.DataFrame([{"id": 1}])
    tables = {"summaries": df, "findings": df}

    report_df, meta = build_summary_validation_report(tables, profile)
    assert not report_df.empty
    assert meta["all_valid"] is True
