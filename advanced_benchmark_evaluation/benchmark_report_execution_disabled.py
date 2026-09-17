# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Report Execution Disabled Module.

Formally documents and enforces the prohibition of real benchmark execution or live simulation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DISABLED_EXECUTION_DOMAIN,
    EXEC_BLOCKED_NO_BENCHMARK_REPORT,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_BENCHMARK_EXECUTION_TERMS = [
    "run_benchmark_report",
    "execute_benchmark",
    "run_benchmark_simulation",
    "execute_baseline",
    "simulate_benchmark",
]


def build_benchmark_report_execution_disabled_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying benchmark report execution is disabled."""
    rows = [
        {
            "operation": "benchmark_execution",
            "is_disabled": True,
            "policy_code": EXEC_BLOCKED_NO_BENCHMARK_REPORT,
            "reason": "Phase 151 is strictly a contract and placeholder layer; zero real execution permitted.",
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DISABLED_EXECUTION_DOMAIN,
        "operation": "benchmark_execution",
        "is_disabled": True,
        "status": EXEC_BLOCKED_NO_BENCHMARK_REPORT,
        "non_signal": True,
    }
    return df, summary


def validate_no_benchmark_report_execution_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no benchmark execution was requested."""
    text_to_check = request if isinstance(request, str) else " ".join(str(v) for v in request.values())
    text_lower = text_to_check.lower()

    detected = [term for term in FORBIDDEN_BENCHMARK_EXECUTION_TERMS if term in text_lower]
    is_blocked = len(detected) > 0

    return {
        "is_permitted": not is_blocked,
        "is_blocked": is_blocked,
        "detected_terms": detected,
        "status": "PASS" if not is_blocked else EXEC_BLOCKED_NO_BENCHMARK_REPORT,
        "policy_action": "ALLOW" if not is_blocked else "EXECUTION_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
