# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Output Contracts."""

from typing import Any, Dict, List


def build_ensemble_output_contracts() -> Dict[str, Any]:
    """Build ensemble output contracts specifying blocked predictions and pure metadata outputs.
    
    Returns:
        Dict[str, Any]: Registered ensemble output contracts.
    """
    contracts: Dict[str, Any] = {
        "voting_output_contract": {
            "strategy": "voting",
            "prediction_output_allowed": False,
            "probability_output_allowed": False,
            "class_label_allowed": False,
            "regression_output_allowed": False,
            "trade_signal_allowed": False,
            "performance_metric_allowed": False,
            "status": "ensemble_contract_registered",
            "blocked_reason": "ensemble_execution_blocked_by_phase_140_policy",
            "manual_review_required": True,
            "non_signal": True,
        },
        "blending_output_contract": {
            "strategy": "blending",
            "prediction_output_allowed": False,
            "probability_output_allowed": False,
            "class_label_allowed": False,
            "regression_output_allowed": False,
            "trade_signal_allowed": False,
            "performance_metric_allowed": False,
            "status": "ensemble_contract_registered",
            "blocked_reason": "ensemble_execution_blocked_by_phase_140_policy",
            "manual_review_required": True,
            "non_signal": True,
        },
        "stacking_output_contract": {
            "strategy": "stacking",
            "prediction_output_allowed": False,
            "probability_output_allowed": False,
            "class_label_allowed": False,
            "regression_output_allowed": False,
            "trade_signal_allowed": False,
            "performance_metric_allowed": False,
            "status": "ensemble_contract_registered",
            "blocked_reason": "ensemble_execution_blocked_by_phase_140_policy",
            "manual_review_required": True,
            "non_signal": True,
        },
        "averaging_output_contract": {
            "strategy": "averaging",
            "prediction_output_allowed": False,
            "probability_output_allowed": False,
            "class_label_allowed": False,
            "regression_output_allowed": False,
            "trade_signal_allowed": False,
            "performance_metric_allowed": False,
            "status": "ensemble_contract_registered",
            "blocked_reason": "ensemble_execution_blocked_by_phase_140_policy",
            "manual_review_required": True,
            "non_signal": True,
        },
        "rank_aggregation_output_contract": {
            "strategy": "rank_aggregation",
            "prediction_output_allowed": False,
            "probability_output_allowed": False,
            "class_label_allowed": False,
            "regression_output_allowed": False,
            "trade_signal_allowed": False,
            "performance_metric_allowed": False,
            "status": "ensemble_contract_registered",
            "blocked_reason": "ensemble_execution_blocked_by_phase_140_policy",
            "manual_review_required": True,
            "non_signal": True,
        },
        "meta_model_output_contract": {
            "strategy": "meta_model",
            "prediction_output_allowed": False,
            "probability_output_allowed": False,
            "class_label_allowed": False,
            "regression_output_allowed": False,
            "trade_signal_allowed": False,
            "performance_metric_allowed": False,
            "status": "ensemble_contract_registered",
            "blocked_reason": "ensemble_execution_blocked_by_phase_140_policy",
            "manual_review_required": True,
            "non_signal": True,
        },
    }
    return contracts


def validate_ensemble_output_contracts(contracts: Dict[str, Any]) -> bool:
    """Validate ensemble output contracts.
    
    Args:
        contracts: Dict of output contracts.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(contracts, dict) or len(contracts) == 0:
        return False
    for name, spec in contracts.items():
        if not isinstance(spec, dict):
            return False
        if not spec.get("non_signal", False):
            return False
        if spec.get("prediction_output_allowed", True):
            return False
        if spec.get("trade_signal_allowed", True):
            return False
        if spec.get("probability_output_allowed", True):
            return False
    return True


def summarize_ensemble_output_contracts(contracts: Dict[str, Any]) -> Dict[str, Any]:
    """Summarize ensemble output contracts.
    
    Args:
        contracts: Dict of output contracts.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "total_contracts": len(contracts),
        "contract_names": list(contracts.keys()),
        "all_predictions_blocked": all(not c.get("prediction_output_allowed", True) for c in contracts.values()),
        "all_signals_blocked": all(not c.get("trade_signal_allowed", True) for c in contracts.values()),
        "all_non_signal": all(c.get("non_signal", False) for c in contracts.values()),
        "dry_run": True,
    }
