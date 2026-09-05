"""Phase 131: Cross-Asset Regime Validation Engine.

Executes comprehensive contract validation and strict forbidden claims scans across
all Phase 131 Cross-Asset Regime Context Expansion tables and summaries.
"""

from typing import Any, Dict, List, Optional, Tuple
import re
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

FORBIDDEN_CLAIM_WORDS = [
    "official approval",
    "production ready",
    "broker ready",
    "buy signal",
    "sell signal",
    "long position",
    "short position",
    "target label",
    "model prediction",
    "investment advice",
    "arbitrage strategy",
    "pairs trading entry",
]


def validate_cross_asset_regime_profile_registry(
    df: pd.DataFrame, profile: Optional[CrossAssetRegimeProfile] = None
) -> Dict[str, Any]:
    """Validate profile registry compliance."""
    if df.empty:
        return {"check": "profile_registry", "status": "FAIL", "reason": "DataFrame is empty"}

    valid_phase = (df["current_phase"] == 131).all()
    valid_final = (df["target_final_phase"] == 160).all()
    valid_next = (df["next_phase"] == 132).all()
    valid_local = df["local_only"].all()
    valid_non_signal = df["non_signal"].all()

    passed = bool(valid_phase and valid_final and valid_next and valid_local and valid_non_signal)
    return {
        "check": "profile_registry_integrity",
        "status": "PASS" if passed else "FAIL",
        "passed": passed,
    }


def validate_cross_asset_entity_pair_registry(
    df: pd.DataFrame, profile: Optional[CrossAssetRegimeProfile] = None
) -> Dict[str, Any]:
    """Validate entity pair registry compliance."""
    if df.empty:
        return {"check": "entity_pair_registry", "status": "FAIL", "reason": "DataFrame is empty"}

    valid_non_signal = bool(df["non_signal"].all())
    valid_source = bool(df["source_preserved"].all())
    passed = valid_non_signal and valid_source
    return {
        "check": "entity_pair_registry_integrity",
        "status": "PASS" if passed else "FAIL",
        "passed": passed,
    }


def validate_cross_asset_context_contracts(
    df: pd.DataFrame, profile: Optional[CrossAssetRegimeProfile] = None
) -> Dict[str, Any]:
    """Validate cross-asset context contracts compliance."""
    if df.empty:
        return {"check": "context_contracts", "status": "FAIL", "reason": "DataFrame is empty"}

    valid_lookahead = bool(df["no_lookahead_required"].all())
    valid_signal = bool(df["non_signal_required"].all())
    valid_news = bool(df["metadata_only_news_required"].all())
    passed = valid_lookahead and valid_signal and valid_news
    return {
        "check": "context_contracts_integrity",
        "status": "PASS" if passed else "FAIL",
        "passed": passed,
    }


def validate_cross_asset_regime_context_manifest(
    df: pd.DataFrame, profile: Optional[CrossAssetRegimeProfile] = None
) -> Dict[str, Any]:
    """Validate master manifest compliance."""
    if df.empty:
        return {"check": "context_manifest", "status": "FAIL", "reason": "DataFrame is empty"}

    row = df.iloc[0].to_dict()
    valid_status = row.get("manifest_status") == "MANIFEST_VALID"
    valid_non_signal = bool(row.get("non_signal", False))
    valid_phase = row.get("current_phase") == 131
    zero_training = not bool(row.get("model_training_executed", True))
    zero_clustering = not bool(row.get("clustering_executed", True))
    zero_destructive = not bool(row.get("destructive_action_allowed", True))

    passed = (
        valid_status
        and valid_non_signal
        and valid_phase
        and zero_training
        and zero_clustering
        and zero_destructive
    )
    return {
        "check": "manifest_integrity",
        "status": "PASS" if passed else "FAIL",
        "passed": passed,
    }


def validate_no_forbidden_cross_asset_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Scan text, table content, or summary dictionary for forbidden commercial or execution claims.
    
    Respects negation patterns like 'official approval: False' or 'zero trading signals'.
    """
    violations: List[str] = []

    content_str = ""
    if text:
        content_str += " " + text
    if summary:
        content_str += " " + str(summary)
    if df is not None and not df.empty:
        content_str += " " + df.to_string()

    content_lower = content_str.lower().replace("-", " ")

    for forbidden in FORBIDDEN_CLAIM_WORDS:
        # Scan occurrences
        matches = list(re.finditer(rf"\b{re.escape(forbidden)}\b", content_lower))
        for m in matches:
            # Check context within 40 characters before and after
            start = max(0, m.start() - 40)
            end = min(len(content_lower), m.end() + 40)
            window = content_lower[start:end]

            # Allowed negation tokens indicating explicit compliance
            negation_tokens = [
                "false", "0", "zero", "not", "no ", "without", "prohibited", "forbidden", "disclaimer",
                "non-signal", "never", "cannot", "assert", "neither", "değildir", "yasak"
            ]
            is_negated = any(tok in window for tok in negation_tokens)
            if not is_negated:
                violations.append(f"Forbidden claim detected without negation: '{forbidden}' in '{window.strip()}'")

    return {
        "clean": len(violations) == 0,
        "violations": violations,
        "violation_count": len(violations),
        "status": "PASS" if len(violations) == 0 else "FAIL",
    }


def build_cross_asset_regime_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build composite validation report across all supplied Phase 131 tables."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    checks: List[Dict[str, Any]] = []

    if "profiles" in tables:
        checks.append(validate_cross_asset_regime_profile_registry(tables["profiles"], profile))
    if "pairs" in tables:
        checks.append(validate_cross_asset_entity_pair_registry(tables["pairs"], profile))
    if "contracts" in tables:
        checks.append(validate_cross_asset_context_contracts(tables["contracts"], profile))
    if "manifest" in tables:
        checks.append(validate_cross_asset_regime_context_manifest(tables["manifest"], profile))

    # General claims validation across all tables
    all_clean = True
    for tbl_name, df_tbl in tables.items():
        res = validate_no_forbidden_cross_asset_claims(df=df_tbl)
        if not res["clean"]:
            all_clean = False
            checks.append({"check": f"forbidden_claims_{tbl_name}", "status": "FAIL", "passed": False})
        else:
            checks.append({"check": f"forbidden_claims_{tbl_name}", "status": "PASS", "passed": True})

    df_out = pd.DataFrame(checks)
    total = len(df_out)
    passed_count = int(df_out["passed"].sum()) if not df_out.empty else 0
    all_passed = total == passed_count and all_clean

    summary = {
        "total_checks": total,
        "passed_checks": passed_count,
        "failed_checks": total - passed_count,
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "forbidden_claims_clean": all_clean,
        "all_passed": all_passed,
        "active_profile": profile.profile_name,
    }
    return df_out, summary
