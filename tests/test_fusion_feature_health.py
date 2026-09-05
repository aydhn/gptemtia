"""Tests for Fusion Feature Health Check."""

from advanced_feature_fusion.fusion_feature_health import check_fusion_feature_health


def test_health_check():
    health = check_fusion_feature_health()
    assert health["status"] == "HEALTHY"
    assert health["phase"] == 120
    assert health["next_phase"] == 121
    assert health["checks"]["settings_enabled"] is True
    assert health["checks"]["profiles_ok"] is True
    assert health["checks"]["domains_ok"] is True
    assert health["checks"]["metadata_ok"] is True
    assert health["checks"]["contracts_ok"] is True
