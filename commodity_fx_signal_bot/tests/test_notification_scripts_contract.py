import pytest
import importlib

def test_scripts_importable():
    scripts = [
        "scripts.run_telegram_test_message",
        "scripts.run_telegram_paper_summary",
        "scripts.run_telegram_system_status",
        "scripts.run_telegram_daily_digest",
        "scripts.run_telegram_quality_alerts",
        "scripts.run_notification_status"
    ]

    for script in scripts:
        module = importlib.import_module(script)
        assert hasattr(module, "main")
