import pytest
from datetime import datetime, timezone
from notifications.notification_models import (
    NotificationMessage,
    DeliveryResult,
    build_notification_message_id,
    notification_message_to_dict,
    delivery_result_to_dict,
    sanitize_sensitive_text,
    sanitize_metadata
)

def test_build_notification_message_id_deterministic():
    id1 = build_notification_message_id("test", "Test", "2024-01-01T00:00:00Z")
    id2 = build_notification_message_id("test", "Test", "2024-01-01T00:00:00Z")
    assert id1 == id2
    assert id1.startswith("msg_")

def test_message_delivery_to_dict():
    created = datetime.now(timezone.utc).isoformat()
    msg = NotificationMessage(
        message_id="msg_123",
        notification_type="test",
        severity="info",
        title="Test",
        body="Body",
        created_at_utc=created,
        metadata={"secret_key": "12345"}
    )
    d = notification_message_to_dict(msg)
    assert d["message_id"] == "msg_123"
    assert d["metadata"]["secret_key"] == "***MASKED***"

    res = DeliveryResult(
        message_id="msg_123",
        delivery_status="sent",
        dry_run=True,
        destination="dest",
        sent_at_utc=created,
        error_message=None
    )
    r = delivery_result_to_dict(res)
    assert r["message_id"] == "msg_123"
    assert r["dry_run"] is True

def test_sanitize_sensitive_text():
    text = "Here is a token 123456789:ABCdefGHIjklMNOpqrsTUVwxyz123456789"
    sanitized = sanitize_sensitive_text(text)
    assert "***TOKEN***" in sanitized
    assert "123456789:" not in sanitized

def test_sanitize_metadata():
    meta = {"api_token": "12345", "normal_key": "value"}
    sanitized = sanitize_metadata(meta)
    assert sanitized["api_token"] == "***MASKED***"
    assert sanitized["normal_key"] == "value"
