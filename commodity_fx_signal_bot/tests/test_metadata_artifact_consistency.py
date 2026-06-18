import pytest
from pathlib import Path
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.metadata_artifact_consistency import build_metadata_artifact_consistency_report

def test_build_metadata_artifact_consistency_report():
    profile = get_default_local_consistency_profile()
    df, summary = build_metadata_artifact_consistency_report(Path("."), profile)
    assert df is not None
