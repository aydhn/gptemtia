import pandas as pd
from typing import Dict, Any, Optional
from commodity_fx_signal_bot.ml.prediction_config import MLPredictionProfile

_FORBIDDEN_LIVE_TERMS = [
    "LIVE_SIGNAL",
    "BUY",
    "SELL",
    "OPEN_LONG",
    "OPEN_SHORT",
    "LIVE_ORDER",
    "BROKER_ORDER",
    "SEND_ORDER",
    "EXECUTE_TRADE",
    "REAL_POSITION",
    "LIVE_POSITION",
    "DEPLOYED_LIVE_MODEL"
]

def check_prediction_dataframe(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"passed": False, "reason": "empty"}
    return {"passed": True}

def check_prediction_score_ranges(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"passed": True}

    invalid_count = 0

    for col in ["confidence_score", "uncertainty_score", "prediction_score", "calibrated_score"]:
        if col in df.columns:
            # Drop na for check
            s = df[col].dropna()
            if not s.empty:
                invalid = s[(s < 0.0) | (s > 1.0)]
                invalid_count += len(invalid)

    return {
        "passed": invalid_count == 0,
        "invalid_score_count": invalid_count
    }

def check_prediction_duplicates(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty or "prediction_id" not in df.columns:
        return {"passed": True, "duplicate_prediction_count": 0}

    dupes = df.duplicated(subset=["prediction_id"]).sum()
    return {
        "passed": dupes == 0,
        "duplicate_prediction_count": int(dupes)
    }

def check_prediction_schema_compatibility(audit: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "passed": audit.get("schema_compatible", False)
    }

def check_prediction_model_quality(audit: Dict[str, Any], profile: MLPredictionProfile) -> Dict[str, Any]:
    return {
        "passed": audit.get("model_quality_score", 0.0) >= profile.min_model_quality_score
    }

def check_prediction_uncertainty(df: pd.DataFrame, threshold: float = 0.60) -> Dict[str, Any]:
    if df.empty or "uncertainty_score" not in df.columns:
        return {"passed": True, "high_uncertainty_count": 0}

    high = (df["uncertainty_score"] > threshold).sum()
    return {
        "passed": high == 0,  # Just returning count, technically it's a warning not strict fail
        "high_uncertainty_count": int(high)
    }

def check_for_forbidden_live_terms_in_predictions(df: Optional[pd.DataFrame] = None, summary: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    found_terms = []

    if df is not None and not df.empty:
        for col in df.select_dtypes(include=['object', 'string']).columns:
            for term in _FORBIDDEN_LIVE_TERMS:
                # Vectorized string check
                if df[col].astype(str).str.contains(term, case=False).any():
                    found_terms.append(term)

    if summary is not None:
        summary_str = str(summary).upper()
        for term in _FORBIDDEN_LIVE_TERMS:
            if term in summary_str:
                if term not in found_terms:
                    found_terms.append(term)

    return {
        "passed": len(found_terms) == 0,
        "forbidden_live_terms_found": found_terms
    }

def build_prediction_quality_report(df: pd.DataFrame, audit_summary: Dict[str, Any], profile: MLPredictionProfile) -> Dict[str, Any]:
    warnings = []

    empty_chk = check_prediction_dataframe(df)
    if not empty_chk["passed"]:
        return {"passed": False, "warnings": ["Empty prediction dataframe"]}

    range_chk = check_prediction_score_ranges(df)
    dupe_chk = check_prediction_duplicates(df)
    unc_chk = check_prediction_uncertainty(df, profile.uncertainty_warning_threshold)
    live_chk = check_for_forbidden_live_terms_in_predictions(df, audit_summary)

    passed = True

    if not range_chk["passed"]:
        passed = False
        warnings.append(f"Invalid scores found: {range_chk['invalid_score_count']}")

    if not dupe_chk["passed"]:
        passed = False
        warnings.append(f"Duplicate predictions found: {dupe_chk['duplicate_prediction_count']}")

    if not live_chk["passed"]:
        passed = False
        warnings.append(f"Forbidden live terms found: {live_chk['forbidden_live_terms_found']}")

    if unc_chk["high_uncertainty_count"] > 0:
        if not profile.allow_warning_models:
            passed = False
        warnings.append(f"High uncertainty predictions: {unc_chk['high_uncertainty_count']}")

    return {
        "rows": len(df),
        "duplicate_prediction_count": dupe_chk["duplicate_prediction_count"],
        "invalid_score_count": range_chk.get("invalid_score_count", 0),
        "schema_compatibility_passed": check_prediction_schema_compatibility(audit_summary)["passed"],
        "model_quality_passed": check_prediction_model_quality(audit_summary, profile)["passed"],
        "high_uncertainty_count": unc_chk["high_uncertainty_count"],
        "forbidden_live_terms_found": live_chk["forbidden_live_terms_found"],
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": warnings
    }
