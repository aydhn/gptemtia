import pytest
from pathlib import Path
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.contradiction_detector import build_contradiction_detection_report, build_contradiction_rule_registry

def test_build_contradiction_rule_registry():
    df = build_contradiction_rule_registry()
    assert not df.empty

def test_build_contradiction_detection_report():
    profile = get_default_local_consistency_profile()
    df, summary = build_contradiction_detection_report(Path("."), profile)
    assert df is not None
