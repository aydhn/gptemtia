import pytest
from report_exports.export_labels import (
    list_export_type_labels,
    list_export_status_labels,
    list_report_archive_labels,
    list_comparison_labels,
    validate_export_type,
    validate_export_status
)

def test_export_type_labels():
    labels = list_export_type_labels()
    assert "html_export" in labels
    assert "pdf_export" in labels

def test_validate_export_type():
    validate_export_type("html_export")
    with pytest.raises(ValueError):
        validate_export_type("invalid_type")

def test_comparison_labels_not_trade_signals():
    labels = list_comparison_labels()
    assert "improved" in labels
    assert "deteriorated" in labels
    assert "BUY" not in [l.upper() for l in labels]
