import pandas as pd
import numpy as np


def calculate_group_dispersion(
    return_matrix: pd.DataFrame,
    window: int = 63,
) -> pd.DataFrame:
    """
    Calculate cross-sectional dispersion of returns.
    High dispersion means group members are behaving differently.
    """
    df = pd.DataFrame(index=return_matrix.index)
    if return_matrix.empty:
        return df

    # Cross-sectional standard deviation of returns at each time step
    # Then smoothed over the window
    cs_std = return_matrix.std(axis=1)
    dispersion = cs_std.rolling(window=window).mean()

    # We can also calculate rolling returns first, then find cross sectional std
    rolling_returns = return_matrix.rolling(window=window).apply(
        lambda x: (
            (x.iloc[-1] + 1) / (x.iloc[0] + 1) - 1
            if len(x) > 0 and x.iloc[0] != -1
            else np.nan
        ),
        raw=False,
    )
    rolling_dispersion = rolling_returns.std(axis=1)

    # Use the latter as it captures long term dispersion better
    df[f"dispersion_{window}"] = rolling_dispersion
    return df


def calculate_group_breadth(
    return_matrix: pd.DataFrame,
    window: int = 21,
) -> pd.DataFrame:
    """
    Calculate market breadth (e.g., % of members with positive returns).
    """
    df = pd.DataFrame(index=return_matrix.index)
    if return_matrix.empty:
        return df

    rolling_returns = return_matrix.rolling(window=window).apply(
        lambda x: (
            (x.iloc[-1] + 1) / (x.iloc[0] + 1) - 1
            if len(x) > 0 and x.iloc[0] != -1
            else np.nan
        ),
        raw=False,
    )

    positive_count = (rolling_returns > 0).sum(axis=1)
    valid_count = rolling_returns.notna().sum(axis=1)

    # Avoid division by zero
    breadth = np.where(valid_count > 0, positive_count / valid_count, np.nan)
    df[f"breadth_positive_{window}"] = breadth

    return df


def calculate_leader_laggard_spread(
    return_matrix: pd.DataFrame,
    window: int = 63,
) -> pd.DataFrame:
    """Calculate the return spread between the best and worst performing members."""
    df = pd.DataFrame(index=return_matrix.index)
    if return_matrix.empty or return_matrix.shape[1] < 2:
        return df

    rolling_returns = return_matrix.rolling(window=window).apply(
        lambda x: (
            (x.iloc[-1] + 1) / (x.iloc[0] + 1) - 1
            if len(x) > 0 and x.iloc[0] != -1
            else np.nan
        ),
        raw=False,
    )

    max_ret = rolling_returns.max(axis=1)
    min_ret = rolling_returns.min(axis=1)

    df[f"leader_laggard_spread_{window}"] = max_ret - min_ret
    return df


def build_dispersion_feature_frame(
    asset_class: str,
    return_matrix: pd.DataFrame,
) -> tuple[pd.DataFrame, dict]:
    """Build all dispersion features for a group."""
    summary = {"warnings": [], "asset_class": asset_class}
    features = pd.DataFrame(index=return_matrix.index)

    if return_matrix.empty:
        summary["warnings"].append(
            f"Empty return matrix for dispersion in {asset_class}"
        )
        return features, summary

    if return_matrix.shape[1] < 3:
        summary["warnings"].append(
            f"Not enough members for meaningful dispersion in {asset_class} (has {return_matrix.shape[1]})"
        )
        # Continue anyway, but maybe results are less meaningful

    dispersion = calculate_group_dispersion(return_matrix, window=63)
    breadth = calculate_group_breadth(return_matrix, window=21)
    spread = calculate_leader_laggard_spread(return_matrix, window=63)

    for col in dispersion.columns:
        features[f"group_{asset_class}_{col}"] = dispersion[col]

    for col in breadth.columns:
        features[f"group_{asset_class}_{col}"] = breadth[col]

    for col in spread.columns:
        features[f"group_{asset_class}_{col}"] = spread[col]

    # High/Low flags based on historical percentiles
    if f"group_{asset_class}_dispersion_63" in features.columns:
        disp_col = features[f"group_{asset_class}_dispersion_63"]
        rolling_rank = disp_col.rolling(window=252).apply(
            lambda x: pd.Series(x).rank(pct=True).iloc[-1] if len(x) > 0 else np.nan,
            raw=True,
        )
        features[f"group_{asset_class}_dispersion_high"] = (rolling_rank >= 0.8).astype(
            int
        )
        features[f"group_{asset_class}_dispersion_low"] = (rolling_rank <= 0.2).astype(
            int
        )

    summary["rows"] = len(features)
    summary["columns"] = list(features.columns)

    return features, summary
