from advanced_feature_factor_acceptance.feature_factor_acceptance_labels import (
    list_acceptance_domain_labels,
    list_acceptance_status_labels,
    validate_acceptance_domain_label,
    validate_acceptance_status_label,
)

def test_acceptance_labels():
    domains = list_acceptance_domain_labels()
    assert "inventory_domain" in domains
    assert "dependency_domain" in domains
    assert "acceptance_gate_domain" in domains
    assert "safety_boundary_domain" in domains
    assert "manifest_domain" in domains
    assert "phase_126_handoff_domain" in domains
    assert validate_acceptance_domain_label("acceptance_gate_domain") is True
    assert validate_acceptance_domain_label("invalid_label") is False

    statuses = list_acceptance_status_labels()
    assert "acceptance_pass" in statuses
    assert "acceptance_manual_review_required" in statuses
    assert "acceptance_fail" in statuses
    assert validate_acceptance_status_label("acceptance_pass") is True
    assert validate_acceptance_status_label("random_status") is False
