import pytest
from unittest.mock import MagicMock
from notifications.daily_digest import DailyDigestBuilder
from notifications.report_collector import ReportCollector
from notifications.notification_config import get_notification_profile

def test_daily_digest_builder():
    profile = get_notification_profile("research_digest_reporting")
    mock_lake = MagicMock()
    collector = ReportCollector(mock_lake)

    builder = DailyDigestBuilder(collector, profile)
    msg, meta = builder.build_digest()

    assert msg.notification_type == "daily_digest"
    assert msg.severity == "info"
    assert "Günlük Sistem Özeti" in msg.title
    assert "Paper Trading Portföyü" in msg.body
    assert "Backtest" in msg.body
    assert "Kalite" in msg.body
