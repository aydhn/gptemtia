import pandas as pd
from local_training.training_config import get_default_local_training_profile
from local_training.training_risks import build_training_risk_summary

def test_risks():
    prof = get_default_local_training_profile()
    df, sum = build_training_risk_summary(pd.DataFrame([{"gap": "1"}]), pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
