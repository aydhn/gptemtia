from advanced_regime_foundation.regime_foundation_models import (
    RegimeFoundationProfileItem,
    MarketBehaviorTaxonomyItem,
    RegimeStateTaxonomyItem,
    RegimeFamilyItem,
    RegimeInputFeatureContract,
    RegimeDependencyItem,
    RegimeStateOutputSchema,
    RegimeFoundationManifest,
)


def test_regime_foundation_models():
    prof_item = RegimeFoundationProfileItem(
        profile_name="test_profile",
        description="test description",
    )
    assert prof_item.current_phase == 126
    assert prof_item.target_final_phase == 160
    assert prof_item.next_phase == 127
    assert prof_item.non_signal is True
    assert prof_item.official_approval is False
    assert prof_item.production_ready is False

    beh_item = MarketBehaviorTaxonomyItem(
        behavior_id="beh_test",
        behavior_name="trending_behavior",
        behavior_category="directional",
        description="desc",
        associated_regime_family="regime_family_trend",
    )
    assert beh_item.non_signal is True
    assert beh_item.contains_trading_recommendation is False

    state_item = RegimeStateTaxonomyItem(
        state_id="state_test",
        regime_state_name="regime_state_trend_context",
        regime_family="regime_family_trend",
        state_description="desc",
        source_feature_contract="contract_trend",
        validation_dependency="val_dep",
        quality_dependency="qual_dep",
    )
    assert state_item.non_signal is True
    assert state_item.contains_target_or_prediction is False

    manifest = RegimeFoundationManifest()
    assert manifest.current_phase == 126
    assert manifest.next_phase == 127
    assert manifest.target_final_phase == 160
    assert manifest.non_signal is True
    assert manifest.source_preserved is True
    assert manifest.official_approval is False
    assert manifest.production_ready is False
    assert manifest.broker_ready is False
    assert manifest.model_training_executed is False
    assert manifest.clustering_executed is False
    assert manifest.destructive_action_allowed is False
    assert manifest.auto_fix_allowed is False
    assert manifest.auto_drop_allowed is False
