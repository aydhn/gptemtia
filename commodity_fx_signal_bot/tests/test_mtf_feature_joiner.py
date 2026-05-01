import pytest
import pandas as pd
from mtf.mtf_feature_joiner import MTFFeatureJoiner
from mtf.mtf_config import get_default_mtf_profile


def test_join_feature_sets_for_timeframe():
    profile = get_default_mtf_profile()
    joiner = MTFFeatureJoiner(profile)

    df1 = pd.DataFrame({"a": [1, 2]}, index=[1, 2])
    df2 = pd.DataFrame({"b": [3, 4]}, index=[1, 2])

    res, summ = joiner.join_feature_sets_for_timeframe({"s1": df1, "s2": df2}, "1d")

    assert list(res.columns) == ["a", "b"]
    assert len(res) == 2
