from local_delivery.artifact_trace_matrix import build_delivery_artifact_trace_matrix
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd

def test_build_trace_matrix():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_artifact_trace_matrix(pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
