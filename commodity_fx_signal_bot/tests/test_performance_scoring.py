from local_performance.performance_scoring import build_performance_readiness_score_report
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
import pandas as pd

def test_performance_scoring():
    p = get_default_local_performance_profile()
    df, s = build_performance_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
