"""Phase 122 Factor Forbidden Claims Registry.

Maintains an exhaustive dictionary of prohibited phrases and validates that
no reports, manifests, or factor descriptions produce disallowed claims.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY

FORBIDDEN_CLAIM_PATTERNS: List[str] = [
    "kesin al",
    "kesin sat",
    "buy signal",
    "sell signal",
    "long aç",
    "short aç",
    "position aç",
    "trade signal",
    "yatırım tavsiyesi",
    "model prediction",
    "target label",
    "production ready",
    "broker ready",
    "official approval",
]


def build_factor_forbidden_claim_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Forbidden Claim Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records: List[Dict[str, Any]] = []
    for pattern in FORBIDDEN_CLAIM_PATTERNS:
        records.append(
            {
                "claim_pattern": pattern,
                "category": "trading_or_deployment_claim",
                "severity": "CRITICAL",
                "enforcement": "STRICT_PROHIBITION",
                "non_signal": True,
                "status_label": FACTOR_READY,
            }
        )

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_forbidden_claims": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary


def validate_factor_forbidden_claims(text: str) -> Dict[str, Any]:
    """Audit text against forbidden claims list."""
    matched_claims: List[str] = []
    text_lower = text.lower()

    for pattern in FORBIDDEN_CLAIM_PATTERNS:
        if pattern in text_lower:
            matched_claims.append(pattern)

    is_clean = len(matched_claims) == 0
    return {
        "is_clean": is_clean,
        "matched_claims": matched_claims,
        "violations_count": len(matched_claims),
        "non_signal": is_clean,
    }


def summarize_factor_forbidden_claims(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor forbidden claims DataFrame."""
    return {
        "total_forbidden_patterns": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
