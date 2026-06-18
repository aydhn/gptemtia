import pytest
import pandas as pd
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.consistency_validation import build_consistency_validation_report

def test_build_consistency_validation_report():
    profile = get_default_local_consistency_profile()
    df, summary = build_consistency_validation_report({}, profile)
    assert df is not None
