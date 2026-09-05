import pandas as pd
from advanced_feature_grid.feature_grid_computations import (
    compute_moving_average_grid,
    compute_momentum_grid,
    compute_volatility_grid,
    compute_bollinger_grid,
    compute_donchian_grid,
    compute_mean_reversion_grid,
    compute_return_grid,
    compute_feature_grid_by_name,
    list_supported_feature_grids,
    build_feature_grid_computation_module_report,
)
from advanced_feature_grid.feature_grid_computation_rehearsal import build_synthetic_grid_ohlcv_fixture
from advanced_feature_grid.feature_grid_models import FORBIDDEN_OUTPUT_WORDS


def test_feature_grid_computations_no_mutation_and_no_signals():
    df = build_synthetic_grid_ohlcv_fixture(60)
    original_cols = list(df.columns)
    original_copy = df.copy()

    # 1. Moving average grid
    df_ma = compute_moving_average_grid(df, windows=[5, 10])
    assert df.equals(original_copy)  # In-place mutation check
    assert "sma_w5" in df_ma.columns
    assert "ema_w10" in df_ma.columns

    # 2. Momentum grid
    df_mom = compute_momentum_grid(df, windows=[7, 14])
    assert df.equals(original_copy)
    assert "rsi_w7" in df_mom.columns
    assert "roc_w14" in df_mom.columns

    # 3. Volatility grid
    df_vol = compute_volatility_grid(df, windows=[7, 14])
    assert df.equals(original_copy)
    assert "atr_w7" in df_vol.columns
    assert "rolling_std_w14" in df_vol.columns

    # 4. Bollinger grid
    df_bb = compute_bollinger_grid(df, windows=[10], std_values=[2.0])
    assert df.equals(original_copy)
    assert "bb_upper_w10_std2" in df_bb.columns
    assert "bb_width_w10_std2" in df_bb.columns

    # 5. Donchian grid
    df_don = compute_donchian_grid(df, windows=[10])
    assert df.equals(original_copy)
    assert "donchian_high_w10" in df_don.columns

    # 6. Mean reversion grid
    df_mr = compute_mean_reversion_grid(df, windows=[10])
    assert df.equals(original_copy)
    assert "zscore_w10" in df_mr.columns

    # 7. Return grid
    df_ret = compute_return_grid(df, windows=[1, 5])
    assert df.equals(original_copy)
    assert "return_w1" in df_ret.columns
    assert "log_return_w5" in df_ret.columns

    # Check that none of the generated columns contain forbidden terms
    for res_df in [df_ma, df_mom, df_vol, df_bb, df_don, df_mr, df_ret]:
        new_cols = [c for c in res_df.columns if c not in original_cols]
        for c in new_cols:
            c_lower = c.lower()
            for fw in FORBIDDEN_OUTPUT_WORDS:
                assert fw not in c_lower, f"Yasaklı kelime '{fw}' kolonda bulundu: {c}"

    # Test compute by name
    df_by_name = compute_feature_grid_by_name(df, "moving_average_grid", [{"window": 5}])
    assert "sma_w5" in df_by_name.columns

    # Test module report
    df_rep, sum_rep = build_feature_grid_computation_module_report()
    assert not df_rep.empty
    assert sum_rep["total_supported_grids"] == len(list_supported_feature_grids())
