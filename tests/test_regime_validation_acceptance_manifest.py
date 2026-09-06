"""Tests for Regime Validation Acceptance Manifest."""

from advanced_regime_validation_acceptance.regime_validation_acceptance_manifest import (
    create_regime_validation_acceptance_manifest,
    build_regime_validation_acceptance_manifest,
    summarize_regime_validation_acceptance_manifest,
)


def test_validation_acceptance_manifest():
    mani = create_regime_validation_acceptance_manifest()
    assert mani.current_phase == 133
    assert mani.target_final_phase == 160
    assert mani.next_phase == 134
    assert mani.non_signal is True
    assert mani.source_preserved is True
    assert mani.official_approval is False
    assert mani.production_ready is False
    assert mani.broker_ready is False
    assert mani.contains_full_article_text is False
    assert mani.contains_article_body is False
    assert mani.contains_raw_content is False
    assert mani.contains_scraped_html is False
    assert mani.contains_embedding is False
    assert mani.contains_vector is False
    assert mani.sentiment_model_output is False
    assert mani.model_training_executed is False
    assert mani.model_fit_executed is False
    assert mani.model_predict_executed is False
    assert mani.clustering_executed is False
    assert mani.unsupervised_execution is False

    df, summary = build_regime_validation_acceptance_manifest()
    assert not df.empty
    assert summary["current_phase"] == 133
    assert summary["next_phase"] == 134
    assert summary["target_final_phase"] == 160
    assert summary["manifest_valid"] is True

    s_df = summarize_regime_validation_acceptance_manifest(df)
    assert s_df["current_phase"] == 133
    assert s_df["non_signal"] is True
