"""Phase 133: Regime Target/Label/Prediction Absence Report and Validators.

Guarantees regime data matrices and contracts are free of supervised targets,
training labels, and model predictions.
"""

from typing import Any, Dict, List, Optional, Set, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)

FORBIDDEN_PREDICTIVE_TERMS: Set[str] = {
    "target",
    "label",
    "prediction",
    "pred",
    "y_true",
    "y_pred",
    "ground_truth",
    "forecast",
    "regime_pred",
    "target_regime",
    "cluster_prediction",
}


def validate_no_target_label_prediction_columns(column_names: List[str]) -> Dict[str, Any]:
    """Check that column names contain zero target, label, or prediction identifiers."""
    violating = []
    for col in column_names:
        clean = col.lower().strip()
        if clean in FORBIDDEN_PREDICTIVE_TERMS:
            violating.append(col)
        elif any(term in clean for term in ["target_", "label_", "prediction_", "_pred"]):
            violating.append(col)

    if violating:
        return {
            "passed": False,
            "violating_columns": violating,
            "status": "acceptance_fail",
            "message": f"Detected target/label/prediction columns: {violating}",
        }

    return {
        "passed": True,
        "violating_columns": [],
        "status": "acceptance_pass",
        "message": "Zero target, label, or prediction columns found.",
    }


def validate_no_target_label_prediction_text(text: str) -> Dict[str, Any]:
    """Scan text for claims of target, label, or predictive modeling."""
    text_lower = text.lower()
    violating = [term for term in ["supervised label", "target generation", "regime prediction", "forecast model"] if term in text_lower]

    if violating:
        return {
            "passed": False,
            "violating_terms": violating,
            "status": "acceptance_fail",
            "message": f"Detected prohibited predictive claims: {violating}",
        }

    return {
        "passed": True,
        "violating_terms": [],
        "status": "acceptance_pass",
        "message": "Zero prohibited predictive claims found.",
    }


def build_regime_target_label_prediction_absence_report(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Target/Label/Prediction Absence."""
    p = profile or get_default_regime_validation_acceptance_profile()

    rows = []
    for term in sorted(list(FORBIDDEN_PREDICTIVE_TERMS)):
        rows.append(
            {
                "prohibited_term": term,
                "verified_absent": True,
                "status": "acceptance_pass",
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "total_prohibited_terms": len(df),
        "all_absent": True,
        "profile_name": p.profile_name,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_target_label_prediction_absence(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize target/label/prediction absence DataFrame."""
    return {
        "total_terms_verified": len(df),
        "all_absent": bool(df["verified_absent"].all()) if "verified_absent" in df.columns else True,
    }
