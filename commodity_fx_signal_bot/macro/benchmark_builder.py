from dataclasses import dataclass
from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd


@dataclass
class BenchmarkSpec:
    code: str
    name: str
    type: str
    components: tuple[str, ...]
    base_currency: str = "TRY"
    rebalance: str = "monthly"
    enabled: bool = True
    notes: str = ""


def build_price_return_index(
    price_series: pd.Series, base_value: float = 100.0
) -> pd.Series:
    """Build a normalized price return index."""
    if price_series.empty or price_series.dropna().empty:
        return pd.Series(index=price_series.index, dtype=float)

    first_valid = price_series.dropna().iloc[0]
    if first_valid == 0:
        # Avoid division by zero
        return pd.Series(index=price_series.index, dtype=float)

    idx = (price_series / first_valid) * base_value
    return idx


def build_equal_weight_basket(
    price_frames: Dict[str, pd.Series], base_value: float = 100.0
) -> pd.Series:
    """Build an equal-weight basket index from multiple price series."""
    if not price_frames:
        return pd.Series(dtype=float)

    # Align all series
    df = pd.DataFrame(price_frames)

    # Calculate daily returns for each component
    returns = df.pct_change()
    returns = returns.replace([np.inf, -np.inf], np.nan)

    # Average daily returns
    avg_return = returns.mean(axis=1, skipna=True)

    # Reconstruct index
    # Cumprod of (1 + return) * base_value
    idx = (1 + avg_return.fillna(0)).cumprod() * base_value

    # Set pre-first-valid values to NaN if they were completely NaN
    mask = df.notna().any(axis=1)
    # But cumprod will make everything non-NaN after the first 0, so we just use the starting index
    if not mask.empty:
        first_valid_idx = mask.idxmax()
        if not pd.isna(first_valid_idx):
            idx.loc[:first_valid_idx] = base_value  # the starting point is 100

    return idx


def convert_usd_asset_to_try(asset_usd: pd.Series, usdtry: pd.Series) -> pd.Series:
    """Convert a USD-denominated asset to TRY terms."""
    df = pd.DataFrame({"asset": asset_usd, "usdtry": usdtry})
    df["usdtry"] = df["usdtry"].ffill()  # Forward fill USDTRY
    return df["asset"] * df["usdtry"]


def build_inflation_index(
    cpi_series: pd.Series, base_value: float = 100.0
) -> pd.Series:
    """Build an inflation index normalized to base_value."""
    return build_price_return_index(cpi_series, base_value)


def calculate_real_return_index(
    nominal_index: pd.Series, inflation_index: pd.Series
) -> pd.Series:
    """Calculate real return index by deflating nominal index with inflation index."""
    df = pd.DataFrame({"nominal": nominal_index, "inflation": inflation_index})
    df["inflation"] = df[
        "inflation"
    ].ffill()  # Inflation might be monthly, nominal daily

    # Real return index = Nominal Index / (Inflation Index / 100)
    # Avoid division by zero
    real_idx = df["nominal"] / (df["inflation"] / 100.0).replace(0, np.nan)
    return real_idx


def build_benchmark_frame(inputs: Dict[str, pd.Series]) -> Tuple[pd.DataFrame, dict]:
    """Build the full benchmark frame using provided input series."""
    summary = {"errors": [], "processed": []}

    # Find the union of all indices to align
    all_dates = set()
    for s in inputs.values():
        if not s.empty:
            all_dates.update(s.index)

    if not all_dates:
        return pd.DataFrame(), {"error": "No input data provided"}

    date_idx = pd.DatetimeIndex(sorted(list(all_dates)))
    result = pd.DataFrame(index=date_idx)

    # Align all inputs to this index
    aligned = {k: v.reindex(date_idx) for k, v in inputs.items()}

    if "USDTRY" in aligned:
        result["bench_usdtry_index"] = build_price_return_index(
            aligned["USDTRY"].ffill()
        )
        summary["processed"].append("bench_usdtry_index")

    if "GOLD_USD" in aligned:
        result["bench_gold_usd_index"] = build_price_return_index(
            aligned["GOLD_USD"].ffill()
        )
        summary["processed"].append("bench_gold_usd_index")

    if "GOLD_USD" in aligned and "USDTRY" in aligned:
        gold_try = convert_usd_asset_to_try(aligned["GOLD_USD"], aligned["USDTRY"])
        result["bench_gold_try_index"] = build_price_return_index(gold_try.ffill())
        summary["processed"].append("bench_gold_try_index")

    # Commodity Basket (Gold, Oil)
    comm_components = {}
    if "GOLD_USD" in aligned:
        comm_components["gold"] = aligned["GOLD_USD"]
    if "OIL_WTI" in aligned:
        comm_components["oil"] = aligned["OIL_WTI"]

    if comm_components:
        result["bench_equal_commodity_index"] = build_equal_weight_basket(
            comm_components
        )
        summary["processed"].append("bench_equal_commodity_index")

    # CPI Indices
    if "TR_CPI" in aligned:
        result["bench_tr_cpi_index"] = build_inflation_index(aligned["TR_CPI"].ffill())
        summary["processed"].append("bench_tr_cpi_index")

    if "US_CPI" in aligned:
        result["bench_us_cpi_index"] = build_inflation_index(aligned["US_CPI"].ffill())
        summary["processed"].append("bench_us_cpi_index")

    # Real Returns vs TR_CPI
    if "TR_CPI" in aligned:
        cpi_idx = result.get("bench_tr_cpi_index")
        if cpi_idx is not None:
            if "bench_gold_try_index" in result:
                result["real_gold_try_vs_tr_cpi"] = calculate_real_return_index(
                    result["bench_gold_try_index"], cpi_idx
                )
                summary["processed"].append("real_gold_try_vs_tr_cpi")

            if "bench_usdtry_index" in result:
                result["real_usdtry_vs_tr_cpi"] = calculate_real_return_index(
                    result["bench_usdtry_index"], cpi_idx
                )
                summary["processed"].append("real_usdtry_vs_tr_cpi")

            if "bench_equal_commodity_index" in result and "USDTRY" in aligned:
                # Need commodity basket in TRY to compare against TR CPI
                comm_try = convert_usd_asset_to_try(
                    result["bench_equal_commodity_index"], aligned["USDTRY"]
                )
                comm_try_idx = build_price_return_index(comm_try.ffill())
                result["real_equal_commodity_vs_tr_cpi"] = calculate_real_return_index(
                    comm_try_idx, cpi_idx
                )
                summary["processed"].append("real_equal_commodity_vs_tr_cpi")

    summary["rows"] = len(result)
    summary["columns"] = list(result.columns)

    return result, summary
