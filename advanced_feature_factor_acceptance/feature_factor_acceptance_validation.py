"""Phase 125: Feature Factor Acceptance Validation Report.

Validates profile registries, block inventories, acceptance gates, manifests,
and ensures strict prevention of forbidden trading claims, signals, or production endorsements.
"""

import re
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)

FORBIDDEN_CLAIM_PATTERNS: List[str] = [
    r"\bbuy\s+signal\b",
    r"\bsell\s+signal\b",
    r"\bal-sat\s+sinyali\b",
    r"\bkesin\s+al\b",
    r"\bkesin\s+sat\b",
    r"\byatırım\s+tavsiyesi\b",
    r"\binvestment\s+advice\b",
    r"\btrading\s+signal\b",
    r"\bofficial\s+approval\b",
    r"\bproduction\s+ready\b",
    r"\bbroker\s+ready\b",
    r"\btarget\s+price\b",
    r"\bguaranteed\s+profit\b",
]


def validate_no_forbidden_acceptance_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Scan text, DataFrames, and summary dicts for forbidden trading and approval claims."""
    violations = []
    combined_texts = []

    if text:
        combined_texts.append(text)
    if summary:
        for k, v in summary.items():
            combined_texts.append(f"{k}: {v}")
    if df is not None and not df.empty:
        for col in df.columns:
            combined_texts.extend(df[col].astype(str).tolist())

    full_corpus = " ".join(combined_texts).lower()
    for pattern in FORBIDDEN_CLAIM_PATTERNS:
        matches = re.findall(pattern, full_corpus, re.IGNORECASE)
        if matches:
            violations.append(pattern)

    return {
        "valid": len(violations) == 0,
        "violations_found": len(violations),
        "violations": violations,
    }


def validate_feature_factor_acceptance_profile_registry(
    df: pd.DataFrame, profile: Optional[FeatureFactorAcceptanceProfile] = None
) -> Dict[str, Any]:
    """Validate acceptance profile DataFrame."""
    if df.empty:
        return {"valid": False, "reason": "Empty profile DataFrame"}
    required_cols = ["profile_name", "current_phase", "target_final_phase", "next_phase", "non_signal"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        return {"valid": False, "reason": f"Missing columns: {missing}"}
    if not (df["current_phase"] == 125).all():
        return {"valid": False, "reason": "current_phase must be 125"}
    if not (df["target_final_phase"] == 160).all():
        return {"valid": False, "reason": "target_final_phase must be 160"}
    if not (df["next_phase"] == 126).all():
        return {"valid": False, "reason": "next_phase must be 126"}
    if not df["non_signal"].all():
        return {"valid": False, "reason": "non_signal must be True"}
    return {"valid": True, "reason": "Profile registry valid"}


def validate_feature_engine_block_inventory(
    df: pd.DataFrame, profile: Optional[FeatureFactorAcceptanceProfile] = None
) -> Dict[str, Any]:
    """Validate block inventory DataFrame."""
    if df.empty:
        return {"valid": False, "reason": "Empty inventory DataFrame"}
    if len(df) != 10:
        return {"valid": False, "reason": f"Expected exactly 10 modules in block, got {len(df)}"}
    if not df["non_signal"].all():
        return {"valid": False, "reason": "All modules must be non_signal"}
    if not df["source_preserved"].all():
        return {"valid": False, "reason": "All modules must preserve source"}
    return {"valid": True, "reason": "Inventory valid"}


def validate_feature_engine_block_acceptance_gates(
    df: pd.DataFrame, profile: Optional[FeatureFactorAcceptanceProfile] = None
) -> Dict[str, Any]:
    """Validate acceptance gates DataFrame."""
    if df.empty:
        return {"valid": False, "reason": "Empty gates DataFrame"}
    if len(df) < 16:
        return {"valid": False, "reason": f"Expected at least 16 gates, got {len(df)}"}
    if not df["passed"].all():
        return {"valid": False, "reason": "Not all acceptance gates passed"}
    return {"valid": True, "reason": "Acceptance gates valid"}


def validate_phase_116_125_acceptance_manifest(
    df: pd.DataFrame, profile: Optional[FeatureFactorAcceptanceProfile] = None
) -> Dict[str, Any]:
    """Validate the Phase 116-125 acceptance manifest DataFrame."""
    if df.empty:
        return {"valid": False, "reason": "Empty manifest DataFrame"}
    row = df.iloc[0]
    if row.get("phase_start") != 116 or row.get("phase_end") != 125:
        return {"valid": False, "reason": "Invalid phase range in manifest"}
    if row.get("target_final_phase") != 160:
        return {"valid": False, "reason": "target_final_phase must be 160"}
    if row.get("next_phase") != 126:
        return {"valid": False, "reason": "next_phase must be 126"}
    if not row.get("non_signal", False):
        return {"valid": False, "reason": "Manifest must enforce non_signal=True"}
    if row.get("official_approval", True):
        return {"valid": False, "reason": "Manifest must enforce official_approval=False"}
    if row.get("production_ready", True):
        return {"valid": False, "reason": "Manifest must enforce production_ready=False"}
    if row.get("broker_ready", True):
        return {"valid": False, "reason": "Manifest must enforce broker_ready=False"}
    if not row.get("source_preserved", False):
        return {"valid": False, "reason": "Manifest must enforce source_preserved=True"}
    return {"valid": True, "reason": "Acceptance manifest valid"}


def build_feature_factor_acceptance_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute comprehensive validation across all acceptance tables."""
    active_profile = profile or get_default_feature_factor_acceptance_profile()
    checks = []

    if "profiles" in tables:
        v = validate_feature_factor_acceptance_profile_registry(tables["profiles"], active_profile)
        checks.append({"check": "profile_registry_validation", "passed": v["valid"], "reason": v["reason"]})

    if "inventory" in tables:
        v = validate_feature_engine_block_inventory(tables["inventory"], active_profile)
        checks.append({"check": "block_inventory_validation", "passed": v["valid"], "reason": v["reason"]})

    if "gates" in tables:
        v = validate_feature_engine_block_acceptance_gates(tables["gates"], active_profile)
        checks.append({"check": "acceptance_gates_validation", "passed": v["valid"], "reason": v["reason"]})

    if "manifest" in tables:
        v = validate_phase_116_125_acceptance_manifest(tables["manifest"], active_profile)
        checks.append({"check": "acceptance_manifest_validation", "passed": v["valid"], "reason": v["reason"]})

    claim_check = validate_no_forbidden_acceptance_claims()
    checks.append({"check": "forbidden_claims_validation", "passed": claim_check["valid"], "reason": "No claims detected"})

    df = pd.DataFrame(checks)
    all_pass = bool(df["passed"].all()) if not df.empty else True
    summary = {
        "validation_status": "VALIDATION_PASS" if all_pass else "VALIDATION_FAIL",
        "total_rules": len(df),
        "passed_rules": int(df["passed"].sum()) if not df.empty else 0,
        "forbidden_claims_detected": claim_check["violations_found"],
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary
