from advanced_feature_grid.feature_grid_safety_boundary import (
    build_feature_grid_safety_boundary,
    build_feature_grid_no_go_conditions,
    build_feature_grid_safe_go_conditions,
    summarize_feature_grid_safety_boundary,
)


def test_feature_grid_safety_boundary():
    df_no_go = build_feature_grid_no_go_conditions()
    assert len(df_no_go) >= 15
    assert (df_no_go["boundary_type"] == "NO_GO").all()

    df_safe_go = build_feature_grid_safe_go_conditions()
    assert len(df_safe_go) >= 5
    assert (df_safe_go["boundary_type"] == "SAFE_GO").all()

    df_all, summary = build_feature_grid_safety_boundary()
    assert summary["total_conditions"] == len(df_no_go) + len(df_safe_go)
    assert summary["safety_status"] == "ACTIVE"
    assert summary["strict_boundaries_enforced"] is True
