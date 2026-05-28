from final_review.final_review_labels import (
    list_audit_type_labels, list_audit_status_labels, list_final_readiness_labels,
    list_risk_severity_labels, list_gap_category_labels,
    validate_audit_type, validate_final_readiness
)

def test_label_lists_not_empty():
    assert len(list_audit_type_labels()) > 0
    assert len(list_audit_status_labels()) > 0
    assert len(list_final_readiness_labels()) > 0
    assert len(list_risk_severity_labels()) > 0
    assert len(list_gap_category_labels()) > 0

def test_validate_labels():
    validate_audit_type("architecture_audit")
    validate_final_readiness("offline_ready_for_research_use")

def test_offline_ready_label_name():
    assert "offline_ready_for_research_use" in list_final_readiness_labels()
    assert "production_release" not in list_final_readiness_labels()
