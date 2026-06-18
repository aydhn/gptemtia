from local_readiness.readiness_labels import (
    list_readiness_gate_labels,
    list_readiness_domain_labels,
    list_go_no_go_labels,
    list_checklist_status_labels,
    list_risk_level_labels,
    validate_readiness_gate_label,
    validate_go_no_go_label
)

def test_labels_not_empty():
    assert len(list_readiness_gate_labels()) > 0
    assert len(list_readiness_domain_labels()) > 0
    assert len(list_go_no_go_labels()) > 0
    assert len(list_checklist_status_labels()) > 0
    assert len(list_risk_level_labels()) > 0

def test_validate_labels():
    validate_readiness_gate_label("gate_passed")
    validate_go_no_go_label("safe_go_condition")
    assert "safe_go_condition_canli_trading" not in list_go_no_go_labels()
