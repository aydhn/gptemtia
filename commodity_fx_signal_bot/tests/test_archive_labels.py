import pytest
from local_archive.archive_labels import (
    list_archive_domain_labels,
    list_archive_item_status_labels,
    list_retention_labels,
    list_archive_risk_labels,
    list_integrity_status_labels,
    validate_archive_domain_label,
    validate_retention_label
)

def test_labels_not_empty():
    assert len(list_archive_domain_labels()) > 0
    assert len(list_archive_item_status_labels()) > 0
    assert len(list_retention_labels()) > 0
    assert len(list_archive_risk_labels()) > 0
    assert len(list_integrity_status_labels()) > 0

def test_valid_domain_label():
    validate_archive_domain_label("documentation_archive")

def test_invalid_domain_label():
    with pytest.raises(ValueError):
        validate_archive_domain_label("invalid_label")

def test_valid_retention_label():
    validate_retention_label("retain_long_term_manual")

def test_manifested_not_cold_storage():
    assert "archive_manifested" in list_archive_item_status_labels()
