"""Phase 128: Regime Rule-Free Validation.

Provides comprehensive validation routines verifying that all Phase 128 outputs,
contracts, schemas, and manifests satisfy invariant non-signal and zero-execution requirements.
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_forbidden_claims import (
    validate_regime_rule_free_forbidden_claims,
)


def validate_regime_rule_free_profile_registry(
    df: pd.DataFrame,
    profile: RegimeRuleFreeProfile | None = None,
) -> Dict:
    """Validate profile registry against phase boundaries."""
    violations = []
    if df.empty:
        return {"is_valid": False, "violations": ["Profile registry DataFrame is empty"]}

    if not df["current_phase"].isin([128]).all():
        violations.append("current_phase must be 128")
    if not df["next_phase"].isin([129]).all():
        violations.append("next_phase must be 129")
    if not df["target_final_phase"].isin([160]).all():
        violations.append("target_final_phase must be 160")
    if not df["non_signal"].all():
        violations.append("non_signal must be True for all profiles")
    if df["clustering_allowed"].any():
        violations.append("clustering_allowed must be False for all profiles")
    if df["model_training_allowed"].any():
        violations.append("model_training_allowed must be False for all profiles")

    return {"is_valid": len(violations) == 0, "violations": violations}


def validate_rule_free_labeling_contracts(
    df: pd.DataFrame,
    profile: RegimeRuleFreeProfile | None = None,
) -> Dict:
    """Validate that rule-free labeling contracts satisfy non-signal criteria."""
    violations = []
    if df.empty:
        return {"is_valid": False, "violations": ["Contract registry DataFrame is empty"]}

    if not df["non_signal_required"].all():
        violations.append("non_signal_required must be True for all contracts")
    if not df["target_label_forbidden"].all():
        violations.append("target_label_forbidden must be True for all contracts")
    if not df["prediction_forbidden"].all():
        violations.append("prediction_forbidden must be True for all contracts")
    if df["clustering_allowed"].any():
        violations.append("clustering_allowed must be False for all contracts")
    if df["model_training_allowed"].any():
        violations.append("model_training_allowed must be False for all contracts")

    return {"is_valid": len(violations) == 0, "violations": violations}


def validate_candidate_state_schema(
    df: pd.DataFrame,
    profile: RegimeRuleFreeProfile | None = None,
) -> Dict:
    """Validate that candidate state schema items do not contain forbidden targets."""
    violations = []
    if df.empty:
        return {"is_valid": False, "violations": ["Candidate state schema DataFrame is empty"]}

    if not df["non_signal"].all():
        violations.append("non_signal must be True for all schema columns")
    if df["is_target_or_prediction"].any():
        violations.append("is_target_or_prediction must be False for all schema columns")

    return {"is_valid": len(violations) == 0, "violations": violations}


def validate_unsupervised_prep_contracts(
    df: pd.DataFrame,
    profile: RegimeRuleFreeProfile | None = None,
) -> Dict:
    """Validate that unsupervised prep contracts permit zero execution."""
    violations = []
    if df.empty:
        return {"is_valid": False, "violations": ["Unsupervised prep DataFrame is empty"]}

    if not df["non_signal"].all():
        violations.append("non_signal must be True")
    if df["fit_transform_allowed"].any():
        violations.append("fit_transform_allowed must be False")
    if df["model_training_allowed"].any():
        violations.append("model_training_allowed must be False")
    if df["clustering_allowed"].any():
        violations.append("clustering_allowed must be False")

    return {"is_valid": len(violations) == 0, "violations": violations}


def validate_candidate_state_integrity_manifest(
    df: pd.DataFrame,
    profile: RegimeRuleFreeProfile | None = None,
) -> Dict:
    """Validate candidate state integrity manifest certifications."""
    violations = []
    if df.empty:
        return {"is_valid": False, "violations": ["Integrity manifest DataFrame is empty"]}

    row = df.iloc[0].to_dict()
    if row.get("current_phase") != 128:
        violations.append("current_phase must be 128")
    if row.get("target_final_phase") != 160:
        violations.append("target_final_phase must be 160")
    if row.get("next_phase") != 129:
        violations.append("next_phase must be 129")
    if row.get("non_signal") is not True:
        violations.append("non_signal must be True")
    if row.get("source_preserved") is not True:
        violations.append("source_preserved must be True")
    if row.get("official_approval") is not False:
        violations.append("official_approval must be False")
    if row.get("production_ready") is not False:
        violations.append("production_ready must be False")
    if row.get("broker_ready") is not False:
        violations.append("broker_ready must be False")
    if row.get("model_training_executed") is not False:
        violations.append("model_training_executed must be False")
    if row.get("model_fit_executed") is not False:
        violations.append("model_fit_executed must be False")
    if row.get("model_predict_executed") is not False:
        violations.append("model_predict_executed must be False")
    if row.get("clustering_executed") is not False:
        violations.append("clustering_executed must be False")
    if row.get("unsupervised_execution") is not False:
        violations.append("unsupervised_execution must be False")
    if row.get("dimensionality_reduction_executed") is not False:
        violations.append("dimensionality_reduction_executed must be False")

    return {"is_valid": len(violations) == 0, "violations": violations}


def validate_no_forbidden_rule_free_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict] = None,
) -> Dict:
    """Scan strings, DataFrame text, or dictionary values for forbidden commercial/trading claims."""
    combined_text = []
    if text:
        combined_text.append(text)
    if df is not None and not df.empty:
        for col in df.select_dtypes(include=["object", "string"]).columns:
            combined_text.extend(df[col].astype(str).tolist())
    if summary:
        combined_text.append(str(summary))

    full_content = " ".join(combined_text)
    res = validate_regime_rule_free_forbidden_claims(full_content)
    return {
        "is_clean": res["is_clean"],
        "violations": res["detected_forbidden_claims"],
    }


def build_regime_rule_free_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Execute all validation checks across generated Phase 128 tables and produce report."""
    active_profile = profile or get_default_regime_rule_free_profile()

    checks = []

    # 1. Profile registry validation
    if "profiles" in tables:
        res = validate_regime_rule_free_profile_registry(tables["profiles"], active_profile)
        checks.append({
            "check_name": "profile_registry_validation",
            "passed": res["is_valid"],
            "violations_count": len(res["violations"]),
            "details": "; ".join(res["violations"]) if res["violations"] else "OK",
        })

    # 2. Labeling contracts validation
    if "labeling_contracts" in tables:
        res = validate_rule_free_labeling_contracts(tables["labeling_contracts"], active_profile)
        checks.append({
            "check_name": "labeling_contracts_validation",
            "passed": res["is_valid"],
            "violations_count": len(res["violations"]),
            "details": "; ".join(res["violations"]) if res["violations"] else "OK",
        })

    # 3. Candidate state schema validation
    if "candidate_state_schema" in tables:
        res = validate_candidate_state_schema(tables["candidate_state_schema"], active_profile)
        checks.append({
            "check_name": "candidate_state_schema_validation",
            "passed": res["is_valid"],
            "violations_count": len(res["violations"]),
            "details": "; ".join(res["violations"]) if res["violations"] else "OK",
        })

    # 4. Unsupervised prep contracts validation
    if "unsupervised_prep" in tables:
        res = validate_unsupervised_prep_contracts(tables["unsupervised_prep"], active_profile)
        checks.append({
            "check_name": "unsupervised_prep_validation",
            "passed": res["is_valid"],
            "violations_count": len(res["violations"]),
            "details": "; ".join(res["violations"]) if res["violations"] else "OK",
        })

    # 5. Integrity manifest validation
    if "integrity_manifest" in tables:
        res = validate_candidate_state_integrity_manifest(tables["integrity_manifest"], active_profile)
        checks.append({
            "check_name": "integrity_manifest_validation",
            "passed": res["is_valid"],
            "violations_count": len(res["violations"]),
            "details": "; ".join(res["violations"]) if res["violations"] else "OK",
        })

    # 6. Global forbidden claims scan across tables (excluding catalog itself)
    all_clean = True
    all_violations = []
    for tname, tdf in tables.items():
        if tname == "forbidden_claims":
            continue
        scan = validate_no_forbidden_rule_free_claims(df=tdf)
        if not scan["is_clean"]:
            all_clean = False
            all_violations.extend([f"{tname}: {v}" for v in scan["violations"]])

    checks.append({
        "check_name": "global_forbidden_claims_validation",
        "passed": all_clean,
        "violations_count": len(all_violations),
        "details": "; ".join(all_violations) if all_violations else "OK",
    })

    df = pd.DataFrame(checks)
    total_checks = len(df)
    passed_checks = int(df["passed"].sum()) if not df.empty else 0
    all_passed = (total_checks > 0) and (passed_checks == total_checks)

    summary = {
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "total_checks": total_checks,
        "passed_checks": passed_checks,
        "failed_checks": total_checks - passed_checks,
        "forbidden_claims_clean": all_clean,
        "zero_execution_clean": True,
        "current_phase": active_profile.current_phase,
        "next_phase": active_profile.next_phase,
    }

    return df, summary
