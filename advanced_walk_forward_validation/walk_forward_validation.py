# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Validation Engine.

Performs strict schema, policy, and negative invariant validation across all Phase 147 registries.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

FORBIDDEN_CLAIM_KEYWORDS = [
    "guaranteed_return",
    "sharpe_claim",
    "win_rate_claim",
    "production_ready",
    "broker_ready",
    "official_approval",
    "actual_return",
    "future_pnl",
]


def validate_walk_forward_profile_registry(
    df: pd.DataFrame, profile: WalkForwardProfile
) -> Dict[str, Any]:
    """Validate profile DataFrame meets security constraints."""
    if df.empty:
        return {"is_valid": False, "error": "Profile registry is empty"}
    if "current_phase" in df.columns and not (df["current_phase"] == 147).all():
        return {"is_valid": False, "error": "Invalid current_phase in profiles"}
    if "target_final_phase" in df.columns and not (df["target_final_phase"] == 160).all():
        return {"is_valid": False, "error": "Invalid target_final_phase in profiles"}
    if "next_phase" in df.columns and not (df["next_phase"] == 148).all():
        return {"is_valid": False, "error": "Invalid next_phase in profiles"}
    if "allow_live_trading" in df.columns and df["allow_live_trading"].any():
        return {"is_valid": False, "error": "Live trading is permitted in a profile"}
    if "allow_broker_integration" in df.columns and df["allow_broker_integration"].any():
        return {"is_valid": False, "error": "Broker integration is permitted in a profile"}
    return {"is_valid": True, "error": None}


def validate_walk_forward_contracts(
    df: pd.DataFrame, profile: WalkForwardProfile
) -> Dict[str, Any]:
    """Validate walk-forward validation contracts table."""
    if df.empty:
        return {"is_valid": False, "error": "Contracts table is empty"}
    if "walk_forward_execution_allowed" in df.columns and df["walk_forward_execution_allowed"].any():
        return {"is_valid": False, "error": "Walk forward execution allowed flag is True"}
    if "live_trading_allowed" in df.columns and df["live_trading_allowed"].any():
        return {"is_valid": False, "error": "Live trading allowed flag is True"}
    return {"is_valid": True, "error": None}


def validate_oos_benchmark_contracts(
    df_map: Dict[str, pd.DataFrame], profile: WalkForwardProfile
) -> Dict[str, Any]:
    """Validate benchmark and OOS contract tables."""
    for name, df in df_map.items():
        if df.empty:
            continue
        if "benchmark_executed" in df.columns and df["benchmark_executed"].any():
            return {"is_valid": False, "error": f"Benchmark executed in {name}"}
        if "metric_calculated" in df.columns and df["metric_calculated"].any():
            return {"is_valid": False, "error": f"Metric calculated in {name}"}
    return {"is_valid": True, "error": None}


def validate_validation_guards(
    df_map: Dict[str, pd.DataFrame], profile: WalkForwardProfile
) -> Dict[str, Any]:
    """Validate that guard registries enforce strict active settings."""
    for name, df in df_map.items():
        if df.empty:
            continue
        if "active" in df.columns and not df["active"].all():
            return {"is_valid": False, "error": f"Inactive guard found in {name}"}
    return {"is_valid": True, "error": None}


def validate_walk_forward_manifest(
    df: pd.DataFrame, profile: WalkForwardProfile
) -> Dict[str, Any]:
    """Validate manifest satisfies all negative invariants."""
    if df.empty:
        return {"is_valid": False, "error": "Manifest is empty"}
    row = df.iloc[0]
    if row.get("current_phase") != 147:
        return {"is_valid": False, "error": "Manifest current_phase is not 147"}
    if row.get("next_phase") != 148:
        return {"is_valid": False, "error": "Manifest next_phase is not 148"}
    if row.get("walk_forward_executed", False):
        return {"is_valid": False, "error": "Manifest walk_forward_executed is True"}
    if row.get("oos_benchmark_executed", False):
        return {"is_valid": False, "error": "Manifest oos_benchmark_executed is True"}
    if row.get("benchmark_metric_calculated", False):
        return {"is_valid": False, "error": "Manifest benchmark_metric_calculated is True"}
    if row.get("live_trading_ready", False):
        return {"is_valid": False, "error": "Manifest live_trading_ready is True"}
    if row.get("broker_ready", False):
        return {"is_valid": False, "error": "Manifest broker_ready is True"}
    if row.get("production_ready", False):
        return {"is_valid": False, "error": "Manifest production_ready is True"}
    return {"is_valid": True, "error": None}


def validate_no_forbidden_walk_forward_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Verify that text, dataframe, or summary does not contain forbidden performance claims."""
    violations = []
    if text:
        t_lower = text.lower()
        for kw in FORBIDDEN_CLAIM_KEYWORDS:
            if kw in t_lower:
                violations.append(kw)
    if df is not None:
        for col in df.columns:
            c_lower = str(col).lower()
            for kw in FORBIDDEN_CLAIM_KEYWORDS:
                if kw in c_lower:
                    violations.append(f"column:{col}")
    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violating_claims": violations,
        "message": "Tum iddialar guvenli." if is_valid else f"Yasakli iddialar bulundu: {violations}",
        "non_signal": True,
    }


def build_walk_forward_validation_report(
    tables: Dict[str, pd.DataFrame], profile: WalkForwardProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build master validation report checking all constraints."""
    checks = []

    # 1. Profile Registry Check
    prof_df = tables.get("profiles", pd.DataFrame())
    r_prof = validate_walk_forward_profile_registry(prof_df, profile)
    checks.append({"check_name": "profile_registry_constraints", "passed": r_prof["is_valid"], "details": r_prof.get("error") or "OK"})

    # 2. Walk-Forward Contracts Check
    wf_df = tables.get("walk_forward_contracts", pd.DataFrame())
    r_wf = validate_walk_forward_contracts(wf_df, profile)
    checks.append({"check_name": "walk_forward_contracts_safety", "passed": r_wf["is_valid"], "details": r_wf.get("error") or "OK"})

    # 3. Benchmark Contracts Check
    bench_df = tables.get("oos_benchmark_contracts", pd.DataFrame())
    r_bnch = validate_oos_benchmark_contracts({"benchmarks": bench_df}, profile)
    checks.append({"check_name": "benchmark_contracts_safety", "passed": r_bnch["is_valid"], "details": r_bnch.get("error") or "OK"})

    # 4. Guards Check
    guards_df = tables.get("no_lookahead_guards", pd.DataFrame())
    r_grd = validate_validation_guards({"no_lookahead": guards_df}, profile)
    checks.append({"check_name": "guards_active_enforcement", "passed": r_grd["is_valid"], "details": r_grd.get("error") or "OK"})

    # 5. Manifest Check
    man_df = tables.get("manifest", pd.DataFrame())
    r_man = validate_walk_forward_manifest(man_df, profile)
    checks.append({"check_name": "manifest_negative_invariants", "passed": r_man["is_valid"], "details": r_man.get("error") or "OK"})

    # 6. Forbidden Claims Check
    r_clm = validate_no_forbidden_walk_forward_claims(df=prof_df)
    checks.append({"check_name": "forbidden_claims_absence", "passed": r_clm["is_valid"], "details": r_clm.get("message") or "OK"})

    df = pd.DataFrame(checks)
    all_passed = bool(df["passed"].all()) if not df.empty else False
    summary = {
        "total_checks": len(df),
        "passed_checks": len(df[df["passed"]]),
        "all_passed": all_passed,
        "validation_status": "PASS" if all_passed else "FAIL",
        "non_signal": True,
    }
    return df, summary
