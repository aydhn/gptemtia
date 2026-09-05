from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.mean_reversion_indicator_catalog import build_mean_reversion_indicator_catalog


def test_mean_reversion_indicator_catalog():
    profile = get_default_feature_engine_profile()
    df, summary = build_mean_reversion_indicator_catalog(profile)

    assert not df.empty
    assert len(df) >= 6
    names = df["indicator_name"].tolist()
    assert "zscore" in names
    assert "bollinger_zscore" in names
    assert "distance_to_sma" in names
    assert summary["all_non_signal"] is True
