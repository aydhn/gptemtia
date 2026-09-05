"""Phase 128: Regime Rule-Free Forbidden Claims.

Defines catalog of strictly forbidden commercial, directional, trading, and approval claims.
"""

from typing import Dict, Tuple
import re
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

FORBIDDEN_CLAIMS_CATALOG = [
    {"claim_id": "fc_01", "phrase": "kesin al", "category": "trade_signal", "risk": "CRITICAL"},
    {"claim_id": "fc_02", "phrase": "kesin sat", "category": "trade_signal", "risk": "CRITICAL"},
    {"claim_id": "fc_03", "phrase": "buy signal", "category": "trade_signal", "risk": "CRITICAL"},
    {"claim_id": "fc_04", "phrase": "sell signal", "category": "trade_signal", "risk": "CRITICAL"},
    {"claim_id": "fc_05", "phrase": "long aç", "category": "order_instruction", "risk": "CRITICAL"},
    {"claim_id": "fc_06", "phrase": "short aç", "category": "order_instruction", "risk": "CRITICAL"},
    {"claim_id": "fc_07", "phrase": "position aç", "category": "order_instruction", "risk": "CRITICAL"},
    {"claim_id": "fc_08", "phrase": "trade signal", "category": "signal_claim", "risk": "CRITICAL"},
    {"claim_id": "fc_09", "phrase": "yatırım tavsiyesi", "category": "regulatory", "risk": "CRITICAL"},
    {"claim_id": "fc_10", "phrase": "model prediction", "category": "unsupported_ml", "risk": "HIGH"},
    {"claim_id": "fc_11", "phrase": "target label", "category": "unsupported_supervised", "risk": "HIGH"},
    {"claim_id": "fc_12", "phrase": "supervised label", "category": "unsupported_supervised", "risk": "HIGH"},
    {"claim_id": "fc_13", "phrase": "production ready", "category": "commercial_claim", "risk": "HIGH"},
    {"claim_id": "fc_14", "phrase": "broker ready", "category": "commercial_claim", "risk": "HIGH"},
    {"claim_id": "fc_15", "phrase": "official approval", "category": "regulatory", "risk": "CRITICAL"},
]


def validate_regime_rule_free_forbidden_claims(text: str) -> Dict:
    """Scan text for any affirmative forbidden claim occurrences."""
    text_lower = text.lower()
    detected = []
    negations = [
        "without", "not ", "no ", "false", "forbidden", "prohibited",
        "disallowed", "zero", "banned", "değildir", "banned", "yasak", "izin verilmez"
    ]

    for item in FORBIDDEN_CLAIMS_CATALOG:
        phrase = item["phrase"]
        if phrase in text_lower:
            idx = 0
            is_affirmative = False
            while True:
                pos = text_lower.find(phrase, idx)
                if pos == -1:
                    break
                snippet = text_lower[max(0, pos - 40): min(len(text_lower), pos + len(phrase) + 40)]
                if not any(neg in snippet for neg in negations):
                    is_affirmative = True
                    break
                idx = pos + len(phrase)

            if is_affirmative:
                detected.append(phrase)

    return {
        "is_clean": len(detected) == 0,
        "detected_forbidden_claims": detected,
    }


def build_regime_rule_free_forbidden_claim_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for forbidden claims catalog."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for fc in FORBIDDEN_CLAIMS_CATALOG:
        row = fc.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_regime_rule_free_forbidden_claims(df)
    return df, summary


def summarize_regime_rule_free_forbidden_claims(df: pd.DataFrame) -> Dict:
    """Summarize forbidden claim rules."""
    total = len(df)
    critical_count = int((df["risk"] == "CRITICAL").sum()) if not df.empty else 0

    return {
        "total_forbidden_claims": total,
        "critical_risk_claims": critical_count,
        "status": "CATALOG_ACTIVE" if total > 0 else "EMPTY",
    }
