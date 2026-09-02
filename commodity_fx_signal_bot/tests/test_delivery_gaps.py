from local_delivery.delivery_gaps import build_delivery_gap_register
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd

def test_build_gaps():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_gap_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
