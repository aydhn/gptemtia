import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.file_timeline import classify_file_timeline_category, build_file_change_summary

def test_classify_file_timeline_category():
    assert classify_file_timeline_category(Path("scripts/a.py"), Path(".")) == "script"
    assert classify_file_timeline_category(Path("config/b.py"), Path(".")) == "config"
    assert classify_file_timeline_category(Path("core/c.py"), Path(".")) == "source"

def test_build_file_change_summary():
    df = pd.DataFrame([{"relative_path": "a.txt"}, {"relative_path": "b.txt"}])
    summary = build_file_change_summary(df)
    assert summary["total_file_events"] == 2
    assert summary["unique_files"] == 2
