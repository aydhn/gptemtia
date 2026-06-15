"""
Metadata Validation module.
"""

import pandas as pd
from pathlib import Path
from .metadata_config import ArtifactMetadataProfile

def validate_research_artifacts(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> dict:
    if artifact_df.empty:
        return {"valid": True, "warnings": []}

    warnings = []
    if "artifact_id" not in artifact_df.columns:
        warnings.append("Missing artifact_id column.")

    return {
        "valid": len(warnings) == 0,
        "warnings": warnings
    }

def validate_no_deployment_or_advice_claims(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    forbidden = [
        "model deployment approved", "production model approved",
        "officially certified", "compliance certified",
        "investment advice", "yatirim tavsiyesidir", "kesin al", "kesin sat",
        "live order", "broker order", "real trade",
        "open position", "close position", "guaranteed profit", "risk-free return"
    ]

    found = []

    def check_text(t: str):
        if not t or not isinstance(t, str): return
        t_low = t.lower()
        for f in forbidden:
            if f in t_low:
                # false positive check
                if "degildir" in t_low or "değildir" in t_low or "yoktur" in t_low or "no " in t_low or "not " in t_low:
                     continue
                found.append(f)

    if text:
        check_text(text)

    if df is not None and not df.empty:
        for col in df.columns:
            if df[col].dtype == object:
                for val in df[col].dropna():
                    check_text(str(val))

    return {
        "valid": len(found) == 0,
        "forbidden_terms_found": list(set(found))
    }

def validate_artifact_cards(cards_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> dict:
    if cards_df.empty:
        return {"valid": True, "warnings": []}

    warnings = []
    required = ["card_id", "artifact_id", "intended_use", "non_use_policy", "limitations"]
    for req in required:
        if req not in cards_df.columns:
            warnings.append(f"Missing column: {req}")

    val_res = validate_no_deployment_or_advice_claims(df=cards_df)
    if not val_res["valid"]:
        warnings.extend([f"Forbidden term found: {term}" for term in val_res["forbidden_terms_found"]])

    return {
        "valid": len(warnings) == 0,
        "warnings": warnings
    }

def validate_card_tables(card_tables: dict[str, pd.DataFrame], profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    results = []
    all_warnings = []

    for name, df in card_tables.items():
        res = validate_artifact_cards(df, profile)
        results.append({
            "table_name": name,
            "valid": res["valid"],
            "warning_count": len(res["warnings"])
        })
        all_warnings.extend([f"[{name}] {w}" for w in res["warnings"]])

    res_df = pd.DataFrame(results) if results else pd.DataFrame()
    return res_df, {
        "all_valid": all(r["valid"] for r in results) if results else True,
        "total_warnings": len(all_warnings),
        "warnings": all_warnings
    }

def validate_non_use_policies(card_tables: dict[str, pd.DataFrame], profile: ArtifactMetadataProfile) -> dict:
    # ensuring non_use_policy exists and is not empty in all tables
    warnings = []
    for name, df in card_tables.items():
        if df.empty: continue
        if "non_use_policy" not in df.columns:
            warnings.append(f"[{name}] missing non_use_policy")
        else:
            missing = df["non_use_policy"].isna().sum() + (df["non_use_policy"] == "").sum()
            if missing > 0:
                 warnings.append(f"[{name}] {missing} rows missing non_use_policy")

    return {"valid": len(warnings) == 0, "warnings": warnings}

def build_card_validation_report(tables: dict[str, pd.DataFrame], profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    return validate_card_tables(tables, profile)
