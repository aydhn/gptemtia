"""Phase 134: Regime FeatureStore Non-Signal Policies.

Enforces strict textual and semantic boundaries prohibiting trade recommendations,
directional predictions, or readiness claims in FeatureStore metadata and reports.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    NON_SIGNAL_POLICY_DOMAIN,
    REGIME_STORE_READY,
)

FORBIDDEN_CLAIMS: List[Dict[str, Any]] = [
    {"claim_pattern": "kesin al", "category": "trade_signal", "risk_level": "CRITICAL"},
    {"claim_pattern": "kesin sat", "category": "trade_signal", "risk_level": "CRITICAL"},
    {"claim_pattern": "buy signal", "category": "trade_signal", "risk_level": "CRITICAL"},
    {"claim_pattern": "sell signal", "category": "trade_signal", "risk_level": "CRITICAL"},
    {"claim_pattern": "long aç", "category": "trade_signal", "risk_level": "CRITICAL"},
    {"claim_pattern": "short aç", "category": "trade_signal", "risk_level": "CRITICAL"},
    {"claim_pattern": "pozisyon aç", "category": "trade_signal", "risk_level": "CRITICAL"},
    {"claim_pattern": "trade signal", "category": "trade_signal", "risk_level": "CRITICAL"},
    {"claim_pattern": "yatırım tavsiyesi", "category": "advisory", "risk_level": "CRITICAL"},
    {"claim_pattern": "model prediction", "category": "prediction", "risk_level": "HIGH"},
    {"claim_pattern": "production ready", "category": "production_claim", "risk_level": "HIGH"},
    {"claim_pattern": "broker ready", "category": "broker_claim", "risk_level": "HIGH"},
    {"claim_pattern": "official approval", "category": "approval_claim", "risk_level": "HIGH"},
    {"claim_pattern": "live ready", "category": "live_claim", "risk_level": "HIGH"},
]


def build_regime_featurestore_non_signal_policy_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for non-signal policies."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(FORBIDDEN_CLAIMS)
    summary = {
        "domain": NON_SIGNAL_POLICY_DOMAIN,
        "total_forbidden_claims": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def validate_regime_featurestore_non_signal_text(text: str) -> Dict[str, Any]:
    """Inspect text for prohibited trade signal, advisory, or deployment claims."""
    clean_text = text.lower()
    found_violations = [
        c["claim_pattern"] for c in FORBIDDEN_CLAIMS if c["claim_pattern"].lower() in clean_text
    ]

    return {
        "is_valid": len(found_violations) == 0,
        "found_violations": found_violations,
        "non_signal": len(found_violations) == 0,
    }


def summarize_regime_featurestore_non_signal_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize non-signal policy registry DataFrame."""
    return {
        "total_forbidden_patterns": len(df),
        "categories": df["category"].unique().tolist() if not df.empty else [],
        "all_strictly_forbidden": True,
    }
