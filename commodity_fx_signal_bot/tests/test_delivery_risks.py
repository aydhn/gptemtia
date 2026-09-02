from local_delivery.delivery_risks import build_delivery_risk_summary
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd

def test_build_risks():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
