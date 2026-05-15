import pytest
import pandas as pd
from notifications.status_summary_builder import build_system_status_message
from notifications.notification_config import get_notification_profile

def test_build_system_status_message():
    profile = get_notification_profile("balanced_telegram_reporting")
    summary = {
        "Status": "Running",
        "Telegram_Token": "123456789:ABCDEF", # Should be hidden by key name check
        "API_Secret": "supersecret"
    }

    msg = build_system_status_message(summary, profile)

    assert msg.notification_type == "system_status"
    assert "Sistem Durum Özeti" in msg.title
    assert "Status" in msg.body
    assert "Telegram_Token" not in msg.body # Hidden
    assert "123456789:ABCDEF" not in msg.body
