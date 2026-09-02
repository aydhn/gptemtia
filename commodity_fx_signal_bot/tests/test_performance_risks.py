from local_performance.performance_risks import build_performance_risk_summary
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
import pandas as pd

def test_performance_risks():
    p = get_default_local_performance_profile()
    df, s = build_performance_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
