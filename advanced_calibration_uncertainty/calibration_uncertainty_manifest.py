# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Manifest."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)
from advanced_calibration_uncertainty.calibration_uncertainty_models import (
    CalibrationUncertaintyManifest,
)


def create_calibration_uncertainty_manifest(
    manifest_name: str = "calibration_uncertainty_manifest_v141",
    calibration_contract_count: int = 7,
    uncertainty_contract_count: int = 8,
    disabled_execution_report_count: int = 5,
    finding_count: int = 3,
    manual_review_count: int = 7,
    readiness_score: float = 1.0,
    manual_review_required: bool = True,
) -> CalibrationUncertaintyManifest:
    """Instantiate a CalibrationUncertaintyManifest object."""
    return CalibrationUncertaintyManifest(
        manifest_name=manifest_name,
        current_phase=141,
        target_final_phase=160,
        next_phase=142,
        calibration_contract_count=calibration_contract_count,
        uncertainty_contract_count=uncertainty_contract_count,
        disabled_execution_report_count=disabled_execution_report_count,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        readiness_score=readiness_score,
        manual_review_required=manual_review_required,
        non_signal=True,
        source_preserved=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        dataset_materialized=False,
        feature_snapshot_materialized=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        contains_article_body=False,
        contains_raw_content=False,
        contains_scraped_html=False,
        contains_embedding=False,
        contains_vector=False,
        sentiment_model_output=False,
        real_training_executed=False,
        model_training_executed=False,
        model_fit_executed=False,
        model_predict_executed=False,
        model_inference_executed=False,
        probability_prediction_executed=False,
        confidence_score_calculated=False,
        calibration_executed=False,
        calibration_fit_executed=False,
        calibration_transform_executed=False,
        uncertainty_estimation_executed=False,
        prediction_interval_calculated=False,
        conformal_prediction_executed=False,
        metric_calculation_executed=False,
        performance_claim_generated=False,
        artifact_persisted=False,
        model_registry_written=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
    )


def build_calibration_uncertainty_manifest(
    profile: Optional[CalibrationUncertaintyProfile] = None,
    calibration_contract_count: int = 7,
    uncertainty_contract_count: int = 8,
    disabled_execution_report_count: int = 5,
    finding_count: int = 3,
    manual_review_count: int = 7,
    readiness_score: float = 1.0,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for master manifest."""
    prof = profile or get_calibration_uncertainty_profile()
    manifest_obj = create_calibration_uncertainty_manifest(
        calibration_contract_count=calibration_contract_count,
        uncertainty_contract_count=uncertainty_contract_count,
        disabled_execution_report_count=disabled_execution_report_count,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        readiness_score=readiness_score,
    )

    df = pd.DataFrame([manifest_obj.__dict__])
    summary = summarize_calibration_uncertainty_manifest(df)
    return df, summary


def summarize_calibration_uncertainty_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manifest DataFrame."""
    if df.empty:
        return {"manifest_name": "empty", "valid": False}
    row = df.iloc[0]
    return {
        "manifest_name": str(row["manifest_name"]),
        "current_phase": int(row["current_phase"]),
        "next_phase": int(row["next_phase"]),
        "target_final_phase": int(row["target_final_phase"]),
        "calibration_contract_count": int(row["calibration_contract_count"]),
        "uncertainty_contract_count": int(row["uncertainty_contract_count"]),
        "disabled_execution_report_count": int(row["disabled_execution_report_count"]),
        "readiness_score": float(row["readiness_score"]),
        "zero_execution_verified": bool(
            not row["calibration_executed"]
            and not row["uncertainty_estimation_executed"]
            and not row["probability_prediction_executed"]
            and not row["real_training_executed"]
            and not row["artifact_persisted"]
        ),
        "non_signal": bool(row["non_signal"]),
        "source_preserved": bool(row["source_preserved"]),
    }
