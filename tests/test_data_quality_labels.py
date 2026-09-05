import pytest
from advanced_data_quality.data_quality_labels import (
    list_quality_domain_labels,
    list_quality_severity_labels,
    list_quality_status_labels,
    list_dataset_type_labels,
    list_quality_finding_type_labels,
    validate_quality_domain_label,
    validate_quality_severity_label,
    validate_quality_status_label,
    validate_dataset_type_label,
    validate_quality_finding_type_label,
)


def test_quality_labels():
    domains = list_quality_domain_labels()
    assert len(domains) >= 25
    assert validate_quality_domain_label("schema_compliance_domain") is True
    assert validate_quality_domain_label("invalid_domain") is False

    sevs = list_quality_severity_labels()
    assert "quality_critical" in sevs
    assert "quality_high" in sevs
    assert validate_quality_severity_label("quality_critical") is True

    statuses = list_quality_status_labels()
    assert "quality_pass" in statuses
    assert validate_quality_status_label("quality_pass") is True

    datasets = list_dataset_type_labels()
    assert "dataset_fx_ohlcv" in datasets
    assert validate_dataset_type_label("dataset_fx_ohlcv") is True

    findings = list_quality_finding_type_labels()
    assert "finding_schema_mismatch" in findings
    assert validate_quality_finding_type_label("finding_schema_mismatch") is True
