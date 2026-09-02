import pandas as pd
from local_dr.dr_config import get_default_local_dr_profile
from local_dr.failure_mode_registry import build_failure_mode_registry, build_default_failure_modes, classify_failure_severity, summarize_failure_modes

def test_failure_mode_registry():
    profile = get_default_local_dr_profile()
    
    modes = build_default_failure_modes(profile)
    assert len(modes) == 1
    
    assert classify_failure_severity("Corruption", "archive_restore_dr") == "high"
    assert classify_failure_severity("Other", "archive_restore_dr") == "medium"
    
    df, summary = build_failure_mode_registry(profile)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert summary["total_failures"] == 1
    assert summary["high_severity_failures"] == 1
