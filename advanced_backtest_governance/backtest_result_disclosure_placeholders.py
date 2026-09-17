# -*- coding: utf-8 -*-
"""Phase 150: Backtest Result Disclosure Placeholders.

Registers template disclosure sections required in all subsequent backtest reports.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    RESULT_REPORTING_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

DISCLOSURE_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "section_id": "DISC_01_HYPOTHESIS",
        "section_title": "Strategy Economic Rationale & Hypotheses",
        "mandatory": True,
        "purpose": "State economic premise before presenting simulation results.",
    },
    {
        "section_id": "DISC_02_PERIOD_SELECTION",
        "section_title": "Observation Period & Data Coverage Rationale",
        "mandatory": True,
        "purpose": "Explain selection of backtest start and end dates with full regime coverage.",
    },
    {
        "section_id": "DISC_03_FRICTION_BREAKDOWN",
        "section_title": "Transaction Cost & Slippage Model Details",
        "mandatory": True,
        "purpose": "Detailed disclosure of commission tiers, exchange fees, and spread-slippage modeling.",
    },
    {
        "section_id": "DISC_04_BENCHMARK_COMPARISON",
        "section_title": "Passive & Buy-and-Hold Benchmark Baselines",
        "mandatory": True,
        "purpose": "Side-by-side comparative evaluation against neutral asset benchmark.",
    },
    {
        "section_id": "DISC_05_STRESS_AND_ROBUSTNESS",
        "section_title": "Stress Testing & Monte Carlo Robustness Context",
        "mandatory": True,
        "purpose": "Cross-reference Phase 148 stress scenarios and Phase 149 resampling distributions.",
    },
    {
        "section_id": "DISC_06_MANDATORY_DISCLAIMER",
        "section_title": "Regulatory & Non-Execution Disclaimer",
        "mandatory": True,
        "purpose": "Explicit statement that historical backtesting does not guarantee future results.",
    },
]


def build_backtest_result_disclosure_placeholder_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for result disclosure placeholders."""
    rows: List[Dict[str, Any]] = []
    for d in DISCLOSURE_PLACEHOLDERS:
        rows.append({
            "section_id": d["section_id"],
            "section_title": d["section_title"],
            "mandatory": d["mandatory"],
            "purpose": d["purpose"],
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": RESULT_REPORTING_DOMAIN,
        "total_disclosures": len(df),
        "all_mandatory": bool((df["mandatory"] == True).all()) if not df.empty else True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
