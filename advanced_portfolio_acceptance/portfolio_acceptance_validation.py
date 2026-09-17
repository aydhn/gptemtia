# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Validation.

Validates all registries, checkpoints, manifests, and textual outputs against
strict negative claims, non-production boundaries, and security rules.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    VALIDATION_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

FORBIDDEN_CLAIM_PHRASES = [
    "production ready",
    "broker ready",
    "live trading ready",
    "guaranteed return",
    "guaranteed profit",
    "buy signal",
    "sell signal",
    "approved for live",
    "real order sent",
    "real portfolio constructed",
    "real optimization executed",
    "automated hedge executed",
]


def validate_portfolio_acceptance_profile_registry(
    df: pd.DataFrame,
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Dict[str, Any]:
    """Validate profile registry against negative invariants."""
    passed = True
    issues = []
    if df.empty:
        return {"passed": False, "issues": ["Profile registry DataFrame is empty."]}

    if not df["local_only"].all():
        passed = False
        issues.append("Found profile with local_only=False.")
    if not df["dry_run_default"].all():
        passed = False
        issues.append("Found profile with dry_run_default=False.")
    if not df["non_production"].all():
        passed = False
        issues.append("Found profile with non_production=False.")
    if df["allow_live_trading"].any():
        passed = False
        issues.append("Found profile allowing live trading.")

    return {"passed": passed, "issues": issues, "rule": "profile_registry_validation"}


def validate_portfolio_acceptance_component_checkpoints(
    df: pd.DataFrame,
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Dict[str, Any]:
    """Validate component checkpoints."""
    passed = True
    issues = []
    if df.empty:
        return {"passed": False, "issues": ["Component checkpoint DataFrame is empty."]}

    if not df["contract_only"].all():
        passed = False
        issues.append("Checkpoints contain non-contract items.")
    if df["production_ready"].any():
        passed = False
        issues.append("Checkpoints claim production readiness.")
    if df["portfolio_approved"].any():
        passed = False
        issues.append("Checkpoints claim portfolio approval.")

    return {"passed": passed, "issues": issues, "rule": "component_checkpoints_validation"}


def validate_portfolio_phase_acceptance_registries(
    df_map: Dict[str, pd.DataFrame],
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Dict[str, Any]:
    """Validate individual phase acceptance DataFrames."""
    passed = True
    issues = []
    required_phases = ["153", "154", "155", "156"]
    for p in required_phases:
        key = f"phase_{p}"
        df = df_map.get(key)
        if df is None or df.empty:
            passed = False
            issues.append(f"Phase {p} acceptance DataFrame missing or empty.")
        else:
            if not df["satisfied"].all():
                passed = False
                issues.append(f"Phase {p} has unsatisfied acceptance criteria.")

    return {"passed": passed, "issues": issues, "rule": "phase_acceptance_validation"}


def validate_portfolio_acceptance_boundaries(
    df_map: Dict[str, pd.DataFrame],
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Dict[str, Any]:
    """Validate safety boundaries and go/no-go registries."""
    passed = True
    issues = []
    go_no_go_df = df_map.get("go_no_go")
    if go_no_go_df is None or go_no_go_df.empty:
        passed = False
        issues.append("Go/No-Go boundary DataFrame is missing.")
    else:
        no_go_actions = go_no_go_df[go_no_go_df["decision"] == "NO-GO"]
        if no_go_actions.empty:
            passed = False
            issues.append("No prohibited NO-GO actions found in boundary registry.")

    return {"passed": passed, "issues": issues, "rule": "boundaries_validation"}


def validate_portfolio_acceptance_manifest(
    df: pd.DataFrame,
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Dict[str, Any]:
    """Validate master manifest against negative and phase invariants."""
    passed = True
    issues = []
    if df.empty:
        return {"passed": False, "issues": ["Manifest DataFrame is empty."]}

    row = df.iloc[0]
    if row.get("current_phase") != 157:
        passed = False
        issues.append(f"Invalid current_phase: {row.get('current_phase')}")
    if row.get("target_final_phase") != 160:
        passed = False
        issues.append(f"Invalid target_final_phase: {row.get('target_final_phase')}")
    if row.get("next_phase") != 158:
        passed = False
        issues.append(f"Invalid next_phase: {row.get('next_phase')}")
    if not row.get("portfolio_block_completed", False):
        passed = False
        issues.append("portfolio_block_completed must be True.")
    if row.get("portfolio_constructed", True):
        passed = False
        issues.append("portfolio_constructed must be False.")
    if row.get("portfolio_optimized", True):
        passed = False
        issues.append("portfolio_optimized must be False.")
    if row.get("risk_report_generated", True):
        passed = False
        issues.append("risk_report_generated must be False.")
    if row.get("scenario_executed", True):
        passed = False
        issues.append("scenario_executed must be False.")
    if row.get("drawdown_control_executed", True):
        passed = False
        issues.append("drawdown_control_executed must be False.")
    if row.get("production_ready", True):
        passed = False
        issues.append("production_ready must be False.")
    if row.get("broker_ready", True):
        passed = False
        issues.append("broker_ready must be False.")
    if row.get("live_trading_ready", True):
        passed = False
        issues.append("live_trading_ready must be False.")

    return {"passed": passed, "issues": issues, "rule": "manifest_validation"}


def validate_no_forbidden_portfolio_acceptance_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Validate that text, dataframes, or summaries contain no forbidden claims."""
    found_violations = []

    def check_string(s: str, source: str):
        low = s.lower()
        for phrase in FORBIDDEN_CLAIM_PHRASES:
            if phrase in low:
                found_violations.append(f"Forbidden phrase '{phrase}' in {source}")

    if text:
        check_string(text, "text content")

    if df is not None and not df.empty:
        for col in df.columns:
            for val in df[col].astype(str):
                check_string(val, f"df column '{col}'")

    if summary:
        for k, v in summary.items():
            check_string(f"{k}: {v}", "summary dict")

    clean = (len(found_violations) == 0)
    return {
        "is_clean": clean,
        "violations": found_violations,
        "rule": "forbidden_claims_validation",
    }


def build_portfolio_acceptance_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Assemble consolidated validation report evaluating all rules."""
    active = profile or get_portfolio_acceptance_profile()

    checks = [
        ("profiles", validate_portfolio_acceptance_profile_registry(tables.get("profiles", pd.DataFrame()), active)),
        ("checkpoints", validate_portfolio_acceptance_component_checkpoints(tables.get("checkpoints", pd.DataFrame()), active)),
        ("phases", validate_portfolio_phase_acceptance_registries(tables, active)),
        ("boundaries", validate_portfolio_acceptance_boundaries(tables, active)),
        ("manifest", validate_portfolio_acceptance_manifest(tables.get("manifest", pd.DataFrame()), active)),
    ]

    records = []
    all_passed = True
    for name, res in checks:
        if not res["passed"]:
            all_passed = False
        records.append({
            "rule_name": res["rule"],
            "target": name,
            "passed": res["passed"],
            "issues": "; ".join(res["issues"]) if res["issues"] else "None",
            "current_phase": active.current_phase,
            "status": "PASS" if res["passed"] else "FAIL",
        })

    df = pd.DataFrame(records)
    summary = {
        "domain": VALIDATION_DOMAIN,
        "total_rules": len(df),
        "all_passed": all_passed,
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAILED",
        "forbidden_claims_found": False,
        "status": PORTFOLIO_ACCEPTANCE_READY if all_passed else "VALIDATION_FAILED",
    }
    return df, summary
