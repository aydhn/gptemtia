from advanced_feature_store_integration.feature_store_integration_models import (
    FeatureStoreIntegrationProfileItem,
    FeatureStoreContract,
    FeatureStoreEntity,
    FeatureStoreFeatureRecord,
    FeatureStoreFactorRecord,
    FeatureStoreSchemaRecord,
    FeatureStoreLineageReference,
    FeatureStoreValidationStatus,
    FeatureStoreQualityScoreRecord,
    FeatureStoreDriftScoreRecord,
    FeatureStoreManualReviewBlocker,
    FeatureStoreMetadataManifest,
)

def test_models_invariants():
    m = FeatureStoreMetadataManifest(
        store_name="test_store",
        entity_count=7,
        feature_count=10,
        factor_count=6,
        validation_status_count=5,
        quality_score_count=6,
        drift_score_count=6,
        manual_review_blocker_count=4,
        source_phase_refs=[116, 117, 118],
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        manual_review_required=True,
    )
    assert m.non_signal is True
    assert m.source_preserved is True
    assert m.official_approval is False
    assert m.production_ready is False
    assert m.broker_ready is False
    assert m.contains_target_or_prediction is False
