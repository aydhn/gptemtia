"""
Walk-forward validation evaluator.
"""

import logging
from typing import Optional, Tuple
import pandas as pd
import numpy as np

from validation.validation_models import TimeSplit
from validation.validation_config import ValidationProfile
from validation.time_splits import filter_dataframe_by_split

logger = logging.getLogger(__name__)


class WalkForwardValidator:
    """Evaluates strategy performance across walk-forward splits."""

    def __init__(self, profile: ValidationProfile):
        self.profile = profile

    def _calculate_metrics(self, df: pd.DataFrame, is_trades: bool = True) -> dict:
        """Helper to calculate basic metrics from a trades DataFrame or equity curve."""
        if df is None or df.empty:
            return {
                "trade_count": 0,
                "total_return_pct": 0.0,
                "sharpe_ratio": 0.0,
                "max_drawdown_pct": 0.0,
                "profit_factor": 0.0,
                "win_rate": 0.0,
            }

        if is_trades and 'pnl_pct' in df.columns:
            trade_count = len(df)
            total_return_pct = df['pnl_pct'].sum() * 100.0  # Assuming pnl_pct is decimal

            winning_trades = df[df['pnl_pct'] > 0]
            losing_trades = df[df['pnl_pct'] < 0]

            win_rate = len(winning_trades) / trade_count if trade_count > 0 else 0.0

            gross_profit = winning_trades['pnl_pct'].sum() if not winning_trades.empty else 0.0
            gross_loss = abs(losing_trades['pnl_pct'].sum()) if not losing_trades.empty else 0.0
            profit_factor = gross_profit / gross_loss if gross_loss > 0 else (99.0 if gross_profit > 0 else 0.0)

            # Simple Sharpe approx from trades if daily returns not available
            returns = df['pnl_pct']
            mean_ret = returns.mean()
            std_ret = returns.std()
            sharpe_ratio = (mean_ret / std_ret * np.sqrt(252)) if std_ret > 0 else 0.0

            # Max drawdown approx from cumulative sum of trade returns
            cum_returns = returns.cumsum()
            running_max = cum_returns.expanding().max()
            drawdowns = cum_returns - running_max
            max_drawdown_pct = abs(drawdowns.min()) * 100.0 if not drawdowns.empty else 0.0

            return {
                "trade_count": trade_count,
                "total_return_pct": total_return_pct,
                "sharpe_ratio": sharpe_ratio,
                "max_drawdown_pct": max_drawdown_pct,
                "profit_factor": profit_factor,
                "win_rate": win_rate,
            }

        return {
            "trade_count": 0,
            "total_return_pct": 0.0,
            "sharpe_ratio": 0.0,
            "max_drawdown_pct": 0.0,
            "profit_factor": 0.0,
            "win_rate": 0.0,
        }

    def evaluate_split(
        self,
        split: TimeSplit,
        trades_df: pd.DataFrame,
        equity_curve: pd.DataFrame,
        performance_summary: Optional[dict] = None,
    ) -> dict:
        """Evaluates a single train/test split."""
        train_trades = filter_dataframe_by_split(trades_df, split, "train")
        test_trades = filter_dataframe_by_split(trades_df, split, "test")

        train_metrics = self._calculate_metrics(train_trades)
        test_metrics = self._calculate_metrics(test_trades)

        train_passed_min = train_metrics["trade_count"] >= self.profile.min_trades_per_split
        test_passed_min = test_metrics["trade_count"] >= self.profile.min_trades_per_split

        warnings = []
        if not train_passed_min:
            warnings.append(f"Train split {split.split_index} has insufficient trades ({train_metrics['trade_count']} < {self.profile.min_trades_per_split})")
        if not test_passed_min:
            warnings.append(f"Test split {split.split_index} has insufficient trades ({test_metrics['trade_count']} < {self.profile.min_trades_per_split})")

        return {
            "split_id": split.split_id,
            "split_index": split.split_index,
            "train_start": split.train_start,
            "train_end": split.train_end,
            "test_start": split.test_start,
            "test_end": split.test_end,
            "train_trade_count": train_metrics["trade_count"],
            "test_trade_count": test_metrics["trade_count"],
            "train_total_return_pct": train_metrics["total_return_pct"],
            "test_total_return_pct": test_metrics["total_return_pct"],
            "train_sharpe_ratio": train_metrics["sharpe_ratio"],
            "test_sharpe_ratio": test_metrics["sharpe_ratio"],
            "train_max_drawdown_pct": train_metrics["max_drawdown_pct"],
            "test_max_drawdown_pct": test_metrics["max_drawdown_pct"],
            "train_profit_factor": train_metrics["profit_factor"],
            "test_profit_factor": test_metrics["profit_factor"],
            "train_win_rate": train_metrics["win_rate"],
            "test_win_rate": test_metrics["win_rate"],
            "train_passed_min_trades": train_passed_min,
            "test_passed_min_trades": test_passed_min,
            "split_quality_warning": "; ".join(warnings) if warnings else "",
        }

    def evaluate_walk_forward(
        self,
        splits: list[TimeSplit],
        trades_df: pd.DataFrame,
        equity_curve: pd.DataFrame,
    ) -> Tuple[pd.DataFrame, dict]:
        """Evaluates all walk-forward splits and produces a summary."""
        if not splits:
            logger.warning("No splits provided for walk-forward evaluation.")
            return pd.DataFrame(), {"split_count": 0, "warnings": ["No splits provided"]}

        results = []
        for split in splits:
            res = self.evaluate_split(split, trades_df, equity_curve)
            results.append(res)

        df = pd.DataFrame(results)

        valid_df = df[df['test_passed_min_trades'] == True]

        avg_train_return = valid_df['train_total_return_pct'].mean() if not valid_df.empty else 0.0
        avg_test_return = valid_df['test_total_return_pct'].mean() if not valid_df.empty else 0.0
        avg_train_sharpe = valid_df['train_sharpe_ratio'].mean() if not valid_df.empty else 0.0
        avg_test_sharpe = valid_df['test_sharpe_ratio'].mean() if not valid_df.empty else 0.0

        test_positive_ratio = (valid_df['test_total_return_pct'] > 0).mean() if not valid_df.empty else 0.0

        # Calculate degradation (how much worse is test vs train)
        # Using Sharpe as primary metric for degradation
        if avg_train_sharpe > 0:
            train_test_degradation = max(0.0, (avg_train_sharpe - avg_test_sharpe) / avg_train_sharpe)
        else:
            # If train sharpe is negative, any positive test is good, negative test is bad
            train_test_degradation = 1.0 if avg_test_sharpe <= 0 else 0.0

        summary = {
            "split_count": len(splits),
            "valid_split_count": len(valid_df),
            "avg_train_return": float(avg_train_return),
            "avg_test_return": float(avg_test_return),
            "avg_train_sharpe": float(avg_train_sharpe),
            "avg_test_sharpe": float(avg_test_sharpe),
            "test_positive_ratio": float(test_positive_ratio),
            "train_test_degradation": float(train_test_degradation),
            "warnings": [],
        }

        if len(valid_df) < len(splits):
             summary["warnings"].append(f"{len(splits) - len(valid_df)} splits had insufficient trades.")

        return df, summary
