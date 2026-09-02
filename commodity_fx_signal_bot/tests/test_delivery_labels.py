import pytest
from local_delivery.delivery_labels import list_delivery_domain_labels, list_delivery_item_labels, list_delivery_status_labels, list_transfer_readiness_labels, list_delivery_risk_labels
from local_delivery.delivery_labels import validate_delivery_domain_label, validate_delivery_status

def test_label_lists():
    assert len(list_delivery_domain_labels()) > 0
    assert len(list_delivery_item_labels()) > 0
    assert len(list_delivery_status_labels()) > 0
    assert len(list_transfer_readiness_labels()) > 0
    assert len(list_delivery_risk_labels()) > 0

def test_validate_labels():
    validate_delivery_domain_label("bundle_manifest_domain")
    validate_delivery_status("delivery_ready_for_rehearsal")
    with pytest.raises(ValueError):
        validate_delivery_domain_label("invalid")
