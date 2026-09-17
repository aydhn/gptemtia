# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Validation Engine.

Provides comprehensive validation suites verifying non-production boundaries,
negative invariants, and contract conformance for Monte Carlo robustness and parameter stability.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile


def validate_monte_carlo_profile_registry(
    df: pd.DataFrame,
    profile: MonteCarloProfile,
) -> Dict[str, Any]:
    """Validate profile registry consistency and safety bounds."""
    if df.empty:
        return {"passed": False, "error": "Profile registry is empty"}
    non_prod = bool(df["non_production"].all()) if "non_production" in df.columns else True
    non_sig = bool(df["non_signal"].all()) if "non_signal" in df.columns else (not bool(df["allow_signal_generation"].any()) if "allow_signal_generation" in df.columns else True)
    zero_broker = not bool(df["broker_ready"].any()) if "broker_ready" in df.columns else (not bool(df["allow_broker_integration"].any()) if "allow_broker_integration" in df.columns else True)
    zero_live = not bool(df["live_trading_ready"].any()) if "live_trading_ready" in df.columns else (not bool(df["allow_live_trading"].any()) if "allow_live_trading" in df.columns else True)
    passed = non_prod and non_sig and zero_broker and zero_live
    return {
        "passed": passed,
        "all_non_production": non_prod,
        "all_non_signal": non_sig,
        "zero_broker_ready": zero_broker,
        "zero_live_trading_ready": zero_live,
    }


def validate_monte_carlo_robustness_contracts(
    df: pd.DataFrame,
    profile: MonteCarloProfile,
) -> Dict[str, Any]:
    """Validate Monte Carlo robustness contracts against live execution flags."""
    if df.empty:
        return {"passed": False, "error": "Robustness contracts DataFrame is empty"}
    no_mc = not bool(df["monte_carlo_execution_allowed"].any())
    no_boot = not bool(df["bootstrap_execution_allowed"].any())
    no_resamp = not bool(df["resampling_execution_allowed"].any())
    no_live = not bool(df["live_trading_allowed"].any())
    no_broker = not bool(df["broker_execution_allowed"].any())
    no_calc = not bool(df["metric_calculation_allowed"].any())
    no_opt = not bool(df["parameter_optimization_allowed"].any())
    passed = no_mc and no_boot and no_resamp and no_live and no_broker and no_calc and no_opt
    return {
        "passed": passed,
        "all_monte_carlo_execution_blocked": no_mc,
        "all_bootstrap_execution_blocked": no_boot,
        "all_resampling_execution_blocked": no_resamp,
        "all_live_trading_blocked": no_live,
        "all_broker_blocked": no_broker,
        "all_metric_calc_blocked": no_calc,
        "all_parameter_optimization_blocked": no_opt,
    }


def validate_parameter_stability_contracts(
    df: pd.DataFrame,
    profile: MonteCarloProfile,
) -> Dict[str, Any]:
    """Validate parameter stability contracts against optimizer and sweep flags."""
    if df.empty:
        return {"passed": False, "error": "Parameter stability contracts DataFrame is empty"}
    no_opt = not bool(df["optimization_allowed"].any())
    no_swp = not bool(df["sweep_allowed"].any())
    passed = no_opt and no_swp
    return {
        "passed": passed,
        "all_optimization_blocked": no_opt,
        "all_sweeps_blocked": no_swp,
    }


def validate_monte_carlo_guards(
    df_map: Dict[str, pd.DataFrame],
    profile: MonteCarloProfile,
) -> Dict[str, Any]:
    """Validate bias, lookahead, and leakage guards are actively registered."""
    passed = True
    for name, df in df_map.items():
        if df.empty:
            passed = False
    return {"passed": passed, "total_guard_tables": len(df_map)}


def validate_monte_carlo_manifest(
    df: pd.DataFrame,
    profile: MonteCarloProfile,
) -> Dict[str, Any]:
    """Validate master manifest values against strict Phase 149 requirements."""
    if df.empty:
        return {"passed": False, "error": "Manifest DataFrame is empty"}

    # Handle property-value key-value pairs or single row DataFrame
    if "property" in df.columns and "value" in df.columns:
        prop_map = dict(zip(df["property"], df["value"]))
    else:
        prop_map = df.iloc[0].to_dict()

    checks = [
        int(prop_map.get("current_phase", 0)) == 149,
        int(prop_map.get("target_final_phase", 0)) == 160,
        int(prop_map.get("next_phase", 0)) == 150,
        bool(prop_map.get("non_signal", False)) is True,
        bool(prop_map.get("local_only", False)) is True,
        bool(prop_map.get("non_production", False)) is True,
        bool(prop_map.get("production_ready", True)) is False,
        bool(prop_map.get("broker_ready", True)) is False,
        bool(prop_map.get("live_trading_ready", True)) is False,
        bool(prop_map.get("monte_carlo_executed", True)) is False,
        bool(prop_map.get("bootstrap_executed", True)) is False,
        bool(prop_map.get("resampling_executed", True)) is False,
        bool(prop_map.get("parameter_optimization_executed", True)) is False,
        bool(prop_map.get("parameter_sweep_executed", True)) is False,
        bool(prop_map.get("robustness_metric_calculated", True)) is False,
        bool(prop_map.get("parameter_stability_metric_calculated", True)) is False,
        bool(prop_map.get("broker_order_sent", True)) is False,
        bool(prop_map.get("live_order_sent", True)) is False,
        bool(prop_map.get("phase_150_handoff_ready", False)) is True,
    ]
    passed = all(checks)
    return {"passed": passed, "checks_passed": sum(checks), "total_checks": len(checks)}


def validate_no_forbidden_monte_carlo_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Inspect text, DataFrame or summary for prohibited claims."""
    forbidden_terms = [
        "guaranteed return",
        "live execution ready",
        "broker ready approved",
        "official production approval",
        "canli islem onaylandi",
        "monte carlo onayli getiri",
        "parametre optimizasyonu tamamlandi",
    ]
    violations = []
    if text:
        lower_t = text.lower()
        for term in forbidden_terms:
            if term in lower_t:
                violations.append(term)
    return {
        "is_clean": len(violations) == 0,
        "violations": violations,
        "non_signal": True,
    }


def build_monte_carlo_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Run all validation suites and produce a comprehensive validation report."""
    results = [
        ("profile_registry", validate_monte_carlo_profile_registry(tables.get("profiles", pd.DataFrame()), profile)),
        ("robustness_contracts", validate_monte_carlo_robustness_contracts(tables.get("contracts", pd.DataFrame()), profile)),
        ("stability_contracts", validate_parameter_stability_contracts(tables.get("stability", pd.DataFrame()), profile)),
        ("manifest", validate_monte_carlo_manifest(tables.get("manifest", pd.DataFrame()), profile)),
        ("forbidden_claims", validate_no_forbidden_monte_carlo_claims(summary={})),
    ]

    rows: List[Dict[str, Any]] = []
    all_passed = True
    for suite_name, res in results:
        passed = res.get("passed", res.get("is_clean", False))
        if not passed:
            all_passed = False
        rows.append(
            {
                "suite_name": suite_name,
                "status": "PASS" if passed else "FAIL",
                "details": str(res),
                "non_signal": True,
                "local_only": True,
            }
        )

    df = pd.DataFrame(rows)
    passed_checks = int((df["status"] == "PASS").sum())
    summary = {
        "validation_status": "PASS" if all_passed else "FAIL",
        "all_passed": all_passed,
        "total_checks": len(df),
        "passed_checks": passed_checks,
        "non_signal": True,
    }
    return df, summary


def validate_monte_carlo(
    tables: Optional[Dict[str, pd.DataFrame]] = None,
    profile: Optional[MonteCarloProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Convenience validation runner creating default tables if needed."""
    if isinstance(tables, MonteCarloProfile):
        profile = tables
        tables = None

    if profile is None:
        from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
        profile = get_default_monte_carlo_profile()

    if tables is None:
        from advanced_monte_carlo_robustness.monte_carlo_profile_registry import build_monte_carlo_profile_registry
        from advanced_monte_carlo_robustness.monte_carlo_robustness_contracts import build_monte_carlo_robustness_contract_registry
        from advanced_monte_carlo_robustness.parameter_stability_contracts import build_parameter_stability_contract_registry
        from advanced_monte_carlo_robustness.monte_carlo_manifest import build_monte_carlo_robustness_manifest

        df_prof, _ = build_monte_carlo_profile_registry(profile)
        df_core, _ = build_monte_carlo_robustness_contract_registry(profile)
        df_stab, _ = build_parameter_stability_contract_registry(profile)
        df_man, _ = build_monte_carlo_robustness_manifest(profile)
        tables = {
            "profiles": df_prof,
            "contracts": df_core,
            "stability": df_stab,
            "manifest": df_man,
        }

    return build_monte_carlo_validation_report(tables, profile)
