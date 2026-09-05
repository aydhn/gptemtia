from advanced_feature_factor_acceptance.feature_factor_acceptance_models import (
    FeatureFactorAcceptanceProfileItem,
    FeatureEngineBlockInventoryItem,
    FeatureEngineBlockDependencyItem,
    FeatureEngineAcceptanceGate,
    FeatureEngineAcceptanceScore,
    FeatureEngineManualReviewItem,
    FeatureEngineComplianceItem,
    FeatureEngineBlockStatusItem,
    Phase116125AcceptanceManifest,
)

def test_acceptance_models():
    item = FeatureFactorAcceptanceProfileItem(
        profile_name="test_profile",
        description="test",
    )
    assert item.current_phase == 125
    assert item.non_signal is True
    assert item.official_approval is False
    assert item.production_ready is False
    assert item.broker_ready is False

    inv = FeatureEngineBlockInventoryItem(
        phase_number=116,
        module_name="advanced_feature_engine",
        package_name="advanced_feature_engine",
        description="Foundation",
        expected_scripts=9,
        expected_tests=15,
        expected_reports=6,
        expected_datalake_outputs=8,
        expected_docs=8,
        status_label="acceptance_pass",
    )
    assert inv.non_signal is True
    assert inv.source_preserved is True

    manifest = Phase116125AcceptanceManifest(
        block_name="advanced_feature_factor_engine_block",
    )
    assert manifest.phase_start == 116
    assert manifest.phase_end == 125
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 126
    assert manifest.non_signal is True
    assert manifest.official_approval is False
    assert manifest.production_ready is False
    assert manifest.broker_ready is False
    assert manifest.source_preserved is True
    assert manifest.contains_target_or_prediction is False
    assert manifest.contains_trading_recommendation is False
    assert manifest.contains_full_article_text is False
    assert manifest.destructive_action_allowed is False
    assert manifest.auto_fix_allowed is False
    assert manifest.auto_drop_allowed is False
