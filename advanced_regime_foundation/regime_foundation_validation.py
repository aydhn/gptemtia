"""Phase 126: Regime Foundation Validation.

Performs rigorous rule-based validation across all Phase 126 registries, taxonomies, and manifests.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.regime_forbidden_claims import validate_regime_forbidden_claims


def validate_regime_foundation_profile_registry(
    df: pd.DataFrame,
    profile: Optional[RegimeFoundationProfile] = None,
) -> Dict[str, Any]:
    """Validate profile registry DataFrame."""
    issues = []
    if df.empty:
        issues.append("Profile registry is empty")

    for _, row in df.iterrows():
        if row.get("current_phase") != 126:
            issues.append(f"Profile {row.get('profile_name')} has invalid current_phase: {row.get('current_phase')}")
        if row.get("target_final_phase") != 160:
            issues.append(f"Profile {row.get('profile_name')} has invalid target_final_phase: {row.get('target_final_phase')}")
        if row.get("next_phase") != 127:
            issues.append(f"Profile {row.get('profile_name')} has invalid next_phase: {row.get('next_phase')}")
        if not row.get("non_signal", False):
            issues.append(f"Profile {row.get('profile_name')} must have non_signal=True")
        if row.get("allow_model_training", False):
            issues.append(f"Profile {row.get('profile_name')} must not allow model training")
        if row.get("allow_clustering_execution", False):
            issues.append(f"Profile {row.get('profile_name')} must not allow clustering execution")
        if row.get("allow_live_trading", False) or row.get("allow_broker_integration", False):
            issues.append(f"Profile {row.get('profile_name')} must not allow live trading or broker integration")

    return {"is_valid": len(issues) == 0, "issues": issues, "non_signal": True}


def validate_market_behavior_taxonomy(
    df: pd.DataFrame,
    profile: Optional[RegimeFoundationProfile] = None,
) -> Dict[str, Any]:
    """Validate market behavior taxonomy DataFrame."""
    issues = []
    if df.empty:
        issues.append("Market behavior taxonomy is empty")

    expected_behaviors = [
        "trending_behavior",
        "ranging_behavior",
        "high_volatility_behavior",
        "low_volatility_behavior",
        "volatility_expansion_behavior",
        "volatility_compression_behavior",
        "event_sensitive_behavior",
        "macro_sensitive_behavior",
        "cross_asset_sensitive_behavior",
        "liquidity_sensitive_placeholder",
        "transition_behavior_placeholder",
        "uncertain_behavior_placeholder",
    ]
    present_behaviors = list(df["behavior_name"]) if "behavior_name" in df.columns else []
    for b in expected_behaviors:
        if b not in present_behaviors:
            issues.append(f"Missing expected market behavior: {b}")

    if not bool((df["non_signal"] == True).all()):
        issues.append("All market behaviors must be flagged non_signal=True")

    return {"is_valid": len(issues) == 0, "issues": issues, "non_signal": True}


def validate_regime_state_taxonomy(
    df: pd.DataFrame,
    profile: Optional[RegimeFoundationProfile] = None,
) -> Dict[str, Any]:
    """Validate regime state taxonomy DataFrame."""
    issues = []
    if df.empty:
        issues.append("Regime state taxonomy is empty")

    for _, row in df.iterrows():
        name = row.get("regime_state_name", "")
        if not name.startswith("regime_state_"):
            issues.append(f"Regime state name missing required prefix: {name}")
        if row.get("contains_target_or_prediction", True):
            issues.append(f"Regime state {name} contains target or prediction")
        if row.get("contains_trading_recommendation", True):
            issues.append(f"Regime state {name} contains trading recommendation")
        if not row.get("non_signal", False):
            issues.append(f"Regime state {name} must be non-signal")

    return {"is_valid": len(issues) == 0, "issues": issues, "non_signal": True}


def validate_regime_family_registry(
    df: pd.DataFrame,
    profile: Optional[RegimeFoundationProfile] = None,
) -> Dict[str, Any]:
    """Validate regime family registry DataFrame."""
    issues = []
    if df.empty:
        issues.append("Regime family registry is empty")

    expected_families = [
        "regime_family_volatility",
        "regime_family_trend",
        "regime_family_range",
        "regime_family_liquidity_placeholder",
        "regime_family_macro_context",
        "regime_family_event_context",
        "regime_family_news_metadata_context",
        "regime_family_cross_asset_context",
    ]
    present_families = list(df["family_name"]) if "family_name" in df.columns else []
    for f in expected_families:
        if f not in present_families:
            issues.append(f"Missing expected regime family: {f}")

    if any(df.get("model_training_executed", [False])):
        issues.append("Model training must NOT have been executed")
    if any(df.get("clustering_executed", [False])):
        issues.append("Clustering execution must NOT have been executed")

    return {"is_valid": len(issues) == 0, "issues": issues, "non_signal": True}


def validate_regime_foundation_manifest(
    df: pd.DataFrame,
    profile: Optional[RegimeFoundationProfile] = None,
) -> Dict[str, Any]:
    """Validate regime foundation manifest DataFrame."""
    issues = []
    if df.empty:
        return {"is_valid": False, "issues": ["Manifest is empty"], "non_signal": True}

    row = df.iloc[0].to_dict()
    if row.get("current_phase") != 126:
        issues.append(f"Manifest current_phase must be 126, got {row.get('current_phase')}")
    if row.get("target_final_phase") != 160:
        issues.append(f"Manifest target_final_phase must be 160, got {row.get('target_final_phase')}")
    if row.get("next_phase") != 127:
        issues.append(f"Manifest next_phase must be 127, got {row.get('next_phase')}")
    if not row.get("non_signal", False):
        issues.append("Manifest non_signal must be True")
    if not row.get("source_preserved", False):
        issues.append("Manifest source_preserved must be True")
    if row.get("official_approval", True):
        issues.append("Manifest official_approval must be False")
    if row.get("production_ready", True):
        issues.append("Manifest production_ready must be False")
    if row.get("broker_ready", True):
        issues.append("Manifest broker_ready must be False")
    if row.get("model_training_executed", True):
        issues.append("Manifest model_training_executed must be False")
    if row.get("clustering_executed", True):
        issues.append("Manifest clustering_executed must be False")

    return {"is_valid": len(issues) == 0, "issues": issues, "non_signal": True}


def validate_no_forbidden_regime_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Validate that text or DataFrame strings do not contain forbidden commercial/trade claims."""
    violations = []
    if text:
        res = validate_regime_forbidden_claims(text)
        if not res["is_valid"]:
            violations.extend(res["violations"])

    if df is not None:
        for col in df.columns:
            for val in df[col].astype(str):
                res = validate_regime_forbidden_claims(val)
                if not res["is_valid"]:
                    violations.extend(res["violations"])

    return {
        "is_valid": len(violations) == 0,
        "violations_count": len(violations),
        "violations": violations,
        "non_signal": True,
    }


def build_regime_foundation_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build unified validation report DataFrame and summary across all Phase 126 artifacts."""
    active_profile = profile or get_default_regime_foundation_profile()

    checks = []

    # Check 1: Profile Registry
    if "profiles" in tables:
        v_prof = validate_regime_foundation_profile_registry(tables["profiles"], active_profile)
        checks.append({"rule_name": "profile_registry_validation", "status": "PASS" if v_prof["is_valid"] else "FAIL", "issues": str(v_prof["issues"])})

    # Check 2: Market Behavior Taxonomy
    if "market_behavior" in tables:
        v_beh = validate_market_behavior_taxonomy(tables["market_behavior"], active_profile)
        checks.append({"rule_name": "market_behavior_taxonomy_validation", "status": "PASS" if v_beh["is_valid"] else "FAIL", "issues": str(v_beh["issues"])})

    # Check 3: Regime State Taxonomy
    if "regime_states" in tables:
        v_state = validate_regime_state_taxonomy(tables["regime_states"], active_profile)
        checks.append({"rule_name": "regime_state_taxonomy_validation", "status": "PASS" if v_state["is_valid"] else "FAIL", "issues": str(v_state["issues"])})

    # Check 4: Regime Family Registry
    if "regime_families" in tables:
        v_fam = validate_regime_family_registry(tables["regime_families"], active_profile)
        checks.append({"rule_name": "regime_family_registry_validation", "status": "PASS" if v_fam["is_valid"] else "FAIL", "issues": str(v_fam["issues"])})

    # Check 5: Manifest Validation
    if "manifest" in tables:
        v_man = validate_regime_foundation_manifest(tables["manifest"], active_profile)
        checks.append({"rule_name": "manifest_validation", "status": "PASS" if v_man["is_valid"] else "FAIL", "issues": str(v_man["issues"])})

    # Check 6: Forbidden Claims Validation
    forbidden_clean = True
    for name, t_df in tables.items():
        if name in ("forbidden_claims", "forbidden_claims_registry"):
            continue
        v_claim = validate_no_forbidden_regime_claims(df=t_df)
        if not v_claim["is_valid"]:
            forbidden_clean = False
            checks.append({"rule_name": f"forbidden_claims_{name}", "status": "FAIL", "issues": str(v_claim["violations"])})

    if forbidden_clean:
        checks.append({"rule_name": "forbidden_claims_overall", "status": "PASS", "issues": "[]"})

    df = pd.DataFrame(checks)
    passed_rules = len(df[df["status"] == "PASS"])
    total_rules = len(df)

    summary = {
        "active_profile": active_profile.profile_name,
        "total_rules": total_rules,
        "passed_rules": passed_rules,
        "validation_status": "VALIDATION_PASS" if passed_rules == total_rules else "VALIDATION_FAIL",
        "forbidden_claims_clean": forbidden_clean,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary
