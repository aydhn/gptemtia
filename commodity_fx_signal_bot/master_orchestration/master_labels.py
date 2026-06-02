"""
Master orchestration controlled label set.
"""

def list_layer_type_labels() -> list[str]:
    return [
        "data_layer",
        "feature_layer",
        "research_layer",
        "validation_layer",
        "ml_layer",
        "paper_layer",
        "governance_layer",
        "reporting_layer",
        "knowledge_layer",
        "command_center_layer",
        "quality_layer",
        "performance_layer",
        "maintenance_layer",
        "documentation_layer",
        "scenario_layer",
        "regression_layer",
        "analyst_ux_layer",
        "summarization_layer",
        "final_review_layer",
        "master_orchestration_layer",
        "unknown_layer"
    ]

def list_operating_mode_labels() -> list[str]:
    return [
        "daily_offline_review_mode",
        "weekly_offline_review_mode",
        "monthly_maintenance_mode",
        "full_audit_mode",
        "scenario_demo_mode",
        "regression_check_mode",
        "documentation_refresh_mode",
        "quality_performance_maintenance_mode",
        "final_review_mode",
        "summary_briefing_mode",
        "unknown_mode"
    ]

def list_command_plan_status_labels() -> list[str]:
    return [
        "plan_ready_dry_run",
        "plan_ready_with_warnings",
        "plan_blocked_by_safety",
        "plan_incomplete",
        "plan_unknown"
    ]

def list_meta_runner_safety_labels() -> list[str]:
    return [
        "safe_dry_run_only",
        "safe_offline_executable_if_explicit",
        "review_required",
        "blocked_live",
        "blocked_broker",
        "blocked_deploy",
        "blocked_daemon",
        "blocked_external_llm",
        "blocked_real_market_download",
        "unsafe_unknown"
    ]

def list_consolidation_labels() -> list[str]:
    return [
        "phase_complete",
        "phase_partial",
        "phase_missing",
        "phase_warning",
        "phase_unknown"
    ]

def validate_layer_type(label: str) -> None:
    if label not in list_layer_type_labels():
        raise ValueError(f"Invalid layer type label: {label}")

def validate_operating_mode(label: str) -> None:
    if label not in list_operating_mode_labels():
        raise ValueError(f"Invalid operating mode label: {label}")

def validate_command_plan_status(label: str) -> None:
    if label not in list_command_plan_status_labels():
        raise ValueError(f"Invalid command plan status label: {label}")

def validate_meta_runner_safety(label: str) -> None:
    if label not in list_meta_runner_safety_labels():
        raise ValueError(f"Invalid meta runner safety label: {label}")

def validate_consolidation_label(label: str) -> None:
    if label not in list_consolidation_labels():
        raise ValueError(f"Invalid consolidation label: {label}")
