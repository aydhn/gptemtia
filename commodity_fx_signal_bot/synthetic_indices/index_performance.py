import pandas as pd
import numpy as np
import logging
from synthetic_indices.index_models import SyntheticIndexSeries

logger = logging.getLogger(__name__)

def calculate_index_drawdown(level_series: pd.Series) -> pd.Series:
    if level_series.empty:
        return pd.Series(dtype=float)

    roll_max = level_series.cummax()
    drawdown = (level_series - roll_max) / roll_max
    return drawdown

def calculate_index_volatility(return_series: pd.Series) -> float | None:
    if return_series.empty:
        return None
    # Assuming daily returns
    vol = return_series.std()
    if pd.isna(vol):
        return None
    return float(vol * np.sqrt(252))

def calculate_index_performance(series: SyntheticIndexSeries) -> dict:
    perf = {
        "index_id": series.index_id,
        "timeframe": series.timeframe,
        "total_return_pct": None,
        "annualized_return_pct": None,
        "annualized_volatility_pct": None,
        "max_drawdown_pct": None,
        "best_period_return": None,
        "worst_period_return": None,
        "observation_count": series.observation_count
    }

    if series.level_series.empty or series.return_series.empty:
        return perf

    start_val = series.level_series.iloc[0]
    end_val = series.level_series.iloc[-1]

    if start_val > 0:
         total_ret = (end_val / start_val) - 1.0
         perf["total_return_pct"] = float(total_ret * 100)

         # Annualize
         years = series.observation_count / 252.0 # Approximation for daily
         if years > 0:
             ann_ret = (1 + total_ret) ** (1 / years) - 1.0
             perf["annualized_return_pct"] = float(ann_ret * 100)

    vol = calculate_index_volatility(series.return_series)
    if vol is not None:
         perf["annualized_volatility_pct"] = float(vol * 100)

    dd = calculate_index_drawdown(series.level_series)
    if not dd.empty:
         perf["max_drawdown_pct"] = float(dd.min() * 100)

    perf["best_period_return"] = float(series.return_series.max() * 100)
    perf["worst_period_return"] = float(series.return_series.min() * 100)

    return perf

def build_index_performance_table(index_series_map: dict[str, SyntheticIndexSeries]) -> pd.DataFrame:
    records = []
    for series in index_series_map.values():
        perf = calculate_index_performance(series)
        records.append(perf)

    return pd.DataFrame(records)

def summarize_index_performance(performance_df: pd.DataFrame) -> dict:
    summary = {
        "indices_analyzed": 0,
        "best_performing_index": None,
        "worst_performing_index": None
    }

    if performance_df.empty or "total_return_pct" not in performance_df.columns:
        return summary

    summary["indices_analyzed"] = len(performance_df)

    # Sort and find best/worst
    sorted_df = performance_df.sort_values("total_return_pct", ascending=False)
    if not sorted_df.empty:
         summary["best_performing_index"] = sorted_df.iloc[0]["index_id"]
         summary["worst_performing_index"] = sorted_df.iloc[-1]["index_id"]

    return summary
