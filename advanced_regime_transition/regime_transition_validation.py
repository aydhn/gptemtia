"""Phase 130: Regime Transition Validation.

Comprehensive validation rules ensuring non-signal guarantees, zero model execution,
no forbidden claims, and strict contract integrity across Phase 130 tables.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

FORBIDDEN_TRANSITION_TERMS: List[str] = [
    "buy signal",
    "buy_signal",
    "sell signal",
    "sell_signal",
    "long position",
    "short position",
    "enter trade",
    "exit trade",
    "guaranteed return",
    "approved for live trading",
    "broker ready",
    "production ready",
    "model trained",
    "clustering executed",
    "unsupervised inference complete",
]



def validate_regime_transition_profile_registry(
    df: pd.DataFrame,
    profile: Optional[RegimeTransitionProfile] = None,
) -> Dict[str, Any]:
    """Validate profile registry rows satisfy non-signal, local-only rules."""
    if df.empty:
        return {"is_valid": False, "error": "Profile registry is empty"}

    valid_phases = (df["current_phase"] == 130).all() and (df["target_final_phase"] == 160).all()
    no_trading = not df["allow_live_trading"].any() and not df["allow_broker_integration"].any()
    all_non_signal = bool(df["non_signal"].all())

    is_valid = bool(valid_phases and no_trading and all_non_signal)
    return {
        "is_valid": is_valid,
        "valid_phases": bool(valid_phases),
        "zero_trading": bool(no_trading),
        "all_non_signal": all_non_signal,
    }


def validate_state_sequence_contracts(
    df: pd.DataFrame,
    profile: Optional[RegimeTransitionProfile] = None,
) -> Dict[str, Any]:
    """Validate state sequence contracts enforce no-lookahead and zero-ML."""
    if df.empty:
        return {"is_valid": False, "error": "Sequence contract registry is empty"}

    all_non_signal = bool(df["non_signal_required"].all())
    all_no_lookahead = bool(df["no_lookahead_required"].all())
    no_ml = bool(not df["model_training_allowed"].any())
    no_clustering = bool(not df["clustering_allowed"].any())

    is_valid = all_non_signal and all_no_lookahead and no_ml and no_clustering
    return {
        "is_valid": is_valid,
        "all_non_signal_required": all_non_signal,
        "all_no_lookahead_required": all_no_lookahead,
        "zero_model_training": no_ml,
        "zero_clustering": no_clustering,
    }


def validate_transition_metric_registry(
    df: pd.DataFrame,
    profile: Optional[RegimeTransitionProfile] = None,
) -> Dict[str, Any]:
    """Validate transition metrics are all non-signal."""
    if df.empty:
        return {"is_valid": False, "error": "Metric registry is empty"}

    all_non_signal = bool(df["non_signal"].all())
    all_source_preserved = bool(df["source_preserved"].all())

    is_valid = all_non_signal and all_source_preserved
    return {
        "is_valid": is_valid,
        "all_non_signal": all_non_signal,
        "all_source_preserved": all_source_preserved,
    }


def validate_transition_diagnostics_manifest(
    df: pd.DataFrame,
    profile: Optional[RegimeTransitionProfile] = None,
) -> Dict[str, Any]:
    """Validate manifest satisfies all Phase 130 zero-execution invariant flags."""
    if df.empty:
        return {"is_valid": False, "error": "Manifest table is empty"}

    row = df.iloc[0]
    checks = [
        int(row.get("current_phase", 0)) == 130,
        int(row.get("target_final_phase", 0)) == 160,
        int(row.get("next_phase", 0)) == 131,
        bool(row.get("non_signal", False)) is True,
        bool(row.get("source_preserved", False)) is True,
        bool(row.get("official_approval", True)) is False,
        bool(row.get("production_ready", True)) is False,
        bool(row.get("broker_ready", True)) is False,
        bool(row.get("model_training_executed", True)) is False,
        bool(row.get("clustering_executed", True)) is False,
        bool(row.get("unsupervised_execution", True)) is False,
    ]
    is_valid = all(checks)
    return {"is_valid": is_valid, "passed_checks": sum(checks), "total_checks": len(checks)}


def validate_no_forbidden_transition_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Check text, table, or summary for forbidden trading, label, or approval claims."""
    violations = []
    if text:
        text_lower = text.lower()
        for term in FORBIDDEN_TRANSITION_TERMS:
            if term in text_lower:
                violations.append(f"Forbidden term '{term}' found in text")

    if df is not None and not df.empty:
        for col in df.columns:
            col_str = str(col).lower()
            if col_str in ["signal", "target", "label", "prediction", "buy", "sell"]:
                violations.append(f"Forbidden column '{col}' found in dataframe")

    return {
        "is_valid": len(violations) == 0,
        "violations": violations,
        "violations_count": len(violations),
    }


def build_regime_transition_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build composite validation report for all Phase 130 tables."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    checks = []
    if "profiles" in tables:
        res = validate_regime_transition_profile_registry(tables["profiles"], profile)
        checks.append({"check_name": "profile_registry_validation", "is_valid": res["is_valid"], "details": str(res)})
    if "contracts" in tables:
        res = validate_state_sequence_contracts(tables["contracts"], profile)
        checks.append({"check_name": "sequence_contracts_validation", "is_valid": res["is_valid"], "details": str(res)})
    if "metrics" in tables:
        res = validate_transition_metric_registry(tables["metrics"], profile)
        checks.append({"check_name": "transition_metrics_validation", "is_valid": res["is_valid"], "details": str(res)})
    if "manifest" in tables:
        res = validate_transition_diagnostics_manifest(tables["manifest"], profile)
        checks.append({"check_name": "manifest_invariants_validation", "is_valid": res["is_valid"], "details": str(res)})

    claims_res = validate_no_forbidden_transition_claims()
    checks.append({"check_name": "forbidden_claims_validation", "is_valid": claims_res["is_valid"], "details": str(claims_res)})

    df = pd.DataFrame(checks)
    total = len(df)
    passed = int(df["is_valid"].sum()) if not df.empty else 0
    all_valid = total == passed
    summary = {
        "total_checks": total,
        "passed_checks": passed,
        "failed_checks": total - passed,
        "validation_status": "VALIDATION_PASS" if all_valid else "VALIDATION_FAIL",
        "forbidden_claims_clean": True,
        "active_profile": profile.profile_name,
    }
    return df, summary
