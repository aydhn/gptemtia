import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
import json
from local_timeline.timeline_export import (
    validate_timeline_export_safety, build_timeline_export_manifest,
    export_timeline_to_json, export_timeline_to_csv, summarize_timeline_export
)
from local_timeline.timeline_config import LocalTimelineProfile, get_default_local_timeline_profile

def test_validate_timeline_export_safety():
    profile = LocalTimelineProfile(name="test", description="desc", language="tr", allow_cloud_upload=True)
    manifest = validate_timeline_export_safety({}, profile)
    assert not manifest["safety_validated"]
    assert "cloud_upload_should_be_false" in manifest["safety_warnings"]

def test_build_timeline_export_manifest():
    df = pd.DataFrame([{"a": 1}])
    profile = get_default_local_timeline_profile()
    manifest = build_timeline_export_manifest(df, df, df, profile)
    assert manifest["total_events"] == 1
    assert manifest["safety_validated"]

def test_export_timeline_to_json(tmp_path):
    df = pd.DataFrame([{"a": 1}])
    out = tmp_path / "out.json"
    export_timeline_to_json(df, pd.DataFrame(), pd.DataFrame(), out)
    assert out.exists()
    with open(out) as f:
        data = json.load(f)
        assert "events" in data

def test_export_timeline_to_csv(tmp_path):
    df = pd.DataFrame([{"a": 1}])
    paths = export_timeline_to_csv(df, df, df, tmp_path)
    assert "events" in paths
    assert paths["events"].exists()
