import pytest
import pandas as pd
from notifications.paper_summary_builder import build_paper_summary_message
from notifications.notification_config import get_notification_profile

def test_build_paper_summary_message():
    profile = get_notification_profile("balanced_telegram_reporting")
    summary = {
        "virtual_equity": 10000.0,
        "virtual_return": 0.05
    }

    msg = build_paper_summary_message(summary, profile)

    assert msg.notification_type == "paper_summary"
    assert msg.severity == "info"
    assert "Sanal Portföy" in msg.title
    assert "virtual_equity" in msg.body
    assert "gerçek emir" in msg.body # From disclaimer
