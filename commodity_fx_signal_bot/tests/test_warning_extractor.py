import pandas as pd
from report_summarization.warning_extractor import extract_warning_lines, classify_warning_priority
from report_summarization.summary_config import get_default_report_summary_profile

def test_extract_warning_lines():
    profile = get_default_report_summary_profile()
    text = "This is a normal line. Warning: Disk space low. Caution: High risk detected."
    warnings = extract_warning_lines("r1", "p1", "m1", text, profile)
    assert len(warnings) == 2

def test_classify_warning_priority():
    assert classify_warning_priority("This is critical!") == "critical_priority"
    assert classify_warning_priority("This is just a warning.") == "high_priority"

def test_extract_warning_false_positives():
    profile = get_default_report_summary_profile()
    text = "Bu sistemde canli emir yoktur."
    warnings = extract_warning_lines("r1", "p1", "m1", text, profile)
    assert len(warnings) == 1
    assert warnings[0].priority == "low_priority"
