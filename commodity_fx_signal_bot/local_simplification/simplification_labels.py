def list_simplification_domain_labels() -> list[str]:
    return [
        "complexity_map_domain", "module_family_complexity_domain", "sprawl_analysis_domain",
        "optional_slimming_domain", "consolidation_candidate_domain", "naming_simplification_domain",
        "config_simplification_domain", "datalake_simplification_domain", "script_cli_simplification_domain",
        "test_suite_simplification_domain", "docs_navigation_domain", "repo_ergonomics_domain",
        "maintainability_seed_domain", "quality_validation_domain", "unknown_simplification_domain"
    ]

def list_simplification_candidate_labels() -> list[str]:
    return [
        "safe_consolidation_candidate", "duplicate_pattern_candidate", "naming_simplification_candidate",
        "config_simplification_candidate", "datalake_method_simplification_candidate",
        "script_cli_simplification_candidate", "test_suite_simplification_candidate",
        "docs_navigation_simplification_candidate", "maintainability_seed_candidate",
        "blocked_by_safety_candidate", "unknown_simplification_candidate"
    ]

def list_simplification_status_labels() -> list[str]:
    return [
        "simplification_ready_for_rehearsal", "simplification_ready_with_warnings",
        "simplification_missing", "simplification_blocked_by_safety",
        "simplification_needs_manual_review", "simplification_unknown"
    ]

def list_complexity_level_labels() -> list[str]:
    return [
        "complexity_low", "complexity_medium", "complexity_high",
        "complexity_very_high", "complexity_unknown"
    ]

def list_simplification_risk_labels() -> list[str]:
    return [
        "simplification_critical_risk", "simplification_high_risk",
        "simplification_medium_risk", "simplification_low_risk",
        "simplification_info", "simplification_unknown_risk"
    ]

def validate_simplification_domain_label(label: str) -> None:
    if label not in list_simplification_domain_labels():
        raise ValueError(f"Invalid domain label: {label}")

def validate_simplification_candidate_label(label: str) -> None:
    if label not in list_simplification_candidate_labels():
        raise ValueError(f"Invalid candidate label: {label}")

def validate_simplification_status(label: str) -> None:
    if label not in list_simplification_status_labels():
        raise ValueError(f"Invalid status label: {label}")

def validate_complexity_level(label: str) -> None:
    if label not in list_complexity_level_labels():
        raise ValueError(f"Invalid complexity level: {label}")

def validate_simplification_risk(label: str) -> None:
    if label not in list_simplification_risk_labels():
        raise ValueError(f"Invalid risk label: {label}")
