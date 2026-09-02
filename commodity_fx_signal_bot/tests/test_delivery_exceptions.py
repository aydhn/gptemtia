from local_delivery.delivery_exceptions import build_delivery_exception_register
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd

def test_build_exceptions():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_exception_register(pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
