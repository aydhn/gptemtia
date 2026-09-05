from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.momentum_indicator_catalog import build_momentum_indicator_catalog


def test_momentum_indicator_catalog():
    profile = get_default_feature_engine_profile()
    df, summary = build_momentum_indicator_catalog(profile)

    assert not df.empty
    assert len(df) >= 6
    names = df["indicator_name"].tolist()
    assert "RSI" in names
    assert "ROC" in names
    assert "momentum" in names
    assert summary["all_non_signal"] is True
