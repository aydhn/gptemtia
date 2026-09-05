"""Tests for Fusion Quality Handoff Assessment."""

from advanced_feature_fusion.fusion_quality_handoff import assess_fusion_quality_handoff
from advanced_feature_fusion.fusion_feature_models import FusionValidationFinding


def test_assess_quality_handoff_clean():
    res = assess_fusion_quality_handoff()
    assert res["current_phase"] == 120
    assert res["next_phase"] == 121
    assert res["readiness_score"] >= 0.45
    assert res["handoff_ready"] is True
    assert res["blocking_findings_count"] == 0


def test_assess_quality_handoff_with_blocking_finding():
    finding = FusionValidationFinding(
        finding_id="FIND-TEST",
        rule_id="VR-TEST",
        severity="CRITICAL",
        target_field="test",
        message="Critical leak detected",
        is_blocking=True,
    )
    res = assess_fusion_quality_handoff(findings=[finding])
    assert res["readiness_score"] == 0.0
    assert res["handoff_ready"] is False
    assert res["blocking_findings_count"] == 1
