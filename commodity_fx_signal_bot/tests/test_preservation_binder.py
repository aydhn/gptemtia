import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.preservation_binder import build_long_horizon_preservation_binder

def test_preservation_binder():
    profile = get_default_local_archive_profile()
    dom = pd.DataFrame([{"1": 1}])
    item = pd.DataFrame([{"1": 1}])
    snap = pd.DataFrame([{"1": 1}])
    man = {"manifest_created_at_utc": "2024"}
    risk = pd.DataFrame([{"1": 1}])

    text, summary = build_long_horizon_preservation_binder(dom, item, snap, man, risk, profile)

    assert "Long-Horizon Preservation Binder" in text
    assert "NOT" in text
    assert "balanced_local_archive" in text
    assert summary["binder_length_chars"] > 0
