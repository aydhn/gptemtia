
import pytest
from local_review_governance.review_labels import list_review_domain_labels, validate_review_domain_label

def test_labels():
    labels = list_review_domain_labels()
    assert len(labels) > 0
    validate_review_domain_label(labels[0])
    with pytest.raises(ValueError):
        validate_review_domain_label("invalid")
