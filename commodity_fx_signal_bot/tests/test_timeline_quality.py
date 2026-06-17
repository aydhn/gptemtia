import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import pandas as pd
from local_timeline.timeline_quality import (
    check_for_forbidden_terms_in_timeline, check_event_registry_quality,
    build_timeline_quality_report
)
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_check_for_forbidden_terms_in_timeline():
    res = check_for_forbidden_terms_in_timeline(text="broker event stream running")
    assert not res["valid"]

def test_check_event_registry_quality():
    profile = get_default_local_timeline_profile()
    df = pd.DataFrame([{"event_id": "1", "event_type": "phase_event", "source_label": "project_files_source"}])
    q = check_event_registry_quality(df, profile)
    assert q["passed"]

def test_build_timeline_quality_report():
    df = pd.DataFrame([{"event_id": "1", "event_type": "phase_event", "source_label": "project_files_source", "text": "yatırım tavsiyesi değildir"}])
    report = build_timeline_quality_report({}, event_df=df)

    # "yatırım tavsiyesi değildir" should be filtered as false positive
    assert report["passed"]
    assert report["local_only_confirmed"]
