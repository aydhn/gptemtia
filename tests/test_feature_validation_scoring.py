import pytest
from advanced_feature_validation.feature_validation_scoring import (
    compute_feature_validation_scores,
    get_score_grade,
    get_scoring_summary,
)


def test_feature_validation_scoring():
    scores = compute_feature_validation_scores(
        lookahead_score=1.0,
        forbidden_column_score=1.0,
        integrity_score=0.95,
        numeric_sanity_score=0.98,
        completeness_score=0.92,
    )
    assert 0.0 <= scores["overall_score"] <= 1.0
    assert scores["is_passing"] is True

    grade = get_score_grade(scores["overall_score"])
    assert grade in ["A+", "A", "B", "C", "D", "F"]

    summary = get_scoring_summary(scores)
    assert summary["current_phase"] == 121
    assert "overall_score" in summary
