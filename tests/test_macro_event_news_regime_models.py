"""Tests for Phase 132 Macro/Event/News Regime Data Models."""

from advanced_macro_event_news_regime.macro_event_news_regime_models import (
    MacroEventNewsRegimeProfileItem,
    MacroRegimeEntity,
    EventRegimeEntity,
    NewsMetadataRegimeEntity,
    MacroEventNewsContextTaxonomyItem,
    MacroEventNewsContextContract,
    MetadataOnlyNewsBoundaryItem,
    MacroEventNewsContextFinding,
    MacroEventNewsContextScore,
    MacroEventNewsRegimeManifest,
    MacroEventNewsManualReviewItem,
)


def test_models_instantiation_and_invariants():
    prof = MacroEventNewsRegimeProfileItem(
        profile_name="test_profile",
        description="test description",
    )
    assert prof.current_phase == 132
    assert prof.target_final_phase == 160
    assert prof.next_phase == 133
    assert prof.non_signal is True
    assert prof.source_preserved is True
    assert prof.official_approval is False

    entity = MacroRegimeEntity(
        entity_id="test_id",
        entity_name="test_name",
        entity_type="inflation_indicator",
        country_code="US",
        currency_code="USD",
        source_provider="BLS",
        release_frequency="monthly",
        nominal_lag_days=14,
    )
    assert entity.non_signal is True
    assert entity.source_preserved is True

    news_ent = NewsMetadataRegimeEntity(
        entity_id="test_news",
        entity_name="test news",
        entity_type="news_topic_tag",
        tag_category="topic",
        source_system="feed",
    )
    assert news_ent.contains_full_article_text is False
    assert news_ent.contains_article_body is False
    assert news_ent.sentiment_model_output is False
    assert news_ent.contains_embedding is False

    score = MacroEventNewsContextScore(
        context_score=0.95,
        classification="high_context_integrity",
        total_findings=0,
        blocker_count=0,
        warning_count=0,
        manual_review_count=0,
    )
    assert 0.0 <= score.context_score <= 1.0
    assert score.official_approval is False
    assert score.production_ready is False

    manifest = MacroEventNewsRegimeManifest(
        manifest_name="test_manifest",
    )
    assert manifest.current_phase == 132
    assert manifest.next_phase == 133
    assert manifest.non_signal is True
    assert manifest.contains_full_article_text is False
    assert manifest.sentiment_model_output is False
    assert manifest.model_training_executed is False
