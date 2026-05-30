from report_summarization.summary_labels import list_summary_type_labels, list_finding_type_labels, list_brief_priority_labels, list_follow_up_type_labels, validate_summary_type, validate_finding_type, validate_brief_priority, validate_follow_up_type
import pytest

def test_summary_labels_list():
    assert len(list_summary_type_labels()) > 0
    assert len(list_finding_type_labels()) > 0
    assert len(list_brief_priority_labels()) > 0
    assert len(list_follow_up_type_labels()) > 0

def test_summary_labels_validation():
    validate_summary_type("executive_summary")
    with pytest.raises(ValueError):
        validate_summary_type("invalid_summary_type")

    validate_finding_type("key_finding")
    with pytest.raises(ValueError):
        validate_finding_type("invalid_finding_type")

    validate_brief_priority("critical_priority")
    assert "critical_priority" in list_brief_priority_labels() # check it exists but is named priority not "trade emergency"

    validate_follow_up_type("review_report_follow_up")
    with pytest.raises(ValueError):
        validate_follow_up_type("invalid_follow_up_type")
