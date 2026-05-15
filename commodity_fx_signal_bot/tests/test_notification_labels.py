import pytest
from notifications.notification_labels import (
    list_notification_type_labels,
    list_delivery_status_labels,
    list_notification_severity_labels,
    validate_notification_type,
    validate_delivery_status,
    validate_notification_severity,
    is_alert_notification,
    is_failed_delivery
)

def test_lists_not_empty():
    assert len(list_notification_type_labels()) > 0
    assert len(list_delivery_status_labels()) > 0
    assert len(list_notification_severity_labels()) > 0

def test_validate_notification_type_passes():
    validate_notification_type("system_status")

def test_validate_delivery_status_passes():
    validate_delivery_status("delivery_sent")

def test_validate_notification_severity_passes():
    validate_notification_severity("info")

def test_is_alert_notification():
    assert is_alert_notification("quality_alert") is True
    assert is_alert_notification("system_status") is False

def test_is_failed_delivery():
    assert is_failed_delivery("delivery_failed") is True
    assert is_failed_delivery("delivery_sent") is False
