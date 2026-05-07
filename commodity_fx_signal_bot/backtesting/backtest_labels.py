_LIFECYCLE_STATUS = [
    "pending_candidate",
    "simulated_open",
    "simulated_closed",
    "simulated_cancelled",
    "simulated_rejected",
    "simulated_expired",
    "unknown",
]

_ENTRY_REASON = [
    "candidate_entry",
    "next_bar_open_entry",
    "delayed_entry",
    "invalid_entry_context",
    "missing_level_candidate",
    "missing_sizing_candidate",
    "risk_rejected",
    "unknown_entry_reason",
]

_EXIT_REASON = [
    "target_touch_simulated",
    "stop_touch_simulated",
    "invalidation_touch_simulated",
    "max_holding_period",
    "opposite_candidate_context",
    "end_of_data",
    "missing_exit_context",
    "unknown_exit_reason",
]

_RESULT_LABELS = [
    "win",
    "loss",
    "breakeven",
    "open_at_end",
    "cancelled",
    "rejected",
    "unknown",
]


def list_trade_lifecycle_statuses() -> list[str]:
    return _LIFECYCLE_STATUS.copy()


def list_entry_reason_labels() -> list[str]:
    return _ENTRY_REASON.copy()


def list_exit_reason_labels() -> list[str]:
    return _EXIT_REASON.copy()


def list_backtest_result_labels() -> list[str]:
    return _RESULT_LABELS.copy()


def validate_lifecycle_status(label: str) -> None:
    if label not in _LIFECYCLE_STATUS:
        raise ValueError(f"Invalid lifecycle status: {label}")


def validate_entry_reason(label: str) -> None:
    if label not in _ENTRY_REASON:
        raise ValueError(f"Invalid entry reason: {label}")


def validate_exit_reason(label: str) -> None:
    if label not in _EXIT_REASON:
        raise ValueError(f"Invalid exit reason: {label}")


def validate_backtest_result(label: str) -> None:
    if label not in _RESULT_LABELS:
        raise ValueError(f"Invalid backtest result: {label}")
