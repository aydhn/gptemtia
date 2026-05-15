import pytest
from notifications.alert_builder import build_error_alert_message
from notifications.notification_config import get_notification_profile

def test_build_error_alert_message():
    profile = get_notification_profile("balanced_telegram_reporting")
    summary = {
        "Error_Type": "DataLakeException",
        "Details": "Could not connect to storage"
    }

    msg = build_error_alert_message(summary, profile)

    assert msg.notification_type == "error_alert"
    assert msg.severity == "error"
    assert "Sistem Hata Uyarısı" in msg.title
    assert "DataLakeException" in msg.body
