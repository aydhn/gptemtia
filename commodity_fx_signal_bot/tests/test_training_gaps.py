import pandas as pd
from local_training.training_config import get_default_local_training_profile
from local_training.training_gaps import build_training_gap_register

def test_gaps():
    prof = get_default_local_training_profile()
    df, sum = build_training_gap_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
