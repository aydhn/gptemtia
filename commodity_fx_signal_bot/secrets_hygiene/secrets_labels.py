
from core.exceptions import ConfigError

_SECRET_FINDING_TYPE_LABELS = [
    "api_key_finding", "api_secret_finding", "broker_key_finding", "exchange_key_finding",
    "token_finding", "password_finding", "private_key_finding", "jwt_finding",
    "high_entropy_finding", "env_value_finding", "personal_data_finding",
    "credential_reference_finding", "unknown_secret_finding"
]

_SECRET_SEVERITY_LABELS = [
    "critical_secret_risk", "high_secret_risk", "medium_secret_risk",
    "low_secret_warning", "informational_secret_note", "unknown_secret_severity"
]

_BOUNDARY_STATUS_LABELS = ["boundary_ok", "boundary_warning", "boundary_failed", "boundary_blocked", "boundary_unknown"]
_REDACTION_STATUS_LABELS = ["redacted_ok", "redacted_partial", "redaction_not_needed", "redaction_failed", "redaction_unknown"]
_HYGIENE_STATUS_LABELS = ["hygiene_passed", "hygiene_passed_with_warnings", "hygiene_failed", "hygiene_blocked", "hygiene_unknown"]

def list_secret_finding_type_labels() -> list[str]: return _SECRET_FINDING_TYPE_LABELS
def list_secret_severity_labels() -> list[str]: return _SECRET_SEVERITY_LABELS
def list_boundary_status_labels() -> list[str]: return _BOUNDARY_STATUS_LABELS
def list_redaction_status_labels() -> list[str]: return _REDACTION_STATUS_LABELS
def list_hygiene_status_labels() -> list[str]: return _HYGIENE_STATUS_LABELS

def validate_secret_finding_type(label: str) -> None:
    if label not in _SECRET_FINDING_TYPE_LABELS:
        raise ConfigError(f"Invalid secret finding type label: {label}")

def validate_secret_severity(label: str) -> None:
    if label not in _SECRET_SEVERITY_LABELS:
        raise ConfigError(f"Invalid secret severity label: {label}")

def validate_boundary_status(label: str) -> None:
    if label not in _BOUNDARY_STATUS_LABELS:
        raise ConfigError(f"Invalid boundary status label: {label}")

def validate_redaction_status(label: str) -> None:
    if label not in _REDACTION_STATUS_LABELS:
        raise ConfigError(f"Invalid redaction status label: {label}")

def validate_hygiene_status(label: str) -> None:
    if label not in _HYGIENE_STATUS_LABELS:
        raise ConfigError(f"Invalid hygiene status label: {label}")
