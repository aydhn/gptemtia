import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.calendar_quality_rules import (
    build_calendar_quality_rule_set,
    check_calendar_event_quality,
    check_release_event_quality,
)


def test_calendar_quality_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_calendar_quality_rule_set(profile)
    assert len(df_rules) >= 2

    # Calendar event check
    cal_df = pd.DataFrame([{"canonical_event": "Fed Interest Rate"}])
    f_cal = check_calendar_event_quality(cal_df, "cal_test_prov")
    assert any(f.field_name == "scheduled_time" for f in f_cal)

    # Release event check
    rel_df = pd.DataFrame([{"actual": 5.25}])
    f_rel = check_release_event_quality(rel_df, "cal_test_prov")
    assert any(f.field_name == "forecast" for f in f_rel)
