from advanced_feature_factor_acceptance.phase_116_125_acceptance_manifest import (
    build_phase_116_125_acceptance_manifest,
    create_phase_116_125_acceptance_manifest,
    summarize_phase_116_125_acceptance_manifest,
)

def test_phase_116_125_acceptance_manifest():
    m = create_phase_116_125_acceptance_manifest()
    assert m.phase_start == 116
    assert m.phase_end == 125
    assert m.target_final_phase == 160
    assert m.next_phase == 126
    assert m.module_count == 10
    assert m.non_signal is True
    assert m.official_approval is False
    assert m.production_ready is False
    assert m.broker_ready is False
    assert m.source_preserved is True
    assert m.destructive_action_allowed is False
    assert m.auto_fix_allowed is False
    assert m.auto_drop_allowed is False

    df, summary = build_phase_116_125_acceptance_manifest()
    assert not df.empty
    assert summary["phase_start"] == 116
    assert summary["phase_end"] == 125
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    s = summarize_phase_116_125_acceptance_manifest(df)
    assert s["non_signal"] is True
    assert s["official_approval"] is False
