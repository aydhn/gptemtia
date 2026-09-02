
from pathlib import Path
import pandas as pd
from local_closure.closure_exceptions import build_closure_exception_register
from local_closure.closure_config import get_default_local_closure_profile

def test_exc():
    p = get_default_local_closure_profile()
    df, summary = build_closure_exception_register(Path.cwd(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
