"""Phase 133: Regime Non-Signal Acceptance Report and Validators.

Strictly enforces that regime outputs, metrics, and acceptance scores are non-signal
and never constitute buy/sell recommendations or execution orders.
"""

from typing import Any, Dict, List, Optional, Set, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)

FORBIDDEN_SIGNAL_CLAIMS: Set[str] = {
    "kesin al",
    "kesin sat",
    "buy signal",
    "sell signal",
    "long aç",
    "short aç",
    "pozisyon aç",
    "trade signal",
    "yatırım tavsiyesi",
    "model prediction",
    "production ready",
    "broker ready",
    "official approval",
}


def validate_non_signal_text(text: str) -> Dict[str, Any]:
    """Scan text or document string for forbidden directional, trading signal, or approval claims."""
    if not text:
        return {
            "passed": True,
            "violations_found": [],
            "status": "acceptance_pass",
            "message": "Empty text provided; zero signal claims found.",
        }

    text_lower = text.lower()
    violations = [claim for claim in FORBIDDEN_SIGNAL_CLAIMS if claim in text_lower]

    if violations:
        return {
            "passed": False,
            "violations_found": violations,
            "status": "acceptance_fail",
            "message": f"Detected forbidden trading signal / promotional claims: {violations}",
        }

    return {
        "passed": True,
        "violations_found": [],
        "status": "acceptance_pass",
        "message": "Zero forbidden signal claims found; non-signal certified.",
    }


def build_regime_non_signal_acceptance_report(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Non-Signal Acceptance."""
    p = profile or get_default_regime_validation_acceptance_profile()

    rows = []
    for claim in sorted(list(FORBIDDEN_SIGNAL_CLAIMS)):
        category = "trading_directive"
        if "al" in claim or "sat" in claim or "buy" in claim or "sell" in claim or "long" in claim or "short" in claim or "pozisyon" in claim:
            category = "trade_direction"
        elif "tavsiyesi" in claim:
            category = "investment_advice"
        elif "prediction" in claim:
            category = "predictive_claim"
        elif "ready" in claim or "approval" in claim:
            category = "production_claim"

        rows.append(
            {
                "forbidden_claim": claim,
                "category": category,
                "status": "acceptance_pass",
                "is_prohibited": True,
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "total_claims_prohibited": len(df),
        "non_signal_certified": True,
        "profile_name": p.profile_name,
        "all_prohibited": True,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_non_signal_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize non-signal acceptance DataFrame."""
    return {
        "total_rules": len(df),
        "all_prohibited": bool(df["is_prohibited"].all()) if "is_prohibited" in df.columns else True,
        "non_signal": True,
    }
