import pytest
import pandas as pd
from local_synthesis.cross_phase_final_map import build_cross_phase_final_map
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_cross_phase_final_map():
    prof = get_default_local_synthesis_profile()
    df, summary = build_cross_phase_final_map(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert isinstance(df, pd.DataFrame)
