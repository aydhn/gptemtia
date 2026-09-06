"""Tests for Phase 132 Macro/Event/News Regime Context Manifest."""

from advanced_macro_event_news_regime.macro_event_news_regime_context_manifest import (
    create_macro_event_news_regime_context_manifest,
    build_macro_event_news_regime_context_manifest,
    summarize_macro_event_news_regime_context_manifest,
)


def test_create_manifest_object():
    obj = create_macro_event_news_regime_context_manifest(
        manifest_name="test_manifest",
        macro_entity_count=5,
        event_entity_count=5,
        news_metadata_entity_count=5,
        context_report_count=10,
        finding_count=0,
        manual_review_count=0,
        context_score=1.0,
    )
    assert obj.manifest_name == "test_manifest"
    assert obj.current_phase == 132
    assert obj.target_final_phase == 160
    assert obj.next_phase == 133
    assert obj.non_signal is True
    assert obj.contains_full_article_text is False
    assert obj.contains_embedding is False
    assert obj.sentiment_model_output is False


def test_build_macro_event_news_regime_context_manifest():
    df, summary = build_macro_event_news_regime_context_manifest()
    assert not df.empty
    assert len(df) == 1
    assert df["current_phase"].iloc[0] == 132
    assert df["next_phase"].iloc[0] == 133
    assert summary["zero_article_text"] is True
    assert summary["zero_sentiment"] is True
    assert summary["zero_ml"] is True


def test_summarize_macro_event_news_regime_context_manifest():
    df, _ = build_macro_event_news_regime_context_manifest()
    summary = summarize_macro_event_news_regime_context_manifest(df)
    assert summary["current_phase"] == 132
    assert summary["next_phase"] == 133
    assert summary["all_non_signal"] is True
