import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import pandas as pd
from local_timeline.timeline_report_builder import (
    build_timeline_disclaimer, build_project_event_registry_markdown_report,
    build_change_history_digest_markdown_report
)

def test_build_timeline_disclaimer():
    d = build_timeline_disclaimer()
    assert "UYARI / YASAL BİLDİRİM" in d
    assert "yatırım tavsiyesi değildir" in d

def test_build_project_event_registry_markdown_report():
    df = pd.DataFrame([{"event_id": "1"}])
    txt = build_project_event_registry_markdown_report({"total_events": 1}, df)
    assert "Project Event Registry" in txt
    assert "event_id" in txt

def test_build_change_history_digest_markdown_report():
    txt = build_change_history_digest_markdown_report({}, "My custom digest")
    assert "Change History Digest" in txt
    assert "My custom digest" in txt
