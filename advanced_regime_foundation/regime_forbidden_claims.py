"""Phase 126: Regime Forbidden Claims Registry.

Registers and validates forbidden claims, guarantees, and marketing assertions.
"""

import re
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

FORBIDDEN_CLAIMS: List[Dict[str, Any]] = [
    {"claim_id": "fc_01", "claim_text": "kesin al", "severity": "CRITICAL", "category": "trade_instruction"},
    {"claim_id": "fc_02", "claim_text": "kesin sat", "severity": "CRITICAL", "category": "trade_instruction"},
    {"claim_id": "fc_03", "claim_text": "buy signal", "severity": "CRITICAL", "category": "signal_claim"},
    {"claim_id": "fc_04", "claim_text": "sell signal", "severity": "CRITICAL", "category": "signal_claim"},
    {"claim_id": "fc_05", "claim_text": "long aç", "severity": "CRITICAL", "category": "trade_instruction"},
    {"claim_id": "fc_06", "claim_text": "short aç", "severity": "CRITICAL", "category": "trade_instruction"},
    {"claim_id": "fc_07", "claim_text": "position aç", "severity": "CRITICAL", "category": "trade_instruction"},
    {"claim_id": "fc_08", "claim_text": "trade signal", "severity": "CRITICAL", "category": "signal_claim"},
    {"claim_id": "fc_09", "claim_text": "yatırım tavsiyesi", "severity": "CRITICAL", "category": "regulatory_violation"},
    {"claim_id": "fc_10", "claim_text": "model prediction", "severity": "HIGH", "category": "unsupported_claim"},
    {"claim_id": "fc_11", "claim_text": "production ready", "severity": "HIGH", "category": "premature_deployment"},
    {"claim_id": "fc_12", "claim_text": "broker ready", "severity": "HIGH", "category": "premature_deployment"},
    {"claim_id": "fc_13", "claim_text": "official approval", "severity": "HIGH", "category": "unauthorized_endorsement"},
]


def build_regime_forbidden_claim_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for forbidden claim registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(FORBIDDEN_CLAIMS)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_forbidden_claims": len(df),
        "critical_claims": len(df[df["severity"] == "CRITICAL"]),
        "high_claims": len(df[df["severity"] == "HIGH"]),
        "all_blocked": True,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def validate_regime_forbidden_claims(text: Optional[str] = None) -> Dict[str, Any]:
    """Inspect text string to verify absence of all forbidden claims."""
    if not text:
        return {"is_valid": True, "violations_count": 0, "violations": []}

    violations = []
    text_lower = text.lower()
    for claim in FORBIDDEN_CLAIMS:
        c_text = claim["claim_text"]
        # Match as phrase with word boundaries or space flexibility
        pattern = r"\b" + re.escape(c_text).replace(r"\ ", r"\s+") + r"\b"
        if re.search(pattern, text_lower):
            violations.append(claim)

    return {
        "is_valid": len(violations) == 0,
        "violations_count": len(violations),
        "violations": violations,
        "non_signal": True,
    }


def summarize_regime_forbidden_claims(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize forbidden claim registry DataFrame."""
    return {
        "total_claims": len(df),
        "claim_texts": list(df["claim_text"].unique()) if "claim_text" in df.columns else [],
        "all_blocked": True,
        "non_signal": True,
    }
