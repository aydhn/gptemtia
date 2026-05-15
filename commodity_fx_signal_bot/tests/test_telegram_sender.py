import pytest
from unittest.mock import MagicMock
from notifications.telegram_client import TelegramClient
from notifications.message_formatter import MessageFormatter
from notifications.notification_config import get_notification_profile, NotificationProfile
from notifications.telegram_sender import TelegramSender
from notifications.notification_models import NotificationMessage

@pytest.fixture
def sender():
    client = TelegramClient("token", "chat")
    # Mock send_message to prevent actual network calls if dry_run isn't respected
    client.send_message = MagicMock(return_value={"success": True, "status": "delivery_sent"})
    profile = NotificationProfile(
        name="test",
        description="test",
        telegram_enabled=True,
        dry_run=True, # Default to dry run for safety
        parse_mode="HTML",
        message_max_chars=3500,
        rate_limit_seconds=0.0
    )
    formatter = MessageFormatter(profile)
    return TelegramSender(client, formatter, profile)

def test_dry_run_does_not_call_client(sender):
    msg = NotificationMessage("1", "test", "info", "T", "B", "now")
    res = sender.send(msg)

    assert len(res) == 1
    assert res[0].delivery_status == "delivery_dry_run"
    assert res[0].dry_run is True
    sender.client.send_message.assert_not_called()

def test_not_configured(sender):
    sender.profile = NotificationProfile(name="test", description="", dry_run=False) # Turn off dry run
    sender.client = TelegramClient(None, None) # Not configured

    msg = NotificationMessage("1", "test", "info", "T", "B", "now")
    res = sender.send(msg)

    assert len(res) == 1
    assert res[0].delivery_status == "delivery_not_configured"
