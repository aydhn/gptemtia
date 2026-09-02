from local_delivery.delivery_validation import build_delivery_validation_report
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd

def test_build_validation():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_validation_report({"test": pd.DataFrame()}, prof)
    assert not df.empty
