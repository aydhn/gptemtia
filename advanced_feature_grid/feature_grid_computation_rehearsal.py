from typing import Tuple, Dict, Any, List
import numpy as np
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_models import FORBIDDEN_OUTPUT_WORDS
from advanced_feature_grid.feature_grid_computations import (
    compute_moving_average_grid,
    compute_momentum_grid,
    compute_volatility_grid,
    compute_bollinger_grid,
    compute_donchian_grid,
    compute_mean_reversion_grid,
    compute_return_grid,
)


def build_synthetic_grid_ohlcv_fixture(n_rows: int = 120) -> pd.DataFrame:
    np.random.seed(42)
    dates = pd.date_range("2025-01-01", periods=n_rows, freq="B")
    base_price = 100.0
    returns = np.random.normal(0.0005, 0.015, n_rows)
    close_prices = base_price * np.exp(np.cumsum(returns))

    high_prices = close_prices * (1.0 + np.abs(np.random.normal(0.005, 0.005, n_rows)))
    low_prices = close_prices * (1.0 - np.abs(np.random.normal(0.005, 0.005, n_rows)))
    open_prices = low_prices + (high_prices - low_prices) * np.random.uniform(0.2, 0.8, n_rows)
    volumes = np.random.uniform(1000, 50000, n_rows).astype(float)

    df = pd.DataFrame({
        "timestamp": dates,
        "open": open_prices,
        "high": high_prices,
        "low": low_prices,
        "close": close_prices,
        "volume": volumes,
    })
    return df


def build_synthetic_grid_quote_fixture(n_rows: int = 60) -> pd.DataFrame:
    np.random.seed(42)
    dates = pd.date_range("2025-01-01 09:30:00", periods=n_rows, freq="min")
    mid_price = 100.0 + np.cumsum(np.random.normal(0.0, 0.05, n_rows))
    half_spread = np.random.uniform(0.01, 0.05, n_rows)

    df = pd.DataFrame({
        "timestamp": dates,
        "bid": mid_price - half_spread,
        "ask": mid_price + half_spread,
        "bid_size": np.random.randint(10, 500, n_rows),
        "ask_size": np.random.randint(10, 500, n_rows),
    })
    return df


def run_feature_grid_rehearsal_suite(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    fixture = build_synthetic_grid_ohlcv_fixture(120)
    original_cols = list(fixture.columns)
    original_copy = fixture.copy()

    rehearsal_runs = [
        ("moving_average_grid", lambda df: compute_moving_average_grid(df, windows=[5, 10, 20])),
        ("momentum_grid", lambda df: compute_momentum_grid(df, windows=[7, 14, 21])),
        ("volatility_grid", lambda df: compute_volatility_grid(df, windows=[7, 14, 20])),
        ("bollinger_grid", lambda df: compute_bollinger_grid(df, windows=[10, 20], std_values=[1.5, 2.0])),
        ("donchian_grid", lambda df: compute_donchian_grid(df, windows=[10, 20])),
        ("mean_reversion_grid", lambda df: compute_mean_reversion_grid(df, windows=[10, 20])),
        ("return_grid", lambda df: compute_return_grid(df, windows=[1, 3, 5])),
    ]

    rows = []
    all_passed = True
    no_mutation_guaranteed = True

    for name, func in rehearsal_runs:
        df_input = fixture.copy()
        df_result = func(df_input)

        # Check in-place mutation
        mutated = not df_input.equals(original_copy)
        if mutated:
            no_mutation_guaranteed = False
            all_passed = False

        # Check forbidden columns
        forbidden_found = []
        new_cols = [c for c in df_result.columns if c not in original_cols]
        for col in new_cols:
            col_lower = col.lower()
            for fw in FORBIDDEN_OUTPUT_WORDS:
                if fw in col_lower:
                    forbidden_found.append(col)

        has_forbidden = len(forbidden_found) > 0
        if has_forbidden:
            all_passed = False

        warmup_nan_max = int(df_result[new_cols].isna().sum().max()) if new_cols else 0

        status = "PASS" if not mutated and not has_forbidden else "FAIL"

        rows.append({
            "rehearsal_name": name,
            "input_rows": len(fixture),
            "generated_features_count": len(new_cols),
            "in_place_mutated": mutated,
            "forbidden_columns_count": len(forbidden_found),
            "max_warmup_nan": warmup_nan_max,
            "status": status,
        })

    df = pd.DataFrame(rows)
    summary = {
        "profile": active_profile.name,
        "total_rehearsals": len(df),
        "all_passed": all_passed,
        "no_mutation_guaranteed": no_mutation_guaranteed,
        "total_features_generated": int(df["generated_features_count"].sum()),
        "non_signal": True,
        "status": "PASS" if all_passed else "FAIL",
    }
    return df, summary


def build_feature_grid_computation_rehearsal_report(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    return run_feature_grid_rehearsal_suite(profile)
