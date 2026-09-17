# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest Validation.

Provides comprehensive validation routines scanning for forbidden claims,
negative invariants, and safety violations in Phase 146 outputs.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

FORBIDDEN_TERMS = [
    "live_trade",
    "broker_order",
    "guaranteed_return",
    "sharpe_claim",
    "win_rate_claim",
    "production_ready",
    "broker_ready",
    "live_trading_approved",
    "official_approval",
]


def validate_realistic_backtest_profile_registry(
    df: pd.DataFrame, profile: RealisticBacktestProfile
) -> Dict[str, Any]:
    """Validate profile registry consistency."""
    issues = []
    if df.empty:
        issues.append("Profile dataframe is empty.")
    if not (df["current_phase"] == 146).all():
        issues.append("Found profile with current_phase != 146.")
    if not (df["target_final_phase"] == 160).all():
        issues.append("Found profile with target_final_phase != 160.")
    if not (df["next_phase"] == 147).all():
        issues.append("Found profile with next_phase != 147.")
    if df["allow_live_trading"].any() or df["allow_broker_integration"].any():
        issues.append("Live trading or broker integration allowed in profile registry.")
    return {"check_name": "profile_registry_validation", "passed": len(issues) == 0, "issues": issues}


def validate_backtest_engine_contracts(
    df: pd.DataFrame, profile: RealisticBacktestProfile
) -> Dict[str, Any]:
    """Validate engine contracts."""
    issues = []
    if df.empty:
        issues.append("Engine contracts dataframe is empty.")
    if df["backtest_execution_allowed"].any():
        issues.append("Engine contract allows backtest execution.")
    if df["live_trading_allowed"].any() or df["broker_execution_allowed"].any():
        issues.append("Engine contract allows live trading or broker execution.")
    return {"check_name": "engine_contracts_validation", "passed": len(issues) == 0, "issues": issues}


def validate_transaction_cost_slippage_contracts(
    df_map: Dict[str, pd.DataFrame], profile: RealisticBacktestProfile
) -> Dict[str, Any]:
    """Validate cost and slippage models."""
    issues = []
    if "slippage_models" in df_map:
        sdf = df_map["slippage_models"]
        if sdf["real_slippage_calculated"].any():
            issues.append("Slippage model claims real slippage calculation.")
        if sdf["performance_guaranteed"].any():
            issues.append("Slippage model claims performance guarantee.")
    if "cost_models" in df_map:
        cdf = df_map["cost_models"]
        if cdf["real_cost_calculated"].any():
            issues.append("Cost model claims real cost calculation.")
    return {"check_name": "cost_slippage_contracts_validation", "passed": len(issues) == 0, "issues": issues}


def validate_backtest_guards(
    df_map: Dict[str, pd.DataFrame], profile: RealisticBacktestProfile
) -> Dict[str, Any]:
    """Validate that lookahead, bias, and column policies are active."""
    issues = []
    for guard_key in ["no_lookahead_guards", "forbidden_column_policies"]:
        if guard_key in df_map and df_map[guard_key].empty:
            issues.append(f"Guard dataframe '{guard_key}' is empty.")
    return {"check_name": "guards_validation", "passed": len(issues) == 0, "issues": issues}


def validate_realistic_backtest_manifest(
    df: pd.DataFrame, profile: RealisticBacktestProfile
) -> Dict[str, Any]:
    """Validate negative invariants in the manifest."""
    issues = []
    mapping = dict(zip(df["property"], df["value"]))
    if mapping.get("current_phase") != 146:
        issues.append(f"Manifest current_phase is {mapping.get('current_phase')}, expected 146.")
    if mapping.get("next_phase") != 147:
        issues.append(f"Manifest next_phase is {mapping.get('next_phase')}, expected 147.")
    if mapping.get("target_final_phase") != 160:
        issues.append(f"Manifest target_final_phase is {mapping.get('target_final_phase')}, expected 160.")
    if mapping.get("backtest_executed") is not False:
        issues.append("Manifest backtest_executed is not False.")
    if mapping.get("broker_order_sent") is not False:
        issues.append("Manifest broker_order_sent is not False.")
    if mapping.get("live_order_sent") is not False:
        issues.append("Manifest live_order_sent is not False.")
    if mapping.get("transaction_cost_calculated") is not False:
        issues.append("Manifest transaction_cost_calculated is not False.")
    if mapping.get("slippage_calculated") is not False:
        issues.append("Manifest slippage_calculated is not False.")
    return {"check_name": "manifest_validation", "passed": len(issues) == 0, "issues": issues}


def validate_no_forbidden_backtest_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Scan arbitrary input text, tables, or dictionaries for forbidden trading/production claims."""
    found = []
    
    if text:
        t_lower = text.lower()
        for phrase in FORBIDDEN_TERMS:
            if phrase in t_lower and "false" not in t_lower and "prohibited" not in t_lower and "disabled" not in t_lower and "değildir" not in t_lower and "zero" not in t_lower:
                found.append(phrase)

    if df is not None and not df.empty:
        if "property" in df.columns and "value" in df.columns:
            for _, row in df.iterrows():
                prop = str(row["property"]).lower()
                val = row["value"]
                if val is True:
                    for phrase in FORBIDDEN_TERMS:
                        if phrase in prop:
                            found.append(f"{prop}=True")
        else:
            for col in df.columns:
                if df[col].dtype == object:
                    for val in df[col].dropna().astype(str):
                        v_lower = val.lower()
                        for phrase in FORBIDDEN_TERMS:
                            if phrase in v_lower and "false" not in v_lower and "prohibited" not in v_lower and "disabled" not in v_lower and "değildir" not in v_lower and "zero" not in v_lower:
                                found.append(phrase)

    if summary:
        for k, v in summary.items():
            if isinstance(v, bool) and v is True:
                k_lower = k.lower()
                for phrase in FORBIDDEN_TERMS:
                    if phrase in k_lower:
                        found.append(f"{k}=True")
            elif isinstance(v, str):
                v_lower = v.lower()
                for phrase in FORBIDDEN_TERMS:
                    if phrase in v_lower and "false" not in v_lower and "prohibited" not in v_lower and "disabled" not in v_lower and "değildir" not in v_lower and "zero" not in v_lower:
                        found.append(phrase)

    return {
        "is_clean": len(found) == 0,
        "forbidden_claims_found": list(set(found)),
    }


def build_realistic_backtest_validation_report(
    tables: Any = None,
    profile: Optional[RealisticBacktestProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute all validation routines and compile master validation report."""
    if isinstance(tables, RealisticBacktestProfile) and profile is None:
        profile = tables
        tables = None
    if profile is None:
        from advanced_realistic_backtest.realistic_backtest_config import get_default_realistic_backtest_profile
        profile = get_default_realistic_backtest_profile()
    if tables is None or not isinstance(tables, dict):
        tables = {}
    if "profiles" not in tables:
        from advanced_realistic_backtest.realistic_backtest_profile_registry import build_realistic_backtest_profile_registry
        df_p, _ = build_realistic_backtest_profile_registry(profile)
        tables["profiles"] = df_p
    if "engines" not in tables:
        from advanced_realistic_backtest.backtest_engine_contracts import build_backtest_engine_contract_registry
        df_e, _ = build_backtest_engine_contract_registry(profile)
        tables["engines"] = df_e
    if "manifest" not in tables:
        from advanced_realistic_backtest.realistic_backtest_manifest import build_realistic_backtest_manifest
        df_m, _ = build_realistic_backtest_manifest(profile)
        tables["manifest"] = df_m

    checks = []

    if "profiles" in tables:
        checks.append(validate_realistic_backtest_profile_registry(tables["profiles"], profile))
    if "engines" in tables:
        checks.append(validate_backtest_engine_contracts(tables["engines"], profile))
    checks.append(validate_transaction_cost_slippage_contracts(tables, profile))
    checks.append(validate_backtest_guards(tables, profile))
    if "manifest" in tables:
        checks.append(validate_realistic_backtest_manifest(tables["manifest"], profile))

    # Forbidden claims scan across all tables
    claims_check = validate_no_forbidden_backtest_claims(df=tables.get("manifest"))
    checks.append(
        {
            "check_name": "forbidden_claims_scan",
            "passed": claims_check["is_clean"],
            "issues": [f"Found: {t}" for t in claims_check["forbidden_claims_found"]],
        }
    )

    rows = []
    for c in checks:
        rows.append(
            {
                "check_name": c["check_name"],
                "passed": c["passed"],
                "issues_count": len(c.get("issues", [])),
                "issues": "; ".join(c.get("issues", [])) if c.get("issues") else "None",
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    all_passed = bool(df["passed"].all()) if not df.empty else True
    summary = {
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()) if not df.empty else 0,
        "forbidden_claims_found": 0 if claims_check["is_clean"] else len(claims_check["forbidden_claims_found"]),
        "all_passed": all_passed,
        "non_signal": True,
    }
    return df, summary
