import pytest

from observability.observability_models import (
    StructuredLogRecord,
    ComponentHealth,
    RuntimeMetric,
    build_log_record_id,
    structured_log_record_to_dict,
    component_health_to_dict,
    runtime_metric_to_dict,
    sanitize_observability_metadata
)

def test_sanitize_observability_metadata():
    raw_meta = {
        "normal_val": "normal_value",
        "nested": {"api_key": "12345", "safe": 10},
        "bot_token": "abc:123",
        "chat_id": "9999",
        "list_val": [1, 2, "secret_key", 4],
        "obj_val": object()
    }

    sanitized = sanitize_observability_metadata(raw_meta)

    assert sanitized["normal_val"] == "normal_value"
    assert sanitized["bot_token"] == "********"
    assert sanitized["chat_id"] == "********"
    assert sanitized["nested"]["api_key"] == "********"
    assert sanitized["nested"]["safe"] == 10
    assert sanitized["list_val"] == ["1", "2", "secret_key", "4"]
    assert "object at" in sanitized["obj_val"]

def test_structured_log_record_to_dict():
    record = StructuredLogRecord(
        timestamp_utc="2023-01-01T00:00:00Z",
        level="INFO",
        component="test_comp",
        event_name="test_event",
        message="test msg",
        metadata={"token": "123"}
    )

    d = structured_log_record_to_dict(record)
    assert d["timestamp_utc"] == "2023-01-01T00:00:00Z"
    assert d["metadata"]["token"] == "********"

def test_component_health_to_dict():
    health = ComponentHealth(
        component="db",
        status="healthy",
        health_score=1.0,
        checks_passed=5,
        checks_failed=0,
        warnings=[],
        errors=[]
    )

    d = component_health_to_dict(health)
    assert d["component"] == "db"
    assert d["health_score"] == 1.0

def test_runtime_metric_to_dict():
    metric = RuntimeMetric(
        metric_id="m1",
        component="comp",
        operation="op",
        started_at_utc="start",
        finished_at_utc="end",
        duration_seconds=5.0,
        status="success"
    )

    d = runtime_metric_to_dict(metric)
    assert d["metric_id"] == "m1"
    assert d["duration_seconds"] == 5.0
