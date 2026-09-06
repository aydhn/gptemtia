"""Test suite for Phase 126-135 Acceptance Manifest."""

from advanced_regime_acceptance.phase_126_135_acceptance_manifest import (
    build_phase_126_135_acceptance_manifest,
    create_phase_126_135_acceptance_manifest,
    summarize_phase_126_135_acceptance_manifest,
)


def test_acceptance_manifest():
    manifest = create_phase_126_135_acceptance_manifest()
    assert manifest.phase_start == 126
    assert manifest.phase_end == 135
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 136
    assert manifest.non_signal is True
    assert manifest.source_preserved is True
    assert manifest.official_approval is False
    assert manifest.production_ready is False
    assert manifest.broker_ready is False
    assert manifest.contains_target_or_prediction is False
    assert manifest.contains_trading_recommendation is False
    assert manifest.contains_full_article_text is False
    assert manifest.contains_article_body is False
    assert manifest.contains_raw_content is False
    assert manifest.contains_scraped_html is False
    assert manifest.contains_embedding is False
    assert manifest.contains_vector is False
    assert manifest.sentiment_model_output is False
    assert manifest.model_training_executed is False
    assert manifest.model_fit_executed is False
    assert manifest.model_predict_executed is False
    assert manifest.clustering_executed is False
    assert manifest.unsupervised_execution is False
    assert manifest.destructive_action_allowed is False
    assert manifest.auto_fix_allowed is False
    assert manifest.auto_drop_allowed is False

    df, summary = build_phase_126_135_acceptance_manifest()
    assert not df.empty
    assert summary["phase_start"] == 126
    assert summary["phase_end"] == 135
    assert summary["acceptance_score"] == 1.0

    s2 = summarize_phase_126_135_acceptance_manifest(df)
    assert s2["manifest_valid"] is True
    assert s2["non_signal"] is True
