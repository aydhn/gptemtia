# -*- coding: utf-8 -*-
"""Phase 149: Parameter Stability Contracts Module.

Defines parameter stability contracts to ensure strategy parameters occupy robust plateaus
rather than fragile, overfitted local spikes. Zero parameter optimization permitted.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    PARAMETER_STABILITY_CONTRACT_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

STABILITY_CONTRACTS: List[Dict[str, Any]] = [
    {
        "parameter_name": "lookback_window_length",
        "strategy_ref": "STRAT_MOMENTUM_TREND_V1",
        "perturbation_range": "[lookback * 0.80, lookback * 1.20]",
        "sensitivity_metric": "Sharpe_Ratio_Variance_Pct",
        "plateau_detection_rule": "Sharpe drop < 15% across +/- 20% lookback neighborhood",
        "description": "Stability contract evaluating lookback window robustness against small parameter shifts.",
    },
    {
        "parameter_name": "volatility_stop_loss_multiplier",
        "strategy_ref": "STRAT_VOL_BREAKOUT_V1",
        "perturbation_range": "[atr_mult - 0.5, atr_mult + 0.5]",
        "sensitivity_metric": "Max_Drawdown_Variance_Pct",
        "plateau_detection_rule": "Drawdown increase < 20% across ATR multiple shifts",
        "description": "Stop-loss parameter stability assessing trade exit resilience across neighborhood values.",
    },
    {
        "parameter_name": "entry_threshold_z_score",
        "strategy_ref": "STRAT_MEAN_REVERSION_V1",
        "perturbation_range": "[z_score - 0.25, z_score + 0.25]",
        "sensitivity_metric": "Win_Rate_Sensitivity_Slope",
        "plateau_detection_rule": "Win-rate slope |dWR/dz| < 0.10 in local neighborhood",
        "description": "Mean reversion entry threshold contract verifying broad plateau behavior.",
    },
    {
        "parameter_name": "position_sizing_risk_budget_pct",
        "strategy_ref": "STRAT_RISK_PARITY_ALLOC_V1",
        "perturbation_range": "[risk_pct * 0.85, risk_pct * 1.15]",
        "sensitivity_metric": "Tail_Loss_Elasticity",
        "plateau_detection_rule": "Elasticity |dCVaR/dRisk| < 1.25",
        "description": "Portfolio risk allocation stability contract examining tail loss linearity.",
    },
]


def validate_parameter_stability_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate parameter stability contract safety requirements."""
    required = ["parameter_name", "strategy_ref", "perturbation_range", "plateau_detection_rule"]
    for r in required:
        if r not in contract or not contract[r]:
            return {"valid": False, "reason": f"Missing required parameter stability field: {r}"}

    if contract.get("optimization_allowed", False) or contract.get("sweep_allowed", False):
        return {"valid": False, "reason": "Optimization or sweep execution is strictly prohibited."}

    return {"valid": True, "reason": "Contract satisfies all stability invariants."}


def summarize_parameter_stability_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the parameter stability contracts DataFrame."""
    all_valid = True
    for _, row in df.iterrows():
        res = validate_parameter_stability_contract(row.to_dict())
        if not res["valid"]:
            all_valid = False
            break

    return {
        "domain": PARAMETER_STABILITY_CONTRACT_DOMAIN,
        "total_contracts": len(df),
        "all_valid": all_valid,
        "all_optimizations_disabled": bool((~df["optimization_allowed"]).all() and (~df["sweep_allowed"]).all()),
        "status": MONTE_CARLO_CONTRACT_READY if all_valid else "BLOCKED",
    }


def build_parameter_stability_contract_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the parameter stability contract registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for c in STABILITY_CONTRACTS:
        rows.append(
            {
                "parameter_name": c["parameter_name"],
                "strategy_ref": c["strategy_ref"],
                "perturbation_range": c["perturbation_range"],
                "sensitivity_metric": c["sensitivity_metric"],
                "plateau_detection_rule": c["plateau_detection_rule"],
                "description": c["description"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "optimization_allowed": False,
                "sweep_allowed": False,
                "status": MONTE_CARLO_CONTRACT_READY,
                "domain": PARAMETER_STABILITY_CONTRACT_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_parameter_stability_contracts(df)
    return df, summary
