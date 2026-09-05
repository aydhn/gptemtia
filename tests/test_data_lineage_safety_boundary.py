from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_lineage_safety_boundary import (
    build_data_lineage_safety_boundary,
    build_data_lineage_no_go_conditions,
    build_data_lineage_safe_go_conditions,
    summarize_data_lineage_safety_boundary,
)


def test_data_lineage_safety_boundary():
    profile = get_default_data_lineage_profile()
    no_go_df = build_data_lineage_no_go_conditions(profile)
    safe_go_df = build_data_lineage_safe_go_conditions(profile)
    assert len(no_go_df) >= 30
    assert len(safe_go_df) >= 12

    df, summary = build_data_lineage_safety_boundary(profile)
    assert len(df) == len(no_go_df) + len(safe_go_df)
    assert summary["total_no_go"] >= 30
    assert summary["total_safe_go"] >= 12
    assert summary["safety_status"] == "ACTIVE_ENFORCED"
