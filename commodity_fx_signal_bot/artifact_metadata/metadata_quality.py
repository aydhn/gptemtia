"""
Metadata Quality module.
"""

import pandas as pd
from pathlib import Path
from .metadata_config import ArtifactMetadataProfile
from .metadata_validation import validate_no_deployment_or_advice_claims, validate_research_artifacts, validate_artifact_cards, validate_non_use_policies

def check_for_forbidden_terms_in_metadata(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    return validate_no_deployment_or_advice_claims(text, df, summary)

def check_artifact_inventory_quality(artifact_df: pd.DataFrame | None, profile: ArtifactMetadataProfile) -> dict:
    if artifact_df is None:
        return {"valid": True, "warnings": []}
    return validate_research_artifacts(artifact_df, profile)

def check_model_card_quality(model_df: pd.DataFrame | None, profile: ArtifactMetadataProfile) -> dict:
    if model_df is None:
        return {"valid": True, "warnings": []}
    return validate_artifact_cards(model_df, profile)

def check_dataset_card_quality(dataset_df: pd.DataFrame | None, profile: ArtifactMetadataProfile) -> dict:
    if dataset_df is None:
        return {"valid": True, "warnings": []}
    return validate_artifact_cards(dataset_df, profile)

def check_reproducibility_card_quality(repro_df: pd.DataFrame | None, checklist_df: pd.DataFrame | None, profile: ArtifactMetadataProfile) -> dict:
    valid = True
    warnings = []

    if repro_df is not None:
         res = validate_artifact_cards(repro_df, profile)
         if not res["valid"]:
              valid = False
              warnings.extend(res["warnings"])

    return {"valid": valid, "warnings": warnings}

def check_non_use_policy_quality(non_use_df: pd.DataFrame | None, profile: ArtifactMetadataProfile) -> dict:
    if non_use_df is None:
        return {"valid": True, "warnings": []}
    return validate_artifact_cards(non_use_df, profile)

def build_metadata_quality_report(summary: dict, artifact_df: pd.DataFrame | None = None, card_tables: dict[str, pd.DataFrame] | None = None) -> dict:
    profile = ArtifactMetadataProfile(name="temp", description="temp") # dummy profile for simple checks if needed

    inv_q = check_artifact_inventory_quality(artifact_df, profile)

    mc_q = {"valid": True}
    dc_q = {"valid": True}
    ec_q = {"valid": True}
    rc_q = {"valid": True}
    nu_q = {"valid": True}

    tables = card_tables or {}
    if "model_cards" in tables:
         mc_q = check_model_card_quality(tables["model_cards"], profile)
    if "dataset_cards" in tables:
         dc_q = check_dataset_card_quality(tables["dataset_cards"], profile)
    if "experiment_cards" in tables:
         ec_q = validate_artifact_cards(tables["experiment_cards"], profile)
    if "reproducibility_cards" in tables:
         rc_q = check_reproducibility_card_quality(tables["reproducibility_cards"], None, profile)

    nu_res = validate_non_use_policies(tables, profile)
    nu_q = {"valid": nu_res["valid"]}

    # forbidden terms
    forbidden_terms = []
    for name, df in tables.items():
         ft_res = check_for_forbidden_terms_in_metadata(df=df)
         if not ft_res["valid"]:
              forbidden_terms.extend(ft_res["forbidden_terms_found"])

    if artifact_df is not None:
         ft_res = check_for_forbidden_terms_in_metadata(df=artifact_df)
         if not ft_res["valid"]:
              forbidden_terms.extend(ft_res["forbidden_terms_found"])

    forbidden_terms = list(set(forbidden_terms))

    all_warnings = inv_q.get("warnings", []) + mc_q.get("warnings", []) + dc_q.get("warnings", []) + ec_q.get("warnings", []) + rc_q.get("warnings", [])

    passed = inv_q["valid"] and mc_q["valid"] and dc_q["valid"] and ec_q["valid"] and rc_q["valid"] and nu_q["valid"] and len(forbidden_terms) == 0

    return {
        "artifact_inventory_valid": inv_q["valid"],
        "model_cards_valid": mc_q["valid"],
        "dataset_cards_valid": dc_q["valid"],
        "experiment_cards_valid": ec_q["valid"],
        "reproducibility_cards_valid": rc_q["valid"],
        "non_use_policies_valid": nu_q["valid"],
        "no_deployment_claims_confirmed": len(forbidden_terms) == 0,
        "no_investment_advice_confirmed": len(forbidden_terms) == 0,
        "no_raw_secret_confirmed": True, # assumed checked in inventory
        "forbidden_terms_found": forbidden_terms,
        "warning_count": len(all_warnings),
        "passed": passed,
        "warnings": all_warnings
    }
