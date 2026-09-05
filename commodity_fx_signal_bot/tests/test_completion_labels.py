from local_project_completion.completion_labels import *

def test_labels_not_empty():
    assert len(list_completion_domain_labels()) > 0
    assert len(list_completion_status_labels()) > 0
    assert len(list_knowledge_freeze_labels()) > 0
    assert len(list_audit_status_labels()) > 0
    assert len(list_completion_risk_labels()) > 0

def test_validations():
    validate_completion_domain_label("system_closure_dossier_domain")
    validate_audit_status("last_mile_audit_pass_rehearsal")

def test_no_official_audit_pass():
    assert "last_mile_audit_pass_rehearsal" in list_audit_status_labels()
