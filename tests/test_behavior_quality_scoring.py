from advanced_market_behavior_diagnostics.behavior_quality_scoring import (
    calculate_behavior_quality_score,
    build_behavior_quality_score_report,
    summarize_behavior_quality_scores,
)


def test_behavior_quality_scoring():
    score_obj = calculate_behavior_quality_score()
    assert score_obj.overall_quality_score >= 0.85
    assert score_obj.quality_grade == "READY"
    assert score_obj.non_signal is True
    assert score_obj.official_approval is False
    assert score_obj.production_ready is False

    df, summary = build_behavior_quality_score_report()
    assert not df.empty
    assert summary["overall_quality_score"] == score_obj.overall_quality_score
    assert summary["quality_grade"] == score_obj.quality_grade
    assert summary["non_signal"] is True
