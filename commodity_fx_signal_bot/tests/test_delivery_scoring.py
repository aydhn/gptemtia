from local_delivery.delivery_scoring import build_delivery_readiness_score_report
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd

def test_build_scoring():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
