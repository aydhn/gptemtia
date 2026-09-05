from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.price_indicator_catalog import build_price_indicator_catalog


def test_price_indicator_catalog():
    profile = get_default_feature_engine_profile()
    df, summary = build_price_indicator_catalog(profile)

    assert not df.empty
    assert len(df) >= 8
    names = df["indicator_name"].tolist()
    assert "close_return" in names
    assert "log_return" in names
    assert "rolling_mean" in names
    assert "high_low_range" in names
    assert summary["all_non_signal"] is True
