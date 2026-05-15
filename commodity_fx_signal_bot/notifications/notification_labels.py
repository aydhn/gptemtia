
NOTIFICATION_TYPES = [
    "test_message",
    "system_status",
    "paper_summary",
    "order_book_summary",
    "portfolio_summary",
    "backtest_summary",
    "performance_summary",
    "validation_summary",
    "ml_prediction_summary",
    "ml_integration_summary",
    "quality_alert",
    "error_alert",
    "daily_digest",
    "unknown_notification",
]

DELIVERY_STATUSES = [
    "delivery_dry_run",
    "delivery_sent",
    "delivery_failed",
    "delivery_skipped",
    "delivery_not_configured",
    "delivery_rate_limited",
    "unknown_delivery_status",
]

SEVERITIES = [
    "info",
    "warning",
    "error",
    "critical",
    "unknown",
]

def list_notification_type_labels() -> list[str]:
    return NOTIFICATION_TYPES.copy()

def list_delivery_status_labels() -> list[str]:
    return DELIVERY_STATUSES.copy()

def list_notification_severity_labels() -> list[str]:
    return SEVERITIES.copy()

def validate_notification_type(label: str) -> None:
    if label not in NOTIFICATION_TYPES:
        raise ValueError(f"Invalid notification type label: {label}")

def validate_delivery_status(label: str) -> None:
    if label not in DELIVERY_STATUSES:
        raise ValueError(f"Invalid delivery status label: {label}")

def validate_notification_severity(label: str) -> None:
    if label not in SEVERITIES:
        raise ValueError(f"Invalid severity label: {label}")

def is_alert_notification(label: str) -> bool:
    return label in ["quality_alert", "error_alert"]

def is_failed_delivery(label: str) -> bool:
    return label in ["delivery_failed", "delivery_rate_limited"]
