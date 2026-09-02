from local_delivery.delivery_rehearsal_binder import build_delivery_rehearsal_binder
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd

def test_build_binder():
    prof = get_default_local_delivery_profile()
    text, summary = build_delivery_rehearsal_binder({}, pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert isinstance(text, str)
