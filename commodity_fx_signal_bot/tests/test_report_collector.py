import pytest
from unittest.mock import MagicMock
from notifications.report_collector import ReportCollector

def test_collect_latest_paper_summary():
    mock_lake = MagicMock()
    collector = ReportCollector(mock_lake)

    summary, _ = collector.collect_latest_paper_summary()
    assert "virtual_equity" in summary
    assert "status" in summary

def test_collect_quality_alerts():
    mock_lake = MagicMock()
    collector = ReportCollector(mock_lake)

    alerts, _ = collector.collect_quality_alerts()
    assert len(alerts) > 0
    assert alerts[0]["type"] == "missing_data"
