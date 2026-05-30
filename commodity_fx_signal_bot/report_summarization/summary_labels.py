_summary_types = [
    "executive_summary",
    "analyst_brief",
    "weekly_review_pack",
    "research_digest",
    "module_summary",
    "symbol_brief",
    "safety_brief",
    "quality_brief",
    "scenario_regression_brief",
    "maintenance_performance_brief",
    "final_review_brief",
    "unknown_summary"
]

_finding_types = [
    "key_finding",
    "warning_finding",
    "risk_finding",
    "gap_finding",
    "quality_finding",
    "safety_finding",
    "performance_finding",
    "maintenance_finding",
    "scenario_finding",
    "documentation_finding",
    "unknown_finding"
]

_brief_priorities = [
    "critical_priority",
    "high_priority",
    "medium_priority",
    "low_priority",
    "informational_priority",
    "unknown_priority"
]

_follow_up_types = [
    "review_report_follow_up",
    "run_safe_command_follow_up",
    "inspect_warning_follow_up",
    "fix_test_gap_follow_up",
    "update_documentation_follow_up",
    "refresh_index_follow_up",
    "check_quality_gate_follow_up",
    "investigate_regression_follow_up",
    "maintenance_review_follow_up",
    "unknown_follow_up"
]

def list_summary_type_labels() -> list[str]:
    return _summary_types.copy()

def list_finding_type_labels() -> list[str]:
    return _finding_types.copy()

def list_brief_priority_labels() -> list[str]:
    return _brief_priorities.copy()

def list_follow_up_type_labels() -> list[str]:
    return _follow_up_types.copy()

def validate_summary_type(label: str) -> None:
    if label not in _summary_types:
        raise ValueError(f"Invalid summary type label: {label}")

def validate_finding_type(label: str) -> None:
    if label not in _finding_types:
        raise ValueError(f"Invalid finding type label: {label}")

def validate_brief_priority(label: str) -> None:
    if label not in _brief_priorities:
        raise ValueError(f"Invalid brief priority label: {label}")

def validate_follow_up_type(label: str) -> None:
    if label not in _follow_up_types:
        raise ValueError(f"Invalid follow-up type label: {label}")
