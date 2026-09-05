from typing import Tuple, Dict, Any, List, Optional
import numpy as np
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_models import FORBIDDEN_OUTPUT_WORDS
from advanced_feature_grid.feature_grid_naming import build_feature_grid_column_name, validate_feature_grid_column_name


SUPPORTED_FEATURE_GRIDS = [
    "moving_average_grid",
    "momentum_grid",
    "volatility_grid",
    "bollinger_grid",
    "donchian_grid",
    "mean_reversion_grid",
    "return_grid",
]


def list_supported_feature_grids() -> List[str]:
    return list(SUPPORTED_FEATURE_GRIDS)


def _ensure_no_forbidden_column(col_name: str) -> None:
    validation = validate_feature_grid_column_name(col_name)
    if not validation["valid"]:
        raise ValueError(f"Geçersiz veya yasaklı kolon adı: '{col_name}'. Hatalar: {validation['errors']}")


def compute_moving_average_grid(
    df: pd.DataFrame,
    field: str = "close",
    windows: Optional[List[int]] = None,
) -> pd.DataFrame:
    if field not in df.columns:
        raise ValueError(f"Alan '{field}' DataFrame içinde bulunamadı.")
    wins = windows or [5, 10, 20, 50, 100, 200]

    out = df.copy()
    for w in wins:
        # SMA
        col_sma = f"sma_w{w}"
        _ensure_no_forbidden_column(col_sma)
        out[col_sma] = out[field].rolling(window=w).mean().astype(float)

        # EMA
        col_ema = f"ema_w{w}"
        _ensure_no_forbidden_column(col_ema)
        out[col_ema] = out[field].ewm(span=w, adjust=False).mean().astype(float)

    return out


def compute_momentum_grid(
    df: pd.DataFrame,
    field: str = "close",
    windows: Optional[List[int]] = None,
) -> pd.DataFrame:
    if field not in df.columns:
        raise ValueError(f"Alan '{field}' DataFrame içinde bulunamadı.")
    wins = windows or [7, 14, 21, 28]

    out = df.copy()
    for w in wins:
        # RSI
        col_rsi = f"rsi_w{w}"
        _ensure_no_forbidden_column(col_rsi)
        delta = out[field].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(window=w).mean()
        avg_loss = loss.rolling(window=w).mean()
        rs = avg_gain / avg_loss.replace(0, np.nan)
        out[col_rsi] = (100.0 - (100.0 / (1.0 + rs))).fillna(50.0).astype(float)

        # ROC
        col_roc = f"roc_w{w}"
        _ensure_no_forbidden_column(col_roc)
        shifted = out[field].shift(w).replace(0, np.nan)
        out[col_roc] = (((out[field] - shifted) / shifted) * 100.0).astype(float)

        # Momentum
        col_mom = f"momentum_w{w}"
        _ensure_no_forbidden_column(col_mom)
        out[col_mom] = (out[field] - out[field].shift(w)).astype(float)

    return out


def compute_volatility_grid(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    windows: Optional[List[int]] = None,
) -> pd.DataFrame:
    for f in [high_field, low_field, close_field]:
        if f not in df.columns:
            raise ValueError(f"Alan '{f}' DataFrame içinde bulunamadı.")
    wins = windows or [7, 14, 20, 30]

    out = df.copy()
    prev_close = out[close_field].shift(1)
    hl = out[high_field] - out[low_field]
    hpc = np.abs(out[high_field] - prev_close)
    lpc = np.abs(out[low_field] - prev_close)
    tr = np.maximum(hl, np.maximum(hpc, lpc))

    for w in wins:
        # ATR
        col_atr = f"atr_w{w}"
        _ensure_no_forbidden_column(col_atr)
        out[col_atr] = pd.Series(tr, index=out.index).rolling(window=w).mean().astype(float)

        # Rolling Std
        col_std = f"rolling_std_w{w}"
        _ensure_no_forbidden_column(col_std)
        out[col_std] = out[close_field].rolling(window=w).std().astype(float)

        # Realized Volatility
        col_rvol = f"realized_vol_w{w}"
        _ensure_no_forbidden_column(col_rvol)
        log_ret = np.log(out[close_field] / out[close_field].shift(1).replace(0, np.nan))
        out[col_rvol] = (log_ret.rolling(window=w).std() * np.sqrt(252)).astype(float)

    return out


def compute_bollinger_grid(
    df: pd.DataFrame,
    field: str = "close",
    windows: Optional[List[int]] = None,
    std_values: Optional[List[float]] = None,
) -> pd.DataFrame:
    if field not in df.columns:
        raise ValueError(f"Alan '{field}' DataFrame içinde bulunamadı.")
    wins = windows or [10, 20, 30]
    stds = std_values or [1.5, 2.0, 2.5]

    out = df.copy()
    for w in wins:
        mid = out[field].rolling(window=w).mean()
        roll_std = out[field].rolling(window=w).std()

        for std in stds:
            std_str = str(std).replace(".", "_")
            if std_str.endswith("_0"):
                std_str = std_str[:-2]

            upper_col = f"bb_upper_w{w}_std{std_str}"
            lower_col = f"bb_lower_w{w}_std{std_str}"
            width_col = f"bb_width_w{w}_std{std_str}"
            pct_b_col = f"bb_pct_b_w{w}_std{std_str}"

            for c in [upper_col, lower_col, width_col, pct_b_col]:
                _ensure_no_forbidden_column(c)

            upper = mid + (std * roll_std)
            lower = mid - (std * roll_std)
            width = (upper - lower) / mid.replace(0, np.nan)
            diff = (upper - lower).replace(0, np.nan)
            pct_b = (out[field] - lower) / diff

            out[upper_col] = upper.astype(float)
            out[lower_col] = lower.astype(float)
            out[width_col] = width.astype(float)
            out[pct_b_col] = pct_b.astype(float)

    return out


def compute_donchian_grid(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    windows: Optional[List[int]] = None,
) -> pd.DataFrame:
    for f in [high_field, low_field, close_field]:
        if f not in df.columns:
            raise ValueError(f"Alan '{f}' DataFrame içinde bulunamadı.")
    wins = windows or [10, 20, 55]

    out = df.copy()
    for w in wins:
        high_col = f"donchian_high_w{w}"
        low_col = f"donchian_low_w{w}"
        mid_col = f"donchian_mid_w{w}"
        pos_col = f"donchian_pos_w{w}"

        for c in [high_col, low_col, mid_col, pos_col]:
            _ensure_no_forbidden_column(c)

        d_high = out[high_field].rolling(window=w).max()
        d_low = out[low_field].rolling(window=w).min()
        d_mid = (d_high + d_low) / 2.0
        d_range = (d_high - d_low).replace(0, np.nan)
        d_pos = (out[close_field] - d_low) / d_range

        out[high_col] = d_high.astype(float)
        out[low_col] = d_low.astype(float)
        out[mid_col] = d_mid.astype(float)
        out[pos_col] = d_pos.astype(float)

    return out


def compute_mean_reversion_grid(
    df: pd.DataFrame,
    field: str = "close",
    windows: Optional[List[int]] = None,
) -> pd.DataFrame:
    if field not in df.columns:
        raise ValueError(f"Alan '{field}' DataFrame içinde bulunamadı.")
    wins = windows or [10, 20, 50, 100]

    out = df.copy()
    for w in wins:
        zscore_col = f"zscore_w{w}"
        dist_sma_col = f"dist_sma_w{w}"
        dist_ema_col = f"dist_ema_w{w}"

        for c in [zscore_col, dist_sma_col, dist_ema_col]:
            _ensure_no_forbidden_column(c)

        roll_mean = out[field].rolling(window=w).mean()
        roll_std = out[field].rolling(window=w).std().replace(0, np.nan)
        roll_ema = out[field].ewm(span=w, adjust=False).mean()

        out[zscore_col] = ((out[field] - roll_mean) / roll_std).astype(float)
        out[dist_sma_col] = ((out[field] - roll_mean) / roll_mean.replace(0, np.nan)).astype(float)
        out[dist_ema_col] = ((out[field] - roll_ema) / roll_ema.replace(0, np.nan)).astype(float)

    return out


def compute_return_grid(
    df: pd.DataFrame,
    field: str = "close",
    windows: Optional[List[int]] = None,
) -> pd.DataFrame:
    if field not in df.columns:
        raise ValueError(f"Alan '{field}' DataFrame içinde bulunamadı.")
    wins = windows or [1, 3, 5, 10, 20]

    out = df.copy()
    for w in wins:
        ret_col = f"return_w{w}"
        log_ret_col = f"log_return_w{w}"

        for c in [ret_col, log_ret_col]:
            _ensure_no_forbidden_column(c)

        shifted = out[field].shift(w).replace(0, np.nan)
        out[ret_col] = ((out[field] - shifted) / shifted).astype(float)
        out[log_ret_col] = np.log(out[field] / shifted).astype(float)

    return out


def compute_feature_grid_by_name(
    df: pd.DataFrame,
    grid_name: str,
    parameter_grid: Optional[List[Dict[str, Any]]] = None,
) -> pd.DataFrame:
    name = grid_name.lower().strip()
    if name == "moving_average_grid":
        windows = [p["window"] for p in parameter_grid if "window" in p] if parameter_grid else None
        return compute_moving_average_grid(df, windows=windows)
    elif name == "momentum_grid":
        windows = [p["window"] for p in parameter_grid if "window" in p] if parameter_grid else None
        return compute_momentum_grid(df, windows=windows)
    elif name == "volatility_grid":
        windows = [p["window"] for p in parameter_grid if "window" in p] if parameter_grid else None
        return compute_volatility_grid(df, windows=windows)
    elif name == "bollinger_grid":
        windows = [p["window"] for p in parameter_grid if "window" in p] if parameter_grid else None
        stds = [p["num_std"] for p in parameter_grid if "num_std" in p] if parameter_grid else None
        return compute_bollinger_grid(df, windows=windows, std_values=stds)
    elif name == "donchian_grid":
        windows = [p["window"] for p in parameter_grid if "window" in p] if parameter_grid else None
        return compute_donchian_grid(df, windows=windows)
    elif name == "mean_reversion_grid":
        windows = [p["window"] for p in parameter_grid if "window" in p] if parameter_grid else None
        return compute_mean_reversion_grid(df, windows=windows)
    elif name == "return_grid":
        windows = [p["window"] for p in parameter_grid if "window" in p] if parameter_grid else None
        return compute_return_grid(df, windows=windows)

    raise ValueError(f"Bilinmeyen feature grid hesaplaması: '{grid_name}'. Desteklenen: {SUPPORTED_FEATURE_GRIDS}")


def build_feature_grid_computation_module_report(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []
    for g in SUPPORTED_FEATURE_GRIDS:
        rows.append({
            "grid_name": g,
            "status": "IMPLEMENTED",
            "non_signal": True,
            "framework": "pandas/numpy",
            "in_place_mutation": False,
            "ta_lib_required": False,
        })
    df = pd.DataFrame(rows)
    summary = {
        "profile": active_profile.name,
        "total_supported_grids": len(df),
        "pure_python_numpy": True,
        "ta_lib_required": False,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary
