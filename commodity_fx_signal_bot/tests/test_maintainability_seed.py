import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.maintainability_seed import build_local_maintainability_improvement_seed

def test_build_seed():
    p = get_default_local_simplification_profile()
    text, summary = build_local_maintainability_improvement_seed(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert len(text) > 0
