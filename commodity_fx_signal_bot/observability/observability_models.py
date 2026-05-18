"""
Data models for observability, including structured logs, health reports, and runtime metrics.
"""

import uuid
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any


@dataclass
class StructuredLogRecord:
    """A single structured log record."""
    timestamp_utc: str
    level: str
    component: str
    event_name: str
    message: str
    run_id: Optional[str] = None
    symbol: Optional[str] = None
    timeframe: Optional[str] = None
    job_id: Optional[str] = None
    error_category: Optional[str] = None
    error_code: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)


@dataclass
class ComponentHealth:
    """Health status and metrics for a specific component."""
    component: str
    status: str
    health_score: float
    checks_passed: int
    checks_failed: int
    warnings: List[str]
    errors: List[str]
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RuntimeMetric:
    """Execution time and status for a specific operation."""
    metric_id: str
    component: str
    operation: str
    started_at_utc: str
    finished_at_utc: Optional[str]
    duration_seconds: Optional[float]
    status: str
    symbol: Optional[str] = None
    timeframe: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


def build_log_record_id(record: StructuredLogRecord) -> str:
    """Build a unique identifier for a log record."""
    return f"{record.timestamp_utc}_{record.level}_{record.component}_{uuid.uuid4().hex[:8]}"


def structured_log_record_to_dict(record: StructuredLogRecord) -> Dict[str, Any]:
    """Convert a StructuredLogRecord to a dictionary."""
    return {
        "timestamp_utc": record.timestamp_utc,
        "level": record.level,
        "component": record.component,
        "event_name": record.event_name,
        "message": record.message,
        "run_id": record.run_id,
        "symbol": record.symbol,
        "timeframe": record.timeframe,
        "job_id": record.job_id,
        "error_category": record.error_category,
        "error_code": record.error_code,
        "metadata": sanitize_observability_metadata(record.metadata),
        "warnings": record.warnings,
    }


def component_health_to_dict(health: ComponentHealth) -> Dict[str, Any]:
    """Convert a ComponentHealth to a dictionary."""
    return {
        "component": health.component,
        "status": health.status,
        "health_score": health.health_score,
        "checks_passed": health.checks_passed,
        "checks_failed": health.checks_failed,
        "warnings": health.warnings,
        "errors": health.errors,
        "metadata": sanitize_observability_metadata(health.metadata),
    }


def runtime_metric_to_dict(metric: RuntimeMetric) -> Dict[str, Any]:
    """Convert a RuntimeMetric to a dictionary."""
    return {
        "metric_id": metric.metric_id,
        "component": metric.component,
        "operation": metric.operation,
        "started_at_utc": metric.started_at_utc,
        "finished_at_utc": metric.finished_at_utc,
        "duration_seconds": metric.duration_seconds,
        "status": metric.status,
        "symbol": metric.symbol,
        "timeframe": metric.timeframe,
        "metadata": sanitize_observability_metadata(metric.metadata),
    }


def sanitize_observability_metadata(metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sanitize metadata to ensure no sensitive information or un-serializable objects are included.
    Masks common secret keys (token, secret, key, password, chat_id).
    """
    if not metadata:
        return {}

    sanitized = {}
    sensitive_keys = {"token", "secret", "key", "password", "chat_id", "auth", "api_key", "credentials"}

    for k, v in metadata.items():
        k_lower = str(k).lower()

        # Check if key implies sensitive data
        if any(sensitive in k_lower for sensitive in sensitive_keys):
            sanitized[str(k)] = "********"
            continue

        # Ensure values are serializable (convert to string if not basic type)
        if isinstance(v, (str, int, float, bool, type(None))):
            sanitized[str(k)] = v
        elif isinstance(v, (list, tuple, set)):
            # Sanitize items in list-like structures
            sanitized[str(k)] = [str(item) for item in v]
        elif isinstance(v, dict):
            # Recursively sanitize nested dictionaries
            sanitized[str(k)] = sanitize_observability_metadata(v)
        else:
            # Fallback to string representation for objects
            sanitized[str(k)] = str(v)

    return sanitized
