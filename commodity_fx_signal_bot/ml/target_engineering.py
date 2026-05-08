import pandas as pd
import numpy as np
from .dataset_config import MLDatasetProfile
from .dataset_labels import DIR_UP, DIR_DOWN, DIR_FLAT, DIR_UNKNOWN, OUTCOME_POSITIVE, OUTCOME_NEGATIVE, OUTCOME_NEUTRAL, OUTCOME_INVALID, OUTCOME_UNKNOWN

def calculate_forward_return(close: pd.Series, horizon: int) -> pd.Series:
    """Calculate future percentage return over a given horizon."""
    if horizon <= 0:
        raise ValueError("Horizon must be positive")
    shifted = close.shift(-horizon)
    return (shifted - close) / close

def calculate_forward_log_return(close: pd.Series, horizon: int) -> pd.Series:
    """Calculate future log return over a given horizon."""
    if horizon <= 0:
        raise ValueError("Horizon must be positive")
    shifted = close.shift(-horizon)
    return np.log(shifted / close)

def calculate_direction_class(forward_return: pd.Series, threshold: float = 0.002) -> pd.Series:
    """Classify return into UP, DOWN, or FLAT based on a threshold."""
    direction = pd.Series(index=forward_return.index, dtype='object')
    direction.loc[forward_return > threshold] = DIR_UP
    direction.loc[forward_return < -threshold] = DIR_DOWN
    direction.loc[(forward_return >= -threshold) & (forward_return <= threshold)] = DIR_FLAT

    # Handle NaNs
    direction[forward_return.isna()] = DIR_UNKNOWN
    return direction

def calculate_binary_return_target(forward_return: pd.Series, positive_threshold: float = 0.005, negative_threshold: float = -0.005) -> pd.Series:
    """Create a binary target. 1 if return > pos_thresh, 0 if return < neg_thresh, else NaN (ignored)."""
    binary = pd.Series(index=forward_return.index, dtype='float64')
    binary.loc[forward_return > positive_threshold] = 1.0
    binary.loc[forward_return < negative_threshold] = 0.0
    return binary

def calculate_future_volatility(close: pd.Series, horizon: int) -> pd.Series:
    """Calculate future realized volatility (standard deviation of log returns) over the horizon."""
    if horizon <= 1:
        raise ValueError("Horizon must be > 1 for volatility")

    log_returns = np.log(close / close.shift(1))

    # We want the volatility of the NEXT 'horizon' days
    # Calculate rolling std, then shift backwards to align it with current day
    rolling_vol = log_returns.rolling(window=horizon).std()
    return rolling_vol.shift(-horizon)

def calculate_future_max_drawdown(close: pd.Series, horizon: int) -> pd.Series:
    """Calculate the maximum drawdown from current price over the next horizon days."""
    if horizon <= 0:
         raise ValueError("Horizon must be positive")

    # Need custom rolling window that looks forward
    # This is inefficient but clear. A production version would use stride tricks or numba
    result = pd.Series(index=close.index, dtype='float64')

    for i in range(len(close) - horizon):
        current_price = close.iloc[i]
        future_window = close.iloc[i+1 : i+horizon+1]

        # Max drop from current_price
        min_future = future_window.min()
        if min_future < current_price:
             drawdown = (min_future - current_price) / current_price
        else:
             drawdown = 0.0

        result.iloc[i] = drawdown

    return result

def calculate_future_max_runup(close: pd.Series, horizon: int) -> pd.Series:
    """Calculate the maximum runup from current price over the next horizon days."""
    if horizon <= 0:
         raise ValueError("Horizon must be positive")

    result = pd.Series(index=close.index, dtype='float64')

    for i in range(len(close) - horizon):
        current_price = close.iloc[i]
        future_window = close.iloc[i+1 : i+horizon+1]

        max_future = future_window.max()
        if max_future > current_price:
             runup = (max_future - current_price) / current_price
        else:
             runup = 0.0

        result.iloc[i] = runup

    return result

def build_price_based_target_frame(df: pd.DataFrame, profile: MLDatasetProfile) -> tuple[pd.DataFrame, dict]:
    """Build all price-based targets specified in the profile."""
    targets = pd.DataFrame(index=df.index)
    warnings = []

    if 'close' not in df.columns:
        warnings.append("Missing 'close' column, cannot compute price targets")
        return targets, {"warnings": warnings}

    close = df['close']

    if "forward_return" in profile.target_types:
        for horizon in profile.forward_return_horizons:
            targets[f'target_forward_return_{horizon}'] = calculate_forward_return(close, horizon)
            targets[f'target_forward_log_return_{horizon}'] = calculate_forward_log_return(close, horizon)

    if "direction_class" in profile.target_types:
        for horizon in profile.forward_return_horizons:
            fwd_ret = calculate_forward_return(close, horizon)
            targets[f'target_direction_class_{horizon}'] = calculate_direction_class(fwd_ret, profile.direction_threshold)
            targets[f'target_binary_return_{horizon}'] = calculate_binary_return_target(
                fwd_ret, profile.positive_return_threshold, profile.negative_return_threshold
            )

    if "future_volatility" in profile.target_types:
        for horizon in profile.forward_volatility_horizons:
             targets[f'target_future_volatility_{horizon}'] = calculate_future_volatility(close, horizon)

    if "future_drawdown" in profile.target_types:
        for horizon in profile.future_drawdown_horizons:
             targets[f'target_future_max_drawdown_{horizon}'] = calculate_future_max_drawdown(close, horizon)
             targets[f'target_future_max_runup_{horizon}'] = calculate_future_max_runup(close, horizon)

    return targets, {"warnings": warnings}

def build_candidate_outcome_targets(candidate_df: pd.DataFrame, backtest_trades_df: pd.DataFrame | None = None) -> tuple[pd.DataFrame, dict]:
    """Map backtest outcomes back to candidates."""
    targets = pd.DataFrame(index=candidate_df.index)
    warnings = []

    targets['target_candidate_outcome'] = OUTCOME_UNKNOWN
    targets['target_trade_result'] = np.nan
    targets['target_reward_risk_outcome'] = np.nan

    if backtest_trades_df is None or backtest_trades_df.empty:
        warnings.append("No backtest trades available to build candidate outcomes")
        return targets, {"warnings": warnings}

    # Attempt to join outcomes
    # This assumes candidate_df has an id and trades have a source_candidate_id
    # or they join on timestamp. For now, doing a basic timestamp join if IDs are missing.

    if 'entry_time' in backtest_trades_df.columns:
        trades_by_time = backtest_trades_df.set_index('entry_time')

        for idx in candidate_df.index:
            if idx in trades_by_time.index:
                trade = trades_by_time.loc[idx]
                if isinstance(trade, pd.DataFrame):
                    trade = trade.iloc[0] if isinstance(trade, pd.DataFrame) else trade

                pnl_pct = trade.get('net_pnl_pct', np.nan)
                targets.loc[idx, 'target_trade_result'] = pnl_pct

                if pd.isna(pnl_pct):
                     targets.loc[idx, 'target_candidate_outcome'] = OUTCOME_INVALID
                elif pnl_pct > 0:
                     targets.loc[idx, 'target_candidate_outcome'] = OUTCOME_POSITIVE
                elif pnl_pct < 0:
                     targets.loc[idx, 'target_candidate_outcome'] = OUTCOME_NEGATIVE
                else:
                     targets.loc[idx, 'target_candidate_outcome'] = OUTCOME_NEUTRAL

                targets.loc[idx, 'target_reward_risk_outcome'] = trade.get('realized_rr', np.nan)
    else:
        warnings.append("Backtest trades missing 'entry_time' for joining")

    return targets, {"warnings": warnings}

def build_target_frame(df: pd.DataFrame, candidate_df: pd.DataFrame | None, backtest_trades_df: pd.DataFrame | None, profile: MLDatasetProfile) -> tuple[pd.DataFrame, dict]:
    """Build the complete target frame."""
    targets, price_summary = build_price_based_target_frame(df, profile)
    warnings = price_summary.get("warnings", [])

    if "candidate_outcome" in profile.target_types and candidate_df is not None:
         outcome_targets, outcome_summary = build_candidate_outcome_targets(candidate_df, backtest_trades_df)
         targets = targets.join(outcome_targets)
         warnings.extend(outcome_summary.get("warnings", []))

    return targets, {"warnings": warnings}
