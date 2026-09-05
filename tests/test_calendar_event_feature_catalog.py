from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.calendar_event_feature_catalog import (
    build_calendar_event_feature_catalog,
)


def test_calendar_event_feature_catalog():
    profile = get_default_feature_engine_profile()
    df, summary = build_calendar_event_feature_catalog(profile)

    assert not df.empty
    assert len(df) >= 5
    names = df["feature_name"].tolist()
    assert "event_day_flag_placeholder" in names
    assert "pre_event_window_flag_placeholder" in names
    assert "event_importance_weight_placeholder" in names
    assert summary["all_non_signal"] is True
