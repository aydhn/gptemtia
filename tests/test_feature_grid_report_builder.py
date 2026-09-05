from advanced_feature_grid.feature_grid_report_builder import (
    build_feature_grid_disclaimer,
    build_feature_grid_profile_markdown_report,
    build_window_grid_contract_markdown_report,
    build_parameter_grid_markdown_report,
    build_feature_grid_family_markdown_report,
    build_feature_grid_rehearsal_markdown_report,
    build_feature_grid_validation_markdown_report,
    build_feature_grid_health_markdown_report,
    build_feature_grid_safety_markdown_report,
    build_phase_119_handoff_markdown_report,
)


def test_feature_grid_report_builder():
    disc = build_feature_grid_disclaimer()
    assert "Phase 118" in disc
    assert "yatırım tavsiyesi" in disc
    assert "AL/SAT" in disc

    sum_prof = {"active_profile": "test", "total_profiles": 1, "current_phase": 118, "status": "READY"}
    rep_prof = build_feature_grid_profile_markdown_report(sum_prof)
    assert "Phase 118: Multi-Window Feature Grid Profile Report" in rep_prof
    assert disc in rep_prof

    sum_wgc = {"total_contracts": 1, "status": "READY"}
    rep_wgc = build_window_grid_contract_markdown_report(sum_wgc)
    assert "Window Grid Contracts Report" in rep_wgc

    sum_param = {"total_grids": 1, "status": "READY"}
    rep_param = build_parameter_grid_markdown_report(sum_param)
    assert "Indicator Parameter Grid Registry Report" in rep_param

    sum_reh = {"total_rehearsals": 1, "all_passed": True, "status": "PASS"}
    rep_reh = build_feature_grid_rehearsal_markdown_report(sum_reh)
    assert "Feature Grid Computation Rehearsal Report" in rep_reh

    sum_val = {"validation_status": "PASS", "rules_checked": 10, "violations_count": 0}
    rep_val = build_feature_grid_validation_markdown_report(sum_val)
    assert "Feature Grid Validation Report" in rep_val

    sum_h = {"health_status": "HEALTHY", "total_components": 5}
    rep_h = build_feature_grid_health_markdown_report(sum_h)
    assert "Health Check Report" in rep_h

    sum_s = {"safety_status": "ACTIVE", "total_no_go": 16}
    rep_s = build_feature_grid_safety_markdown_report(sum_s)
    assert "Feature Grid Safety Boundary Report" in rep_s

    sum_ho = {"handoff_status": "READY", "total_handoff_items": 5, "next_phase": 119}
    rep_ho = build_phase_119_handoff_markdown_report(sum_ho)
    assert "Phase 119 Cross-Asset Feature Alignment Handoff Report" in rep_ho
