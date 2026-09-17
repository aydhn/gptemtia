"""Model Drift Monitoring Manifest Builder for Phase 142.

Assembles the master ModelDriftMonitoringManifest combining contracts, linkages,
window policies, threshold placeholders, metric placeholders, disabled execution
enforcements, guards, findings, and readiness scores into a single immutable artifact.
"""

from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from advanced_model_drift_monitoring.calibration_drift_contracts import (
    build_calibration_drift_contracts,
)
from advanced_model_drift_monitoring.current_window_policies import (
    build_current_window_policies,
)
from advanced_model_drift_monitoring.data_drift_monitoring_contracts import (
    build_data_drift_monitoring_contracts,
)
from advanced_model_drift_monitoring.drift_execution_disabled import (
    build_all_drift_disabled_execution_items,
)
from advanced_model_drift_monitoring.drift_findings import build_drift_findings
from advanced_model_drift_monitoring.drift_forbidden_column_policies import (
    build_drift_forbidden_column_guards,
)
from advanced_model_drift_monitoring.drift_metadata_only_news_guards import (
    build_drift_metadata_only_news_guards,
)
from advanced_model_drift_monitoring.drift_metric_placeholders import (
    build_all_drift_metric_placeholders,
)
from advanced_model_drift_monitoring.drift_monitoring_schedule_placeholders import (
    build_drift_monitoring_schedule_placeholders,
)
from advanced_model_drift_monitoring.drift_no_lookahead_guards import (
    build_drift_no_lookahead_guards,
)
from advanced_model_drift_monitoring.drift_readiness_scoring import (
    compute_domain_readiness_scores,
)
from advanced_model_drift_monitoring.drift_segment_policies import (
    build_drift_segment_policies,
)
from advanced_model_drift_monitoring.drift_source_preservation_guards import (
    build_drift_source_preservation_guards,
)
from advanced_model_drift_monitoring.drift_threshold_placeholder_policies import (
    build_drift_threshold_placeholders,
)
from advanced_model_drift_monitoring.feature_drift_linkage import (
    build_feature_drift_linkages,
)
from advanced_model_drift_monitoring.feature_drift_monitoring_contracts import (
    build_feature_drift_monitoring_contracts,
)
from advanced_model_drift_monitoring.feature_quality_drift_linkage import (
    build_feature_quality_drift_linkages,
)
from advanced_model_drift_monitoring.featurestore_drift_linkage import (
    build_featurestore_drift_linkages,
)
from advanced_model_drift_monitoring.model_drift_config import get_model_drift_profile
from advanced_model_drift_monitoring.model_drift_models import (
    DriftFinding,
    DriftGuardItem,
    DriftLinkageItem,
    DriftMetricPlaceholder,
    DriftMonitoringContract,
    DriftReadinessScore,
    DriftThresholdPlaceholder,
    DriftWindowPolicy,
    ModelDriftMonitoringManifest,
)
from advanced_model_drift_monitoring.model_drift_monitoring_contracts import (
    build_model_drift_monitoring_contracts,
)
from advanced_model_drift_monitoring.prediction_distribution_drift_placeholders import (
    build_prediction_distribution_drift_placeholders,
)
from advanced_model_drift_monitoring.reference_window_policies import (
    build_reference_window_policies,
)
from advanced_model_drift_monitoring.regime_drift_linkage import (
    build_regime_drift_linkages,
)
from advanced_model_drift_monitoring.rolling_window_placeholder_policies import (
    build_rolling_window_placeholder_policies,
)
from advanced_model_drift_monitoring.uncertainty_drift_contracts import (
    build_uncertainty_drift_contracts,
)


def build_model_drift_monitoring_manifest(
    profile_name: str = "balanced_local_model_drift_contracts",
) -> ModelDriftMonitoringManifest:
    """Builds the comprehensive Phase 142 drift monitoring manifest."""
    profile = get_model_drift_profile(profile_name)

    # 1. Contracts
    contracts: List[DriftMonitoringContract] = []
    contracts.extend(build_model_drift_monitoring_contracts())
    contracts.extend(build_data_drift_monitoring_contracts())
    contracts.extend(build_feature_drift_monitoring_contracts())
    contracts.extend(build_calibration_drift_contracts())
    contracts.extend(build_uncertainty_drift_contracts())
    contracts.extend(build_prediction_distribution_drift_placeholders())

    # 2. Linkages
    linkages: List[DriftLinkageItem] = []
    linkages.extend(build_feature_drift_linkages())
    linkages.extend(build_feature_quality_drift_linkages())
    linkages.extend(build_featurestore_drift_linkages())
    linkages.extend(build_regime_drift_linkages())

    # 3. Window Policies
    window_policies: List[DriftWindowPolicy] = []
    window_policies.extend(build_reference_window_policies())
    window_policies.extend(build_current_window_policies())
    window_policies.extend(build_rolling_window_placeholder_policies())
    window_policies.extend(build_drift_segment_policies())
    window_policies.extend(build_drift_monitoring_schedule_placeholders())

    # 4. Thresholds
    thresholds: List[DriftThresholdPlaceholder] = build_drift_threshold_placeholders()

    # 5. Metric Placeholders
    metric_placeholders: List[DriftMetricPlaceholder] = build_all_drift_metric_placeholders()

    # 6. Disabled Execution Enforcements
    disabled_executions = build_all_drift_disabled_execution_items()

    # 7. Guards
    guards: List[DriftGuardItem] = []
    guards.extend(build_drift_no_lookahead_guards())
    guards.extend(build_drift_metadata_only_news_guards())
    guards.extend(build_drift_source_preservation_guards())
    guards.extend(build_drift_forbidden_column_guards())

    # 8. Findings & Scores
    findings: List[DriftFinding] = build_drift_findings()
    readiness_scores: List[DriftReadinessScore] = compute_domain_readiness_scores()

    manifest_id = f"drift_manifest_p142_{profile_name}_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"

    return ModelDriftMonitoringManifest(
        manifest_id=manifest_id,
        generated_at=datetime.now(timezone.utc).isoformat(),
        phase=142,
        profile=profile,
        contracts=contracts,
        linkages=linkages,
        window_policies=window_policies,
        thresholds=thresholds,
        metric_placeholders=metric_placeholders,
        disabled_executions=disabled_executions,
        guards=guards,
        findings=findings,
        readiness_scores=readiness_scores,
        metadata={
            "non_executing": True,
            "non_signal": True,
            "dry_run": True,
            "environment": "offline_local",
            "linked_phases": [123, 124, 126, 135, 136, 137, 138, 139, 140, 141],
            "next_phase": 143,
        },
    )


def validate_model_drift_monitoring_manifest(
    manifest: ModelDriftMonitoringManifest,
) -> Dict[str, Any]:
    """Validates full manifest compliance against safety and non-executing requirements."""
    errors = []

    if manifest.phase != 142:
        errors.append(f"Invalid phase: {manifest.phase}, expected 142.")

    # Verify contracts non-executing
    for c in manifest.contracts:
        if c.execution_mode != "non_executing_contract":
            errors.append(f"Contract {c.contract_id} has invalid execution_mode: {c.execution_mode}")

    # Verify window policies non-executing
    for w in manifest.window_policies:
        if w.execution_enabled:
            errors.append(f"Window policy {w.policy_id} must have execution_enabled=False.")

    # Verify metric placeholders non-executing
    for m in manifest.metric_placeholders:
        if m.calculation_enabled:
            errors.append(f"Metric placeholder {m.metric_id} must have calculation_enabled=False.")

    # Verify all disabled execution safeguards are active
    for d in manifest.disabled_executions:
        if not d.is_disabled:
            errors.append(f"Disabled execution safeguard {d.execution_id} is not disabled.")

    # Verify guards active
    for g in manifest.guards:
        if not g.is_active:
            errors.append(f"Guard {g.guard_id} is not active.")

    return {
        "valid": len(errors) == 0,
        "manifest_id": manifest.manifest_id,
        "errors": errors,
        "total_contracts": len(manifest.contracts),
        "total_linkages": len(manifest.linkages),
        "total_metrics": len(manifest.metric_placeholders),
        "total_guards": len(manifest.guards),
        "total_findings": len(manifest.findings),
    }


def summarize_model_drift_monitoring_manifest(
    manifest: ModelDriftMonitoringManifest,
) -> Dict[str, Any]:
    """Generates a high-level summary of the drift monitoring manifest."""
    return {
        "manifest_id": manifest.manifest_id,
        "phase": manifest.phase,
        "profile": manifest.profile.profile_name,
        "generated_at": manifest.generated_at,
        "contracts_count": len(manifest.contracts),
        "linkages_count": len(manifest.linkages),
        "window_policies_count": len(manifest.window_policies),
        "thresholds_count": len(manifest.thresholds),
        "metrics_count": len(manifest.metric_placeholders),
        "disabled_safeguards_count": len(manifest.disabled_executions),
        "guards_count": len(manifest.guards),
        "findings_count": len(manifest.findings),
        "readiness_scores_count": len(manifest.readiness_scores),
        "all_calculation_disabled": all(not m.calculation_enabled for m in manifest.metric_placeholders),
        "all_window_execution_disabled": all(not w.execution_enabled for w in manifest.window_policies),
        "non_executing_compliance": True,
    }
