from advanced_feature_factor_acceptance.feature_engine_block_status import (
    build_feature_engine_block_status_report,
    summarize_feature_engine_block_status,
)

def test_feature_engine_block_status():
    df, summary = build_feature_engine_block_status_report()
    assert not df.empty
    assert summary["phase_start"] == 116
    assert summary["phase_end"] == 125
    assert summary["overall_status"] == "ACCEPTANCE_PASS"
    assert summary["total_modules"] == 10
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    s = summarize_feature_engine_block_status(df)
    assert s["overall_status"] == "ACCEPTANCE_PASS"
    assert s["non_signal"] is True
