import pandas as pd
import numpy as np


def build_group_price_matrix(
    data_by_symbol: dict[str, pd.DataFrame],
    price_col: str = "close",
) -> pd.DataFrame:
    """Combine prices for a group of symbols into a single matrix."""
    series_list = []
    for symbol, df in data_by_symbol.items():
        if price_col in df.columns:
            s = df[price_col].rename(symbol)
            series_list.append(s)

    if not series_list:
        return pd.DataFrame()

    return pd.concat(series_list, axis=1).sort_index()


def build_group_return_matrix(
    price_matrix: pd.DataFrame,
    periods: int = 1,
) -> pd.DataFrame:
    """Calculate returns matrix from price matrix."""
    if price_matrix.empty:
        return pd.DataFrame()
    return price_matrix.pct_change(periods=periods)


def build_equal_weight_group_index(
    price_matrix: pd.DataFrame,
    base_value: float = 100.0,
) -> pd.Series:
    """Build an equal-weight group index from member prices."""
    if price_matrix.empty:
        return pd.Series(dtype=float)

    returns = build_group_return_matrix(price_matrix, periods=1)

    # Fill NA returns with 0 to maintain index continuity for available symbols
    mean_returns = returns.mean(axis=1, skipna=True).fillna(0)

    # Drop leading zeros (before any symbol had data)
    first_valid = returns.notna().any(axis=1).idxmax()
    if pd.isna(first_valid):
        return pd.Series(dtype=float)

    mean_returns = mean_returns.loc[first_valid:]

    cumulative_returns = (1 + mean_returns).cumprod()
    return cumulative_returns * base_value


def calculate_group_momentum(
    group_index: pd.Series,
    windows: tuple[int, ...] = (21, 63, 126),
) -> pd.DataFrame:
    """Calculate momentum of the group index."""
    df = pd.DataFrame(index=group_index.index)

    if group_index.empty:
        return df

    for window in windows:
        df[f"momentum_{window}"] = group_index.pct_change(periods=window)

    return df


def calculate_group_volatility(
    group_returns: pd.DataFrame,
    window: int = 63,
) -> pd.DataFrame:
    """Calculate group level volatility (mean of member volatilities)."""
    if group_returns.empty:
        return pd.DataFrame()

    # Standard deviation of returns for each member, annualized (assuming daily for default)
    # The caller specifies window. Just roll stdev.
    member_vols = group_returns.rolling(window=window).std() * np.sqrt(252)
    mean_vol = member_vols.mean(axis=1, skipna=True)

    df = pd.DataFrame(index=group_returns.index)
    df[f"volatility_{window}"] = mean_vol
    return df


def build_group_feature_frame(
    asset_class: str,
    data_by_symbol: dict[str, pd.DataFrame],
) -> tuple[pd.DataFrame, dict]:
    """Build all group level features for an asset class."""
    summary = {"warnings": [], "asset_class": asset_class}

    price_matrix = build_group_price_matrix(data_by_symbol)
    if price_matrix.empty:
        summary["warnings"].append(f"Could not build price matrix for {asset_class}")
        return pd.DataFrame(), summary

    group_index = build_group_equal_weight_index = build_equal_weight_group_index(
        price_matrix
    )
    group_returns = build_group_return_matrix(price_matrix)

    features = pd.DataFrame(index=price_matrix.index)

    features[f"group_{asset_class}_index"] = group_index

    # 1 period return
    features[f"group_{asset_class}_return_1"] = group_index.pct_change(periods=1)

    momentum = calculate_group_momentum(group_index, windows=(21, 63, 126))
    for col in momentum.columns:
        features[f"group_{asset_class}_{col}"] = momentum[col]

    volatility = calculate_group_volatility(group_returns, window=63)
    for col in volatility.columns:
        features[f"group_{asset_class}_{col}"] = volatility[col]

    # Member counts
    features[f"group_{asset_class}_member_count"] = price_matrix.shape[1]
    features[f"group_{asset_class}_valid_member_count"] = price_matrix.notna().sum(
        axis=1
    )

    summary["rows"] = len(features)
    summary["columns"] = list(features.columns)
    summary["members"] = list(price_matrix.columns)

    return features, summary
