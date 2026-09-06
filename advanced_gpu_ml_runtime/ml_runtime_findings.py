"""Phase 136: ML Runtime Findings Registry.

Catalogs non-signal hardware, dependency, and contract findings for operator review.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    FINDING_DOMAIN,
    RUNTIME_READY,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_models import MlRuntimeFinding
from advanced_gpu_ml_runtime.gpu_capability_registry import safe_detect_gpu_capability
from advanced_gpu_ml_runtime.torch_runtime_capability import safe_detect_torch_runtime
from advanced_gpu_ml_runtime.sklearn_runtime_capability import safe_detect_sklearn_runtime
from advanced_gpu_ml_runtime.memory_capability_registry import safe_detect_memory_capability
from advanced_gpu_ml_runtime.optional_ml_dependency_registry import safe_detect_optional_dependencies


def create_ml_runtime_finding(
    finding_type: str,
    runtime_domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> MlRuntimeFinding:
    """Instantiate a structured MlRuntimeFinding."""
    finding_id = f"find_{finding_type}_{runtime_domain}"
    return MlRuntimeFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        runtime_domain=runtime_domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        non_signal=True,
    )


def build_ml_runtime_findings_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for runtime findings."""
    active = profile or get_gpu_ml_runtime_profile()

    findings: List[MlRuntimeFinding] = []

    gpu_info = safe_detect_gpu_capability()
    if not gpu_info["cuda_available"]:
        findings.append(
            create_ml_runtime_finding(
                finding_type="gpu_unavailable_warning",
                runtime_domain="gpu_capability",
                severity_label="warning",
                message="No CUDA GPU accelerator detected in local environment; CPU execution fallback active.",
                recommendation="Inspect local NVIDIA driver and CUDA installation if hardware acceleration is desired.",
                manual_review_required=True,
            )
        )

    torch_info = safe_detect_torch_runtime()
    if not torch_info["installed"]:
        findings.append(
            create_ml_runtime_finding(
                finding_type="torch_unavailable_warning",
                runtime_domain="torch_capability",
                severity_label="warning",
                message="PyTorch package is not installed in the local Python environment.",
                recommendation="Install torch package offline if tensor operations are required for ML research.",
                manual_review_required=True,
            )
        )

    sk_info = safe_detect_sklearn_runtime()
    if not sk_info["installed"]:
        findings.append(
            create_ml_runtime_finding(
                finding_type="sklearn_unavailable_warning",
                runtime_domain="sklearn_capability",
                severity_label="warning",
                message="Scikit-Learn package is not installed in the active environment.",
                recommendation="Install scikit-learn offline for classical ML baselines.",
                manual_review_required=True,
            )
        )

    mem_info = safe_detect_memory_capability()
    if mem_info["total_ram_gb"] < 4.0:
        findings.append(
            create_ml_runtime_finding(
                finding_type="insufficient_memory_warning",
                runtime_domain="memory_capability",
                severity_label="warning",
                message=f"Host system RAM ({mem_info['total_ram_gb']} GB) is below 4.0 GB recommended minimum.",
                recommendation="Monitor memory usage when loading multi-domain feature matrices.",
                manual_review_required=True,
            )
        )

    opt_deps = safe_detect_optional_dependencies()
    missing_opts = [pkg for pkg, data in opt_deps.items() if not data["installed"]]
    if missing_opts:
        findings.append(
            create_ml_runtime_finding(
                finding_type="optional_dependency_missing",
                runtime_domain="optional_dependencies",
                severity_label="info",
                message=f"Optional ML dependencies not present: {', '.join(missing_opts[:5])}.",
                recommendation="Optional libraries can be installed offline when specific algorithms are selected.",
                manual_review_required=False,
            )
        )

    rows = []
    for f in findings:
        rows.append({
            "finding_id": f.finding_id,
            "finding_type": f.finding_type,
            "runtime_domain": f.runtime_domain,
            "severity_label": f.severity_label,
            "message": f.message,
            "recommendation": f.recommendation,
            "manual_review_required": f.manual_review_required,
            "non_signal": f.non_signal,
            "source_preserved": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_ml_runtime_findings(df)
    summary["domain"] = FINDING_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_ml_runtime_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize runtime findings DataFrame."""
    mr_count = int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0
    return {
        "total_findings": len(df),
        "manual_review_count": mr_count,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
