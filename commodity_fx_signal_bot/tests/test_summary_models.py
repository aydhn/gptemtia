from report_summarization.summary_models import build_summary_id, build_finding_id, build_brief_id, build_follow_up_task_id, ReportSummaryRecord, report_summary_record_to_dict

def test_summary_models_id_generation():
    assert build_summary_id("rep1", "type1") == build_summary_id("rep1", "type1")
    assert build_finding_id("rep1", "text1") == build_finding_id("rep1", "text1")
    assert build_brief_id("type1", "title1") == build_brief_id("type1", "title1")
    assert build_follow_up_task_id("t1", "f1") == build_follow_up_task_id("t1", "f1")

def test_summary_models_to_dict():
    rec = ReportSummaryRecord(
        summary_id="1", source_report_id="1", source_path="", module_name="",
        summary_type="", title="", summary_text="", bullets=[], key_findings=[],
        warnings=[], generated_at_utc="", warnings_meta=[]
    )
    d = report_summary_record_to_dict(rec)
    assert "summary_id" in d
    assert "source_report_id" in d
