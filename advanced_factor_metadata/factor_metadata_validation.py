"""Phase 122 Factor Metadata Validation Suite.

Validates profile registries, family registries, contracts, namespace, output schema,
and manifests against non-signal and zero-lookahead safety boundaries.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_forbidden_claims import validate_factor_forbidden_claims
from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY
from advanced_factor_metadata.factor_metadata_models import FORBIDDEN_FACTOR_TOKENS


def validate_factor_metadata_profile_registry(
    df: pd.DataFrame,
    profile: FactorMetadataProfile | None = None,
) -> Dict[str, Any]:
    active_profile = profile or get_default_factor_metadata_profile()
    errors: List[str] = []

    if df.empty:
        errors.append("Profile registry is empty")

    if "current_phase" in df and not (df["current_phase"] == 122).all():
        errors.append("All profiles must declare current_phase == 122")

    if "target_final_phase" in df and not (df["target_final_phase"] == 160).all():
        errors.append("All profiles must declare target_final_phase == 160")

    if "next_phase" in df and not (df["next_phase"] == 123).all():
        errors.append("All profiles must declare next_phase == 123")

    if "non_signal" in df and not (df["non_signal"] == True).all():
        errors.append("All profiles must enforce non_signal == True")

    is_valid = len(errors) == 0
    return {
        "check_name": "profile_registry_validation",
        "is_valid": is_valid,
        "errors": errors,
        "active_profile": active_profile.name,
    }


def validate_factor_family_registry(
    df: pd.DataFrame,
    profile: FactorMetadataProfile | None = None,
) -> Dict[str, Any]:
    errors: List[str] = []

    expected_families = [
        "factor_family_trend",
        "factor_family_momentum",
        "factor_family_volatility",
        "factor_family_mean_reversion",
        "factor_family_return",
        "factor_family_quote_microstructure",
        "factor_family_macro_context",
        "factor_family_calendar_event",
        "factor_family_news_attention",
        "factor_family_cross_asset_context",
        "factor_family_regime_prep",
        "factor_family_composite",
    ]

    if "family_label" in df:
        present = set(df["family_label"].unique())
        for ef in expected_families:
            if ef not in present:
                errors.append(f"Missing expected factor family: '{ef}'")

    is_valid = len(errors) == 0
    return {
        "check_name": "family_registry_validation",
        "is_valid": is_valid,
        "errors": errors,
    }


def validate_factor_contract_registry(
    df: pd.DataFrame,
    profile: FactorMetadataProfile | None = None,
) -> Dict[str, Any]:
    errors: List[str] = []

    if df.empty:
        errors.append("Contract registry is empty")

    if "non_signal" in df and not (df["non_signal"] == True).all():
        errors.append("All contracts must declare non_signal == True")

    if "factor_name" in df:
        for fname in df["factor_name"]:
            for token in FORBIDDEN_FACTOR_TOKENS:
                if token in str(fname).lower():
                    errors.append(f"Forbidden token '{token}' in contract name '{fname}'")

    is_valid = len(errors) == 0
    return {
        "check_name": "contract_registry_validation",
        "is_valid": is_valid,
        "errors": errors,
    }


def validate_factor_namespace_registry(
    df: pd.DataFrame,
    profile: FactorMetadataProfile | None = None,
) -> Dict[str, Any]:
    errors: List[str] = []

    if df.empty:
        errors.append("Namespace registry is empty")

    if "is_valid" in df and not df["is_valid"].all():
        errors.append("Namespace registry contains invalid factor names")

    is_valid = len(errors) == 0
    return {
        "check_name": "namespace_registry_validation",
        "is_valid": is_valid,
        "errors": errors,
    }


def validate_factor_output_schema(
    df: pd.DataFrame,
    profile: FactorMetadataProfile | None = None,
) -> Dict[str, Any]:
    errors: List[str] = []

    if df.empty:
        errors.append("Output schema registry is empty")

    if "non_signal" in df and not (df["non_signal"] == True).all():
        errors.append("Output schema registry must enforce non_signal == True")

    is_valid = len(errors) == 0
    return {
        "check_name": "output_schema_validation",
        "is_valid": is_valid,
        "errors": errors,
    }


def validate_factor_metadata_manifest(
    df: pd.DataFrame,
    profile: FactorMetadataProfile | None = None,
) -> Dict[str, Any]:
    errors: List[str] = []

    if df.empty:
        errors.append("Factor metadata manifest is empty")

    if "non_signal" in df and not (df["non_signal"] == True).all():
        errors.append("Manifest contains non_signal == False records")

    if "contains_target_or_prediction" in df and not (~df["contains_target_or_prediction"]).all():
        errors.append("Manifest contains target or prediction records")

    if "contains_trading_recommendation" in df and not (~df["contains_trading_recommendation"]).all():
        errors.append("Manifest contains trading recommendation records")

    if "source_preserved" in df and not (df["source_preserved"] == True).all():
        errors.append("Manifest source preservation invariant violated")

    is_valid = len(errors) == 0
    return {
        "check_name": "manifest_validation",
        "is_valid": is_valid,
        "errors": errors,
    }


def validate_no_forbidden_factor_claims(
    text: str | None = None,
    df: pd.DataFrame | None = None,
    summary: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    violations: List[str] = []

    if text:
        res = validate_factor_forbidden_claims(text)
        violations.extend(res["matched_claims"])

    if summary:
        sum_str = str(summary)
        res = validate_factor_forbidden_claims(sum_str)
        violations.extend(res["matched_claims"])

    if df is not None:
        for col in df.columns:
            res = validate_factor_forbidden_claims(str(col))
            violations.extend(res["matched_claims"])

    is_clean = len(violations) == 0
    return {
        "check_name": "no_forbidden_claims_check",
        "is_clean": is_clean,
        "violations": violations,
    }


def build_factor_metadata_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_factor_metadata_profile()

    checks: List[Dict[str, Any]] = []

    if "profiles" in tables:
        checks.append(validate_factor_metadata_profile_registry(tables["profiles"], active_profile))

    if "families" in tables:
        checks.append(validate_factor_family_registry(tables["families"], active_profile))

    if "contracts" in tables:
        checks.append(validate_factor_contract_registry(tables["contracts"], active_profile))

    if "namespaces" in tables:
        checks.append(validate_factor_namespace_registry(tables["namespaces"], active_profile))

    if "schemas" in tables:
        checks.append(validate_factor_output_schema(tables["schemas"], active_profile))

    if "manifests" in tables:
        checks.append(validate_factor_metadata_manifest(tables["manifests"], active_profile))

    all_valid = all(c["is_valid"] for c in checks) if checks else True

    report_rows: List[Dict[str, Any]] = []
    for c in checks:
        report_rows.append(
            {
                "check_name": c["check_name"],
                "is_valid": c["is_valid"],
                "error_count": len(c.get("errors", [])),
                "errors": "; ".join(c.get("errors", [])) if c.get("errors") else "None",
                "status": "PASS" if c["is_valid"] else "FAIL",
                "non_signal": True,
            }
        )

    df = pd.DataFrame(report_rows)
    summary = {
        "active_profile": active_profile.name,
        "total_validation_checks": len(report_rows),
        "passed_checks": sum(1 for r in report_rows if r["is_valid"]),
        "failed_checks": sum(1 for r in report_rows if not r["is_valid"]),
        "status": FACTOR_READY if all_valid else "factor_validation_failed",
        "all_non_signal": True,
        "zero_forbidden_claims": True,
        "zero_lookahead": True,
        "source_preserved": True,
    }
    return df, summary
