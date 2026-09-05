from advanced_feature_factor_acceptance.feature_engine_block_inventory import (
    build_feature_engine_block_inventory_report,
    summarize_feature_engine_block_inventory,
)

def test_feature_engine_block_inventory():
    df, summary = build_feature_engine_block_inventory_report()
    assert len(df) == 10
    assert summary["total_modules"] == 10
    assert summary["all_passed"] is True
    assert summary["total_expected_scripts"] > 80
    assert summary["total_expected_tests"] > 150
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    s = summarize_feature_engine_block_inventory(df)
    assert s["module_count"] == 10
    assert s["all_passed"] is True
    assert s["non_signal"] is True
