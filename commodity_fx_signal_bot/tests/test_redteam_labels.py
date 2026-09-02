import pytest
from local_redteam.redteam_labels import (
    list_redteam_domain_labels,
    list_misuse_category_labels,
    list_safety_response_labels,
    list_redteam_status_labels,
    list_redteam_risk_labels,
    validate_redteam_domain_label,
    validate_misuse_category_label,
    LabelError
)

def test_lists_not_empty():
    assert len(list_redteam_domain_labels()) > 0
    assert len(list_misuse_category_labels()) > 0
    assert len(list_safety_response_labels()) > 0
    assert len(list_redteam_status_labels()) > 0
    assert len(list_redteam_risk_labels()) > 0

def test_validates():
    validate_redteam_domain_label("redteam_rehearsal_domain")
    validate_misuse_category_label("misuse_live_trading")

    with pytest.raises(LabelError):
        validate_redteam_domain_label("invalid")
