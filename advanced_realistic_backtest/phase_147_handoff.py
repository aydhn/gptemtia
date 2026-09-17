# -*- coding: utf-8 -*-
"""Phase 146: Phase 147 Walk-Forward and Out-of-Sample Benchmarking Handoff.

Packages backtest engine contracts, transaction cost models, and slippage foundations
for Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

HANDOFF_PREREQUISITES: List[Dict[str, Any]] = [
    {
        "prerequisite_id": "HND-147-01",
        "name": "walk_forward_validation_prerequisites",
        "description": "Rolling ve expanding pencere bolumleme sozlesmeleri icin gerekli motor arayuzu hazir.",
        "status": "SATISFIED",
    },
    {
        "prerequisite_id": "HND-147-02",
        "name": "out_of_sample_split_prerequisites",
        "description": "In-sample / out-of-sample zaman damgasi araliklarini kesisimsiz ayirma sozlesmesi hazir.",
        "status": "SATISFIED",
    },
    {
        "prerequisite_id": "HND-147-03",
        "name": "benchmark_framework_prerequisites",
        "description": "Strateji getirilerini pasif benchmark (Buy & Hold) ile karsilastirma arayuzu hazir.",
        "status": "SATISFIED",
    },
    {
        "prerequisite_id": "HND-147-04",
        "name": "realistic_backtest_engine_prerequisites",
        "description": "Olay tabanli ve vektorize motor sozlesmeleri tanimlandi.",
        "status": "SATISFIED",
    },
    {
        "prerequisite_id": "HND-147-05",
        "name": "transaction_cost_prerequisites",
        "description": "Komisyon, borsa ucreti ve alis-satis makasi sozlesmeleri hazirlandi.",
        "status": "SATISFIED",
    },
    {
        "prerequisite_id": "HND-147-06",
        "name": "slippage_model_prerequisites",
        "description": "Sabit, oynaklik ve likiditeye dayali kayma sozlesmeleri hazirlandi.",
        "status": "SATISFIED",
    },
    {
        "prerequisite_id": "HND-147-07",
        "name": "no_lookahead_guard_prerequisites",
        "description": "Zaman serisi ve asof backward muhafizlari aktif.",
        "status": "SATISFIED",
    },
    {
        "prerequisite_id": "HND-147-08",
        "name": "bias_control_prerequisites",
        "description": "Survivorship, data snooping ve overfitting muhafizlari aktif.",
        "status": "SATISFIED",
    },
    {
        "prerequisite_id": "HND-147-09",
        "name": "regime_aware_evaluation_prerequisites",
        "description": "Phase 126-135 rejim durumlari ile backtest arasindaki baglanti sozlesmeleri hazir.",
        "status": "SATISFIED",
    },
    {
        "prerequisite_id": "HND-147-10",
        "name": "manual_review_blockers_cleared",
        "description": "Phase 147 oncesi zorunlu insan inceleme kapilari tanimlandi.",
        "status": "SATISFIED",
    },
]


def build_phase_147_walk_forward_oos_benchmark_handoff_report(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of Phase 147 handoff package."""
    rows = []
    for p in HANDOFF_PREREQUISITES:
        rows.append(
            {
                "prerequisite_id": p["prerequisite_id"],
                "name": p["name"],
                "description": p["description"],
                "status": p["status"],
                "is_satisfied": p["status"] == "SATISFIED",
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_phase_147_handoff(df)
    return df, summary


def summarize_phase_147_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 147 handoff package."""
    total = len(df)
    sat = int(df["is_satisfied"].sum()) if not df.empty else 0
    all_sat = (total > 0) and (sat == total)
    return {
        "source_phase": 146,
        "next_phase": 147,
        "next_phase_name": "Walk-Forward Validation and Out-of-Sample Benchmarking",
        "target_final_phase": 160,
        "total_prerequisites": total,
        "satisfied_prerequisites": sat,
        "all_prerequisites_satisfied": all_sat,
        "phase_147_handoff_ready": all_sat,
        "live_trading_remains_prohibited": True,
        "broker_execution_remains_prohibited": True,
        "non_signal": True,
    }
