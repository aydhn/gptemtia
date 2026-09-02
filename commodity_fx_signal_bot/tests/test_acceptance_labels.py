from local_acceptance.acceptance_labels import (
    list_acceptance_domain_labels,
    list_acceptance_status_labels,
    validate_acceptance_domain_label,
    validate_acceptance_status
)

def test_list_labels():
    assert len(list_acceptance_domain_labels()) > 0
    assert len(list_acceptance_status_labels()) > 0

def test_validate_labels():
    validate_acceptance_domain_label("final_acceptance_domain")
    validate_acceptance_status("acceptance_ready_for_rehearsal")
