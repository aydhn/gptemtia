"""
Controlled label sets for scenario categorization.
"""

from typing import List


class ScenarioLabelError(Exception):
    pass


SCENARIO_TYPE_LABELS = [
    "symbol_research_scenario",
    "factor_research_scenario",
    "meta_research_scenario",
    "portfolio_research_scenario",
    "regime_research_scenario",
    "experiment_tracking_scenario",
    "governance_scenario",
    "planning_scenario",
    "knowledge_base_scenario",
    "command_center_scenario",
    "quality_gate_scenario",
    "performance_scenario",
    "maintenance_scenario",
    "final_review_scenario",
    "end_to_end_scenario",
    "unknown_scenario"
]

SCENARIO_STATUS_LABELS = [
    "scenario_planned",
    "scenario_fixture_ready",
    "scenario_dry_run_ready",
    "scenario_validated",
    "scenario_warning",
    "scenario_failed",
    "scenario_skipped",
    "scenario_unknown"
]

SCENARIO_SAFETY_LABELS = [
    "synthetic_offline_only",
    "dry_run_only",
    "safe_demo_flow",
    "blocked_live_command",
    "blocked_broker_command",
    "blocked_deploy_command",
    "blocked_daemon_command",
    "unsafe_scenario_unknown"
]

CASE_STUDY_LABELS = [
    "trend_regime_case_study",
    "inflation_comparison_case_study",
    "factor_conflict_case_study",
    "governance_gap_case_study",
    "experiment_ablation_case_study",
    "knowledge_query_case_study",
    "planning_backlog_case_study",
    "maintenance_cleanup_case_study",
    "final_review_case_study",
    "unknown_case_study"
]


def list_scenario_type_labels() -> List[str]:
    """Returns list of valid scenario type labels."""
    return SCENARIO_TYPE_LABELS.copy()


def list_scenario_status_labels() -> List[str]:
    """Returns list of valid scenario status labels."""
    return SCENARIO_STATUS_LABELS.copy()


def list_scenario_safety_labels() -> List[str]:
    """Returns list of valid scenario safety labels."""
    return SCENARIO_SAFETY_LABELS.copy()


def list_case_study_labels() -> List[str]:
    """Returns list of valid case study labels."""
    return CASE_STUDY_LABELS.copy()


def validate_scenario_type(label: str) -> None:
    """Validates a scenario type label."""
    if label not in SCENARIO_TYPE_LABELS:
        raise ScenarioLabelError(f"Invalid scenario type label: {label}")


def validate_scenario_status(label: str) -> None:
    """Validates a scenario status label."""
    if label not in SCENARIO_STATUS_LABELS:
        raise ScenarioLabelError(f"Invalid scenario status label: {label}")


def validate_scenario_safety(label: str) -> None:
    """Validates a scenario safety label."""
    if label not in SCENARIO_SAFETY_LABELS:
        raise ScenarioLabelError(f"Invalid scenario safety label: {label}")


def validate_case_study_label(label: str) -> None:
    """Validates a case study label."""
    if label not in CASE_STUDY_LABELS:
        raise ScenarioLabelError(f"Invalid case study label: {label}")
