# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Metric Placeholders."""

from typing import Any, Dict


def build_ensemble_metric_placeholders() -> Dict[str, Any]:
    """Build ensemble metric placeholders with zero computation executed.
    
    Returns:
        Dict[str, Any]: Registered metric placeholders.
    """
    placeholders: Dict[str, Any] = {
        "ensemble_log_loss_placeholder": {
            "metric_name": "log_loss",
            "category": "probabilistic",
            "computation_executed": False,
            "metric_value": None,
            "is_signal": False,
            "is_performance_claim": False,
            "non_signal": True,
        },
        "ensemble_brier_score_placeholder": {
            "metric_name": "brier_score",
            "category": "probabilistic",
            "computation_executed": False,
            "metric_value": None,
            "is_signal": False,
            "is_performance_claim": False,
            "non_signal": True,
        },
        "ensemble_roc_auc_placeholder": {
            "metric_name": "roc_auc",
            "category": "ranking",
            "computation_executed": False,
            "metric_value": None,
            "is_signal": False,
            "is_performance_claim": False,
            "non_signal": True,
        },
        "ensemble_diversity_score_placeholder": {
            "metric_name": "candidate_diversity_score",
            "category": "ensemble_diversity",
            "computation_executed": False,
            "metric_value": None,
            "is_signal": False,
            "is_performance_claim": False,
            "non_signal": True,
        },
        "ensemble_correlation_matrix_placeholder": {
            "metric_name": "candidate_correlation_matrix",
            "category": "correlation",
            "computation_executed": False,
            "metric_value": None,
            "is_signal": False,
            "is_performance_claim": False,
            "non_signal": True,
        },
    }
    return placeholders


def validate_ensemble_metric_placeholders(placeholders: Dict[str, Any]) -> bool:
    """Validate that metric placeholders have zero execution and are non-signal.
    
    Args:
        placeholders: Dict of placeholders.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(placeholders, dict) or len(placeholders) == 0:
        return False
    for name, spec in placeholders.items():
        if not isinstance(spec, dict):
            return False
        if spec.get("computation_executed", True):
            return False
        if spec.get("metric_value") is not None:
            return False
        if not spec.get("non_signal", False):
            return False
    return True


def summarize_ensemble_metric_placeholders(placeholders: Dict[str, Any]) -> Dict[str, Any]:
    """Summarize metric placeholders.
    
    Args:
        placeholders: Dict of placeholders.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "total_metric_placeholders": len(placeholders),
        "metric_names": list(placeholders.keys()),
        "all_zero_computation": all(not p.get("computation_executed", True) for p in placeholders.values()),
        "all_non_signal": all(p.get("non_signal", False) for p in placeholders.values()),
        "dry_run": True,
    }
