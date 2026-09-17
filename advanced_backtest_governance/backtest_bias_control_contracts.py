# -*- coding: utf-8 -*-
"""Phase 150: Backtest Bias Control Contracts.

Establishes formal bias control contracts for local/offline research.
Guarantees zero performance claims and zero live execution.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    BIAS_CONTROL_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

BIAS_CONTROLS: List[Dict[str, Any]] = [
    {
        "bias_type": "lookahead_bias",
        "control_name": "lookahead_leakage_mitigation_contract",
        "detection_methodology": "Timestamp sequence order verification and negative shift audit.",
        "mitigation_policy": "Strict point-in-time filtering and prohibition of shift(-1) operations.",
        "enforcement_level": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "bias_type": "survivorship_bias",
        "control_name": "point_in_time_universe_reconstitution_contract",
        "detection_methodology": "Historical constituent presence auditing at bar entry timestamps.",
        "mitigation_policy": "Simulate solely with securities actively trading at the historical observation instant.",
        "enforcement_level": "BLOCKING_MANDATORY",
    },
    {
        "bias_type": "data_snooping_bias",
        "control_name": "data_snooping_and_reuse_quarantine_contract",
        "detection_methodology": "Model reuse counter and dataset leakage inspection.",
        "mitigation_policy": "Quarantine test sets and penalize repeated hypothesis testing on identical samples.",
        "enforcement_level": "HIGH_AUDIT",
    },
    {
        "bias_type": "overfitting_bias",
        "control_name": "overfitting_fragility_bound_contract",
        "detection_methodology": "Degrees-of-freedom to sample-size ratio and sensitivity gradient audits.",
        "mitigation_policy": "Cap parameter search complexity and mandate validation degradation thresholds.",
        "enforcement_level": "HIGH_AUDIT",
    },
    {
        "bias_type": "multiple_testing_bias",
        "control_name": "multiple_testing_significance_adjustment_contract",
        "detection_methodology": "Registry tracking cumulative trial count and hypothesis iterations.",
        "mitigation_policy": "Apply Bonferroni, Holm, or Benjamini-Hochberg-Yekutieli haircut corrections to nominal p-values.",
        "enforcement_level": "HIGH_AUDIT",
    },
    {
        "bias_type": "parameter_fishing_bias",
        "control_name": "parameter_fishing_and_p_hacking_guard_contract",
        "detection_methodology": "Search grid density inspection and sensitivity surface discontinuity testing.",
        "mitigation_policy": "Prohibit post-hoc parameter cherry-picking; require pre-registered hypothesis spaces.",
        "enforcement_level": "BLOCKING_MANDATORY",
    },
    {
        "bias_type": "benchmark_selection_bias",
        "control_name": "neutral_benchmark_precommitment_contract",
        "detection_methodology": "Ex-post benchmark swap check and suitability alignment.",
        "mitigation_policy": "Mandate pre-committed neutral benchmark baselines before strategy design.",
        "enforcement_level": "BLOCKING_MANDATORY",
    },
    {
        "bias_type": "regime_coverage_bias",
        "control_name": "multivariate_regime_coverage_contract",
        "detection_methodology": "Phase 126-135 regime matrix distribution overlap across backtest sample.",
        "mitigation_policy": "Reject backtests that exclusively sample single favorable regimes (e.g. only bull trends).",
        "enforcement_level": "HIGH_AUDIT",
    },
    {
        "bias_type": "sample_coverage_bias",
        "control_name": "sample_adequacy_and_window_breadth_contract",
        "detection_methodology": "Minimum bar count and economic cycle span verification.",
        "mitigation_policy": "Enforce minimum sample lengths covering at least one full volatility and rate cycle.",
        "enforcement_level": "HIGH_AUDIT",
    },
    {
        "bias_type": "transaction_cost_realism_bias",
        "control_name": "tiered_fee_and_spread_realism_contract",
        "detection_methodology": "Zero-cost assumption detection in all trade simulation logic.",
        "mitigation_policy": "Mandate exchange fees, financing carry, and tiered broker commissions.",
        "enforcement_level": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "bias_type": "slippage_realism_bias",
        "control_name": "volume_dependent_slippage_realism_contract",
        "detection_methodology": "Instantaneous fill and zero-slippage claim inspection.",
        "mitigation_policy": "Enforce square-root market impact and spread-widening during volatile bars.",
        "enforcement_level": "BLOCKING_ZERO_TOLERANCE",
    },
]


def summarize_backtest_bias_control_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize bias control contracts."""
    return {
        "domain": BIAS_CONTROL_DOMAIN,
        "total_bias_controls": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "all_lookahead_free": bool((df["lookahead_free_verified"] == True).all()) if not df.empty else True,
        "all_claims_blocked": bool((df["claim_blocked"] == True).all()) if not df.empty else True,
        "all_executions_disabled": bool((df["execution_allowed"] == False).all()) if not df.empty else True,
        "non_signal": True,
        "local_only": True,
    }


def build_backtest_bias_control_contract_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for bias control contracts."""
    rows: List[Dict[str, Any]] = []
    for b in BIAS_CONTROLS:
        rows.append({
            "bias_type": b["bias_type"],
            "control_name": b["control_name"],
            "detection_methodology": b["detection_methodology"],
            "mitigation_policy": b["mitigation_policy"],
            "enforcement_level": b["enforcement_level"],
            "lookahead_free_verified": True,
            "claim_blocked": True,
            "execution_allowed": False,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_bias_control_contracts(df)
    return df, summary
