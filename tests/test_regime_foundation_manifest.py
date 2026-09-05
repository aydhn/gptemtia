from advanced_regime_foundation.regime_foundation_manifest import (
    build_regime_foundation_manifest,
    create_regime_foundation_manifest,
    summarize_regime_foundation_manifest,
)


def test_regime_foundation_manifest():
    manifest_obj = create_regime_foundation_manifest()
    assert manifest_obj.current_phase == 126
    assert manifest_obj.target_final_phase == 160
    assert manifest_obj.next_phase == 127
    assert manifest_obj.non_signal is True
    assert manifest_obj.source_preserved is True
    assert manifest_obj.official_approval is False
    assert manifest_obj.production_ready is False
    assert manifest_obj.broker_ready is False
    assert manifest_obj.model_training_executed is False
    assert manifest_obj.clustering_executed is False
    assert manifest_obj.destructive_action_allowed is False
    assert manifest_obj.auto_fix_allowed is False
    assert manifest_obj.auto_drop_allowed is False

    df, summary = build_regime_foundation_manifest()
    assert not df.empty
    assert summary["manifest_status"] == "MANIFEST_VALID"
    assert summary["current_phase"] == 126
    assert summary["next_phase"] == 127
    assert summary["target_final_phase"] == 160

    summ = summarize_regime_foundation_manifest(df)
    assert summ["manifest_status"] == "VALID"
