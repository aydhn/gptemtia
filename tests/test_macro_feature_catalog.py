from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.macro_feature_catalog import build_macro_feature_catalog


def test_macro_feature_catalog():
    profile = get_default_feature_engine_profile()
    df, summary = build_macro_feature_catalog(profile)

    assert not df.empty
    assert len(df) >= 4
    names = df["feature_name"].tolist()
    assert "macro_value_change" in names
    assert "macro_surprise_placeholder" in names
    assert "macro_revision_flag_placeholder" in names
    assert summary["all_non_signal"] is True
