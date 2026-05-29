_ANALYST_INTENT_LABELS = [
    "status_check_intent",
    "report_generation_intent",
    "knowledge_query_intent",
    "documentation_lookup_intent",
    "scenario_demo_intent",
    "scenario_regression_intent",
    "final_review_intent",
    "quality_gate_intent",
    "maintenance_intent",
    "performance_intent",
    "governance_intent",
    "experiment_intent",
    "research_planning_intent",
    "troubleshooting_intent",
    "unknown_intent"
]

_ALIAS_TYPE_LABELS = [
    "status_alias",
    "report_alias",
    "query_alias",
    "workflow_alias",
    "runbook_alias",
    "documentation_alias",
    "scenario_alias",
    "quality_alias",
    "maintenance_alias",
    "unknown_alias"
]

_PROMPT_PACK_LABELS = [
    "operator_prompt_pack",
    "analyst_prompt_pack",
    "codex_agent_prompt_pack",
    "troubleshooting_prompt_pack",
    "documentation_prompt_pack",
    "scenario_prompt_pack",
    "regression_prompt_pack",
    "final_review_prompt_pack",
    "unknown_prompt_pack"
]

_SUGGESTION_SAFETY_LABELS = [
    "safe_offline_suggestion",
    "dry_run_only_suggestion",
    "review_required_suggestion",
    "blocked_live_suggestion",
    "blocked_broker_suggestion",
    "blocked_deploy_suggestion",
    "blocked_daemon_suggestion",
    "unsafe_unknown_suggestion"
]

class LabelError(Exception):
    pass

def list_analyst_intent_labels() -> list[str]:
    return _ANALYST_INTENT_LABELS.copy()

def list_alias_type_labels() -> list[str]:
    return _ALIAS_TYPE_LABELS.copy()

def list_prompt_pack_labels() -> list[str]:
    return _PROMPT_PACK_LABELS.copy()

def list_suggestion_safety_labels() -> list[str]:
    return _SUGGESTION_SAFETY_LABELS.copy()

def validate_analyst_intent(label: str) -> None:
    if label not in _ANALYST_INTENT_LABELS:
        raise LabelError(f"Invalid analyst intent label: {label}")

def validate_alias_type(label: str) -> None:
    if label not in _ALIAS_TYPE_LABELS:
        raise LabelError(f"Invalid alias type label: {label}")

def validate_prompt_pack_label(label: str) -> None:
    if label not in _PROMPT_PACK_LABELS:
        raise LabelError(f"Invalid prompt pack label: {label}")

def validate_suggestion_safety(label: str) -> None:
    if label not in _SUGGESTION_SAFETY_LABELS:
        raise LabelError(f"Invalid suggestion safety label: {label}")
