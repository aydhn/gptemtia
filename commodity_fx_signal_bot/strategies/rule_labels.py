_RULE_GROUPS = [
    "entry_context",
    "exit_context",
    "invalidation",
    "continuation",
    "wait",
    "risk_warning",
    "quality_warning",
    "no_trade_context",
]

_CONDITION_CANDIDATE_LABELS = [
    "entry_condition_candidate",
    "exit_condition_candidate",
    "invalidation_condition_candidate",
    "continuation_condition_candidate",
    "wait_condition_candidate",
    "no_trade_condition_candidate",
    "insufficient_quality_condition_candidate",
    "conflict_condition_candidate",
    "unknown_condition_candidate",
]

_RULE_STATUS_LABELS = [
    "matched_candidate",
    "partial_match_candidate",
    "blocked_candidate",
    "watchlist_candidate",
    "wait_candidate",
    "invalidated_candidate",
    "insufficient_context",
    "insufficient_quality",
    "conflict_blocked",
    "unknown",
]


def list_rule_groups() -> list[str]:
    return list(_RULE_GROUPS)


def list_condition_candidate_labels() -> list[str]:
    return list(_CONDITION_CANDIDATE_LABELS)


def list_rule_status_labels() -> list[str]:
    return list(_RULE_STATUS_LABELS)


def validate_rule_group(label: str) -> None:
    if label not in _RULE_GROUPS:
        raise ValueError(f"Invalid rule group label: {label}")


def validate_condition_candidate_label(label: str) -> None:
    if label not in _CONDITION_CANDIDATE_LABELS:
        raise ValueError(f"Invalid condition candidate label: {label}")


def validate_rule_status(label: str) -> None:
    if label not in _RULE_STATUS_LABELS:
        raise ValueError(f"Invalid rule status label: {label}")


def is_entry_condition(label: str) -> bool:
    return label == "entry_condition_candidate"


def is_exit_condition(label: str) -> bool:
    return label == "exit_condition_candidate"


def is_wait_condition(label: str) -> bool:
    return label == "wait_condition_candidate"


def is_blocked_status(label: str) -> bool:
    return label in (
        "blocked_candidate",
        "conflict_blocked",
        "insufficient_quality",
        "insufficient_context",
    )
