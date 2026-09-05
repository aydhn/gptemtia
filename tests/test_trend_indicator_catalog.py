from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.trend_indicator_catalog import build_trend_indicator_catalog


def test_trend_indicator_catalog():
    profile = get_default_feature_engine_profile()
    df, summary = build_trend_indicator_catalog(profile)

    assert not df.empty
    assert len(df) >= 8
    names = df["indicator_name"].tolist()
    assert "SMA" in names
    assert "EMA" in names
    assert "MACD_placeholder" in names
    assert "ADX_placeholder" in names
    assert summary["all_non_signal"] is True
