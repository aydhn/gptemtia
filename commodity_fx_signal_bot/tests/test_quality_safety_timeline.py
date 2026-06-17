import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.quality_safety_timeline import classify_quality_safety_event, build_quality_safety_activity_summary

def test_classify_quality_safety_event():
    assert classify_quality_safety_event(Path("safety/a.txt"), Path(".")) == "safety_update"
    assert classify_quality_safety_event(Path("quality/a.txt"), Path(".")) == "quality_update"

def test_build_quality_safety_activity_summary():
    df = pd.DataFrame([{"relative_path": "safety/a.txt"}])
    summary = build_quality_safety_activity_summary(df)
    assert not summary.empty
    assert summary.iloc[0]['category'] == "safety_update"
