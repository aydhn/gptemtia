import pytest
from unittest.mock import MagicMock
from notifications.notification_pipeline import NotificationPipeline
from notifications.notification_config import get_notification_profile
from config.settings import Settings

@pytest.fixture
def pipeline():
    mock_lake = MagicMock()
    settings = Settings()
    profile = get_notification_profile("balanced_telegram_reporting")
    # Force dry_run = True for tests
    profile = type('obj', (object,), {
        'name': 'test',
        'description': '',
        'telegram_enabled': True,
        'dry_run': True,
        'parse_mode': 'HTML',
        'message_max_chars': 3500,
        'rate_limit_seconds': 0.0,
        'include_paper_summary': True,
        'include_backtest_summary': True,
        'include_ml_summary': True,
        'include_quality_alerts': True,
        'include_error_alerts': True,
        'max_symbols_in_digest': 20,
        'max_rows_per_section': 10,
        'enabled': True,
        'notes': ''
    })()
    return NotificationPipeline(mock_lake, settings, profile)

def test_pipeline_send_test_message(pipeline):
    # Ensure it runs without error
    results, quality = pipeline.send_test_message(save=False)
    assert len(results) > 0
    assert results[0].delivery_status == "delivery_dry_run"
    assert quality["passed"] is True

def test_pipeline_send_paper_summary(pipeline):
    results, quality = pipeline.send_paper_summary(save=False)
    assert len(results) > 0

def test_pipeline_send_system_status(pipeline):
    results, quality = pipeline.send_system_status(save=False)
    assert len(results) > 0

def test_pipeline_send_daily_digest(pipeline):
    results, quality = pipeline.send_daily_digest(save=False)
    assert len(results) > 0
