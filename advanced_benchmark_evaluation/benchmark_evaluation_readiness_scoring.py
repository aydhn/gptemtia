# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Readiness Scoring Module.

Calculates contract completeness score and classifies readiness status.
Strictly non-signal and non-production.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    BenchmarkEvaluationProfile,
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_READINESS_SCORE_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)
from advanced_benchmark_evaluation.benchmark_evaluation_models import BenchmarkEvaluationReadinessScore


def classify_benchmark_evaluation_readiness_score(score: float) -> str:
    """Classify the numeric readiness score into standard status labels."""
    if score < 0.25:
        return "blocked"
    elif score < 0.50:
        return "incomplete"
    elif score < 0.75:
        return "contract_ready_with_manual_review"
    else:
        return "benchmark_evaluation_contract_ready_non_production"


def calculate_benchmark_evaluation_readiness_score(
    findings_df: pd.DataFrame | None = None,
    profile: BenchmarkEvaluationProfile | None = None,
) -> BenchmarkEvaluationReadinessScore:
    """Calculate readiness score based on findings and profile invariants."""
    prof = profile or get_default_benchmark_evaluation_profile()

    base_score = 1.0
    if findings_df is not None and not findings_df.empty:
        critical_count = (findings_df["severity_label"] == "CRITICAL").sum()
        blocker_count = findings_df["is_blocker"].sum()
        base_score -= (critical_count * 0.25 + blocker_count * 0.50)
        base_score = max(0.0, min(1.0, float(base_score)))

    classification = classify_benchmark_evaluation_readiness_score(base_score)
    meets_threshold = base_score >= prof.min_readiness_score

    return BenchmarkEvaluationReadinessScore(
        score=base_score,
        classification=classification,
        meets_threshold=meets_threshold,
        current_phase=prof.current_phase,
        target_final_phase=prof.target_final_phase,
        next_phase=prof.next_phase,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
    )


def build_benchmark_evaluation_readiness_score_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report of readiness score."""
    prof = profile or get_default_benchmark_evaluation_profile()
    res = calculate_benchmark_evaluation_readiness_score(None, prof)

    rows = [
        {
            "metric": "readiness_score",
            "score": res.score,
            "classification": res.classification,
            "meets_threshold": res.meets_threshold,
            "min_threshold": prof.min_readiness_score,
            "current_phase": res.current_phase,
            "next_phase": res.next_phase,
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_READINESS_SCORE_DOMAIN,
        "score": res.score,
        "classification": res.classification,
        "meets_threshold": res.meets_threshold,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
