# Virtual order status
VIRTUAL_ORDER_STATUSES = {
    "virtual_pending",
    "virtual_filled",
    "virtual_cancelled",
    "virtual_rejected",
    "virtual_expired",
    "virtual_unknown"
}

# Virtual order side
VIRTUAL_ORDER_SIDES = {
    "virtual_long_bias",
    "virtual_short_bias",
    "virtual_neutral",
    "virtual_unknown_side"
}

# Virtual position status
VIRTUAL_POSITION_STATUSES = {
    "virtual_open",
    "virtual_closed",
    "virtual_invalidated",
    "virtual_expired",
    "virtual_rejected",
    "virtual_unknown"
}

# Virtual exit reason
VIRTUAL_EXIT_REASONS = {
    "virtual_target_touch",
    "virtual_stop_touch",
    "virtual_invalidation_touch",
    "virtual_max_holding",
    "virtual_opposite_context",
    "virtual_end_of_data",
    "virtual_manual_sim_cancel",
    "virtual_unknown_exit"
}

# Paper result label
PAPER_RESULT_LABELS = {
    "virtual_win",
    "virtual_loss",
    "virtual_breakeven",
    "virtual_open_at_end",
    "virtual_cancelled",
    "virtual_rejected",
    "virtual_unknown_result"
}

def list_virtual_order_statuses() -> list[str]:
    return sorted(list(VIRTUAL_ORDER_STATUSES))

def list_virtual_order_sides() -> list[str]:
    return sorted(list(VIRTUAL_ORDER_SIDES))

def list_virtual_position_statuses() -> list[str]:
    return sorted(list(VIRTUAL_POSITION_STATUSES))

def list_virtual_exit_reasons() -> list[str]:
    return sorted(list(VIRTUAL_EXIT_REASONS))

def list_paper_result_labels() -> list[str]:
    return sorted(list(PAPER_RESULT_LABELS))

def validate_virtual_order_status(label: str) -> None:
    if label not in VIRTUAL_ORDER_STATUSES:
        raise ValueError(f"Invalid virtual order status label: {label}")

def validate_virtual_order_side(label: str) -> None:
    if label not in VIRTUAL_ORDER_SIDES:
        raise ValueError(f"Invalid virtual order side label: {label}")

def validate_virtual_position_status(label: str) -> None:
    if label not in VIRTUAL_POSITION_STATUSES:
        raise ValueError(f"Invalid virtual position status label: {label}")

def validate_virtual_exit_reason(label: str) -> None:
    if label not in VIRTUAL_EXIT_REASONS:
        raise ValueError(f"Invalid virtual exit reason label: {label}")

def validate_paper_result_label(label: str) -> None:
    if label not in PAPER_RESULT_LABELS:
        raise ValueError(f"Invalid paper result label: {label}")
