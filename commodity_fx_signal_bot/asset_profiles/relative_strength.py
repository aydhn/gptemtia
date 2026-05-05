import pandas as pd
import numpy as np


def calculate_relative_strength_vs_group(
    symbol_series: pd.Series,
    group_index: pd.Series,
    windows: tuple[int, ...] = (21, 63, 126, 252),
) -> pd.DataFrame:
    """Calculate relative strength of a symbol vs its group index."""
    df = pd.DataFrame(index=symbol_series.index)

    if symbol_series.empty or group_index.empty:
        return df

    for window in windows:
        symbol_ret = symbol_series.pct_change(periods=window)
        group_ret = group_index.pct_change(periods=window)
        # Relative strength is ratio of symbol return to group return
        # Simple difference is often more robust when returns are near zero
        rs = symbol_ret - group_ret
        df[f"rs_vs_group_{window}"] = rs

    return df


def calculate_relative_strength_rank(
    return_matrix: pd.DataFrame,
    window: int = 63,
) -> pd.DataFrame:
    """Calculate the cross-sectional rank of returns within the group."""
    if return_matrix.empty:
        return pd.DataFrame()

    rolling_returns = return_matrix.rolling(window=window).apply(
        lambda x: (
            (x.iloc[-1] + 1) / (x.iloc[0] + 1) - 1
            if len(x) > 0 and x.iloc[0] != -1
            else np.nan
        ),
        raw=False,
    )

    # 1 is best, n is worst
    ranks = rolling_returns.rank(axis=1, ascending=False, pct=False)
    # 1.0 is best, 0.0 is worst
    percentiles = rolling_returns.rank(axis=1, ascending=True, pct=True)

    return ranks, percentiles


def calculate_cross_asset_relative_strength(
    group_indices: dict[str, pd.Series],
    window: int = 63,
) -> pd.DataFrame:
    """Calculate relative strength between different asset classes."""
    df = pd.DataFrame()
    if not group_indices:
        return df

    idx_df = pd.DataFrame(group_indices)
    returns = idx_df.pct_change(periods=window)

    # Calculate ranks across asset classes
    ranks = returns.rank(axis=1, ascending=False)
    return ranks


def build_relative_strength_features(
    symbol: str,
    symbol_df: pd.DataFrame,
    group_index: pd.Series | None,
    return_matrix: pd.DataFrame | None,
) -> tuple[pd.DataFrame, dict]:
    """Build all relative strength features for a symbol."""
    features = pd.DataFrame(index=symbol_df.index)
    summary = {"warnings": []}

    if symbol_df.empty:
        return features, summary

    if group_index is None or group_index.empty:
        summary["warnings"].append(
            f"No group index provided for RS calculation for {symbol}"
        )
        return features, summary

    price_col = "close"
    if price_col not in symbol_df.columns:
        summary["warnings"].append(f"Price column '{price_col}' missing for {symbol}")
        return features, summary

    rs_vs_group = calculate_relative_strength_vs_group(
        symbol_df[price_col], group_index, windows=(21, 63, 126, 252)
    )
    features = pd.concat([features, rs_vs_group], axis=1)

    if return_matrix is not None and not return_matrix.empty:
        ranks, percentiles = calculate_relative_strength_rank(return_matrix, window=63)
        if symbol in ranks.columns:
            features["rs_rank_group_63"] = ranks[symbol]
            features["rs_percentile_group_63"] = percentiles[symbol]

            # Leaders are in top 20%, laggards in bottom 20%
            features["rs_is_group_leader"] = (percentiles[symbol] >= 0.8).astype(int)
            features["rs_is_group_laggard"] = (percentiles[symbol] <= 0.2).astype(int)
        else:
            summary["warnings"].append(
                f"Symbol {symbol} missing from return matrix for ranks"
            )

    summary["rows"] = len(features)
    summary["columns"] = list(features.columns)

    return features, summary
