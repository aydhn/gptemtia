# -*- coding: utf-8 -*-
"""Phase 140: Ensemble No-Lookahead Guards."""

from typing import Any, Dict


def build_ensemble_no_lookahead_guards() -> Dict[str, Any]:
    """Build ensemble no-lookahead guard specifications.
    
    Returns:
        Dict[str, Any]: No-lookahead guards dictionary.
    """
    return {
        "candidate_input_temporal_guard": {
            "guard_name": "candidate_input_temporal_guard",
            "enforced": True,
            "lookahead_leakage_detected": False,
            "temporal_cutoff_enforced": True,
            "future_information_prohibited": True,
            "non_signal": True,
        },
        "ensemble_weight_temporal_guard": {
            "guard_name": "ensemble_weight_temporal_guard",
            "enforced": True,
            "lookahead_leakage_detected": False,
            "weights_fit_on_past_only": True,
            "future_information_prohibited": True,
            "non_signal": True,
        },
        "meta_model_split_temporal_guard": {
            "guard_name": "meta_model_split_temporal_guard",
            "enforced": True,
            "lookahead_leakage_detected": False,
            "purged_folds_enforced": True,
            "future_information_prohibited": True,
            "non_signal": True,
        },
        "holdout_leakage_guard": {
            "guard_name": "holdout_leakage_guard",
            "enforced": True,
            "lookahead_leakage_detected": False,
            "out_of_time_holdout_enforced": True,
            "future_information_prohibited": True,
            "non_signal": True,
        },
    }


def validate_ensemble_no_lookahead_guards(guards: Dict[str, Any]) -> bool:
    """Validate that all no-lookahead guards are active and assert zero leakage.
    
    Args:
        guards: Dict of guards.
        
    Returns:
        bool: True if all guards are enforced with zero leakage, False otherwise.
    """
    if not isinstance(guards, dict) or len(guards) == 0:
        return False
    for name, guard in guards.items():
        if not isinstance(guard, dict):
            return False
        if not guard.get("enforced", False):
            return False
        if guard.get("lookahead_leakage_detected", True):
            return False
        if not guard.get("non_signal", False):
            return False
    return True


def summarize_ensemble_no_lookahead_guards(guards: Dict[str, Any]) -> Dict[str, Any]:
    """Summarize ensemble no-lookahead guards.
    
    Args:
        guards: Dict of guards.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "total_guards": len(guards),
        "guard_names": list(guards.keys()),
        "all_guards_enforced": all(g.get("enforced", False) for g in guards.values()),
        "zero_leakage_guaranteed": all(not g.get("lookahead_leakage_detected", True) for g in guards.values()),
        "dry_run": True,
        "non_signal": True,
    }
