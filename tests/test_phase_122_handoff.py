import pytest
from advanced_feature_validation.phase_122_handoff import (
    build_phase_122_handoff_manifest,
    verify_phase_122_handoff_readiness,
)


def test_phase_122_handoff():
    manifest = build_phase_122_handoff_manifest()
    assert manifest["handoff_status"] == "READY"
    assert manifest["source_phase"] == 121
    assert manifest["target_phase"] == 122
    assert "validated_features" in manifest
    assert "validation_scores" in manifest
    assert "integrity_manifest" in manifest

    readiness = verify_phase_122_handoff_readiness()
    assert readiness["is_ready"] is True
    assert readiness["target_phase"] == 122
