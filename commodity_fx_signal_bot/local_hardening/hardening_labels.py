
def list_hardening_domain_labels() -> list[str]:
    return ["source_hardening", "docs_hardening", "reports_hardening", "datalake_hardening", "scripts_hardening", "tests_hardening", "contracts_hardening", "safety_hardening", "rc_freeze_hardening", "unknown_hardening"]

def list_dead_code_labels() -> list[str]:
    return ["dead_code_candidate", "unused_module_candidate", "orphan_script_candidate", "orphan_test_candidate", "duplicate_utility_candidate", "active_code_reference", "unknown_code_reference"]

def list_contract_labels() -> list[str]:
    return ["public_function_contract", "datalake_contract", "featurestore_contract", "script_cli_contract", "report_builder_contract", "config_contract", "path_contract", "test_contract", "unknown_contract"]

def list_freeze_status_labels() -> list[str]:
    return ["freeze_ready", "freeze_ready_with_warnings", "freeze_missing", "freeze_blocked_by_safety", "freeze_needs_manual_review", "freeze_unknown"]

def list_hardening_risk_labels() -> list[str]:
    return ["hardening_critical_risk", "hardening_high_risk", "hardening_medium_risk", "hardening_low_risk", "hardening_info", "hardening_unknown_risk"]

def validate_hardening_domain_label(label: str) -> None:
    if label not in list_hardening_domain_labels(): raise ValueError()

def validate_dead_code_label(label: str) -> None:
    if label not in list_dead_code_labels(): raise ValueError()

def validate_contract_label(label: str) -> None:
    if label not in list_contract_labels(): raise ValueError()

def validate_freeze_status(label: str) -> None:
    if label not in list_freeze_status_labels(): raise ValueError()

def validate_hardening_risk(label: str) -> None:
    if label not in list_hardening_risk_labels(): raise ValueError()
