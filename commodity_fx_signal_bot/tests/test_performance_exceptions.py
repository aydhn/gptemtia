from local_performance.performance_exceptions import build_performance_exception_register
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
import pandas as pd

def test_performance_exceptions():
    p = get_default_local_performance_profile()
    df, s = build_performance_exception_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
