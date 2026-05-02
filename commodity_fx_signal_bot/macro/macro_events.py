from dataclasses import dataclass
from typing import Optional

import numpy as np
import pandas as pd


@dataclass
class MacroEventConfig:
    inflation_momentum_threshold: float = 0.0
    fx_depreciation_threshold_252d: float = 0.20
    real_return_threshold: float = 0.0
    confidence_threshold: float = 0.55


def detect_inflation_events(
    macro_df: pd.DataFrame, config: Optional[MacroEventConfig] = None
) -> pd.DataFrame:
    """Detect specific inflation events."""
    if config is None:
        config = MacroEventConfig()
    df = pd.DataFrame(index=macro_df.index)

    if "TR_CPI_yoy_rising" in macro_df.columns:
        df["event_macro_tr_inflation_rising"] = (
            macro_df["TR_CPI_yoy_rising"] == 1.0
        ).astype(int)
        df["event_macro_tr_inflation_falling"] = (
            macro_df["TR_CPI_yoy_falling"] == 1.0
        ).astype(int)

    if "US_CPI_yoy_rising" in macro_df.columns:
        df["event_macro_us_inflation_rising"] = (
            macro_df["US_CPI_yoy_rising"] == 1.0
        ).astype(int)
        df["event_macro_us_disinflation"] = (
            macro_df["US_CPI_yoy_falling"] == 1.0
        ).astype(int)

    return df


def detect_fx_macro_events(
    macro_df: pd.DataFrame, config: Optional[MacroEventConfig] = None
) -> pd.DataFrame:
    """Detect specific FX events."""
    if config is None:
        config = MacroEventConfig()
    df = pd.DataFrame(index=macro_df.index)

    if "usdtry_depreciation_pressure" in macro_df.columns:
        df["event_macro_try_depreciation_pressure"] = (
            macro_df["usdtry_depreciation_pressure"] == 1.0
        ).astype(int)

    if "usdtry_return_252d" in macro_df.columns:
        df["event_macro_usdtry_strong_12m"] = (
            macro_df["usdtry_return_252d"] > config.fx_depreciation_threshold_252d
        ).astype(int)

    return df


def detect_benchmark_outperformance_events(
    macro_df: pd.DataFrame, config: Optional[MacroEventConfig] = None
) -> pd.DataFrame:
    """Detect benchmark outperformance events."""
    if config is None:
        config = MacroEventConfig()
    df = pd.DataFrame(index=macro_df.index)

    # Gold vs USDTRY
    if (
        "bench_gold_try_index" in macro_df.columns
        and "bench_usdtry_index" in macro_df.columns
    ):
        gold_try = macro_df["bench_gold_try_index"]
        usdtry = macro_df["bench_usdtry_index"]
        # Check if 6m return of gold_try > 6m return of usdtry
        gold_ret = gold_try / gold_try.shift(126) - 1
        usd_ret = usdtry / usdtry.shift(126) - 1
        df["event_macro_gold_outperforming_usdtry"] = (gold_ret > usd_ret).astype(int)
        df.loc[
            gold_ret.isna() | usd_ret.isna(), "event_macro_gold_outperforming_usdtry"
        ] = np.nan

    if "real_gold_try_vs_tr_cpi" in macro_df.columns:
        idx_series = macro_df["real_gold_try_vs_tr_cpi"]
        ret = idx_series / idx_series.shift(126) - 1
        df["event_macro_gold_real_positive"] = (
            ret > config.real_return_threshold
        ).astype(int)
        df.loc[ret.isna(), "event_macro_gold_real_positive"] = np.nan

    if "real_equal_commodity_vs_tr_cpi" in macro_df.columns:
        idx_series = macro_df["real_equal_commodity_vs_tr_cpi"]
        ret = idx_series / idx_series.shift(126) - 1
        df["event_macro_commodity_basket_real_positive"] = (
            ret > config.real_return_threshold
        ).astype(int)
        df.loc[ret.isna(), "event_macro_commodity_basket_real_positive"] = np.nan

    return df


def detect_macro_regime_events(
    macro_df: pd.DataFrame, config: Optional[MacroEventConfig] = None
) -> pd.DataFrame:
    """Detect regime-based events."""
    if config is None:
        config = MacroEventConfig()
    df = pd.DataFrame(index=macro_df.index)

    if (
        "macro_primary_label" in macro_df.columns
        and "macro_confidence" in macro_df.columns
    ):
        confident = macro_df["macro_confidence"] > config.confidence_threshold

        is_high_inf_fx = (
            macro_df["macro_primary_label"] == "high_local_inflation_fx_pressure"
        )
        df["event_macro_high_local_inflation_fx_pressure"] = (
            is_high_inf_fx & confident
        ).astype(int)

        # Add conflict
        is_conflict = macro_df["macro_primary_label"] == "conflicting_macro"
        df["event_macro_conflicting"] = (is_conflict & confident).astype(int)

    return df


def build_macro_event_frame(
    macro_df: pd.DataFrame, config: Optional[MacroEventConfig] = None
) -> tuple[pd.DataFrame, dict]:
    """Build the complete macro event frame."""
    if macro_df.empty:
        return pd.DataFrame(), {"error": "Empty macro dataframe"}

    if config is None:
        config = MacroEventConfig()

    result = pd.DataFrame(index=macro_df.index)

    events = [
        detect_inflation_events(macro_df, config),
        detect_fx_macro_events(macro_df, config),
        detect_benchmark_outperformance_events(macro_df, config),
        detect_macro_regime_events(macro_df, config),
    ]

    for df in events:
        if not df.empty:
            result = pd.concat([result, df], axis=1)

    summary = {
        "rows": len(result),
        "columns": list(result.columns),
        "events_count": sum(1 for c in result.columns if c.startswith("event_")),
    }

    return result, summary
