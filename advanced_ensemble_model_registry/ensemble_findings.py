# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Findings."""

from typing import Any, Dict, List
from advanced_ensemble_model_registry.ensemble_model_models import EnsembleFinding


def build_ensemble_findings() -> List[EnsembleFinding]:
    """Build findings regarding candidate and ensemble contracts governance.
    
    Returns:
        List[EnsembleFinding]: List of findings.
    """
    findings = [
        EnsembleFinding(
            finding_id="FIND-140-001",
            finding_type="GOVERNANCE_INFO",
            ensemble_domain="candidate_model_registry",
            severity_label="low",
            message="Candidate model contracts are verified in pure contract placeholder state.",
            recommendation="Retain non-executing invariants until Phase 141 uncertainty calibration handoff.",
            manual_review_required=True,
            non_signal=True,
            auto_fix_prohibited=True,
        ),
        EnsembleFinding(
            finding_id="FIND-140-002",
            finding_type="EXECUTION_BOUNDARY_INFO",
            ensemble_domain="ensemble_strategy_layer",
            severity_label="low",
            message="Ensemble execution (voting/blending/stacking) is confirmed disabled.",
            recommendation="Maintain execution guardrails throughout local development runs.",
            manual_review_required=True,
            non_signal=True,
            auto_fix_prohibited=True,
        ),
        EnsembleFinding(
            finding_id="FIND-140-003",
            finding_type="RESOURCE_INFO",
            ensemble_domain="candidate_model_governance",
            severity_label="low",
            message="Compatibility matrix conforms to Phase 139 GPU resource governance budgets.",
            recommendation="Periodically verify hardware allocation references.",
            manual_review_required=True,
            non_signal=True,
            auto_fix_prohibited=True,
        ),
    ]
    return findings


def validate_ensemble_findings(findings: List[EnsembleFinding]) -> bool:
    """Validate ensemble findings.
    
    Args:
        findings: List of findings.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(findings, list) or len(findings) == 0:
        return False
    for finding in findings:
        if not isinstance(finding, EnsembleFinding):
            return False
        if not finding.auto_fix_prohibited:
            return False
        if not finding.non_signal:
            return False
    return True


def summarize_ensemble_findings(findings: List[EnsembleFinding]) -> Dict[str, Any]:
    """Summarize ensemble findings.
    
    Args:
        findings: List of findings.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "total_findings": len(findings),
        "finding_ids": [f.finding_id for f in findings],
        "all_auto_fix_prohibited": all(f.auto_fix_prohibited for f in findings),
        "all_non_signal": all(f.non_signal for f in findings),
        "dry_run": True,
    }
