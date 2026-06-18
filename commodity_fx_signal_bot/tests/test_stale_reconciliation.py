import pytest
from pathlib import Path
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.stale_reconciliation import build_stale_artifact_reconciliation_plan

def test_build_stale_artifact_reconciliation_plan():
    profile = get_default_local_consistency_profile()
    df, summary = build_stale_artifact_reconciliation_plan(Path("."), profile)
    assert df is not None
