import pytest
import pandas as pd
from pathlib import Path
from local_synthesis.master_docs_index import build_master_docs_index
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_master_docs_index():
    prof = get_default_local_synthesis_profile()
    df, summary = build_master_docs_index(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
    assert "count" in summary
