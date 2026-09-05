import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.event_release_consistency_rules import (
    build_event_release_consistency_rule_contract,
    check_event_release_consistency,
)


def test_event_release_consistency_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_event_release_consistency_rule_contract(profile)
    assert len(df_rules) >= 2

    # Revised previous without revision status
    event_df = pd.DataFrame([
        {"actual": 100, "forecast": 95, "previous": 90, "revised_previous": 92}
    ])
    findings = check_event_release_consistency(event_df, "test_p")
    assert any(f.field_name == "revised_previous" for f in findings)
