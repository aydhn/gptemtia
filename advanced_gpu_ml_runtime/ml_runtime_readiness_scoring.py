"""Phase 136: ML Runtime Readiness Scoring.

Calculates an operational readiness score reflecting hardware and runtime capability status.
Strictly non-signal, non-production, and not an approval for model training.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    READINESS_SCORE_DOMAIN,
    RUNTIME_READY,
    RUNTIME_READY_WITH_WARNINGS,
    RUNTIME_MANUAL_REVIEW_REQUIRED,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_models import MlRuntimeReadinessScore
from advanced_gpu_ml_runtime.local_hardware_discovery import build_local_hardware_discovery_report
from advanced_gpu_ml_runtime.gpu_capability_registry import build_gpu_capability_registry
from advanced_gpu_ml_runtime.cpu_capability_registry import build_cpu_capability_registry
from advanced_gpu_ml_runtime.memory_capability_registry import build_memory_capability_registry
from advanced_gpu_ml_runtime.optional_ml_dependency_registry import build_optional_ml_dependency_registry
from advanced_gpu_ml_runtime.ml_runtime_safety_contracts import build_ml_runtime_safety_contract_registry
from advanced_gpu_ml_runtime.ml_experiment_permission_policies import build_ml_experiment_permission_policy_registry
from advanced_gpu_ml_runtime.regime_metadata_ml_input_contracts import build_regime_metadata_ml_input_contract_registry
from advanced_gpu_ml_runtime.ml_runtime_findings import build_ml_runtime_findings_registry
from advanced_gpu_ml_runtime.ml_runtime_manual_review import build_ml_runtime_manual_review_queue


def classify_ml_runtime_readiness_score(score: float) -> str:
    """Classify readiness score into standard status label."""
    if score >= 0.85:
        return RUNTIME_READY
    elif score >= 0.50:
        return RUNTIME_READY_WITH_WARNINGS
    else:
        return RUNTIME_MANUAL_REVIEW_REQUIRED


def calculate_ml_runtime_readiness_score(
    findings_df: Optional[pd.DataFrame] = None,
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> MlRuntimeReadinessScore:
    """Compute score based on hardware discovery, dependencies, and findings."""
    active = profile or get_gpu_ml_runtime_profile()

    if findings_df is None:
        f_df, _ = build_ml_runtime_findings_registry(active)
        findings_df = f_df

    hw_df, _ = build_local_hardware_discovery_report(active)
    gpu_df, _ = build_gpu_capability_registry(active)
    cpu_df, _ = build_cpu_capability_registry(active)
    mem_df, _ = build_memory_capability_registry(active)
    dep_df, _ = build_optional_ml_dependency_registry(active)
    safety_df, _ = build_ml_runtime_safety_contract_registry(active)
    perm_df, _ = build_ml_experiment_permission_policy_registry(active)
    input_df, _ = build_regime_metadata_ml_input_contract_registry(active)
    review_df, _ = build_ml_runtime_manual_review_queue(active)

    # Base score: platform & CPU ready + safety policies enforced
    base_score = 0.60

    # Boost if CUDA GPU is available
    has_cuda = bool(gpu_df.get("cuda_available", pd.Series([False])).any())
    if has_cuda:
        base_score += 0.25

    # Boost if memory is sufficient
    mem_sufficient = bool((mem_df.get("status_label", pd.Series([""])) == RUNTIME_READY).all())
    if mem_sufficient:
        base_score += 0.10

    # Penalize for critical findings
    if not findings_df.empty and "severity_label" in findings_df.columns:
        warnings_count = int((findings_df["severity_label"] == "warning").sum())
        base_score -= min(0.20, warnings_count * 0.05)

    final_score = max(0.0, min(1.0, round(base_score, 4)))
    is_ready = final_score >= active.min_readiness_score
    score_label = classify_ml_runtime_readiness_score(final_score)

    return MlRuntimeReadinessScore(
        readiness_score=final_score,
        score_label=score_label,
        is_ready=is_ready,
        hardware_discovery_count=len(hw_df),
        gpu_capability_count=len(gpu_df),
        cpu_capability_count=len(cpu_df),
        memory_capability_count=len(mem_df),
        dependency_count=len(dep_df),
        safety_contract_count=len(safety_df),
        permission_policy_count=len(perm_df),
        input_contract_count=len(input_df),
        finding_count=len(findings_df),
        manual_review_count=len(review_df),
        non_signal=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
    )


def build_ml_runtime_readiness_score_report(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for readiness score."""
    active = profile or get_gpu_ml_runtime_profile()
    findings_df, _ = build_ml_runtime_findings_registry(active)
    score_obj = calculate_ml_runtime_readiness_score(findings_df, active)

    rows = [
        {
            "metric_name": "readiness_score",
            "metric_value": score_obj.readiness_score,
            "score_label": score_obj.score_label,
            "is_ready": score_obj.is_ready,
            "min_required_score": active.min_readiness_score,
            "hardware_discovery_count": score_obj.hardware_discovery_count,
            "gpu_capability_count": score_obj.gpu_capability_count,
            "cpu_capability_count": score_obj.cpu_capability_count,
            "memory_capability_count": score_obj.memory_capability_count,
            "dependency_count": score_obj.dependency_count,
            "safety_contract_count": score_obj.safety_contract_count,
            "permission_policy_count": score_obj.permission_policy_count,
            "input_contract_count": score_obj.input_contract_count,
            "finding_count": score_obj.finding_count,
            "manual_review_count": score_obj.manual_review_count,
            "non_signal": True,
            "source_preserved": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        }
    ]

    df = pd.DataFrame(rows)
    summary = summarize_ml_runtime_readiness_scores(df)
    summary["domain"] = READINESS_SCORE_DOMAIN
    summary["active_profile"] = active.profile_name
    summary["readiness_score"] = score_obj.readiness_score
    summary["is_ready"] = score_obj.is_ready
    return df, summary


def summarize_ml_runtime_readiness_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize readiness score DataFrame."""
    score = 0.0
    ready = False
    if not df.empty and "metric_value" in df.columns:
        score = float(df.iloc[0]["metric_value"])
        ready = bool(df.iloc[0]["is_ready"])
    return {
        "readiness_score": score,
        "is_ready": ready,
        "classification": classify_ml_runtime_readiness_score(score),
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
