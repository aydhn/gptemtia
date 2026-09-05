import pytest
from advanced_feature_validation.feature_validation_health import check_feature_validation_health


def test_feature_validation_health():
    health = check_feature_validation_health()
    assert health["status"] == "HEALTHY"
    assert health["current_phase"] == 121
    assert health["target_final_phase"] == 160
    assert health["next_phase"] == 122
    assert "subsystems" in health
    assert len(health["subsystems"]) >= 5
