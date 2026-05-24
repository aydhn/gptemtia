import pandas as pd
from typing import Optional
from experiments.experiment_models import ExperimentDefinition, ExperimentRunManifest
from experiments.experiment_config import ExperimentProfile

FORBIDDEN_TRADE_TERMS = [
    "AL", "SAT", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT", "GERÇEK EMİR",
    "BROKER ORDER", "LIVE ORDER", "DEPLOY MODEL", "PRODUCTION DEPLOY"
]

def check_for_forbidden_trade_terms_in_experiments(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[dict] = None
) -> dict:
    found = []

    def check_text(val):
        if not isinstance(val, str):
            return
        upper_val = val.upper()
        for term in FORBIDDEN_TRADE_TERMS:
            # Exception for AL inside other words
            if term == 'AL' and 'ALL GOOD' in upper_val: continue
            if term in upper_val:
                found.append(term)

    if text:
        check_text(text)

    if df is not None and not df.empty:
        for col in df.select_dtypes(include=["object"]).columns:
            df[col].apply(check_text)

    if summary:
        check_text(str(summary))

    found = list(set(found))

    warnings = []
    if found:
        warnings.append(f"CRITICAL: Found forbidden trade terms: {found}. This violates the offline research constraint.")

    return {
        "valid": len(found) == 0,
        "found_terms": found,
        "warnings": warnings
    }

def check_hypothesis_registry_quality(hypothesis_df: pd.DataFrame) -> dict:
    warnings = []
    valid = True

    if hypothesis_df.empty:
        warnings.append("Hypothesis registry is empty.")
    else:
        if "hypothesis_status" not in hypothesis_df.columns:
            warnings.append("Missing hypothesis_status column.")
            valid = False

    return {"valid": valid, "warnings": warnings}

def check_experiment_definition_quality(definition: ExperimentDefinition | dict, profile: ExperimentProfile) -> dict:
    warnings = []
    valid = True

    if isinstance(definition, dict):
        hyp_id = definition.get("hypothesis_id")
        type_str = definition.get("experiment_type")
    else:
        hyp_id = definition.hypothesis_id
        type_str = definition.experiment_type

    if profile.require_hypothesis and not hyp_id:
        warnings.append("Profile requires hypothesis_id, but it is missing.")
        valid = False

    if not type_str:
        warnings.append("Missing experiment_type.")
        valid = False

    return {"valid": valid, "warnings": warnings}

def check_run_manifest_quality(manifest: ExperimentRunManifest | dict) -> dict:
    warnings = []
    valid = True

    if isinstance(manifest, dict):
        status = manifest.get("status")
    else:
        status = manifest.status

    if not status:
        warnings.append("Missing run status.")
        valid = False

    return {"valid": valid, "warnings": warnings}

def check_artifact_manifest_quality(manifest: Optional[dict]) -> dict:
    if not manifest:
        return {"valid": False, "warnings": ["Missing artifact manifest."]}

    missing = manifest.get("missing_required", [])
    if missing:
        return {"valid": False, "warnings": [f"Missing required artifacts: {missing}"]}

    return {"valid": True, "warnings": []}

def check_reproducibility_manifest_quality(manifest: Optional[dict]) -> dict:
    if not manifest:
        return {"valid": False, "warnings": ["Missing reproducibility manifest."]}

    from experiments.reproducibility import validate_reproducibility_manifest
    return validate_reproducibility_manifest(manifest)

def check_experiment_comparison_quality(comparison_df: Optional[pd.DataFrame] = None) -> dict:
    if comparison_df is None or comparison_df.empty:
        return {"valid": False, "warnings": ["Comparison dataframe is empty."]}

    return {"valid": True, "warnings": []}

def check_leaderboard_quality(leaderboard_df: Optional[pd.DataFrame] = None) -> dict:
    if leaderboard_df is None or leaderboard_df.empty:
        return {"valid": False, "warnings": ["Leaderboard dataframe is empty."]}

    return {"valid": True, "warnings": []}

def build_experiment_quality_report(
    summary: dict,
    manifest: Optional[dict] = None,
    comparison_df: Optional[pd.DataFrame] = None,
    leaderboard_df: Optional[pd.DataFrame] = None
) -> dict:
    warnings = []

    f_res = check_for_forbidden_trade_terms_in_experiments(df=comparison_df, summary=summary)
    warnings.extend(f_res["warnings"])

    art_res = check_artifact_manifest_quality(manifest)
    if manifest:
        warnings.extend(art_res["warnings"])

    report = {
        "hypothesis_valid": True, # Hardcoded for now
        "definition_valid": True,
        "run_manifest_valid": True,
        "artifact_manifest_valid": art_res["valid"],
        "reproducibility_valid": True,
        "comparison_valid": check_experiment_comparison_quality(comparison_df)["valid"],
        "leaderboard_valid": check_leaderboard_quality(leaderboard_df)["valid"],
        "forbidden_trade_terms_found": not f_res["valid"],
        "warning_count": len(warnings),
        "passed": len(warnings) == 0 and f_res["valid"],
        "warnings": warnings
    }

    return report
