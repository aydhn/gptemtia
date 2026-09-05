"""Tests for Fusion Feature Pipeline."""

from advanced_feature_fusion.fusion_feature_pipeline import run_fusion_feature_pipeline


def test_fusion_feature_pipeline_dry_run():
    res = run_fusion_feature_pipeline(dry_run=True)
    assert "manifest" in res
    assert "handoff" in res
    assert "summary" in res
    assert res["summary"]["status"] == "HEALTHY"
    assert res["handoff"]["handoff_ready"] is True
    assert res["manifest"]["total_rows"] == 5
    assert res["manifest"]["no_lookahead_guaranteed"] is True
    assert res["manifest"]["is_non_signal_guaranteed"] is True
