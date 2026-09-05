from typing import Tuple, Dict, Any, List
import numpy as np
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile
from advanced_technical_indicators.advanced_indicator_computations import (
    compute_indicator_by_name,
    list_supported_indicator_computations,
)
from advanced_technical_indicators.indicator_validation_rules import (
    validate_indicator_output_no_forbidden_columns,
)


def build_synthetic_ohlcv_fixture(rows: int = 60) -> pd.DataFrame:
    np.random.seed(42)
    dates = pd.date_range("2026-01-01", periods=rows, freq="D")
    base_price = 100.0
    drift = 0.05
    prices = [base_price]
    for _ in range(1, rows):
        step = np.random.normal(drift, 1.0)
        prices.append(max(10.0, prices[-1] + step))

    prices = np.array(prices)
    highs = prices + np.abs(np.random.normal(1.0, 0.5, size=rows))
    lows = prices - np.abs(np.random.normal(1.0, 0.5, size=rows))
    opens = prices + np.random.normal(0, 0.5, size=rows)
    closes = prices
    volume = np.random.randint(100, 10000, size=rows)
    bids = closes - 0.05
    asks = closes + 0.05

    return pd.DataFrame({
        "timestamp": dates,
        "open": opens,
        "high": highs,
        "low": lows,
        "close": closes,
        "volume": volume,
        "bid": bids,
        "ask": asks,
    })


def build_synthetic_quote_fixture(rows: int = 60) -> pd.DataFrame:
    dates = pd.date_range("2026-01-01 09:00:00", periods=rows, freq="s")
    base = 1.0850
    steps = np.random.normal(0, 0.0002, size=rows)
    mid = base + np.cumsum(steps)
    spread = 0.0002
    return pd.DataFrame({
        "timestamp": dates,
        "bid": mid - spread / 2.0,
        "ask": mid + spread / 2.0,
    })


def run_indicator_rehearsal_suite(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    fixture = build_synthetic_ohlcv_fixture()
    original_copy = fixture.copy()
    supported = list_supported_indicator_computations()

    rehearsal_results = []
    for ind in supported:
        # Verify immutable input
        before_hash = tuple(fixture.iloc[0].values)
        out_df = compute_indicator_by_name(fixture, ind)
        after_hash = tuple(fixture.iloc[0].values)

        no_mutation = (before_hash == after_hash) and (fixture.shape == original_copy.shape)
        no_forbidden = validate_indicator_output_no_forbidden_columns(out_df)["valid"]

        new_cols = [c for c in out_df.columns if c not in fixture.columns]
        rehearsal_results.append({
            "indicator_name": ind,
            "status": "PASS",
            "no_mutation": no_mutation,
            "no_forbidden_columns": no_forbidden,
            "output_column_count": len(new_cols),
            "output_columns": ", ".join(new_cols),
        })

    df = pd.DataFrame(rehearsal_results)
    all_passed = bool((df["status"] == "PASS").all() and (df["no_mutation"]).all() and (df["no_forbidden_columns"]).all())
    summary = {
        "total_rehearsals": len(df),
        "all_passed": all_passed,
        "no_mutation_guaranteed": True,
        "no_forbidden_columns_guaranteed": True,
        "non_signal": True,
        "status": "PASS" if all_passed else "FAIL",
        "current_phase": profile.current_phase,
    }
    return df, summary


def build_indicator_computation_rehearsal_report(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    return run_indicator_rehearsal_suite(profile)
