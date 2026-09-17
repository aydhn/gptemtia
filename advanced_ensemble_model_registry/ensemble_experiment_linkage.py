# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Experiment Linkage."""

import hashlib
from typing import Any, Dict


def build_ensemble_experiment_linkage() -> Dict[str, Any]:
    """Build offline experiment linkage mapping candidate models and ensemble strategies.
    
    Returns:
        Dict[str, Any]: Experiment linkage registry.
    """
    candidate_families = [
        "linear_candidate",
        "ridge_lasso_candidate",
        "random_forest_candidate",
        "extra_trees_candidate",
        "lightgbm_candidate",
        "xgboost_candidate",
        "catboost_candidate",
        "mlp_candidate",
        "temporal_conv_candidate",
        "unsupervised_anomaly_candidate",
    ]
    
    linkages: Dict[str, Any] = {}
    for fam in candidate_families:
        exp_id = hashlib.sha256(f"exp_phase_140_{fam}".encode("utf-8")).hexdigest()[:16]
        linkages[fam] = {
            "experiment_id": f"EXP-140-{exp_id}",
            "candidate_family": fam,
            "offline_tracking_only": True,
            "external_server_connected": False,
            "mlflow_synced": False,
            "wandb_synced": False,
            "non_signal": True,
        }
    
    # Ensemble experiment linkage
    ens_id = hashlib.sha256(b"exp_phase_140_ensemble_meta").hexdigest()[:16]
    linkages["ensemble_meta_contract"] = {
        "experiment_id": f"EXP-140-ENS-{ens_id}",
        "candidate_family": "all_candidates_ensemble",
        "offline_tracking_only": True,
        "external_server_connected": False,
        "mlflow_synced": False,
        "wandb_synced": False,
        "non_signal": True,
    }
    
    return linkages


def validate_ensemble_experiment_linkage(linkages: Dict[str, Any]) -> bool:
    """Validate ensemble experiment linkages.
    
    Args:
        linkages: Dict of experiment linkages.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(linkages, dict) or len(linkages) == 0:
        return False
    for name, spec in linkages.items():
        if not isinstance(spec, dict):
            return False
        if not spec.get("offline_tracking_only", False):
            return False
        if spec.get("external_server_connected", True):
            return False
        if not spec.get("non_signal", False):
            return False
    return True


def summarize_ensemble_experiment_linkage(linkages: Dict[str, Any]) -> Dict[str, Any]:
    """Summarize experiment linkages.
    
    Args:
        linkages: Dict of experiment linkages.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "total_experiments_linked": len(linkages),
        "experiment_keys": list(linkages.keys()),
        "all_offline": all(l.get("offline_tracking_only", False) for l in linkages.values()),
        "all_non_signal": all(l.get("non_signal", False) for l in linkages.values()),
        "dry_run": True,
    }
