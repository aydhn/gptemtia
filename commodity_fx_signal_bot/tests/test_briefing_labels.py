from local_briefing.briefing_labels import list_audience_labels, validate_audience_label, list_communication_status_labels, validate_communication_status

def test_labels():
    assert len(list_audience_labels()) > 0
    assert len(list_communication_status_labels()) > 0
    validate_audience_label("executive_audience")
    validate_communication_status("communication_ready")
