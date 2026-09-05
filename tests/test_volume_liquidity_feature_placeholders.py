from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.volume_liquidity_feature_placeholders import (
    build_volume_liquidity_feature_placeholder_catalog,
)


def test_volume_liquidity_feature_placeholders():
    profile = get_default_feature_engine_profile()
    df, summary = build_volume_liquidity_feature_placeholder_catalog(profile)

    assert not df.empty
    assert len(df) >= 4
    names = df["feature_name"].tolist()
    assert "volume_change_placeholder" in names
    assert "rolling_volume_mean_placeholder" in names
    assert "volume_zscore_placeholder" in names
    assert summary["all_non_signal"] is True
