import pytest
from advanced_data_lineage.data_lineage_labels import (
    list_lineage_domain_labels,
    list_lineage_status_labels,
    list_provenance_confidence_labels,
    list_audit_event_labels,
    list_lineage_dataset_type_labels,
    validate_lineage_domain_label,
    validate_lineage_status_label,
    validate_provenance_confidence_label,
    validate_audit_event_label,
    validate_lineage_dataset_type_label,
)


def test_labels_lists():
    assert len(list_lineage_domain_labels()) >= 25
    assert len(list_lineage_status_labels()) >= 5
    assert len(list_provenance_confidence_labels()) >= 3
    assert len(list_audit_event_labels()) >= 8
    assert len(list_lineage_dataset_type_labels()) >= 8


def test_validations_pass():
    assert validate_lineage_domain_label("fx_lineage_domain") is True
    assert validate_lineage_status_label("lineage_complete") is True
    assert validate_provenance_confidence_label("provenance_high_confidence") is True
    assert validate_audit_event_label("audit_source_registered") is True
    assert validate_lineage_dataset_type_label("dataset_fx_quote") is True


def test_validations_fail():
    with pytest.raises(ValueError):
        validate_lineage_domain_label("invalid_domain_xyz")
    with pytest.raises(ValueError):
        validate_lineage_status_label("invalid_status_xyz")
    with pytest.raises(ValueError):
        validate_provenance_confidence_label("invalid_conf_xyz")
    with pytest.raises(ValueError):
        validate_audit_event_label("invalid_audit_xyz")
    with pytest.raises(ValueError):
        validate_lineage_dataset_type_label("invalid_dataset_xyz")
