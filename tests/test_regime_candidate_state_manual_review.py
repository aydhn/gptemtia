from advanced_regime_rule_free.regime_candidate_state_manual_review import (
    build_regime_candidate_state_manual_review_queue,
    summarize_candidate_state_manual_review_queue,
    FORBIDDEN_MANUAL_REVIEW_ACTIONS,
    MANUAL_REVIEW_QUEUE_ITEMS,
)


def test_build_regime_candidate_state_manual_review_queue():
    df, summary = build_regime_candidate_state_manual_review_queue()
    assert len(df) == 9
    assert summary["all_require_human_signoff"] is True
    assert summary["all_destructive_blocked"] is True
    assert summary["all_autofix_blocked"] is True
    assert summary["queue_status"] == "ACTIVE_NON_DESTRUCTIVE"

    assert "auto_delete" in FORBIDDEN_MANUAL_REVIEW_ACTIONS
    assert "run_clustering" in FORBIDDEN_MANUAL_REVIEW_ACTIONS
    assert "train_model" in FORBIDDEN_MANUAL_REVIEW_ACTIONS
    assert "approve_production" in FORBIDDEN_MANUAL_REVIEW_ACTIONS
