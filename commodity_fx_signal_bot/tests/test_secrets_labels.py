
import pytest
from core.exceptions import ConfigError
from secrets_hygiene.secrets_labels import (
    list_secret_finding_type_labels,
    list_secret_severity_labels,
    list_boundary_status_labels,
    list_redaction_status_labels,
    list_hygiene_status_labels,
    validate_secret_finding_type,
    validate_redaction_status
)

def test_labels_not_empty():
    assert list_secret_finding_type_labels()
    assert list_secret_severity_labels()
    assert list_boundary_status_labels()
    assert list_redaction_status_labels()
    assert list_hygiene_status_labels()

def test_validate_secret_finding_type():
    validate_secret_finding_type("api_key_finding")
    with pytest.raises(ConfigError):
        validate_secret_finding_type("invalid_label")

def test_validate_redaction_status():
    validate_redaction_status("redacted_ok")
    with pytest.raises(ConfigError):
        validate_redaction_status("invalid_label")

def test_hygiene_passed_not_production_compliance():
    assert "production_compliance" not in list_hygiene_status_labels()
