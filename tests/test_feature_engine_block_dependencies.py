from advanced_feature_factor_acceptance.feature_engine_block_dependencies import (
    build_feature_engine_block_dependency_report,
    summarize_feature_engine_block_dependencies,
)

def test_feature_engine_block_dependencies():
    df, summary = build_feature_engine_block_dependency_report()
    assert not df.empty
    assert summary["all_satisfied"] is True
    assert summary["phase_start"] == 116
    assert summary["phase_end"] == 126
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    s = summarize_feature_engine_block_dependencies(df)
    assert s["total_edges"] == len(df)
    assert s["all_satisfied"] is True
    assert s["non_signal"] is True
