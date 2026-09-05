"""Tests for Fusion Feature Safety Boundary."""

from advanced_feature_fusion.fusion_feature_safety_boundary import (
    get_fusion_feature_no_go_rules,
    get_fusion_feature_safe_go_rules,
    validate_safety_boundary_compliance,
    get_safety_boundary_summary,
)


def test_safety_boundary_rules():
    no_go = get_fusion_feature_no_go_rules()
    safe_go = get_fusion_feature_safe_go_rules()
    assert len(no_go) >= 8
    assert len(safe_go) >= 5

    summary = get_safety_boundary_summary()
    assert summary["zero_signals"] is True
    assert summary["metadata_only_news"] is True
    assert summary["backward_only_joins"] is True
    assert summary["local_dry_run_only"] is True


def test_validate_safety_boundary_compliance():
    safe_ctx = {"is_live": False, "is_signal": False, "has_full_text": False}
    assert validate_safety_boundary_compliance(safe_ctx) is True

    unsafe_live = {"is_live": True}
    assert validate_safety_boundary_compliance(unsafe_live) is False

    unsafe_signal = {"is_signal": True}
    assert validate_safety_boundary_compliance(unsafe_signal) is False

    unsafe_scraping = {"has_full_text": True}
    assert validate_safety_boundary_compliance(unsafe_scraping) is False
