# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Model Pipeline."""

from typing import Any, Dict, Optional

from advanced_ensemble_model_registry.ensemble_model_config import get_ensemble_model_profile
from advanced_ensemble_model_registry.ensemble_model_domain_registry import build_ensemble_model_domain_registry
from advanced_ensemble_model_registry.candidate_model_families import build_candidate_model_families
from advanced_ensemble_model_registry.candidate_model_contracts import build_candidate_model_contracts
from advanced_ensemble_model_registry.candidate_model_input_contracts import build_candidate_model_input_contracts
from advanced_ensemble_model_registry.candidate_model_output_contracts import build_candidate_model_output_contracts
from advanced_ensemble_model_registry.candidate_model_eligibility_gates import build_candidate_model_eligibility_gates
from advanced_ensemble_model_registry.candidate_model_compatibility_matrix import build_candidate_compatibility_matrix
from advanced_ensemble_model_registry.ensemble_strategy_contracts import build_ensemble_strategy_contracts
from advanced_ensemble_model_registry.ensemble_input_contracts import build_ensemble_input_contracts
from advanced_ensemble_model_registry.ensemble_output_contracts import build_ensemble_output_contracts
from advanced_ensemble_model_registry.ensemble_execution_disabled import build_ensemble_execution_disabled_report
from advanced_ensemble_model_registry.candidate_model_training_disabled import build_candidate_model_training_disabled_report
from advanced_ensemble_model_registry.candidate_model_prediction_disabled import build_candidate_model_prediction_disabled_report
from advanced_ensemble_model_registry.candidate_model_target_label_disabled import build_candidate_model_target_label_disabled_report
from advanced_ensemble_model_registry.candidate_model_artifact_disabled import build_candidate_model_artifact_disabled_report
from advanced_ensemble_model_registry.candidate_model_registry_write_disabled import build_candidate_model_registry_write_disabled_report
from advanced_ensemble_model_registry.ensemble_metric_placeholders import build_ensemble_metric_placeholders
from advanced_ensemble_model_registry.ensemble_evaluation_placeholders import build_ensemble_evaluation_placeholders
from advanced_ensemble_model_registry.ensemble_validation_dependencies import build_ensemble_validation_dependencies
from advanced_ensemble_model_registry.ensemble_quality_dependencies import build_ensemble_quality_dependencies
from advanced_ensemble_model_registry.ensemble_lineage import build_ensemble_lineage
from advanced_ensemble_model_registry.ensemble_experiment_linkage import build_ensemble_experiment_linkage
from advanced_ensemble_model_registry.ensemble_no_lookahead_guards import build_ensemble_no_lookahead_guards
from advanced_ensemble_model_registry.ensemble_metadata_only_news_guards import build_ensemble_metadata_only_news_guards
from advanced_ensemble_model_registry.ensemble_source_preservation_guards import build_ensemble_source_preservation_guards
from advanced_ensemble_model_registry.ensemble_candidate_audit_placeholders import build_ensemble_candidate_audit_placeholders
from advanced_ensemble_model_registry.ensemble_findings import build_ensemble_findings
from advanced_ensemble_model_registry.ensemble_manual_review import build_ensemble_manual_review_queue
from advanced_ensemble_model_registry.ensemble_readiness_scoring import calculate_ensemble_readiness_score
from advanced_ensemble_model_registry.ensemble_model_manifest import build_ensemble_model_manifest
from advanced_ensemble_model_registry.ensemble_model_health import check_ensemble_model_health
from advanced_ensemble_model_registry.ensemble_model_validation import build_ensemble_model_validation_report
from advanced_ensemble_model_registry.phase_141_handoff import build_phase_141_handoff_report
from advanced_ensemble_model_registry.ensemble_model_safety_boundary import enforce_ensemble_model_safety_boundary


def run_ensemble_model_pipeline(profile_name: str = "balanced_local_ensemble_model_contracts") -> Dict[str, Any]:
    """Execute Phase 140 dry-run pipeline to assemble and validate ensemble & candidate model contracts.
    
    Args:
        profile_name: Profile name to use.
        
    Returns:
        Dict[str, Any]: Consolidated pipeline results.
    """
    profile = get_ensemble_model_profile(profile_name)
    df_domains, domains = build_ensemble_model_domain_registry(profile)
    df_families, s_families = build_candidate_model_families(profile)
    df_contracts, s_contracts = build_candidate_model_contracts(profile)
    df_input_contracts, s_input_contracts = build_candidate_model_input_contracts(profile)
    df_output_contracts, s_output_contracts = build_candidate_model_output_contracts(profile)
    df_gates, s_gates = build_candidate_model_eligibility_gates(profile)
    df_matrix, s_matrix = build_candidate_compatibility_matrix(profile)
    df_strategies, s_strategies = build_ensemble_strategy_contracts(profile)
    ensemble_inputs = build_ensemble_input_contracts()
    ensemble_outputs = build_ensemble_output_contracts()
    
    # Disabled execution reports
    disabled_reports = {
        "ensemble_execution": build_ensemble_execution_disabled_report(),
        "candidate_training": build_candidate_model_training_disabled_report(),
        "candidate_prediction": build_candidate_model_prediction_disabled_report(),
        "candidate_target_label": build_candidate_model_target_label_disabled_report(),
        "candidate_artifact": build_candidate_model_artifact_disabled_report(),
        "candidate_registry_write": build_candidate_model_registry_write_disabled_report(),
    }
    
    metrics = build_ensemble_metric_placeholders()
    evaluations = build_ensemble_evaluation_placeholders()
    val_deps = build_ensemble_validation_dependencies()
    qual_deps = build_ensemble_quality_dependencies()
    lineage = build_ensemble_lineage()
    experiment_linkage = build_ensemble_experiment_linkage()
    
    lookahead_guards = build_ensemble_no_lookahead_guards()
    news_guards = build_ensemble_metadata_only_news_guards()
    source_guards = build_ensemble_source_preservation_guards()
    audits = build_ensemble_candidate_audit_placeholders()
    
    findings = build_ensemble_findings()
    review_queue = build_ensemble_manual_review_queue()
    readiness = calculate_ensemble_readiness_score()
    
    manifest = build_ensemble_model_manifest(
        candidate_contract_count=len(df_contracts),
        ensemble_contract_count=len(df_strategies),
        disabled_execution_report_count=len(disabled_reports),
        finding_count=len(findings),
        manual_review_count=len(review_queue),
        readiness_score=readiness.readiness_score,
    )
    
    health = check_ensemble_model_health()
    validation = build_ensemble_model_validation_report()
    handoff = build_phase_141_handoff_report()
    
    pipeline_result = {
        "pipeline_name": "phase_140_ensemble_model_pipeline",
        "phase": 140,
        "target_final_phase": 160,
        "next_phase": 141,
        "profile": profile.__dict__,
        "domains": domains,
        "candidate_family_count": len(df_families),
        "candidate_contract_count": len(df_contracts),
        "ensemble_strategy_count": len(df_strategies),

        "disabled_report_count": len(disabled_reports),
        "health_status": health.get("status"),
        "validation_status": validation.get("validation_status"),
        "readiness_score": readiness.readiness_score,
        "readiness_classification": readiness.classification,
        "manifest": manifest,
        "findings": findings,
        "review_queue": review_queue,
        "handoff": handoff,
        "non_signal": True,
        "dry_run": True,
        "local_only": True,
    }
    
    # Assert safety boundary
    if not enforce_ensemble_model_safety_boundary(pipeline_result):
        raise ValueError("Pipeline result violated safety boundary invariants.")
        
    return pipeline_result


def validate_ensemble_model_pipeline_result(result: Dict[str, Any]) -> bool:
    """Validate ensemble model pipeline result.
    
    Args:
        result: Pipeline result dictionary.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(result, dict):
        return False
    if result.get("phase") != 140:
        return False
    if result.get("health_status") != "HEALTHY":
        return False
    if result.get("validation_status") != "VALID":
        return False
    if not result.get("non_signal", False):
        return False
    if not result.get("dry_run", False):
        return False
    return True


def summarize_ensemble_model_pipeline_result(result: Dict[str, Any]) -> Dict[str, Any]:
    """Summarize pipeline result.
    
    Args:
        result: Pipeline result dictionary.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "pipeline_name": result.get("pipeline_name"),
        "phase": result.get("phase"),
        "candidate_contracts": result.get("candidate_contract_count"),
        "ensemble_strategies": result.get("ensemble_strategy_count"),
        "readiness_score": result.get("readiness_score"),
        "health_status": result.get("health_status"),
        "validation_status": result.get("validation_status"),
        "is_valid": validate_ensemble_model_pipeline_result(result),
        "non_signal": result.get("non_signal", True),
        "dry_run": result.get("dry_run", True),
    }
