from typing import Tuple, Dict, Any, List, Optional
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile

FORBIDDEN_KEYWORDS = [
    "live trading", "broker execution", "buy order", "sell order", "al/sat",
    "yatırım tavsiyesi", "investment advice", "trading signal", "trade sinyali",
    "official approval", "resmi onay", "production deployment", "model deployment",
    "scraped full text", "article body download", "paywall bypass", "reverse engineered api"
]


def validate_no_forbidden_data_quality_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    breaches: List[str] = []
    
    if text:
        lower_txt = text.lower()
        for kw in FORBIDDEN_KEYWORDS:
            if kw in lower_txt and "değildir" not in lower_txt and "yasak" not in lower_txt and "yoktur" not in lower_txt:
                breaches.append(f"Forbidden claim detected in text: '{kw}'")

    if df is not None and not df.empty:
        # Check string columns for forbidden phrases
        for col in df.select_dtypes(include="object").columns:
            for val in df[col].dropna().astype(str):
                val_lower = val.lower()
                for kw in FORBIDDEN_KEYWORDS:
                    if kw in val_lower and "değildir" not in val_lower and "yasak" not in val_lower and "yoktur" not in val_lower:
                        breaches.append(f"Forbidden claim in column '{col}': '{kw}'")

    return {
        "valid": len(breaches) == 0,
        "breaches": breaches,
    }


def validate_data_quality_profile_registry(df: pd.DataFrame, profile: DataQualityProfile) -> Dict[str, Any]:
    errors: List[str] = []
    if df is None or len(df) == 0:
        errors.append("Profile registry DataFrame is empty.")
    if "profile_name" not in df.columns:
        errors.append("Missing 'profile_name' column in profile registry.")
    return {"valid": len(errors) == 0, "errors": errors}


def validate_data_quality_domain_registry(df: pd.DataFrame, profile: DataQualityProfile) -> Dict[str, Any]:
    errors: List[str] = []
    if df is None or len(df) < 20:
        errors.append("Domain registry has insufficient domain coverage.")
    return {"valid": len(errors) == 0, "errors": errors}


def validate_quality_severity_registry(df: pd.DataFrame, profile: DataQualityProfile) -> Dict[str, Any]:
    errors: List[str] = []
    if df is None or len(df) == 0:
        errors.append("Severity registry is empty.")
    expected_sevs = {"quality_critical", "quality_high", "quality_medium", "quality_low", "quality_info"}
    actual_sevs = set(df["severity_label"].unique()) if "severity_label" in df.columns else set()
    if not expected_sevs.issubset(actual_sevs):
        errors.append(f"Missing severities: {expected_sevs - actual_sevs}")
    return {"valid": len(errors) == 0, "errors": errors}


def validate_quality_rule_registry(df: pd.DataFrame, profile: DataQualityProfile) -> Dict[str, Any]:
    errors: List[str] = []
    if df is None or len(df) < 15:
        errors.append(f"Rule registry count too low: {len(df) if df is not None else 0}")
    return {"valid": len(errors) == 0, "errors": errors}


def validate_quality_findings(df: pd.DataFrame, profile: DataQualityProfile) -> Dict[str, Any]:
    errors: List[str] = []
    if df is not None and not df.empty:
        if "finding_id" not in df.columns or "severity_label" not in df.columns:
            errors.append("Findings DataFrame missing mandatory identifier/severity columns.")
    return {"valid": len(errors) == 0, "errors": errors}


def validate_manual_review_queue(df: pd.DataFrame, profile: DataQualityProfile) -> Dict[str, Any]:
    errors: List[str] = []
    if df is not None and not df.empty:
        if "destructive_action_allowed" in df.columns:
            if df["destructive_action_allowed"].any():
                errors.append("CRITICAL: Manual review queue contains destructive actions!")
    return {"valid": len(errors) == 0, "errors": errors}


def validate_provider_quality_scores(df: pd.DataFrame, profile: DataQualityProfile) -> Dict[str, Any]:
    errors: List[str] = []
    if df is not None and not df.empty:
        if "score" in df.columns:
            if (df["score"] < 0.0).any() or (df["score"] > 1.0).any():
                errors.append("Provider quality scores must be bounded within [0.0, 1.0].")
    return {"valid": len(errors) == 0, "errors": errors}


def validate_dataset_quality_scores(df: pd.DataFrame, profile: DataQualityProfile) -> Dict[str, Any]:
    errors: List[str] = []
    if df is not None and not df.empty:
        if "score" in df.columns:
            if (df["score"] < 0.0).any() or (df["score"] > 1.0).any():
                errors.append("Dataset quality scores must be bounded within [0.0, 1.0].")
    return {"valid": len(errors) == 0, "errors": errors}


def validate_data_quality_safety_boundary(df: pd.DataFrame, profile: DataQualityProfile) -> Dict[str, Any]:
    errors: List[str] = []
    if df is None or len(df) < 30:
        errors.append("Safety boundary registry has insufficient rules.")
    return {"valid": len(errors) == 0, "errors": errors}


def build_data_quality_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: DataQualityProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    all_errors = []

    checks = [
        ("profile_registry", validate_data_quality_profile_registry),
        ("domain_registry", validate_data_quality_domain_registry),
        ("severity_registry", validate_quality_severity_registry),
        ("rule_registry", validate_quality_rule_registry),
        ("quality_findings", validate_quality_findings),
        ("manual_review_queue", validate_manual_review_queue),
        ("provider_quality_scores", validate_provider_quality_scores),
        ("dataset_quality_scores", validate_dataset_quality_scores),
        ("safety_boundary", validate_data_quality_safety_boundary),
    ]

    for name, func in checks:
        table = tables.get(name, pd.DataFrame())
        res = func(table, profile)
        is_val = res.get("valid", False)
        errs = res.get("errors", [])
        all_errors.extend(errs)
        records.append({
            "target": name,
            "status": "PASS" if is_val else "FAIL",
            "error_count": len(errs),
            "errors": "; ".join(errs) if errs else "None",
        })

    df = pd.DataFrame.from_records(records)
    summary = {
        "valid": len(all_errors) == 0,
        "total_validations": len(records),
        "errors": all_errors,
        "current_phase": 112,
        "target_final_phase": 160,
    }
    return df, summary
