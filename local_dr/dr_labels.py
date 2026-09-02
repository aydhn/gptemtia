def list_dr_domain_labels() -> list[str]:
    return ["archive_restore_dr", "config_restore_dr", "model_weights_dr"]

def list_dr_scenario_status_labels() -> list[str]:
    return ["defined", "tested", "obsolete"]

def list_restore_drill_status_labels() -> list[str]:
    return ["passed", "failed", "pending"]

def list_failure_severity_labels() -> list[str]:
    return ["high", "medium", "low"]

def list_resilience_risk_labels() -> list[str]:
    return ["critical", "high", "moderate", "low"]

def validate_dr_domain_label(label: str) -> None:
    if label not in list_dr_domain_labels():
        raise ValueError(f"Invalid DR domain label: {label}")

def validate_dr_scenario_status(label: str) -> None:
    if label not in list_dr_scenario_status_labels():
        raise ValueError(f"Invalid DR scenario status label: {label}")

def validate_restore_drill_status(label: str) -> None:
    if label not in list_restore_drill_status_labels():
        raise ValueError(f"Invalid restore drill status label: {label}")

def validate_failure_severity(label: str) -> None:
    if label not in list_failure_severity_labels():
        raise ValueError(f"Invalid failure severity label: {label}")

def validate_resilience_risk(label: str) -> None:
    if label not in list_resilience_risk_labels():
        raise ValueError(f"Invalid resilience risk label: {label}")
