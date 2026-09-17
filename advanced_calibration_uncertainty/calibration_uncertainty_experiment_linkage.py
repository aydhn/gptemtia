# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Experiment Linkage Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

EXPERIMENT_LINKAGE_TEMPLATES: List[Dict[str, Any]] = [
    {
        "experiment_id": "exp_tree_ensemble_calib_001",
        "calibration_contract_ref": "platt_scaling_contract",
        "uncertainty_contract_ref": "ensemble_variance_contract",
        "candidate_contract_ref": "tree_ensemble_candidate_contract",
        "ensemble_strategy_ref": "voting_ensemble_strategy_contract",
        "phase_137_dataset_ref": "commodity_fx_split_contract",
        "description": "Tree ensemble calibration and variance estimation experiment linkage.",
    },
    {
        "experiment_id": "exp_isotonic_calib_002",
        "calibration_contract_ref": "isotonic_calibration_contract",
        "uncertainty_contract_ref": "conformal_prediction_contract",
        "candidate_contract_ref": "neural_candidate_contract",
        "ensemble_strategy_ref": "blending_ensemble_strategy_contract",
        "phase_137_dataset_ref": "macro_event_split_contract",
        "description": "Neural candidate isotonic calibration and conformal prediction experiment linkage.",
    },
    {
        "experiment_id": "exp_temp_scaling_calib_003",
        "calibration_contract_ref": "temperature_scaling_contract",
        "uncertainty_contract_ref": "monte_carlo_dropout_contract",
        "candidate_contract_ref": "boosting_candidate_contract",
        "ensemble_strategy_ref": "stacking_ensemble_strategy_contract",
        "phase_137_dataset_ref": "cross_asset_regime_split_contract",
        "description": "Boosting candidate temperature scaling and MC dropout experiment linkage.",
    },
    {
        "experiment_id": "exp_beta_calib_004",
        "calibration_contract_ref": "beta_calibration_contract",
        "uncertainty_contract_ref": "bootstrap_uncertainty_contract",
        "candidate_contract_ref": "linear_candidate_contract",
        "ensemble_strategy_ref": "dynamic_weighting_ensemble_strategy_contract",
        "phase_137_dataset_ref": "commodity_fx_split_contract",
        "description": "Linear candidate beta calibration and bootstrap uncertainty experiment linkage.",
    },
]


def build_calibration_uncertainty_experiment_linkage_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for calibration and uncertainty experiment linkage."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in EXPERIMENT_LINKAGE_TEMPLATES:
        rows.append(
            {
                "experiment_id": item["experiment_id"],
                "calibration_contract_ref": item["calibration_contract_ref"],
                "uncertainty_contract_ref": item["uncertainty_contract_ref"],
                "candidate_contract_ref": item["candidate_contract_ref"],
                "ensemble_strategy_ref": item["ensemble_strategy_ref"],
                "phase_137_dataset_ref": item["phase_137_dataset_ref"],
                "description": item["description"],
                "offline_only": True,
                "non_signal": True,
                "phase": prof.current_phase,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_uncertainty_experiment_linkage(df)
    return df, summary


def summarize_calibration_uncertainty_experiment_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize experiment linkage DataFrame."""
    return {
        "total_experiments_linked": len(df),
        "experiments": df["experiment_id"].tolist() if not df.empty else [],
        "all_offline": bool(df["offline_only"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
