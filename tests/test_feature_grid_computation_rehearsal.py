from advanced_feature_grid.feature_grid_computation_rehearsal import (
    build_feature_grid_computation_rehearsal_report,
    build_synthetic_grid_ohlcv_fixture,
    build_synthetic_grid_quote_fixture,
    run_feature_grid_rehearsal_suite,
)


def test_feature_grid_computation_rehearsal():
    ohlcv = build_synthetic_grid_ohlcv_fixture(50)
    assert len(ohlcv) == 50
    assert "close" in ohlcv.columns

    quote = build_synthetic_grid_quote_fixture(30)
    assert len(quote) == 30
    assert "bid" in quote.columns

    df, summary = run_feature_grid_rehearsal_suite()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["no_mutation_guaranteed"] is True
    assert summary["total_rehearsals"] >= 7
    assert summary["status"] == "PASS"
