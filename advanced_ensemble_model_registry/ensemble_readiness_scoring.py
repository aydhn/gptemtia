# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Readiness Scoring."""

from typing import Any, Dict
from advanced_ensemble_model_registry.ensemble_model_models import EnsembleReadinessScore


def calculate_ensemble_readiness_score(
    candidate_contracts_valid: bool = True,
    ensemble_contracts_valid: bool = True,
    execution_disabled: bool = True,
    guards_active: bool = True,
) -> EnsembleReadinessScore:
    """Calculate readiness score for Phase 140.
    
    The score evaluates adherence to contract completeness, execution blocking, and safety guards.
    Score is bounded in [0.0, 1.0], non-signal, and strictly research-only.
    
    Args:
        candidate_contracts_valid: Whether candidate contracts are valid.
        ensemble_contracts_valid: Whether ensemble contracts are valid.
        execution_disabled: Whether execution is confirmed disabled.
        guards_active: Whether no-lookahead and metadata guards are active.
        
    Returns:
        EnsembleReadinessScore: Computed readiness score object.
    """
    weights = {
        "candidate": 0.25,
        "ensemble": 0.25,
        "disabled": 0.25,
        "guards": 0.25,
    }
    
    score = 0.0
    if candidate_contracts_valid:
        score += weights["candidate"]
    if ensemble_contracts_valid:
        score += weights["ensemble"]
    if execution_disabled:
        score += weights["disabled"]
    if guards_active:
        score += weights["guards"]
        
    score = max(0.0, min(1.0, round(score, 4)))
    meets_threshold = score >= 0.85
    classification = "READY_FOR_PHASE_141_HANDOFF" if meets_threshold else "INCOMPLETE_CONTRACTS"
    
    return EnsembleReadinessScore(
        score_name="phase_140_ensemble_readiness_score",
        readiness_score=score,
        classification=classification,
        meets_threshold=meets_threshold,
        source_phase=140,
        target_final_phase=160,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
        official_approval=False,
    )


def validate_ensemble_readiness_score(score: EnsembleReadinessScore) -> bool:
    """Validate ensemble readiness score.
    
    Args:
        score: EnsembleReadinessScore instance.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(score, EnsembleReadinessScore):
        return False
    if score.readiness_score < 0.0 or score.readiness_score > 1.0:
        return False
    if not score.non_signal:
        return False
    if score.production_ready:
        return False
    if score.broker_ready:
        return False
    return True


def summarize_ensemble_readiness_score(score: EnsembleReadinessScore) -> Dict[str, Any]:
    """Summarize ensemble readiness score.
    
    Args:
        score: EnsembleReadinessScore instance.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "score_name": score.score_name,
        "readiness_score": score.readiness_score,
        "classification": score.classification,
        "meets_threshold": score.meets_threshold,
        "non_signal": score.non_signal,
        "production_ready": score.production_ready,
        "broker_ready": score.broker_ready,
        "dry_run": True,
    }
