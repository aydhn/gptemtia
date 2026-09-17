"""Drift Governance Findings for Phase 142.

Defines standardized drift findings across model, data, feature, calibration,
uncertainty, and regime linkage domains.
All findings emphasize non-executing posture and requirement for human-in-the-loop review.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftFinding


def build_drift_findings() -> List[DriftFinding]:
    """Builds standard governance findings for Phase 142 drift monitoring contracts."""
    findings = [
        DriftFinding(
            finding_id="find_drift_001_contract_established",
            domain="model_drift",
            target_name="candidate_models",
            severity="info",
            finding_type="contract_governance",
            description="Model drift monitoring contracts successfully established across 59 domains.",
            recommended_action="Maintain contracts in non-executing mode pending Phase 143 explainability linkage.",
            requires_human_review=False,
            execution_blocked=True,
            metadata={"phase": 142, "category": "milestone"},
        ),
        DriftFinding(
            finding_id="find_drift_002_thresholds_calibrated_as_placeholders",
            domain="data_drift",
            target_name="threshold_policies",
            severity="info",
            finding_type="threshold_policy",
            description="PSI, KS, JS, and Wasserstein thresholds established as non-executing placeholders.",
            recommended_action="Do not trigger automated alerts or retrain runs based on placeholder thresholds.",
            requires_human_review=True,
            execution_blocked=True,
            metadata={"phase": 142, "category": "policy"},
        ),
        DriftFinding(
            finding_id="find_drift_003_feature_quality_linkage_verified",
            domain="feature_quality_drift",
            target_name="phase_123_quality_linkage",
            severity="info",
            finding_type="linkage_verification",
            description="Feature quality linkage contracts verified against Phase 123 diagnostics without data mutation.",
            recommended_action="Continue read-only lineage tracking without automated feature dropping.",
            requires_human_review=False,
            execution_blocked=True,
            metadata={"phase": 142, "category": "linkage"},
        ),
        DriftFinding(
            finding_id="find_drift_004_calibration_uncertainty_linkage",
            domain="calibration_drift",
            target_name="phase_141_calibration_linkage",
            severity="info",
            finding_type="linkage_verification",
            description="Calibration and uncertainty drift monitoring contracts linked to Phase 141 baselines.",
            recommended_action="Verify reliability diagram placeholders remain aligned with calibrated confidence intervals.",
            requires_human_review=True,
            execution_blocked=True,
            metadata={"phase": 142, "category": "linkage"},
        ),
        DriftFinding(
            finding_id="find_drift_005_regime_shift_linkage",
            domain="regime_drift",
            target_name="phase_126_135_regime_linkage",
            severity="info",
            finding_type="regime_monitoring",
            description="Regime shift linkage contracts established to track transitions across macro volatility regimes.",
            recommended_action="Condition reference windows on regime clusters in future analytical phases.",
            requires_human_review=True,
            execution_blocked=True,
            metadata={"phase": 142, "category": "regime"},
        ),
    ]
    return findings


def summarize_drift_findings(findings: List[DriftFinding]) -> Dict[str, Any]:
    """Summarizes drift findings by severity and domain."""
    by_severity: Dict[str, int] = {}
    by_domain: Dict[str, int] = {}
    requires_review = sum(1 for f in findings if f.requires_human_review)
    all_blocked = all(f.execution_blocked for f in findings)

    for f in findings:
        by_severity[f.severity] = by_severity.get(f.severity, 0) + 1
        by_domain[f.domain] = by_domain.get(f.domain, 0) + 1

    return {
        "total_findings": len(findings),
        "by_severity": by_severity,
        "by_domain": by_domain,
        "requires_human_review_count": requires_review,
        "all_execution_blocked": all_blocked,
        "findings": [asdict(f) for f in findings],
    }
