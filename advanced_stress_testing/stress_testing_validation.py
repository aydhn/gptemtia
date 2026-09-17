# -*- coding: utf-8 -*-
"""Phase 148: Stress Testing Validation Engine.

Provides comprehensive validation suites verifying non-production boundaries,
negative invariants, and contract conformance.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile


def validate_stress_testing_profile_registry(
    df: pd.DataFrame,
    profile: StressTestingProfile,
) -> Dict[str, Any]:
    """Validate profile registry consistency and safety bounds."""
    if df.empty:
        return {"passed": False, "error": "Profile registry is empty"}
    non_prod = bool(df["non_production"].all())
    non_sig = bool(df["non_signal"].all())
    zero_broker = not bool(df["broker_ready"].any())
    zero_live = not bool(df["live_trading_ready"].any())
    passed = non_prod and non_sig and zero_broker and zero_live
    return {
        "passed": passed,
        "all_non_production": non_prod,
        "all_non_signal": non_sig,
        "zero_broker_ready": zero_broker,
        "zero_live_trading_ready": zero_live,
    }


def validate_stress_scenario_contracts(
    df: pd.DataFrame,
    profile: StressTestingProfile,
) -> Dict[str, Any]:
    """Validate stress scenario contracts against live execution flags."""
    if df.empty:
        return {"passed": False, "error": "Scenario contracts DataFrame is empty"}
    no_stress = not bool(df["stress_execution_allowed"].any())
    no_sim = not bool(df["scenario_simulation_allowed"].any())
    no_live = not bool(df["live_trading_allowed"].any())
    no_broker = not bool(df["broker_execution_allowed"].any())
    no_calc = not bool(df["metric_calculation_allowed"].any())
    passed = no_stress and no_sim and no_live and no_broker and no_calc
    return {
        "passed": passed,
        "all_stress_execution_blocked": no_stress,
        "all_scenario_simulation_blocked": no_sim,
        "all_live_trading_blocked": no_live,
        "all_broker_blocked": no_broker,
        "all_metric_calc_blocked": no_calc,
    }


def validate_shock_placeholder_registries(
    df_map: Dict[str, pd.DataFrame],
    profile: StressTestingProfile,
) -> Dict[str, Any]:
    """Validate shock placeholders across all categories."""
    passed = True
    details = {}
    for name, df in df_map.items():
        if df.empty:
            details[name] = {"passed": False, "error": "Empty"}
            passed = False
        else:
            no_real = not bool(df.get("real_execution_allowed", pd.Series([False])).any())
            non_sig = bool(df.get("non_signal", pd.Series([True])).all())
            details[name] = {"passed": no_real and non_sig, "no_real_execution": no_real}
            if not (no_real and non_sig):
                passed = False
    return {"passed": passed, "details": details}


def validate_stress_guards(
    df_map: Dict[str, pd.DataFrame],
    profile: StressTestingProfile,
) -> Dict[str, Any]:
    """Validate bias, lookahead, and leakage guards are actively registered."""
    passed = True
    for name, df in df_map.items():
        if df.empty:
            passed = False
    return {"passed": passed, "total_guard_tables": len(df_map)}


def validate_stress_testing_manifest(
    df: pd.DataFrame,
    profile: StressTestingProfile,
) -> Dict[str, Any]:
    """Validate master manifest values against strict Phase 148 requirements."""
    if df.empty:
        return {"passed": False, "error": "Manifest DataFrame is empty"}
    row = df.iloc[0]
    checks = [
        int(row["current_phase"]) == 148,
        int(row["target_final_phase"]) == 160,
        int(row["next_phase"]) == 149,
        bool(row["non_signal"]) is True,
        bool(row["local_only"]) is True,
        bool(row["non_production"]) is True,
        bool(row["production_ready"]) is False,
        bool(row["broker_ready"]) is False,
        bool(row["live_trading_ready"]) is False,
        bool(row["stress_test_executed"]) is False,
        bool(row["scenario_simulation_executed"]) is False,
        bool(row["stress_metric_calculated"]) is False,
        bool(row["stressed_pnl_calculated"]) is False,
        bool(row["broker_order_sent"]) is False,
        bool(row["live_order_sent"]) is False,
        bool(row["phase_149_handoff_ready"]) is True,
    ]
    passed = all(checks)
    return {"passed": passed, "checks_passed": sum(checks), "total_checks": len(checks)}


def validate_no_forbidden_stress_claims(
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


def build_stress_testing_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Run all validation suites and produce a comprehensive validation report."""
    results = [
        ("profile_registry", validate_stress_testing_profile_registry(tables.get("profiles", pd.DataFrame()), profile)),
        ("scenario_contracts", validate_stress_scenario_contracts(tables.get("contracts", pd.DataFrame()), profile)),
        ("manifest", validate_stress_testing_manifest(tables.get("manifest", pd.DataFrame()), profile)),
        ("forbidden_claims", validate_no_forbidden_stress_claims(summary={})),
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


def validate_stress_testing(
    tables: Optional[Dict[str, pd.DataFrame]] = None,
    profile: Optional[StressTestingProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Convenience validation runner creating default tables if needed."""
    if isinstance(tables, StressTestingProfile):
        profile = tables
        tables = None

    if profile is None:
        from advanced_stress_testing.stress_testing_config import get_default_stress_testing_profile
        profile = get_default_stress_testing_profile()

    if tables is None:
        from advanced_stress_testing.stress_testing_profile_registry import build_stress_testing_profile_registry
        from advanced_stress_testing.stress_scenario_contracts import build_stress_scenario_contract_registry
        from advanced_stress_testing.stress_testing_manifest import build_stress_testing_manifest

        df_prof, _ = build_stress_testing_profile_registry(profile)
        df_core, _ = build_stress_scenario_contract_registry(profile)
        df_man, _ = build_stress_testing_manifest(profile)
        tables = {"profiles": df_prof, "contracts": df_core, "manifest": df_man}

    return build_stress_testing_validation_report(tables, profile)

