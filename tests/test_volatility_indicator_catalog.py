from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.volatility_indicator_catalog import build_volatility_indicator_catalog


def test_volatility_indicator_catalog():
    profile = get_default_feature_engine_profile()
    df, summary = build_volatility_indicator_catalog(profile)

    assert not df.empty
    assert len(df) >= 7
    names = df["indicator_name"].tolist()
    assert "rolling_std" in names
    assert "ATR" in names
    assert "true_range" in names
    assert "bollinger_band_width_placeholder" in names
    assert summary["all_non_signal"] is True
