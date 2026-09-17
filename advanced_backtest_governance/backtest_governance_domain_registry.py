# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Domain Registry.

Catalogs and verifies the governance functional domains for Phase 150.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    BACKTEST_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
    GOVERNANCE_CONTRACT_DOMAIN,
    BIAS_CONTROL_DOMAIN,
    RESULT_REPORTING_DOMAIN,
    METRIC_CLAIM_BOUNDARY_DOMAIN,
    PERFORMANCE_CLAIM_BOUNDARY_DOMAIN,
    LOOKAHEAD_BIAS_DOMAIN,
    SURVIVORSHIP_BIAS_DOMAIN,
    DATA_SNOOPING_BIAS_DOMAIN,
    OVERFITTING_BIAS_DOMAIN,
    MULTIPLE_TESTING_BIAS_DOMAIN,
    PARAMETER_FISHING_BIAS_DOMAIN,
    BENCHMARK_SELECTION_BIAS_DOMAIN,
    REGIME_COVERAGE_BIAS_DOMAIN,
    SAMPLE_COVERAGE_BIAS_DOMAIN,
    REALISM_GOVERNANCE_DOMAIN,
    SPLIT_GOVERNANCE_DOMAIN,
    WALK_FORWARD_GOVERNANCE_DOMAIN,
    OOS_GOVERNANCE_DOMAIN,
    STRESS_GOVERNANCE_DOMAIN,
    MONTE_CARLO_GOVERNANCE_DOMAIN,
    BENCHMARK_GOVERNANCE_DOMAIN,
    AUDIT_POLICY_DOMAIN,
    EVIDENCE_POLICY_DOMAIN,
    MANUAL_REVIEW_GATE_DOMAIN,
    GO_NO_GO_BOUNDARY_DOMAIN,
    DISABLED_EXECUTION_DOMAIN,
    PHASE_151_HANDOFF_DOMAIN,
)

DOMAINS: List[Dict[str, Any]] = [
    {"domain_name": GOVERNANCE_CONTRACT_DOMAIN, "description": "Central backtest governance contracts spanning Phase 146-150."},
    {"domain_name": BIAS_CONTROL_DOMAIN, "description": "Multi-bias control architecture and guard policies."},
    {"domain_name": RESULT_REPORTING_DOMAIN, "description": "Reporting governance enforcing disclosure without actual metric claims."},
    {"domain_name": METRIC_CLAIM_BOUNDARY_DOMAIN, "description": "Blocks calculated Sharpe, win-rate, alpha, return claims."},
    {"domain_name": PERFORMANCE_CLAIM_BOUNDARY_DOMAIN, "description": "Blocks guaranteed return, proven strategy, and production-ready claims."},
    {"domain_name": LOOKAHEAD_BIAS_DOMAIN, "description": "Strict detection and prohibition of lookahead leakage and negative shifts."},
    {"domain_name": SURVIVORSHIP_BIAS_DOMAIN, "description": "Point-in-time universe reconstitution controls."},
    {"domain_name": DATA_SNOOPING_BIAS_DOMAIN, "description": "Controls for repeated testing and data reusing artifacts."},
    {"domain_name": OVERFITTING_BIAS_DOMAIN, "description": "Overfitting fragility diagnostics and parameter-to-sample ratio bounds."},
    {"domain_name": MULTIPLE_TESTING_BIAS_DOMAIN, "description": "Multiple testing tracking, Bonferroni/Holm/BHY correction placeholders."},
    {"domain_name": PARAMETER_FISHING_BIAS_DOMAIN, "description": "Prohibition of parameter cherry-picking and p-hacking."},
    {"domain_name": BENCHMARK_SELECTION_BIAS_DOMAIN, "description": "Pre-commitment requirement and neutral benchmark baseline selection."},
    {"domain_name": REGIME_COVERAGE_BIAS_DOMAIN, "description": "Ensures backtest spans bull, bear, high vol, and quiet regimes."},
    {"domain_name": SAMPLE_COVERAGE_BIAS_DOMAIN, "description": "Sample window adequacy and unrepresentative period mitigation."},
    {"domain_name": REALISM_GOVERNANCE_DOMAIN, "description": "Transaction cost, tiered commissions, non-linear slippage, and liquidity realism."},
    {"domain_name": SPLIT_GOVERNANCE_DOMAIN, "description": "Train/validation/test chronological partition and embargo rules."},
    {"domain_name": WALK_FORWARD_GOVERNANCE_DOMAIN, "description": "Anchored and rolling walk-forward validation governance."},
    {"domain_name": OOS_GOVERNANCE_DOMAIN, "description": "Strict out-of-sample quarantine and isolation contracts."},
    {"domain_name": STRESS_GOVERNANCE_DOMAIN, "description": "Phase 148 stress testing scenario integration contracts."},
    {"domain_name": MONTE_CARLO_GOVERNANCE_DOMAIN, "description": "Phase 149 Monte Carlo robustness and resampling contracts linkage."},
    {"domain_name": BENCHMARK_GOVERNANCE_DOMAIN, "description": "Passive and active benchmark evaluation governance contracts."},
    {"domain_name": AUDIT_POLICY_DOMAIN, "description": "Audit trails, parameter logging, and provenance tracking policies."},
    {"domain_name": EVIDENCE_POLICY_DOMAIN, "description": "Empirical validation evidence preservation policies."},
    {"domain_name": MANUAL_REVIEW_GATE_DOMAIN, "description": "Required human approval gates before strategy evaluation progression."},
    {"domain_name": GO_NO_GO_BOUNDARY_DOMAIN, "description": "Explicit go/no-go boundaries blocking execution while allowing research handoff."},
    {"domain_name": DISABLED_EXECUTION_DOMAIN, "description": "Formally disabled execution reports for live, broker, backtest, and optimizer."},
    {"domain_name": PHASE_151_HANDOFF_DOMAIN, "description": "Handshake interface to Phase 151 benchmark comparison contracts."},
]


def summarize_backtest_governance_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance domains."""
    return {
        "domain": BACKTEST_GOVERNANCE_DOMAIN,
        "total_domains": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
        "all_local_only": bool((df["local_only"] == True).all()) if not df.empty else True,
        "non_signal": True,
    }


def build_backtest_governance_domain_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of governance domains."""
    rows: List[Dict[str, Any]] = []
    for d in DOMAINS:
        rows.append({
            "domain_name": d["domain_name"],
            "description": d["description"],
            "phase": profile.current_phase,
            "local_only": True,
            "non_signal": True,
            "execution_allowed": False,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_governance_domains(df)
    return df, summary
