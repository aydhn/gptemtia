import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.optional_slimming_plan import build_optional_slimming_plan

def test_build_optional_slimming_plan():
    p = get_default_local_simplification_profile()
    df, summary = build_optional_slimming_plan(pd.DataFrame(), pd.DataFrame(), p)
    assert df is not None
    assert len(summary["warnings"]) > 0
