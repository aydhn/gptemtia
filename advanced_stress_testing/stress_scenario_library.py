# -*- coding: utf-8 -*-
"""Phase 148: Stress Scenario Library.

Provides a unified catalog and registry of all available stress scenarios in the library.
Contract and metadata definition only; no actual scenario simulation or PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

LIBRARY_SCENARIOS: List[Dict[str, Any]] = [
    {"scenario_id": "LIB_HIST_001", "name": "historical_gfc_2008", "group": "HISTORICAL", "severity": "EXTREME", "horizon": "PROLONGED"},
    {"scenario_id": "LIB_HIST_002", "name": "historical_covid_2020", "group": "HISTORICAL", "severity": "BLACK_SWAN", "horizon": "MEDIUM_TERM"},
    {"scenario_id": "LIB_HIST_003", "name": "historical_negative_oil_2020", "group": "HISTORICAL", "severity": "EXTREME", "horizon": "SHORT_TERM"},
    {"scenario_id": "LIB_HIST_004", "name": "historical_flash_crash_2010", "group": "HISTORICAL", "severity": "SEVERE", "horizon": "INTRADAY"},
    {"scenario_id": "LIB_HIST_005", "name": "historical_chf_depeg_2015", "group": "HISTORICAL", "severity": "BLACK_SWAN", "horizon": "INSTANTANEOUS"},
    {"scenario_id": "LIB_HYPO_001", "name": "hypothetical_stagflation_2_0", "group": "HYPOTHETICAL", "severity": "SEVERE", "horizon": "PROLONGED"},
    {"scenario_id": "LIB_HYPO_002", "name": "hypothetical_chokepoint_closure", "group": "HYPOTHETICAL", "severity": "EXTREME", "horizon": "MEDIUM_TERM"},
    {"scenario_id": "LIB_HYPO_003", "name": "hypothetical_sovereign_crisis", "group": "HYPOTHETICAL", "severity": "SEVERE", "horizon": "PROLONGED"},
    {"scenario_id": "LIB_REG_001", "name": "regime_shock_trend_reversal", "group": "REGIME", "severity": "MODERATE", "horizon": "SHORT_TERM"},
    {"scenario_id": "LIB_REG_002", "name": "regime_shock_volatility_breakout", "group": "REGIME", "severity": "SEVERE", "horizon": "SHORT_TERM"},
    {"scenario_id": "LIB_REG_003", "name": "regime_shock_liquidity_drought", "group": "REGIME", "severity": "SEVERE", "horizon": "MEDIUM_TERM"},
    {"scenario_id": "LIB_FRICT_001", "name": "friction_spread_expansion_5x", "group": "FRICTION", "severity": "MODERATE", "horizon": "INTRADAY"},
    {"scenario_id": "LIB_FRICT_002", "name": "friction_catastrophic_slippage_5x", "group": "FRICTION", "severity": "SEVERE", "horizon": "INTRADAY"},
]


def build_stress_scenario_library_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of all scenarios in the stress testing library."""
    rows: List[Dict[str, Any]] = []
    for s in LIBRARY_SCENARIOS:
        rows.append(
            {
                "scenario_id": s["scenario_id"],
                "name": s["name"],
                "group": s["group"],
                "severity": s["severity"],
                "horizon": s["horizon"],
                "execution_allowed": False,
                "metric_calculation_allowed": False,
                "manual_review_required": True,
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_library_scenarios": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_metric_calculation_blocked": not bool(df["metric_calculation_allowed"].any()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
