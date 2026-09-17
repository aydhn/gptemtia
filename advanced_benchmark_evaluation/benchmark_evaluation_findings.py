# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Findings Module.

Tracks diagnostic findings, policy violations, and manual review requirements.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_FINDING_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)
from advanced_benchmark_evaluation.benchmark_evaluation_models import BenchmarkEvaluationFinding

INITIAL_FINDINGS: List[Dict[str, Any]] = [
    {
        "finding_id": "FIND_151_01",
        "finding_type": "contract_boundary_verified",
        "domain": "benchmark_report_contract_domain",
        "severity_label": "INFO",
        "message": "Benchmark comparison report contracts established with zero execution policy.",
        "recommendation": "Operator should inspect contract parameters prior to Phase 152.",
        "manual_review_required": True,
        "is_blocker": False,
    },
    {
        "finding_id": "FIND_151_02",
        "finding_type": "strategy_approval_locked",
        "domain": "strategy_evaluation_report_contract_domain",
        "severity_label": "INFO",
        "message": "Strategy approval and capital allocation strictly locked.",
        "recommendation": "Maintain approval lock; evaluations remain strictly empirical research hypotheses.",
        "manual_review_required": True,
        "is_blocker": False,
    },
    {
        "finding_id": "FIND_151_03",
        "finding_type": "metric_calculation_prohibited",
        "domain": "metric_placeholder_domain",
        "severity_label": "INFO",
        "message": "All metrics are uncalculated placeholders; zero numerical claims generated.",
        "recommendation": "Preserve uncalculated placeholders throughout Phase 151.",
        "manual_review_required": True,
        "is_blocker": False,
    },
]


def create_benchmark_evaluation_finding(
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
    is_blocker: bool = False,
) -> BenchmarkEvaluationFinding:
    """Factory function for creating a structured BenchmarkEvaluationFinding."""
    finding_id = f"FIND_{abs(hash((finding_type, message))) % 100000:05d}"
    return BenchmarkEvaluationFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        is_blocker=is_blocker,
    )


def build_benchmark_evaluation_findings_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of evaluation findings."""
    rows: List[Dict[str, Any]] = []

    for f in INITIAL_FINDINGS:
        rows.append(
            {
                "finding_id": f["finding_id"],
                "finding_type": f["finding_type"],
                "domain": f["domain"],
                "severity_label": f["severity_label"],
                "message": f["message"],
                "recommendation": f["recommendation"],
                "manual_review_required": f["manual_review_required"],
                "is_blocker": f["is_blocker"],
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    critical_count = int((df["severity_label"] == "CRITICAL").sum()) if not df.empty else 0
    blocker_count = int(df["is_blocker"].sum()) if not df.empty else 0

    summary = {
        "domain": LABEL_FINDING_DOMAIN,
        "total_findings": len(df),
        "critical_count": critical_count,
        "blocker_count": blocker_count,
        "has_blockers": blocker_count > 0,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
