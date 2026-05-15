import pytest
from notifications.notification_config import get_notification_profile
from notifications.message_formatter import MessageFormatter
from notifications.notification_models import NotificationMessage

@pytest.fixture
def formatter():
    profile = get_notification_profile("balanced_telegram_reporting")
    # For testing split, pretend max chars is small
    profile = type('obj', (object,), {
        'message_max_chars': 100,
        'parse_mode': 'HTML',
        'rate_limit_seconds': 1.0,
        'name': 'test'
    })()
    return MessageFormatter(profile)

def test_format_message_not_empty(formatter):
    msg = NotificationMessage("1", "test", "info", "Title", "Body", "now")
    res = formatter.format_message(msg)
    assert len(res) > 0
    assert "Title" in res
    assert "Body" in res

def test_split_message(formatter):
    text = "A" * 60 + "\n" + "B" * 60
    parts = formatter.split_message(text)
    assert len(parts) == 2
    assert "[Parça 1/2]" in parts[0]
    assert "[Parça 2/2]" in parts[1]

def test_html_escape(formatter):
    text = "A & B < C > D <b>Bold</b> <i>Italic</i> <code>Code</code>"
    escaped = formatter.escape_text(text)
    assert "A &amp; B &lt; C &gt; D" in escaped
    assert "<b>Bold</b>" in escaped
    assert "<i>Italic</i>" in escaped
    assert "<code>Code</code>" in escaped
