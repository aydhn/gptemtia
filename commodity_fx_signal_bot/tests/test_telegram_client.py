import pytest
from unittest.mock import patch, MagicMock
from notifications.telegram_client import TelegramClient

def test_is_configured():
    client1 = TelegramClient(None, None)
    assert not client1.is_configured()

    client2 = TelegramClient("token", "chat")
    assert client2.is_configured()

def test_send_message_not_configured():
    client = TelegramClient(None, None)
    res = client.send_message("Test")
    assert not res["success"]
    assert res["status"] == "delivery_not_configured"

@patch('requests.post')
def test_send_message_success(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"ok": True, "result": {"message_id": 123}}
    mock_post.return_value = mock_response

    client = TelegramClient("token", "chat")
    res = client.send_message("Test")
    assert res["success"]
    assert res["status"] == "delivery_sent"

def test_get_safe_destination_label():
    client = TelegramClient("token", "1234567890")
    label = client.get_safe_destination_label()
    assert "1234" in label
    assert "90" in label
    assert len(label) < 15
