"""
Overfitting checks module to evaluate model risk.
"""

import logging
import pandas as pd
from typing import Optional

from validation.robustness_analysis import calculate_train_test_degradation

logger = logging.getLogger(__name__)


def calculate_overfitting_risk_from_train_test(train_summary: dict, test_summary: dict) -> dict:
    """Calculates overfitting risk based on a single train/test summary comparison."""
    if not train_summary or not test_summary:
        return {"risk_score": 1.0, "reason": "Missing summary data"}

    train_sharpe = train_summary.get("sharpe_ratio", 0.0)
    test_sharpe = test_summary.get("sharpe_ratio", 0.0)

    degradation = calculate_train_test_degradation(train_sharpe, test_sharpe)

    # Check trade counts - very low trade counts inflate risk
    train_trades = train_summary.get("trade_count", 0)
    test_trades = test_summary.get("trade_count", 0)

    low_trade_risk = 0.0
    if train_trades < 30:
        low_trade_risk += 0.3
    if test_trades < 10:
        low_trade_risk += 0.3

    # High win rate but low profit factor indicates curve fitting to noise
    train_wr = train_summary.get("win_rate", 0.0)
    train_pf = train_summary.get("profit_factor", 0.0)

    curve_fit_risk = 0.0
    if train_wr > 0.8 and train_pf < 1.5:
        curve_fit_risk = 0.4

    score = min(1.0, degradation * 0.6 + low_trade_risk + curve_fit_risk)

    return {"risk_score": float(score)}


def calculate_overfitting_risk_from_walk_forward(walk_forward_df: pd.DataFrame) -> dict:
    """Calculates overfitting risk from walk-forward split variability."""
    if walk_forward_df.empty:
        return {"risk_score": 1.0, "reason": "No walk-forward data"}

    if "train_sharpe_ratio" not in walk_forward_df.columns or "test_sharpe_ratio" not in walk_forward_df.columns:
         return {"risk_score": 1.0, "reason": "Missing required metric columns"}

    # Check average degradation
    avg_train = walk_forward_df["train_sharpe_ratio"].mean()
    avg_test = walk_forward_df["test_sharpe_ratio"].mean()

    avg_degradation = calculate_train_test_degradation(avg_train, avg_test)

    # Check instability - if test performance fluctuates wildly while train is stable, it's overfit
    train_cv = walk_forward_df["train_sharpe_ratio"].std() / abs(avg_train) if abs(avg_train) > 1e-6 else 1.0
    test_cv = walk_forward_df["test_sharpe_ratio"].std() / abs(avg_test) if abs(avg_test) > 1e-6 else 1.0

    instability_penalty = 0.0
    if test_cv > (train_cv * 2.0) and test_cv > 0.5:
        instability_penalty = min(0.5, (test_cv - train_cv) * 0.2)

    score = min(1.0, (avg_degradation * 0.7) + instability_penalty)

    return {"risk_score": float(score), "avg_degradation": float(avg_degradation), "instability_penalty": float(instability_penalty)}


def calculate_overfitting_risk_from_parameter_sensitivity(sensitivity_df: pd.DataFrame) -> dict:
    """Calculates overfitting risk based on parameter fragility."""
    if sensitivity_df.empty:
        return {"risk_score": 0.5, "reason": "No sensitivity data"}

    if "fragility_warning" not in sensitivity_df.columns:
        return {"risk_score": 0.5, "reason": "Missing fragility warning column"}

    fragile_count = len(sensitivity_df[sensitivity_df["fragility_warning"] != ""])
    total_params = len(sensitivity_df)

    if total_params == 0:
         return {"risk_score": 0.5}

    fragile_ratio = fragile_count / total_params

    # If many parameter values cause high variance or failure, risk is high
    score = min(1.0, fragile_ratio * 1.5)

    return {"risk_score": float(score), "fragile_ratio": float(fragile_ratio)}


def aggregate_overfitting_risk(risk_components: list[dict]) -> dict:
    """Aggregates multiple overfitting risk scores."""
    scores = [comp.get("risk_score", 0.5) for comp in risk_components if "risk_score" in comp]

    if not scores:
        return {"aggregate_overfitting_risk_score": 1.0}

    # Use max or a heavy average (overfitting in one area is a red flag)
    # Give higher weight to the highest risk found
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)

    agg_score = (max_score * 0.7) + (avg_score * 0.3)

    return {"aggregate_overfitting_risk_score": float(agg_score)}


def build_overfitting_report(
    train_summary: Optional[dict] = None,
    test_summary: Optional[dict] = None,
    walk_forward_df: Optional[pd.DataFrame] = None,
    sensitivity_df: Optional[pd.DataFrame] = None,
) -> dict:
    """Builds a comprehensive overfitting risk report."""
    components = []

    train_test_risk = 0.5
    if train_summary and test_summary:
        tt_res = calculate_overfitting_risk_from_train_test(train_summary, test_summary)
        train_test_risk = tt_res.get("risk_score", 0.5)
        components.append(tt_res)

    wf_risk = 0.5
    if walk_forward_df is not None and not walk_forward_df.empty:
        wf_res = calculate_overfitting_risk_from_walk_forward(walk_forward_df)
        wf_risk = wf_res.get("risk_score", 0.5)
        components.append(wf_res)

    param_risk = 0.5
    if sensitivity_df is not None and not sensitivity_df.empty:
        param_res = calculate_overfitting_risk_from_parameter_sensitivity(sensitivity_df)
        param_risk = param_res.get("risk_score", 0.5)
        components.append(param_res)

    agg = aggregate_overfitting_risk(components)
    agg_score = agg["aggregate_overfitting_risk_score"]

    # Determine label
    if agg_score < 0.2:
        label = "low"
    elif agg_score < 0.4:
        label = "moderate"
    elif agg_score < 0.7:
        label = "elevated"
    elif agg_score < 0.9:
        label = "high"
    else:
        label = "extreme"

    return {
        "train_test_degradation_risk": float(train_test_risk),
        "split_instability_risk": float(wf_risk),
        "parameter_fragility_risk": float(param_risk),
        "aggregate_overfitting_risk_score": float(agg_score),
        "overfitting_risk_label": label,
        "warnings": ["High overfitting risk detected"] if label in ["high", "extreme"] else []
    }
