# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Model Health Checks."""

from typing import Any, Dict
from advanced_ensemble_model_registry.candidate_model_contracts import (
    build_candidate_model_contracts,
    validate_candidate_model_contracts,
)
from advanced_ensemble_model_registry.candidate_model_eligibility_gates import (
    build_candidate_model_eligibility_gates,
    validate_candidate_model_eligibility_gates,
)
from advanced_ensemble_model_registry.candidate_model_compatibility_matrix import (
    build_candidate_compatibility_matrix,
    validate_candidate_compatibility_matrix,
)
from advanced_ensemble_model_registry.ensemble_strategy_contracts import (
    build_ensemble_strategy_contracts,
    validate_ensemble_strategy_contracts,
)
from advanced_ensemble_model_registry.ensemble_execution_disabled import (
    build_ensemble_execution_disabled_report,
    validate_ensemble_execution_disabled_report,
)
from advanced_ensemble_model_registry.ensemble_no_lookahead_guards import (
    build_ensemble_no_lookahead_guards,
    validate_ensemble_no_lookahead_guards,
)
from advanced_ensemble_model_registry.ensemble_metadata_only_news_guards import (
    build_ensemble_metadata_only_news_guards,
    validate_ensemble_metadata_only_news_guards,
)


def check_ensemble_model_health() -> Dict[str, Any]:
    """Run comprehensive health checks on Phase 140 ensemble model contracts and registry.
    
    Returns:
        Dict[str, Any]: Health check status report.
    """
    candidate_contracts = build_candidate_model_contracts()
    gates = build_candidate_model_eligibility_gates()
    matrix = build_candidate_compatibility_matrix()
    strategies = build_ensemble_strategy_contracts()
    exec_report = build_ensemble_execution_disabled_report()
    lookahead_guards = build_ensemble_no_lookahead_guards()
    news_guards = build_ensemble_metadata_only_news_guards()
    
    checks = {
        "candidate_contracts_valid": validate_candidate_model_contracts(candidate_contracts),
        "eligibility_gates_valid": validate_candidate_model_eligibility_gates(gates),
        "compatibility_matrix_valid": validate_candidate_compatibility_matrix(matrix),
        "strategy_contracts_valid": validate_ensemble_strategy_contracts(strategies),
        "execution_disabled_valid": validate_ensemble_execution_disabled_report(exec_report),
        "lookahead_guards_valid": validate_ensemble_no_lookahead_guards(lookahead_guards),
        "news_guards_valid": validate_ensemble_metadata_only_news_guards(news_guards),
    }
    
    all_healthy = all(checks.values())
    
    return {
        "status": "HEALTHY" if all_healthy else "UNHEALTHY",
        "phase": 140,
        "checks": checks,
        "total_checks": len(checks),
        "passed_checks": sum(1 for v in checks.values() if v),
        "non_signal": True,
        "dry_run": True,
    }


def validate_ensemble_model_health_report(report: Dict[str, Any]) -> bool:
    """Validate health report.
    
    Args:
        report: Health report dict.
        
    Returns:
        bool: True if healthy and non-signal, False otherwise.
    """
    if not isinstance(report, dict):
        return False
    if report.get("status") != "HEALTHY":
        return False
    if not report.get("non_signal", False):
        return False
    checks = report.get("checks", {})
    return all(checks.values()) if checks else False


def summarize_ensemble_model_health_report(report: Dict[str, Any]) -> Dict[str, Any]:
    """Summarize health report.
    
    Args:
        report: Health report dict.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "status": report.get("status"),
        "phase": report.get("phase", 140),
        "passed_checks": report.get("passed_checks", 0),
        "total_checks": report.get("total_checks", 0),
        "all_passed": validate_ensemble_model_health_report(report),
        "dry_run": True,
        "non_signal": True,
    }
