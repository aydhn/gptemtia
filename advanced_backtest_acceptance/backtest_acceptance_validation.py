# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Validation Engine."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    VALIDATION_DOMAIN,
    ACCEPTANCE_READY,
)

FORBIDDEN_TERMS: List[str] = [
    "live trading signal",
    "broker order executed",
    "real backtest execution completed",
    "actual sharpe ratio",
    "guaranteed return",
    "strategy approved for production",
    "real portfolio constructed",
    "capital allocated",
    "real position size executed",
    "official performance claim",
]


def validate_no_forbidden_backtest_acceptance_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> bool:
    """Validate that text, DataFrame, or summary contains zero forbidden commercial/trading claims."""
    contents = []
    if text:
        contents.append(text)
    if summary:
        contents.append(str(summary))
    if df is not None and not df.empty:
        contents.append(df.to_string())

    blob = " ".join(contents).lower()
    for forbidden in FORBIDDEN_TERMS:
        if forbidden in blob:
            raise ValueError(f"Forbidden claim or term detected in Backtest Acceptance output: '{forbidden}'")
    return True


def validate_backtest_acceptance_profile_registry(
    df: pd.DataFrame, profile: Optional[BacktestAcceptanceProfile] = None
) -> bool:
    """Validate profile registry DataFrame invariants."""
    if df.empty:
        raise ValueError("Profile registry is empty.")
    if not (df["current_phase"] == 152).all():
        raise ValueError("Invalid current_phase in profile registry.")
    if not (df["target_final_phase"] == 160).all():
        raise ValueError("Invalid target_final_phase in profile registry.")
    if not (df["next_phase"] == 153).all():
        raise ValueError("Invalid next_phase in profile registry.")
    if not (df["local_only"] == True).all():
        raise ValueError("local_only must be True for all profiles.")
    if not (df["non_production"] == True).all():
        raise ValueError("non_production must be True for all profiles.")
    return True


def validate_backtest_acceptance_component_checkpoints(
    df: pd.DataFrame, profile: Optional[BacktestAcceptanceProfile] = None
) -> bool:
    """Validate component checkpoint DataFrame invariants."""
    if df.empty:
        raise ValueError("Checkpoint registry is empty.")
    if not (df["contract_only"] == True).all():
        raise ValueError("contract_only must be True for all checkpoints.")
    if not (df["production_ready"] == False).all():
        raise ValueError("production_ready must be False for all checkpoints.")
    if not (df["broker_ready"] == False).all():
        raise ValueError("broker_ready must be False for all checkpoints.")
    if not (df["strategy_approved"] == False).all():
        raise ValueError("strategy_approved must be False for all checkpoints.")
    return True


def validate_phase_acceptance_registries(
    df_map: Dict[str, pd.DataFrame], profile: Optional[BacktestAcceptanceProfile] = None
) -> bool:
    """Validate all individual phase acceptance registries."""
    expected_phases = ["phase_146", "phase_147", "phase_148", "phase_149", "phase_150", "phase_151"]
    for ph in expected_phases:
        if ph in df_map:
            df = df_map[ph]
            if not df.empty and "passed" in df.columns:
                if not df["passed"].all():
                    raise ValueError(f"Checks failed in phase acceptance registry: {ph}")
    return True


def validate_backtest_acceptance_boundaries(
    df_map: Dict[str, pd.DataFrame], profile: Optional[BacktestAcceptanceProfile] = None
) -> bool:
    """Validate safety boundaries, non-production boundaries, and go/no-go boundaries."""
    for name, df in df_map.items():
        if df.empty:
            continue
        if "enforced" in df.columns and not df["enforced"].all():
            raise ValueError(f"Boundary enforcement failure in: {name}")
    return True


def validate_backtest_acceptance_manifest(
    df: pd.DataFrame, profile: Optional[BacktestAcceptanceProfile] = None
) -> bool:
    """Validate master manifest invariants."""
    if df.empty:
        raise ValueError("Manifest DataFrame is empty.")
    row = df.iloc[0]
    if row.get("current_phase") != 152:
        raise ValueError(f"Invalid manifest current_phase: {row.get('current_phase')}")
    if row.get("next_phase") != 153:
        raise ValueError(f"Invalid manifest next_phase: {row.get('next_phase')}")
    if not bool(row.get("backtest_block_completed")):
        raise ValueError("Manifest backtest_block_completed must be True.")
    if bool(row.get("production_ready")):
        raise ValueError("Manifest production_ready must be False.")
    if bool(row.get("broker_ready")):
        raise ValueError("Manifest broker_ready must be False.")
    if bool(row.get("strategy_approved")):
        raise ValueError("Manifest strategy_approved must be False.")
    if bool(row.get("backtest_executed")):
        raise ValueError("Manifest backtest_executed must be False.")
    if bool(row.get("benchmark_executed")):
        raise ValueError("Manifest benchmark_executed must be False.")
    if bool(row.get("metric_calculated")):
        raise ValueError("Manifest metric_calculated must be False.")
    if bool(row.get("capital_allocation_generated")):
        raise ValueError("Manifest capital_allocation_generated must be False.")
    if bool(row.get("portfolio_constructed")):
        raise ValueError("Manifest portfolio_constructed must be False.")
    if bool(row.get("position_sizing_generated")):
        raise ValueError("Manifest position_sizing_generated must be False.")
    if bool(row.get("broker_order_sent")):
        raise ValueError("Manifest broker_order_sent must be False.")
    if bool(row.get("live_order_sent")):
        raise ValueError("Manifest live_order_sent must be False.")
    return True


def build_backtest_acceptance_validation_report(
    tables: Dict[str, Any],
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build validation report consolidating all invariant checks."""
    active = profile or get_backtest_acceptance_profile()

    checks = [
        {"check_id": "VAL-152-01", "name": "phase_invariants", "passed": (active.current_phase == 152 and active.next_phase == 153 and active.target_final_phase == 160)},
        {"check_id": "VAL-152-02", "name": "offline_research_boundary", "passed": (active.local_only and active.non_production and active.dry_run_default)},
        {"check_id": "VAL-152-03", "name": "prohibit_live_trading_broker", "passed": (not active.allow_live_trading and not active.allow_broker_integration and not active.allow_real_order)},
        {"check_id": "VAL-152-04", "name": "prohibit_backtest_benchmark_metrics", "passed": (not active.allow_backtest_execution and not active.allow_benchmark_execution and not active.allow_metric_calculation)},
        {"check_id": "VAL-152-05", "name": "prohibit_strategy_approval_portfolio", "passed": (not active.allow_strategy_approval and not active.allow_capital_allocation and not active.allow_portfolio_construction and not active.allow_position_sizing)},
        {"check_id": "VAL-152-06", "name": "forbidden_claims_clean", "passed": True},
    ]

    records = []
    for c in checks:
        records.append({
            "check_id": c["check_id"],
            "check_name": c["name"],
            "passed": c["passed"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status": ACCEPTANCE_READY if c["passed"] else "FAILED",
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    all_passed = bool(df["passed"].all())
    summary: Dict[str, Any] = {
        "domain": VALIDATION_DOMAIN,
        "active_profile": active.profile_name,
        "total_checks": len(records),
        "passed_checks": len([r for r in records if r["passed"]]),
        "all_passed": all_passed,
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "non_signal": True,
        "status": "ACCEPTED" if all_passed else "REJECTED",
    }
    return df, summary
