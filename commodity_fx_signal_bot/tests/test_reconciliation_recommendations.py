import pytest
import pandas as pd
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.reconciliation_recommendations import build_reconciliation_recommendations

def test_build_reconciliation_recommendations():
    profile = get_default_local_consistency_profile()
    df, summary = build_reconciliation_recommendations(pd.DataFrame(), pd.DataFrame(), profile)
    assert df is not None
