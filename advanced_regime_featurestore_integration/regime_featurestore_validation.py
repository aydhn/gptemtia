"""Phase 134: Regime FeatureStore Validation.

Performs rigorous verification across profiles, contracts, schemas, catalogs,
and manifest metadata to certify total compliance with non-signal, zero-training invariants.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_STORE_READY,
    VALIDATION_DOMAIN,
)


def validate_regime_featurestore_profile_registry(
    df: pd.DataFrame,
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Dict[str, Any]:
    """Validate profile registry DataFrame."""
    errors = []
    if df.empty:
        errors.append("Profile registry is empty")
    else:
        if not (df["current_phase"] == 134).all():
            errors.append("Profile current_phase must be 134")
        if not (df["target_final_phase"] == 160).all():
            errors.append("Profile target_final_phase must be 160")
        if not (df["next_phase"] == 135).all():
            errors.append("Profile next_phase must be 135")
        if not (df["local_only"] == True).all():
            errors.append("All profiles must be local_only=True")
        if not (df["non_production"] == True).all():
            errors.append("All profiles must be non_production=True")
        if not (df["research_only"] == True).all():
            errors.append("All profiles must be research_only=True")
        if not (df["non_signal"] == True).all():
            errors.append("All profiles must be non_signal=True")
        if not (df["production_ready"] == False).all():
            errors.append("All profiles must declare production_ready=False")
        if not (df["broker_ready"] == False).all():
            errors.append("All profiles must declare broker_ready=False")

    return {"check": "profile_registry_validation", "passed": len(errors) == 0, "errors": errors}


def validate_regime_featurestore_contract_registry(
    df: pd.DataFrame,
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Dict[str, Any]:
    """Validate contract registry DataFrame."""
    errors = []
    if df.empty:
        errors.append("Contract registry is empty")
    else:
        if not (df["non_signal_required"] == True).all():
            errors.append("All contracts must enforce non_signal_required=True")
        if not (df["source_preservation_required"] == True).all():
            errors.append("All contracts must enforce source_preservation_required=True")
        if not (df["no_lookahead_acceptance_required"] == True).all():
            errors.append("All contracts must enforce no_lookahead_acceptance_required=True")
        if not (df["production_ready"] == False).all():
            errors.append("No contract may declare production_ready=True")
        if not (df["broker_ready"] == False).all():
            errors.append("No contract may declare broker_ready=True")

    return {"check": "contract_registry_validation", "passed": len(errors) == 0, "errors": errors}


def validate_regime_featurestore_schema_registry(
    df: pd.DataFrame,
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Dict[str, Any]:
    """Validate schema registry DataFrame."""
    errors = []
    if df.empty:
        errors.append("Schema registry is empty")
    else:
        field_names = df["field_name"].tolist()
        required_fields = ["store_key", "store_entity_type", "entity_id", "timestamp_utc", "non_signal"]
        for rf in required_fields:
            if rf not in field_names:
                errors.append(f"Missing core schema field: {rf}")

    return {"check": "schema_registry_validation", "passed": len(errors) == 0, "errors": errors}


def validate_regime_component_store_catalogs(
    df_map: Dict[str, pd.DataFrame],
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Dict[str, Any]:
    """Validate all component store catalog DataFrames."""
    errors = []
    for cat_name, cdf in df_map.items():
        if cdf.empty:
            errors.append(f"Catalog {cat_name} is empty")
            continue
        if not (cdf["non_signal"] == True).all():
            errors.append(f"Catalog {cat_name} violates non_signal=True")
        if not (cdf["source_preserved"] == True).all():
            errors.append(f"Catalog {cat_name} violates source_preserved=True")
        if not (cdf["production_ready"] == False).all():
            errors.append(f"Catalog {cat_name} declares production_ready=True")
        if not (cdf["broker_ready"] == False).all():
            errors.append(f"Catalog {cat_name} declares broker_ready=True")

    return {"check": "component_catalogs_validation", "passed": len(errors) == 0, "errors": errors}


def validate_regime_featurestore_metadata_manifest(
    df: pd.DataFrame,
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Dict[str, Any]:
    """Validate master metadata manifest DataFrame."""
    errors = []
    if df.empty:
        errors.append("Metadata manifest is empty")
    else:
        row = df.iloc[0]
        if row["current_phase"] != 134:
            errors.append("Manifest current_phase must be 134")
        if row["target_final_phase"] != 160:
            errors.append("Manifest target_final_phase must be 160")
        if row["next_phase"] != 135:
            errors.append("Manifest next_phase must be 135")
        if not row["non_signal"]:
            errors.append("Manifest must declare non_signal=True")
        if not row["source_preserved"]:
            errors.append("Manifest must declare source_preserved=True")
        if row["official_approval"]:
            errors.append("Manifest must declare official_approval=False")
        if row["production_ready"]:
            errors.append("Manifest must declare production_ready=False")
        if row["broker_ready"]:
            errors.append("Manifest must declare broker_ready=False")
        if row["contains_target_or_prediction"]:
            errors.append("Manifest must not contain target or prediction")
        if row["contains_trading_recommendation"]:
            errors.append("Manifest must not contain trading recommendation")
        if row["contains_full_article_text"]:
            errors.append("Manifest must not contain full article text")
        if row["contains_embedding"] or row["contains_vector"]:
            errors.append("Manifest must not contain embeddings or vectors")
        if row["sentiment_model_output"]:
            errors.append("Manifest must not contain sentiment model output")
        if row["model_training_executed"] or row["clustering_executed"]:
            errors.append("Manifest must certify zero model/clustering execution")

    return {"check": "metadata_manifest_validation", "passed": len(errors) == 0, "errors": errors}


def validate_no_forbidden_regime_featurestore_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Scan arbitrary inputs for forbidden signal/prediction keywords."""
    forbidden = ["kesin al", "kesin sat", "buy signal", "sell signal", "long aç", "short aç", "yatırım tavsiyesi"]
    violations = []
    if text:
        lower = text.lower()
        violations.extend([f for f in forbidden if f in lower])
    if df is not None:
        for col in df.columns:
            if col.lower() in ["signal", "target", "prediction", "buy", "sell"]:
                violations.append(f"forbidden_column:{col}")
    if summary:
        for k, v in summary.items():
            if any(f in str(k).lower() or f in str(v).lower() for f in forbidden):
                violations.append(f"forbidden_summary:{k}")

    return {"check": "forbidden_claims_validation", "passed": len(violations) == 0, "violations": violations}


def build_regime_featurestore_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Aggregate all validation checks into a single report DataFrame."""
    active_profile = profile or get_regime_featurestore_profile()

    checks = []
    if "profiles" in tables:
        checks.append(validate_regime_featurestore_profile_registry(tables["profiles"], active_profile))
    if "contracts" in tables:
        checks.append(validate_regime_featurestore_contract_registry(tables["contracts"], active_profile))
    if "schema" in tables:
        checks.append(validate_regime_featurestore_schema_registry(tables["schema"], active_profile))
    if "catalogs" in tables and isinstance(tables["catalogs"], dict):
        checks.append(validate_regime_component_store_catalogs(tables["catalogs"], active_profile))
    if "manifest" in tables:
        checks.append(validate_regime_featurestore_metadata_manifest(tables["manifest"], active_profile))

    checks.append(validate_no_forbidden_regime_featurestore_claims())

    results = []
    for c in checks:
        results.append({
            "check_name": c["check"],
            "passed": c["passed"],
            "error_count": len(c.get("errors", c.get("violations", []))),
            "errors": "; ".join(c.get("errors", c.get("violations", []))) or "None",
            "non_signal": True,
        })

    df = pd.DataFrame(results)
    all_passed = bool((df["passed"] == True).all()) if not df.empty else True

    summary = {
        "domain": VALIDATION_DOMAIN,
        "total_checks": len(df),
        "failed_checks": int((df["passed"] == False).sum()) if not df.empty else 0,
        "all_passed": all_passed,
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY if all_passed else "VALIDATION_FAILED",
        "non_signal": True,
    }
    return df, summary


def summarize_regime_featurestore_validation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize validation report DataFrame."""
    return {
        "total_checks": len(df),
        "all_passed": bool((df["passed"] == True).all()) if not df.empty else True,
        "failed_checks": int((df["passed"] == False).sum()) if not df.empty else 0,
    }
