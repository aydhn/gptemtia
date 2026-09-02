from local_delivery.transfer_readiness import build_delivery_transfer_readiness_checklist
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd

def test_build_transfer_readiness():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_transfer_readiness_checklist(pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
