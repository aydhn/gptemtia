import pytest
import pandas as pd
import numpy as np
from advanced_feature_validation.warmup_nan_validation import validate_warmup_nans


def test_warmup_nan_validation():
    # Warmup NaNs should be preserved at the beginning and NOT auto-dropped
    df_valid = pd.DataFrame({
        "timestamp": range(10),
        "feat_sma_5": [np.nan, np.nan, np.nan, np.nan, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5],
    })
    res_valid = validate_warmup_nans(df_valid, warmup_window=4)
    assert res_valid["is_valid"] is True
    assert res_valid["warmup_nan_preserved"] is True
    assert res_valid["destructive_action_allowed"] is False

    # NaNs appearing after warmup period indicates potential issue
    df_unexpected_nans = pd.DataFrame({
        "timestamp": range(10),
        "feat_sma_5": [np.nan, np.nan, np.nan, np.nan, 10.0, np.nan, 11.0, 11.5, 12.0, 12.5],
    })
    res_unexpected = validate_warmup_nans(df_unexpected_nans, warmup_window=4)
    assert res_unexpected["is_valid"] is False
    assert res_unexpected["unexpected_post_warmup_nans"] > 0
