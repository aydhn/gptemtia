
from local_closure.closure_labels import list_closure_domain_labels, list_closure_item_labels, list_closure_status_labels, list_roadmap_status_labels, list_closure_risk_labels, validate_closure_domain_label, validate_closure_status

def test_label_lists():
    assert len(list_closure_domain_labels()) > 0
    assert len(list_closure_item_labels()) > 0
    assert len(list_closure_status_labels()) > 0
    assert len(list_roadmap_status_labels()) > 0
    assert len(list_closure_risk_labels()) > 0

def test_validate_labels():
    validate_closure_domain_label("meta_review_domain")
    validate_closure_status("closure_ready_for_rehearsal")

def test_closure_ready_for_rehearsal():
    assert "closure_ready_for_rehearsal" in list_closure_status_labels()
