# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Validation Module.

Validates profile registries, contracts, guards, manifests, and texts against forbidden claims.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_VALIDATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)
from advanced_benchmark_evaluation.evaluation_result_claim_guards import validate_evaluation_result_claim_request
from advanced_benchmark_evaluation.evaluation_performance_claim_guards import validate_evaluation_performance_claim_request
from advanced_benchmark_evaluation.evaluation_strategy_approval_guards import validate_evaluation_strategy_approval_request


def validate_benchmark_evaluation_profile_registry(
    df: pd.DataFrame,
    profile: BenchmarkEvaluationProfile | None = None,
) -> Dict[str, Any]:
    """Validate profile registry compliance."""
    if df.empty:
        return {"suite": "profile_registry", "passed": False, "issue": "DataFrame is empty"}
    dry_run_ok = bool(df["dry_run_default"].all())
    local_ok = bool(df["local_only"].all())
    live_blocked = not bool(df["allow_live_trading"].any())
    passed = dry_run_ok and local_ok and live_blocked
    return {
        "suite": "profile_registry",
        "passed": passed,
        "dry_run_ok": dry_run_ok,
        "local_ok": local_ok,
        "live_blocked": live_blocked,
        "non_signal": True,
    }


def validate_benchmark_report_contracts(
    df: pd.DataFrame,
    profile: BenchmarkEvaluationProfile | None = None,
) -> Dict[str, Any]:
    """Validate benchmark comparison report contracts."""
    if df.empty:
        return {"suite": "benchmark_contracts", "passed": False, "issue": "DataFrame is empty"}
    exec_blocked = not bool(df["benchmark_execution_allowed"].any())
    metrics_blocked = not bool(df["metric_calculation_allowed"].any())
    claims_blocked = not bool(df["result_claim_allowed"].any())
    passed = exec_blocked and metrics_blocked and claims_blocked
    return {
        "suite": "benchmark_contracts",
        "passed": passed,
        "execution_blocked": exec_blocked,
        "metrics_blocked": metrics_blocked,
        "claims_blocked": claims_blocked,
        "non_signal": True,
    }


def validate_strategy_evaluation_report_contracts(
    df: pd.DataFrame,
    profile: BenchmarkEvaluationProfile | None = None,
) -> Dict[str, Any]:
    """Validate strategy evaluation report contracts."""
    if df.empty:
        return {"suite": "strategy_contracts", "passed": False, "issue": "DataFrame is empty"}
    approvals_blocked = not bool(df["strategy_approval_allowed"].any())
    alloc_blocked = not bool(df["capital_allocation_allowed"].any())
    passed = approvals_blocked and alloc_blocked
    return {
        "suite": "strategy_contracts",
        "passed": passed,
        "approvals_blocked": approvals_blocked,
        "allocation_blocked": alloc_blocked,
        "non_signal": True,
    }


def validate_evaluation_guards(
    df_map: Dict[str, pd.DataFrame],
    profile: BenchmarkEvaluationProfile | None = None,
) -> Dict[str, Any]:
    """Validate active status across guard tables."""
    all_active = True
    for name, df in df_map.items():
        if not df.empty and "is_active" in df.columns:
            if not bool(df["is_active"].all()):
                all_active = False
    return {"suite": "guards", "passed": all_active, "all_active": all_active, "non_signal": True}


def validate_benchmark_evaluation_manifest(
    df: pd.DataFrame,
    profile: BenchmarkEvaluationProfile | None = None,
) -> Dict[str, Any]:
    """Validate manifest invariant rows."""
    if df.empty:
        return {"suite": "manifest", "passed": False, "issue": "Manifest is empty"}
    m_dict = dict(zip(df["property"], df["value"]))
    c_phase = int(m_dict.get("current_phase", 0)) == 151
    t_phase = int(m_dict.get("target_final_phase", 0)) == 160
    n_phase = int(m_dict.get("next_phase", 0)) == 152
    non_prod = bool(m_dict.get("non_production", False))
    no_live = not bool(m_dict.get("live_trading_ready", True))
    no_exec = not bool(m_dict.get("benchmark_report_executed", True))
    passed = c_phase and t_phase and n_phase and non_prod and no_live and no_exec
    return {
        "suite": "manifest",
        "passed": passed,
        "current_phase_ok": c_phase,
        "negative_invariants_ok": no_live and no_exec,
        "non_signal": True,
    }


def validate_no_forbidden_benchmark_evaluation_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Inspect text, dataframe, or summary for forbidden claims."""
    content_list: List[str] = []
    if text:
        content_list.append(text)
    if summary:
        content_list.append(" ".join(str(v) for v in summary.values()))
    if df is not None and not df.empty:
        for val in df.astype(str).values.flatten():
            s_val = str(val)
            if "guard" in s_val.lower() or s_val in ("True", "False", "None"):
                continue
            content_list.append(s_val)

    full_content = " ".join(content_list)
    r1 = validate_evaluation_result_claim_request(full_content)
    r2 = validate_evaluation_performance_claim_request(full_content)
    r3 = validate_evaluation_strategy_approval_request(full_content)

    clean = r1["is_clean"] and r2["is_clean"] and r3["is_clean"]
    return {
        "is_clean": clean,
        "result_claim_clean": r1["is_clean"],
        "performance_claim_clean": r2["is_clean"],
        "strategy_approval_clean": r3["is_clean"],
        "status": "PASS" if clean else "FAIL",
        "non_signal": True,
    }


def build_benchmark_evaluation_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build consolidated validation report across all suites."""
    results: List[Dict[str, Any]] = []

    # 1. Profile registry validation
    if "profiles" in tables:
        r_prof = validate_benchmark_evaluation_profile_registry(tables["profiles"], profile)
        results.append({"suite": "profiles", "status": "PASS" if r_prof["passed"] else "FAIL"})

    # 2. Benchmark contracts validation
    if "benchmark_contracts" in tables:
        r_bench = validate_benchmark_report_contracts(tables["benchmark_contracts"], profile)
        results.append({"suite": "benchmark_contracts", "status": "PASS" if r_bench["passed"] else "FAIL"})

    # 3. Strategy contracts validation
    if "strategy_contracts" in tables:
        r_strat = validate_strategy_evaluation_report_contracts(tables["strategy_contracts"], profile)
        results.append({"suite": "strategy_contracts", "status": "PASS" if r_strat["passed"] else "FAIL"})

    # 4. Manifest validation
    if "manifest" in tables:
        r_man = validate_benchmark_evaluation_manifest(tables["manifest"], profile)
        results.append({"suite": "manifest", "status": "PASS" if r_man["passed"] else "FAIL"})

    # 5. Forbidden claims validation
    r_claim = validate_no_forbidden_benchmark_evaluation_claims(df=tables.get("benchmark_contracts"))
    results.append({"suite": "forbidden_claims", "status": r_claim["status"]})

    df = pd.DataFrame(results)
    all_passed = bool((df["status"] == "PASS").all()) if not df.empty else True

    summary = {
        "domain": LABEL_VALIDATION_DOMAIN,
        "total_checks": len(df),
        "all_passed": all_passed,
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
