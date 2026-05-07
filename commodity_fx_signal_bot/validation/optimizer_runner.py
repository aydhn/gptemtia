"""
Optimizer candidate runner for safe candidate evaluation.
"""

import logging
import pandas as pd
from typing import Tuple

from validation.validation_models import ParameterSet
from validation.validation_config import ValidationProfile
from validation.validation_labels import validate_optimizer_candidate_label

logger = logging.getLogger(__name__)


class OptimizerCandidateRunner:
    """Evaluates and ranks parameter sets for strategy validation."""

    def __init__(self, profile: ValidationProfile):
        self.profile = profile

    def score_parameter_set(
        self,
        parameter_set: ParameterSet,
        performance_summary: dict,
        walk_forward_summary: dict | None = None,
        robustness_summary: dict | None = None,
    ) -> dict:
        """
        Scores a single parameter set based on multiple validation criteria.
        """
        warnings = []

        # Extract metrics safely
        primary_metric_val = performance_summary.get(self.profile.primary_metric, 0.0)

        # If looking for test_ metrics but only base metrics exist, adapt
        if self.profile.primary_metric.startswith('test_') and self.profile.primary_metric not in performance_summary:
            base_metric = self.profile.primary_metric.replace('test_', '')
            primary_metric_val = performance_summary.get(base_metric, 0.0)

        secondary_metric_val = performance_summary.get(self.profile.secondary_metric, 0.0)
        if self.profile.secondary_metric.startswith('test_') and self.profile.secondary_metric not in performance_summary:
            base_metric = self.profile.secondary_metric.replace('test_', '')
            secondary_metric_val = performance_summary.get(base_metric, 0.0)

        # Extract context
        robustness_score = 0.0
        overfitting_risk_score = 1.0 # Assume worst if missing
        stability_score = 0.0

        if robustness_summary:
            robustness_score = robustness_summary.get('robustness_score', 0.0)
            overfitting_risk_score = robustness_summary.get('aggregate_overfitting_risk_score', 1.0)

        if walk_forward_summary:
            # Maybe derive stability from walk forward if not in robustness
            if 'test_positive_ratio' in walk_forward_summary:
                 stability_score = walk_forward_summary['test_positive_ratio']

        # Determine label based on config thresholds
        label = "optimizer_candidate_passed"

        if overfitting_risk_score > self.profile.overfitting_risk_threshold:
            label = "optimizer_candidate_overfit_warning"
            warnings.append(f"Overfitting risk ({overfitting_risk_score:.2f}) exceeds threshold ({self.profile.overfitting_risk_threshold})")

        elif robustness_score < self.profile.min_robustness_score:
            label = "optimizer_candidate_watchlist"
            warnings.append(f"Robustness score ({robustness_score:.2f}) below threshold ({self.profile.min_robustness_score})")

        if primary_metric_val <= 0:
            label = "optimizer_candidate_rejected"
            warnings.append(f"Primary metric ({primary_metric_val:.2f}) is not positive")

        if walk_forward_summary and walk_forward_summary.get('valid_split_count', 0) < 2:
             label = "optimizer_candidate_insufficient_data"
             warnings.append("Insufficient valid walk-forward splits")

        validate_optimizer_candidate_label(label)

        # Base candidate score on primary metric modified by robustness/risk
        # This is an arbitrary scoring function just for relative ranking
        candidate_score = primary_metric_val * (1.0 + robustness_score) * (1.0 - overfitting_risk_score)

        return {
            "parameter_set_id": parameter_set.parameter_set_id,
            "optimizer_candidate_score": float(candidate_score),
            "primary_metric_value": float(primary_metric_val),
            "secondary_metric_value": float(secondary_metric_val),
            "robustness_score": float(robustness_score),
            "overfitting_risk_score": float(overfitting_risk_score),
            "stability_score": float(stability_score),
            "candidate_label": label,
            "warnings": warnings,
            # Flatten parameters for easier DataFrame conversion later
            **{f"param_{k}": v for k, v in parameter_set.parameters.items()}
        }

    def rank_parameter_sets(
        self,
        parameter_results: list[dict],
        primary_metric: str = "optimizer_candidate_score",
    ) -> pd.DataFrame:
        """
        Ranks evaluated parameter sets.
        """
        if not parameter_results:
            return pd.DataFrame()

        df = pd.DataFrame(parameter_results)

        # Sort by primary_metric (descending)
        if primary_metric in df.columns:
            df = df.sort_values(by=primary_metric, ascending=False).reset_index(drop=True)

        return df

    def build_optimizer_candidate_report(
        self,
        parameter_results: list[dict],
    ) -> Tuple[pd.DataFrame, dict]:
        """
        Builds the final optimizer candidate report.
        """
        if not parameter_results:
            return pd.DataFrame(), {"warnings": ["No parameter results to report"]}

        df = self.rank_parameter_sets(parameter_results)

        label_counts = df['candidate_label'].value_counts().to_dict() if 'candidate_label' in df.columns else {}

        summary = {
            "total_candidates": len(df),
            "passed_candidates": int(label_counts.get("optimizer_candidate_passed", 0)),
            "rejected_candidates": int(label_counts.get("optimizer_candidate_rejected", 0)),
            "watchlist_candidates": int(label_counts.get("optimizer_candidate_watchlist", 0)),
            "overfit_warning_candidates": int(label_counts.get("optimizer_candidate_overfit_warning", 0)),
            "label_distribution": label_counts,
            "best_candidate_score": float(df['optimizer_candidate_score'].max()) if 'optimizer_candidate_score' in df.columns else 0.0,
            "warnings": [],
            "disclaimer": "This is an optimizer candidate report for historical analysis. It is NOT a live strategy selection or trading signal."
        }

        if summary["passed_candidates"] == 0:
            summary["warnings"].append("No candidates passed the validation criteria")

        return df, summary
