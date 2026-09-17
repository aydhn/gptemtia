"""Drift Experiment Linkage for Phase 142.

Links drift contracts and thresholds to historical ML experiment runs,
benchmarks, and hyperparameter trials (Phase 138, 140, 141).
"""

from __future__ import annotations

from typing import Any, Dict, List


def build_drift_experiment_linkages() -> List[Dict[str, Any]]:
    """Builds linkage records between drift contracts and offline experiment runs."""
    return [
        {
            "linkage_id": "exp_link_p138_baseline_models",
            "source_phase": 138,
            "experiment_group": "baseline_model_benchmarks",
            "drift_domain": "model_drift",
            "monitored_artifacts": ["baseline_model_metrics", "validation_error_spread"],
            "status": "linked",
        },
        {
            "linkage_id": "exp_link_p140_ensemble_models",
            "source_phase": 140,
            "experiment_group": "ensemble_model_benchmarks",
            "drift_domain": "ensemble_drift",
            "monitored_artifacts": ["ensemble_weights", "stacking_cv_residuals"],
            "status": "linked",
        },
        {
            "linkage_id": "exp_link_p141_calibration_runs",
            "source_phase": 141,
            "experiment_group": "calibration_uncertainty_benchmarks",
            "drift_domain": "calibration_drift",
            "monitored_artifacts": ["ece_baseline_scores", "conformal_coverage_intervals"],
            "status": "linked",
        },
    ]
