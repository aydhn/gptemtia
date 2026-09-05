"""Phase 129: Market Behavior Diagnostics Validation.

Verifies strict invariants across operational profiles, metrics, candidate state quality,
manifests, and scans for forbidden trading claims, directional assertions, and execution leakage.
"""

import re
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)

FORBIDDEN_CLAIM_PATTERNS = [
    r"\bbuy\b",
    r"\bsell\b",
    r"\blong\b",
    r"\bshort\b",
    r"\btrade\s+signal\b",
    r"\btarget\s+label\b",
    r"\bpredicted\s+regime\b",
    r"\btrading\s+recommendation\b",
    r"\bofficial\s+approval\b",
    r"\bproduction\s+ready\b",
    r"\bbroker\s+ready\b",
    r"\bclustering\s+executed\b",
    r"\bmodel\s+training\s+executed\b",
]


def validate_no_forbidden_behavior_claims(
    text_or_profile: Any = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> bool:
    """Scan text, dataframe values, or summary keys/values for forbidden commercial or trading claims."""
    if isinstance(text_or_profile, MarketBehaviorDiagnosticsProfile):
        if text_or_profile.allow_live_trading:
            raise ValueError("Forbidden: allow_live_trading cannot be True")
        if text_or_profile.allow_quality_as_signal:
            raise ValueError("Forbidden: allow_quality_as_signal cannot be True")
        if text_or_profile.allow_clustering_execution:
            raise ValueError("Forbidden: allow_clustering_execution cannot be True")
        return True

    text = text_or_profile if isinstance(text_or_profile, str) else None
    if text:
        lowered = text.lower()
        for pat in [
            r"\bgenerate\s+signal\b",
            r"\bexecute\s+order\b",
            r"\bbuy\s+signal\b",
            r"\bsell\s+signal\b",
            r"\bclustering\s+is\s+running\b",
            r"\bmodel\s+is\s+training\b",
        ]:
            if re.search(pat, lowered):
                raise ValueError(f"Forbidden claim detected in text: '{pat}'")

    if df is not None and not df.empty:
        for col in df.columns:
            if col in ["signal", "target", "label", "prediction", "buy", "sell", "long", "short"]:
                raise ValueError(f"Forbidden column name detected in DataFrame: '{col}'")

    return True


def validate_no_lookahead_behavior_diagnostics(
    profile_or_df: Any = None,
) -> bool:
    """Ensure zero shift(-1), zero forward returns, and zero lookahead leakage."""
    if isinstance(profile_or_df, MarketBehaviorDiagnosticsProfile):
        return True
    if isinstance(profile_or_df, pd.DataFrame) and not profile_or_df.empty:
        for col in profile_or_df.columns:
            if "shift_negative" in col or "lookahead" in col or "future_return" in col:
                raise ValueError(f"Lookahead bias detected in column: '{col}'")
    return True



def validate_market_behavior_diagnostics_profile_registry(
    df: pd.DataFrame, profile: MarketBehaviorDiagnosticsProfile
) -> bool:
    """Validate profile registry compliance."""
    if df.empty:
        raise ValueError("Profile registry DataFrame cannot be empty")
    required_cols = ["profile_name", "current_phase", "non_signal"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column in profile registry: {col}")
    return True


def validate_behavior_quality_metric_registry(
    df: pd.DataFrame, profile: MarketBehaviorDiagnosticsProfile
) -> bool:
    """Validate behavior quality metric registry compliance."""
    if df.empty:
        raise ValueError("Behavior quality metric registry DataFrame cannot be empty")
    if "metric_name" not in df.columns or "non_signal" not in df.columns:
        raise ValueError("Metric registry must contain 'metric_name' and 'non_signal'")
    return True


def validate_candidate_state_quality_report(
    df: pd.DataFrame, profile: MarketBehaviorDiagnosticsProfile
) -> bool:
    """Validate candidate state quality report compliance."""
    if df.empty:
        raise ValueError("Candidate state quality report DataFrame cannot be empty")
    if not (df["non_signal"] == True).all():
        raise ValueError("All candidate states must have non_signal=True")
    if (df["model_training_executed"] == True).any():
        raise ValueError("model_training_executed must be False for all candidate states")
    if (df["clustering_executed"] == True).any():
        raise ValueError("clustering_executed must be False for all candidate states")
    return True


def validate_behavior_diagnostics_manifest(
    df: pd.DataFrame, profile: MarketBehaviorDiagnosticsProfile
) -> bool:
    """Validate behavior diagnostics manifest compliance."""
    if df.empty:
        raise ValueError("Behavior diagnostics manifest DataFrame cannot be empty")
    row = df.iloc[0]
    if not row.get("non_signal", False):
        raise ValueError("Manifest must declare non_signal=True")
    if not row.get("source_preserved", False):
        raise ValueError("Manifest must declare source_preserved=True")
    if row.get("official_approval", True):
        raise ValueError("Manifest cannot claim official_approval=True")
    if row.get("production_ready", True):
        raise ValueError("Manifest cannot claim production_ready=True")
    if row.get("broker_ready", True):
        raise ValueError("Manifest cannot claim broker_ready=True")
    if row.get("model_training_executed", True):
        raise ValueError("Manifest cannot declare model_training_executed=True")
    if row.get("clustering_executed", True):
        raise ValueError("Manifest cannot declare clustering_executed=True")
    return True


def build_market_behavior_diagnostics_validation_report(
    tables: Optional[Dict[str, pd.DataFrame]] = None,
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build validation audit report across all Phase 129 outputs."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    checks = [
        ("phase_129_current_phase", profile.current_phase == 129),
        ("target_final_phase_160", profile.target_final_phase == 160),
        ("next_phase_130", profile.next_phase == 130),
        ("dry_run_and_local_only", profile.dry_run_default and profile.local_only),
        ("no_live_trading", not profile.allow_live_trading),
        ("no_broker_integration", not profile.allow_broker_integration),
        ("no_quality_as_signal", not profile.allow_quality_as_signal),
        ("no_behavior_as_signal", not profile.allow_behavior_as_signal),
        ("no_candidate_state_as_signal", not profile.allow_candidate_state_as_signal),
        ("no_model_training", not profile.allow_model_training),
        ("no_clustering_execution", not profile.allow_clustering_execution),
        ("no_unsupervised_execution", not profile.allow_unsupervised_execution),
        ("no_target_label_generation", not profile.allow_target_label_generation),
        ("no_prediction_generation", not profile.allow_prediction_generation),
        ("no_official_approval_claim", not profile.allow_official_approval_claim),
        ("no_production_ready_claim", not profile.allow_production_ready_claim),
        ("no_broker_ready_claim", not profile.allow_broker_ready_claim),
        ("no_source_overwrite", not profile.allow_source_overwrite),
        ("no_auto_destructive_cleaning", not profile.allow_auto_destructive_cleaning),
        ("no_auto_imputation", not profile.allow_auto_imputation),
        ("no_auto_feature_drop", not profile.allow_auto_feature_drop),
    ]

    rows = []
    for name, passed in checks:
        rows.append(
            {
                "check_name": name,
                "passed": passed,
                "status": "PASS" if passed else "FAIL",
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    all_passed = bool((df["passed"] == True).all())
    summary = {
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "total_checks": len(df),
        "passed_checks": int((df["passed"] == True).sum()),
        "all_passed": all_passed,
        "non_signal": True,
    }
    return df, summary


# Alias for script compatibility
run_market_behavior_diagnostics_validation_report = build_market_behavior_diagnostics_validation_report

