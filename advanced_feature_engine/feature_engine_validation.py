from typing import Tuple, Dict, Any, Optional
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile

FORBIDDEN_CLAIM_WORDS = [
    "kesin al",
    "kesin sat",
    "kesin long",
    "kesin short",
    "buy signal",
    "sell signal",
    "trade signal",
    "trading signal",
    "investment advice",
    "yatırım tavsiyesi",
    "official approval",
    "production ready",
    "broker ready",
    "live execution",
    "guaranteed return",
]


def validate_no_forbidden_feature_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    findings = []

    if text:
        text_lower = text.lower()
        for w in FORBIDDEN_CLAIM_WORDS:
            if w in text_lower:
                findings.append(f"Forbidden claim in text: '{w}'")

    if summary:
        for k, v in summary.items():
            if isinstance(v, str):
                v_lower = v.lower()
                for w in FORBIDDEN_CLAIM_WORDS:
                    if w in v_lower:
                        findings.append(f"Forbidden claim in summary key '{k}': '{w}'")
            if any(forbidden in k.lower() for forbidden in ["signal_guarantee", "official_approval", "broker_ready"]):
                findings.append(f"Forbidden flag in summary: '{k}'")

    if df is not None and not df.empty:
        for col in df.columns:
            col_str = str(col).lower()
            for w in ["signal", "buy", "sell", "long", "short", "position", "target", "label"]:
                if col_str == w:
                    findings.append(f"Forbidden column name in DataFrame: '{col}'")

    return {
        "valid": len(findings) == 0,
        "forbidden_claims_found": len(findings) > 0,
        "findings": findings,
    }


def validate_feature_engine_profile_registry(
    df: pd.DataFrame,
    profile: FeatureEngineProfile,
) -> Dict[str, Any]:
    if df.empty:
        return {"valid": False, "error": "Profile registry DataFrame is empty."}
    if not (df["current_phase"] == 116).all():
        return {"valid": False, "error": "All profiles must have current_phase == 116."}
    if not (df["target_final_phase"] == 160).all():
        return {"valid": False, "error": "All profiles must have target_final_phase == 160."}
    if not (df["next_phase"] == 117).all():
        return {"valid": False, "error": "All profiles must have next_phase == 117."}
    if not (df["non_signal"] == True).all():
        return {"valid": False, "error": "All profiles must enforce non_signal == True."}
    return {"valid": True, "total_profiles": len(df)}


def validate_feature_input_contracts(
    df: pd.DataFrame,
    profile: FeatureEngineProfile,
) -> Dict[str, Any]:
    if df.empty:
        return {"valid": False, "error": "Input contract DataFrame is empty."}
    if len(df) < 8:
        return {"valid": False, "error": f"Expected at least 8 input contracts, got {len(df)}."}
    return {"valid": True, "total_contracts": len(df)}


def validate_feature_schema_registry(
    df: pd.DataFrame,
    profile: FeatureEngineProfile,
) -> Dict[str, Any]:
    if df.empty:
        return {"valid": False, "error": "Feature schema registry is empty."}
    if not (df["non_signal"] == True).all():
        return {"valid": False, "error": "All feature schemas must be non_signal == True."}
    return {"valid": True, "total_schemas": len(df)}


def validate_factor_schema_registry(
    df: pd.DataFrame,
    profile: FeatureEngineProfile,
) -> Dict[str, Any]:
    if df.empty:
        return {"valid": False, "error": "Factor schema registry is empty."}
    if not (df["non_signal"] == True).all():
        return {"valid": False, "error": "All factor schemas must be non_signal == True."}
    return {"valid": True, "total_factors": len(df)}


def validate_indicator_catalog_registry(
    df: pd.DataFrame,
    profile: FeatureEngineProfile,
) -> Dict[str, Any]:
    if df.empty:
        return {"valid": False, "error": "Indicator catalog is empty."}
    families = set(df["indicator_family"].unique())
    required_families = {"price", "trend", "momentum", "volatility", "mean_reversion"}
    missing = required_families - families
    if missing:
        return {"valid": False, "error": f"Missing indicator families: {missing}"}
    return {"valid": True, "total_indicators": len(df), "families": list(families)}


def build_feature_engine_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    findings = []

    # 1. Profile registry validation
    prof_df = tables.get("profiles", pd.DataFrame())
    prof_val = validate_feature_engine_profile_registry(prof_df, profile)
    findings.append({
        "check": "profile_registry_validation",
        "valid": prof_val["valid"],
        "details": prof_val.get("error", f"{prof_val.get('total_profiles', 0)} profiles verified"),
    })

    # 2. Input contract validation
    ic_df = tables.get("input_contracts", pd.DataFrame())
    ic_val = validate_feature_input_contracts(ic_df, profile)
    findings.append({
        "check": "input_contracts_validation",
        "valid": ic_val["valid"],
        "details": ic_val.get("error", f"{ic_val.get('total_contracts', 0)} contracts verified"),
    })

    # 3. Feature schema validation
    fs_df = tables.get("feature_schemas", pd.DataFrame())
    fs_val = validate_feature_schema_registry(fs_df, profile)
    findings.append({
        "check": "feature_schema_validation",
        "valid": fs_val["valid"],
        "details": fs_val.get("error", f"{fs_val.get('total_schemas', 0)} schemas verified"),
    })

    # 4. Factor schema validation
    fact_df = tables.get("factor_schemas", pd.DataFrame())
    fact_val = validate_factor_schema_registry(fact_df, profile)
    findings.append({
        "check": "factor_schema_validation",
        "valid": fact_val["valid"],
        "details": fact_val.get("error", f"{fact_val.get('total_factors', 0)} factor schemas verified"),
    })

    # 5. Indicator catalog validation
    ind_df = tables.get("indicator_catalogs", pd.DataFrame())
    ind_val = validate_indicator_catalog_registry(ind_df, profile)
    findings.append({
        "check": "indicator_catalog_validation",
        "valid": ind_val["valid"],
        "details": ind_val.get("error", f"{ind_val.get('total_indicators', 0)} indicators across 5 families verified"),
    })

    # 6. Forbidden claims scan across all tables
    for tbl_name, t_df in tables.items():
        claim_check = validate_no_forbidden_feature_claims(df=t_df)
        findings.append({
            "check": f"forbidden_claims_check_{tbl_name}",
            "valid": claim_check["valid"],
            "details": f"No forbidden claims found in {tbl_name}" if claim_check["valid"] else "; ".join(claim_check["findings"]),
        })

    df = pd.DataFrame.from_records(findings)
    all_valid = bool(df["valid"].all()) if not df.empty else False

    summary = {
        "validation_status": "VALID" if all_valid else "INVALID",
        "total_checks": len(df),
        "passed_checks": int(df["valid"].sum()) if not df.empty else 0,
        "forbidden_claims_found": not all_valid,
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
        "non_signal": True,
    }
    return df, summary
