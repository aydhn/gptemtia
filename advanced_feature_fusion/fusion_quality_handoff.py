"""Fusion Quality Handoff Assessment.

Evaluates quality metrics, safety compliance, and downstream readiness for Phase 121.
Strictly non-signal, research use only.
"""

from typing import Any, Dict, List, Optional
from advanced_feature_fusion.fusion_feature_models import FusionFeatureMatrixManifest, FusionValidationFinding
from config.settings import get_settings


def assess_fusion_quality_handoff(
    manifest: Optional[FusionFeatureMatrixManifest] = None,
    findings: Optional[List[FusionValidationFinding]] = None,
) -> Dict[str, Any]:
    """Calculate quality scores and determine if handoff to Phase 121 is ready."""
    settings = get_settings()
    min_readiness = getattr(settings, "min_readiness_score", 0.45)

    findings_list = findings or []
    blocking_findings = [f for f in findings_list if f.is_blocking]

    # Scores
    no_lookahead_score = 1.0 if (manifest is None or manifest.no_lookahead_guaranteed) else 0.0
    non_signal_score = 1.0 if (manifest is None or manifest.is_non_signal_guaranteed) else 0.0
    metadata_only_score = 1.0 if (manifest is None or manifest.is_strictly_metadata_only) else 0.0

    # If any blocking finding, penalize scores
    if blocking_findings:
        readiness_score = 0.0
        handoff_ready = False
    else:
        readiness_score = (no_lookahead_score * 0.4) + (non_signal_score * 0.3) + (metadata_only_score * 0.3)
        handoff_ready = readiness_score >= min_readiness

    return {
        "current_phase": 120,
        "next_phase": 121,
        "readiness_score": round(readiness_score, 4),
        "min_readiness_threshold": min_readiness,
        "handoff_ready": handoff_ready,
        "total_findings": len(findings_list),
        "blocking_findings_count": len(blocking_findings),
        "scores_breakdown": {
            "no_lookahead_compliance": no_lookahead_score,
            "non_signal_compliance": non_signal_score,
            "metadata_only_compliance": metadata_only_score,
        },
        "target_phase_scope": "Phase 121 Feature Validation, Lag Integrity & Leakage Guard",
    }
